import pandas as pd
import regex as re
import logging
import os
import sys
pickle_path = "Pickled Files/"

logger = logging.getLogger('CleaningFunctions')
if logger.hasHandlers():
    logger.handlers = []
if os.path.isdir('logs') == False:
    os.mkdir('logs')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))
formatter = logging.Formatter('%(levelname)s %(asctime)s - %(message)s')

file_handler = logging.FileHandler(f'./logs/CleaningFunctions.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# %% -----------------------------
# Emojis to clean out of copy messages
# -----------------------------
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)


def prepare_string_matching(string, is_url=False):
    """Prepare strings for matching say in a merge function by removing unnecessary 
        detail, whitespaces and converting to lower case
        Remove emojis as sometimes they can not come through properly in Tracer data

        Parameters
        -----------------
        string : str 
            The string to be cleaned
        is_url : bool 
            If True then remove characters after the '?' which are utm parameters
            These can be present in soem urls we recieve and others not
        Returns 
        ----------------
        string : str
            A cleaned string stripped of whitespace, punctuation and emojis"""
    string = string.lower()
    if is_url:
        # get rid of everything after they start to be utm parameters
        string = string.split('?')[0]
    string = emoji_pattern.sub(r'', string)
    string = string.replace(' ', '',)
    string = re.sub(r'[^\w\s]', '', string)
    return string

def clean_column_names(df, hardcode_col_dict = {},cols_no_change = ['spend', 'date', 'currency', 'cohort', 'creative_name', 'group_id', 'engagements', 'created',
                            'plays', 'saved', 'post_hastags', 'content_type', 'linked_content', 'post_id',
                            'video_duration', 'average_time_watched', 'total_time_watched',
                            'adset_targeting', 'completion_rate', 'targeting', 'cohort_new',
                            'video_completions', 'post_hashtags']):

    """Cleans the column names of a advert performance (organic or paid) dataset, commonly from
        Tracer but could also be from Sprout social. The column names will be standardised so 
        then other functions in other libraries can work with the dataset. 
        
        Parameters
        ----------------
        df : DataFrame
            Input dataframe containing a row item for each peice of creative or a day of advertising
        hardcode_col_dict : dictionary
            A dictionary specifying exact transformations of column names from the key to the value
        cols_no_change : str, list
            A list of column names to be left unchanged
        
        Returns
        ----------------
        df : DataFrame
            Output dataframe with the column names standardised"""
    new_columns = []
    for column in df.columns:
        column = column.lower()
        hardcode_col_dict = {k.lower():v for k,v in hardcode_col_dict.items()} #make sure the keys are lowercase
        #hardcoded columns, for those unusual columns
        if column in hardcode_col_dict.keys():
            column = hardcode_col_dict[column]
        if 'day' == column:
            column = 'date'
        #Columns not to be changed and that don't get called similar things
        elif column in cols_no_change:
            column = column
        elif ('created' in column) and (('date' in column) or ('time' in column) or ('video' in column)):
            column = 'date'  # for organic
        elif ('like' in column) or ('favorite' in column) or ('reaction' in column):
            column = 'likes'
        elif ('video' not in column) and ('impression' in column) and ('unique' not in column):
            column = 'impressions'
        elif (column == 'reach') or (('impressions' in column) and ('unique' in column)):
            column = 'reach'
        elif ('campaign'in column) and ('name' in column):
            column = 'campaign_name'
        elif (('adset' in column) or ('group' in column)) and ('name' in column):
            column = 'group_name'
        elif ('ad' in column) and ('name' in column):
            column = 'name' # for tt_organic
        elif ('creative' in column) and ('name' in column):
            column = 'creative_name'
        elif ('video' in column) and ('impression' in column):                       
            column = 'video_impressions'
        elif ('shares' in column) or ('retweet' in column):
            column = 'shares'
        elif (('conversion' in column) or ('lifetime'in column)) and ('save' in column): #_1d_click_onsite_conversion_post_save in fb_ig_paid data
            column = 'saved'
        elif ('video' in column) and (('100' in column) or ('complete' in column) or('full' in column)):
            column = 'video_completions'
        elif ('video' in column) and ('view' in column) and ('0' not in column) and ('5' not in column): #don't include columsn with 25,50,75% completion
            column = 'video_views'
        elif ('organic' in column) and ('boosted' in column) or ( 'workstream' in column):
            column = 'workstream'
        elif 'currency' in column:
            column = 'currency'
        elif 'country' in column:
            column = 'country'
        elif ('replies' in column) or ('comment' in column):
            column = 'comments'
        elif (('page' in column) and('id' not in column)) or (column == 'profile') or ('business' in column) \
            or (('account' in column) and ('name' in column)) or (column == 'post_username'):
            column = 'account_name'  # for twitter organic
        elif ('caption' in column) or ('text' in column) or ('copy' in column) or ('message' in column) or(column == 'post') or (column == 'video_name'):
            column = 'message'
        elif (column == 'video_id') or ('post_id' in column) or ('ad_id' in column):
            column = 'post_id'
        elif ('url' in column) or (('link' in column) and ('clicks' not in column)):
            column = 'url'
        elif ('clicks' in column) and ('link' in column): #this is also equivalent to a swipe in Snapchat
            column = 'link_clicks'  # for all_plats_paid
        elif ('clicks' in column) and ('link' not in column):
            column = 'clicks'  # for all_plats_paid
        elif ('network' in column) or (column == 'platform'):
            column = 'platform'  # for li_tt_igStories_organic
        elif (('media' in column) and ('product' in column) and ('type' in column)) or ('placement' in column):
            column = 'placement'
        elif (('type' in column) & ('post' in column)) or (('media' in column) and ('type' in column)) \
            or (('content' in column) and ('category' in column)): #creative media type for fb_ig_paid
            column = 'media_type'
        elif('cohort' in column):
            column = 'cohort'
        else:
            logger.info(f'Column "{column}" is not handled in column cleaning function')

        new_columns.append(column)
    if len(new_columns) != len(set(new_columns)):
        logger.exception(f'Duplicate column names found {sorted(new_columns)}')
        raise ValueError
    df.columns = new_columns

    return df

def extract_country_from_string(string, client_name, hardcode_dict):
    """Converts a string containing info identifying a certain 
        Parameters
        ---------------
            string : str 
                string to pass through perhaps in a lambda function, the country is detected from this
            client_name : str 
                name of the client that is removed to make the detection of country easier, 
                for example so you are not searching for 'de' to find Germany with 'indeed' in the string
        Returns
        ---------------
            country_code : str 
                country Tag abbreviation mostly following the ISO 3166-1 alpha-2 format"""
    string = str(string).lower().strip()
    hardcode_dict = {k.lower():v for k,v in hardcode_dict.items()}
    client_name = client_name.lower()
    # remove all non-alphanumeric characters
    if string in hardcode_dict.keys():
        country_code =  hardcode_dict[string]
    string = re.sub(r'[^\w\s]', '', string)
    string = string.replace(client_name, '')
    if ('uk' in string):
        country_code =  'UK/IE'
    elif ('ie' in string) or ('ireland' in string):
        country_code = "UK/IE"
    elif ('au' in string) or ('australia' in string):
        country_code = "AU"
    elif 'fr' in string:
        country_code = "FR"
    elif 'it' in string:
        country_code = "IT"
    elif 'nl' in string:
        country_code = "NL"
    elif 'de' in string:
        country_code = "DE"
    elif 'ca' in string:
        country_code = "CA"
    elif 'us' in string:
        country_code = "US"
    else:
        country_code = "N/A"
    return country_code

def strip_object_columns(df):
    """Strips leading and trailing whitespaces in columns containing strings. 
        This stops effective duplications when two categories in a column 
        are essentially the same but one just has a whitespace"""
    df_obj = df.select_dtypes(['object'])
    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    return df

def extract_region_from_country(country):
    """Extracts the region from the country column"""
    if country == 'UK/IE' or country == 'NL' or country == 'DE' \
            or country == 'FR' or country == 'IT' or country == 'BE':
        return "EMEA"
    elif country == 'CA' or country == 'US':
        return "N. America"
    else:
        return None

def clean_platform_name(platform):
    """Cleans platform name, deals with the fact that most platforms 
    are in the 'title' case, i.e. First letter of each word is capitalised
    However there are some platforms that have are one word but are usually 
    presented as having a capital letter midway through the word."""
    platform = str(platform).lower()
    if 'tiktok' in platform:
        return 'TikTok'
    if 'linkedin' in platform:
        return 'LinkedIn'
    else:
        return platform.title()

def clean_url(url):
    """Clean the url of the post to produce a string with just
        the important information for matching
        In he case of Tiktok remove everything after and including the ?
        This removes the utm parameters"""
    url = str(url)
    url = url.lower()
    url = url.strip()
    url = url.replace('https://', '')
    url = url.replace('http://', '')
    url = url.replace('www.', '')
    url = url.replace('/', '')
    if 'tiktok' in url:
        return url.split('?')[0]
    return url

def updated_value_extract(url):
    """Extract the unique identifier for a post from the url
        This format of this code depends on the platform, sometimes
        it is a numerical code, sometimes it is alphanumeric"""
    try:
        if 'facebook' in url:
            u_url = re.search(r"/(\d{16})/|\w{0,4}/*(\d{11,16})", url).group(0)
            try:
                str(u_url)
            except:
                u_url = re.search(r".*/(\d[9])/$").group(0)
            return u_url
        elif 'instagram' in url:
            u_url = re.search(r"/(.{11})/", url).group(0)
            return u_url
        else:
            u_url = re.search(r"(\d{19})", url).group(0)
            return u_url
    except:
        return 'N/A'

def clean_media_type(media_type):
    """Clean the media type into a standardised version of media type"""
    media_type = str(media_type)
    # replace multiple underscores with a single space
    media_type = re.sub(r'_+', ' ', media_type)
    media_type = media_type.title().strip()

    if (media_type == 'Photo') or (media_type == 'Image') or (media_type == 'Static'):
        media_type_standardised = 'Image'
    elif ('Gif' in media_type) or ('Animated' in media_type):
        media_type_standardised = 'Gif'

    elif ('Native Templates' in media_type):
        media_type_standardised = 'Event'

    elif ('Video' in media_type):
        media_type_standardised = 'Video'

    elif ('Carousel' in media_type) or ('Album' in media_type):
        media_type_standardised = 'Carousel'

    elif media_type == 'Nan' or media_type == 'None' or media_type == 'Null' or media_type == '':
        media_type_standardised = 'N/A'
    else: #else leave it as it was
        media_type_standardised = media_type
    return media_type_standardised


def clean_placement(placement):
    """Clean a placement string into a standardised placement"""
    placement = str(placement).title().strip()
    if placement == 'Nan' or placement == 'None' or placement == 'Null' or placement == '':
        placement = 'N/A'
    elif ('Reel' in placement):
        placement = 'Reel'
    elif 'Story' in placement:
        placement = 'Story'
    else:
        placement = 'Post'
    return placement

def extract_quarter_from_date(date):
    """Extracts the quarter from the date"""
    date = pd.to_datetime(date)
    return date.quarter

def extract_after_nth_occurrence(string, char, n):
    """Extracts the string between the nth and n+1th occurrence of the character"""
    extract = string.split(char)[n]
    extract = extract.strip()
    extract = extract.title()
    return extract

def extract_creative_name(name, group_name):
    asset_name_from_name = extract_value(name, 'a')
    asset_name_from_group = extract_value(group_name, 'ad')

    if asset_name_from_name == None:
        return asset_name_from_group
    else:
        return asset_name_from_name

def extract_value(string, identifier):
    try:
        string = string+'_'
        search_string = f'_{identifier}:(.*?)_'
        value = re.search(search_string, string).group(1)
        value = value.upper()  # all keys in naming convention are upper case
        if value == '':
            value = None
    except:
        value = None
    return value


def two_urls_per_post_to_1(x):
    """Sometimes there are identical posts posted on the same day. 
    This can be used to return just the url of the post with
    the highest amount of 'impressions' or 'video views'"""
    if x['platform'].iloc[0] != 'TikTok':
        target_col = 'impressions'
        max_score = x['impressions'].max()
    else:
        target_col = 'video_views'
        max_score = x['video_views'].max()

    # return pd.Series(d,index=list(d.keys()))
    return x[x[target_col] == max_score]['url']


# for ID_Organic__CA_2022_Q2_USD_ENG_TW
def extract_columns_twitter_2(df):
    df['Group Name'] = df['Group Name'].str.lower()
    df['workstream'] = df['Group Name'].apply(
        lambda x: extract_after_nth_occurrence(x, '_', 1))
    df['country'] = df['Group Name'].apply(
        lambda x: extract_after_nth_occurrence(x, '_', 3))  # double underscore
    df['cohort'] = df['Group Name'].apply(
        lambda x: extract_after_nth_occurrence(x, '_', 5))
    df['Creative Name'] = df['Group Name'].apply(
        lambda x: extract_after_nth_occurrence(x, 'TW'))
    return df

# -----------------------------
#  Checks for Duplicates, boosted Labelling
# -----------------------------
def video_len_toseconds(len_string):
    """Video lengths come through tracer in the format 'minute:seconds', e.g. '1:20' or 80 seconds
        This function converts it into just seconds"""
    try:
        if ':' not in len_string:
            return len_string
        minutes = int(len_string.split(":")[0])
        seconds = int(len_string.split(":")[1])
        return (minutes * 60) + seconds
    except:
        return None
