#%%
import pandas as pd
import regex as re
import numpy as np
from datetime import date
from tqdm.auto import tqdm
import os
import logging
import sys
today = pd.to_datetime(date.today())

#%%-----------------------------
# Initialise Logger
# ------------------------------

logger = logging.getLogger('QAFunctions')
if logger.hasHandlers():
    logger.handlers = []
if os.path.isdir('logs') == False:
    os.mkdir('logs')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))
formatter = logging.Formatter('%(levelname)s %(asctime)s - %(message)s')

file_handler = logging.FileHandler(f'./logs/QAFunctions.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class QualityAssessments:

    def __init__(self,main_error_tracker_name,tracer_error_tracker_name,naming_conv_tracker_name,util_object=None):
        self.main_error_tracker_name = main_error_tracker_name
        self.tracer_error_tracker_name = tracer_error_tracker_name
        self.naming_conv_tracker_name = naming_conv_tracker_name
        if util_object != None:
            self.util = util_object
    
    def null_values_checker(self,df,cols_to_group,cols_to_ignore,tab_name,
                    null_definitions=[np.nan,'N/A','','None'],output_method='Gsheet'):
        """Takes in a dataframe and columns to groupby and checks how many null values or null equivalents
            there are in the rest of the columns. 
            
            Parameters
            -------------------
            df : DataFrame 
                The Input Dataframe of any type where you want to check for nulls
            cols_to_group : list, str
                The list of columns to perform a groupby operation with the null percentage
                counts will be a percentage of nulls in these groupbys
            cols_to_ignore : list, str
                The list of columns to not count nulls in, to make the output dataframe smaller perhaps
            gsheet_name : str
                The name of the google sheet workbook to pass to the google sheet function
            tab_name : str
                The name of the tab in the google sheet workbook to pass to the google sheet function
                The google sheet must be setup with this tab already created
            null_definitions : list
                A list containing elements to be defined as a null value 
            output_method : str
                A string identifying whether the output is to be sent to a Google sheet ('Gsheet') or returned
                as a dataframe ('Dataframe')
            
            Returns
            -------------------
            null_count_df : DataFrame
                Dataframe showing the percentage of nulls in each column grouped by the 'cols_to_group'"""

        for null in null_definitions: 
            df = df.replace(null,'NullValue')

        null_count_df = pd.DataFrame(index=df[cols_to_group].value_counts().index).reset_index()
        other_cols = list(set(df.columns) - set(cols_to_group) - set(cols_to_ignore))

        for col in other_cols:
            col_groupby = df.groupby(cols_to_group)[col].apply(lambda x: round(100 * x[x == 'NullValue'].count()/x.shape[0],1)).reset_index()
            null_count_df = pd.merge(null_count_df,col_groupby)

        if output_method == 'Gsheet':
            self.util.write_to_gsheet(self.main_error_tracker_name,tab_name,null_count_df)
        elif output_method == 'Dataframe': 
            return null_count_df
    
    def check_data_recency(self,df,cols_to_group,three_days_for_monday= True,date_col='date',gsheet_tab='DataRecency'):
        """Post a google sheet showing how many days since different channels have been active.
            Also return a list of channels that have been inactive for more than 2 days which
            might be indicative of an error
            
            Parameters
            ------------------
            df : DataFrame
                Dataframe of data containing a 'date' column 
            cols_to_group : list, str
                Columns to groupby effectively creating the 'channels' 
            three_days_for_monday : bool
                If the check is run on a Monday give 3 days before declaring a
                channel as inactive because of the weekend
            date_col : str
                Column name for the date to find the maximum value for based on grouping by 'cols_to_group'
                If 'created' is used when working with Tracer data then this will find out when the data was 
                last updated by Tracer, regardless of whether the actual date was of the post was 30 days ago
            gsheet_tab : str


            Returns
            ------------------
            error_message : str
                String error message describing which channels are recently inactive. This message can then be sent
                to a slack function"""

        error_message = ''
        organic_or_paid = self.util.identify_paid_or_organic(df)
        print(organic_or_paid)
        buffer_days_since_active = 2
        data_recency = pd.DataFrame(df.groupby(cols_to_group)[date_col].max().apply(lambda x: (today - x).days)).reset_index().rename(columns={'date':'DaysSinceActive'})  
    
        self.util.write_to_gsheet(self.main_error_tracker_name,gsheet_tab,data_recency,sheet_prefix=organic_or_paid)

        #create a tag string to identify a channel, a concatenation of all the column values specified in 'cols_to_group'
        def concat_cols(x):
            result=''
            for col in cols_to_group:
                result += x[col] + '-'
            return result.rstrip('-')
            
        data_recency['Channel'] = data_recency.apply(lambda x: concat_cols(x),axis=1)

        #The option for giving 3 days of buffer for monday is available in case no advertising/posting is done 
        #over the weekend and you don't want many channels appearing as if they are inactive on Monday morning
        if today.day_of_week == 0 and three_days_for_monday: 
            buffer_days_since_active = 3

        channels_recently_inactive = data_recency.query(f'DaysSinceActive >{buffer_days_since_active} and DaysSinceActive <=6')
        channels_recently_inactive_list = channels_recently_inactive['Channel'].unique().tolist()
        if len(channels_recently_inactive_list) != 0:
            error_message = f'{organic_or_paid} Channels Recently that are recently inactive {" , ".join(channels_recently_inactive_list)}\n'

        return error_message
    
    def boosted_function_qa(self,paid_df, organic_df, impressions_threshold = 100000):
        """Takes in organic data and paid data and reports how many of the posts labelled 
            as boosted in the paid data are present in the organic data
            
            Parameters
            ----------------
            paid_df : DataFrame
                Daily ad spend, boosted posts identified in the 'workstream' column
            organic_df : DataFrame
                Organic Post performance Data 
            impressions_threshold : 
                the number of impressions above which it is unlikely the post is purely organic
            
            Returns
            ---------------
            error_message : str
                String detailing what the error is so that it can be passed to a notification 
                service like slack"""
        error_message = ''
        organic_df['Error'] = False

        # count number of unique paid posts with workstream organic minus oranic posts labelled as boosted
        # number of boosted post from paid naming convention Tags
        paid_boosted_count = len(paid_df[paid_df['workstream'] == 'boosted']['post_id'].unique())

        # number of posts our boosted matching function has identified as boosted
        organic_boosted_count = len(organic_df[organic_df['workstream'] == 'boosted']['post_id'].unique())
        missing_boosted = paid_boosted_count-organic_boosted_count

        if (missing_boosted) != 0:
            error_message = error_message + '  ' + \
                f'There are {missing_boosted}({round(missing_boosted*100/paid_boosted_count,2)}%) posts mislabelled as Pure Organic\n'
            logger.warning(error_message)

        # A post that is labelled as organic but has impressions over the impressions_threshold may actually be boosted 
        # but hasn't been identified as such
        misslabelled_og_rows = organic_df[(organic_df['workstream'] == 'Pure Organic') & \
                                        ((organic_df['impressions'] >= impressions_threshold) | \
                                        (organic_df['video_views'] >= impressions_threshold))]

        if len(misslabelled_og_rows.index.values) > 0:
            error_message = error_message + '  ' + \
                f'There are {len(misslabelled_og_rows.index.values)} Pure Organic posts with over {impressions_threshold} impressions or video views\n'
            logger.warning(error_message)
            self.util.write_to_gsheet(self.main_error_tracker_name,'OrganicWithBigImpressions', misslabelled_og_rows)
        # return TT or IG values with empty message field
        # for the date function exlude the dates we paused for the queen

        logger.warning(error_message)
        return error_message
    
    def comparison_with_previous_data(self,df,name_of_df,cols_to_check=['impressions','likes'],perc_increase_threshold=20,
                                   perc_decrease_threshold=0.5, check_cols_set=True,raise_exceptions=False):
        '''This function stores the high level sums from the previous run of the script
            and if they have reduced or increased too sharply an error is raised
        Parameters
        --------------------
            df : DataFrame
                Input dataframe that the historic checks are going to be performed on
            name_of_df : str
                Name of the dataframe, this will be used to name a file to save for future comparison
            cols_to_check : list, str
                A list of strings that detail the columns to be totaled which will then be compared with previous data
            perc_increase_threshold : number
                A number between 0 and 100, the percentage increase threshold above which it is deemed that the totals 
                have raised too rapidly and an error has occured
            perc_decrease_threshold : number
                A number between 0 and 100, the percentage decrease threshold below which it is deemed that the totals
                decreased and an error has occured
            check_cols_set : bool
                If true, store the set of columns present for comparison to see if any new columns have been added or
                removed next time, in which case it is deemed an error has occured
            raise_exceptions : bool
                If true, then raise an exception if an error has occured instead of just returning an error message

        Returns
        -------------------
            error_message : str
                String detailing what the error is so that it can be passed to a notification 
                service like slack'''
        
        error_message, error_occured = '', False
        new_dict = {}
        for col in cols_to_check:
            new_dict[col] = df[col].sum()

        if check_cols_set == True:
            new_dict['Columns'] = df.columns.tolist()

        if os.path.isdir('Historic df Comparison (Do Not Delete)') == False:
            os.mkdir('Historic df Comparison (Do Not Delete)')
        if os.path.exists(f'Historic df Comparison (Do Not Delete)/{name_of_df}_previous_totals') ==False:
            self.util.pickle_data(new_dict,f'{name_of_df}_previous_totals',folder='Historic df Comparison (Do Not Delete)/')
            logger.info(f"Creation of {name_of_df}_previous_totals")
            logger.info(new_dict)
            return
        else:
            old_dict = self.util.unpickle_data(f'{name_of_df}_previous_totals',folder='Historic df Comparison (Do Not Delete)')
        
        for key, value in old_dict.items():
            if key == 'Columns':
                if set(value) != set(new_dict['Columns']):
                    error_occured = True
                    columns_removed = list(set(value) - set(new_dict['Columns']))
                    columns_added = list(set(new_dict['Columns']) - set(value))
                    error_message = error_message + '  ' + f'The columns seems to have changed from last time,\n'\
                                            f' Columns that were added = {columns_added}\n' \
                                            f' Columns that were removed = {columns_removed}\n'
            elif new_dict[key] *(1+perc_decrease_threshold/100) < value:
                error_occured = True
                error_message = error_message + '  ' + f'The total of {key} seems to have decreased from last time\n'\
                                        f' Prev Value = {old_dict[key]} , New Value = {new_dict[key]}\n'
            elif new_dict[key] > value*(1 +perc_increase_threshold/100):
                error_occured = True
                error_message = error_message + '  ' +f'The total of {key} has increased by more than\n'\
                                    f'{perc_increase_threshold}% from last time\n'\
                                        f' Prev Value = {old_dict[key]} , New Value = {new_dict[key]}\n'

        if error_occured:
            error_message = f'Comparison with historic df {name_of_df}: ' + error_message +'\n'
            logger.info('ERROR' + error_message) #if error messages has been added to then log it
        if raise_exceptions and error_occured:
            raise Exception(error_message)
        self.util.pickle_data(new_dict,f'{name_of_df}_previous_totals',folder='Historic df Comparison (Do Not Delete)/')
        
        return error_message
    
    def duplicates_qa(self,df,df_name,subset=None, drop_duplicates=True):
        """Checks for duplicates and optionally drops duplicates in a dataframe
        Parameters
        -----------------
            df : DataFrame
                The Dataframe to be checked for duplicates
            df_name : str
                The name of the dataframe to be used for logging purposes
            subset : list, str
                Only consider certain columns for identifying duplicates, by default use all of the columns
            drop_duplicates : bool
                If true remove duplicate values
        
        Returns
        ----------------
            df : DataFrame
                Returns original dataframe without duplicates if 'drop_duplicates' = True
            error_message : str
                String detailing what the error is so that it can be passed to a notification 
                service like slack"""

        num_duplicates = df.duplicated(subset=subset).sum()
        if num_duplicates >= 0:
            logger.warning(f'{num_duplicates} duplicates found in the {df_name}')
            if drop_duplicates:
                df.drop_duplicates(subset=subset, inplace=True)
        return df
    
    def check_impressions_no_engagements(self,df, raise_exceptions=False):
        """Function to check if a row item has engagements but no impressions and no video views
            This shouldn't happen andis indicative of an error with Tracer but can be valid as 
            some platforms count viral engagements differently
            Parameters
            ------------------
            df : DataFrame
                Input dataframe of advertising data with columns 'impressions' or 'video_views'
            raise_exceptions : bool
                Boolean flag if set to true will raise an exception if an offending row item is discovered
            
            Returns
            ------------------
            error_message : str
                String detailing what the error is so that it can be passed to a notification 
                service like slack
                """
        paid_or_organic = self.util.identify_paid_or_organic(df)
        # https://docs.google.com/spreadsheets/d/1refbPLje6B48qvSRNXrK3U_OAfzjzeuTrzgfqq9O-yw/edit#gid=0
        df['date'] = pd.to_datetime(df['date'])
        error_message = f'{paid_or_organic} Data Quality Check Function Failed'
        engagements_cols = ['likes', 'comments', 'shares']
        engagements_mask = ((df[engagements_cols] != 0).any(1))
        # Check for zeros in impression columns but non zeros in likes, impressions, and other metrics
        no_impr_but_engage = list(df[(df['impressions'] == 0) & engagements_mask].index.values)

        # TikTok organic doesn't have impressions, instead it has video views. There is an error if
        # Video views is equal to zero but there are engagements
        tiktok_org_no_impr_but_engage = list(df[((df['platform'] == 'TikTok') & (df['workstream'] == 'boosted') &
                                                (df['video_views'] == 0) & engagements_mask)].index.values)

        reels_org_no_impr_but_engage = list(df[((df['placement'] == 'Reels') & (df['workstream'] == 'boosted') &
                                                (df['video_views'] == 0) & engagements_mask)].index.values)

        # paid with  impressions but has engagements
        no_impressions_but_engage_rows = set(no_impr_but_engage + tiktok_org_no_impr_but_engage 
                                            + reels_org_no_impr_but_engage)

        if len(no_impressions_but_engage_rows) > 0:
            error_message = error_message + '  ' + f'There are {len(no_impressions_but_engage_rows)} rows with'\
                ' zeros in impressions columns but non-zeros in likes, comments, shares and video_views\n'

            df.loc[no_impressions_but_engage_rows, 'Error'] = True
            # error_message = error_message + " " + "Split By platform"
            # error_message = error_message + " " + pd.crosstab(erroneous_df['platform'],erroneous_df['media_type'],margins=True,dropna=False)
            self.util.write_to_gsheet("Indeed Data Error Tracking Tracer", 'NoImpressionsButEngagements', df.loc[no_impressions_but_engage_rows],
                            sheet_prefix=paid_or_organic)
            exception_occurred = True

        logger.warning(error_message)
        if raise_exceptions and exception_occurred:
            raise Exception(error_message)
        
        return error_message

    def naming_convention_checker(self, df,naming_convention,campaignname_dict=None, adgroupname_dict=None, 
                                    adname_dict=None,campaign_col='campaign_name',adgroup_col='group_name',adname_col='name',
                                    start_char='_',middle_char=':',end_char='_'):
        """Takes in Paid Data with cleaned columns and the naming convention google sheet and
        for each unique campaign_name, adgroup_name and adname will show whether the key is missing or whether
        the values is incorrect
        
        Parameters
        ---------------------- 
        df : DataFrame 
            The Dataframe containing paid df with the campaign name, 
            ad group name and ad name column included
        naming_convention :  dataframe
            The dataframe extracted froom a google sheet which contains all the accepted
            tags and each tag's acceptable values
        campaignname_dict : dictionary
            A dictionary of the tags to be checked, column label as the key, shortcode as the value
        adgroupname_dict : dictionary
            A dictionary of the tags to be checked, column label as the key, shortcode as the value
        adname_dict = dictionary
            A dictionary of the tags to be checked, column label as the key, shortcode as the value
        
        Returns
        ---------------------
        Writes to google sheet a table with the index being a unique instance of the campaign"""
        
        conv_level_tuple = ((campaignname_dict,campaign_col,'CampaignNameErrors'),(adgroupname_dict,adgroup_col,'AdGroupNameErrors'),
                            (adname_dict,adname_col,'AdNameErrors'))
        # df = clean.clean_column_names(df)
        #Obtain the column names of all the Keys available in the convention tracker sheet
        #https://docs.google.com/spreadsheets/d/1Wtwd6xT9zRLhPICWSWDNZ2mXBy74_xszLVX2ZqO_odo/edit#gid=605935420
        key_values_conv_cols = [x.replace(' Key','') for x in naming_convention.columns if ' Key' in x]

        def remove_empties_from_list(input_list):
            '''Obtaining a list of keys from the tracker sheet column often results in multiple empty
                strings, this function removes them from the list'''
            return list(filter(lambda x: x != '',input_list))

        def return_value(string,tag,acceptable_values):
            """This checks for each campaign, group_name or ad_name string, for a certain tag e.g.'pl'
            whether the tag is even present and if so whether a correct value is present"""
            search_string = f'{start_char}{tag}{middle_char}(.*?){end_char}'
            search_result = re.search(search_string, string + '_') #add a underscore at so search string has an endpoint to find
            if search_result == None:
                return 'NoKey'
            elif search_result.group(1).strip(' ') == '':
                return 'NoKey'
            else:
                if search_result.group(1).upper() in acceptable_values:
                    return "Correct"
                else:
                    return 'Incorrect Value'

        for level in conv_level_tuple:
            #For each level of the naming convention, i.e. campaign, adgroup, adname
            output_df = round(df.groupby(level[1])['spend'].sum().reset_index(),1)
            if level[0] == None: continue #no convention dict provided therefore ignore
            for label,tag in level[0].items():
                #For each label and tag in the required set 
                if label in key_values_conv_cols:
                    acceptable_values= remove_empties_from_list(naming_convention[label+' Key'].str.upper().unique().tolist())
                    output_df[f'{label} ("{tag}")'] = output_df[level[1]].apply(lambda x: 
                                                                return_value(x,tag,acceptable_values))
            self.util.write_to_gsheet(self.naming_conv_tracker_name, level[2],output_df)
    
