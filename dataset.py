import requests, zipfile, io
import pandas as pd


def NC_clean(raw):
    """
    Preprocessing function for North Carolina voter registration data from https://www.ncsbe.gov/results-data/voter-registration-data
        Parameters
    ----------
    raw: the raw Pandas dataframe pulled from the website's zipfile
            
    Returns
    -------
    clean: Cleaned pandas dataframe with the five features of interest and missing data removed.
    """
    clean = raw.dropna(subset = ['zip_code'])
    include = ['AV'] #using only verified voters
    features = ['zip_code','race_code','party_cd','gender_code','age_at_year_end']
    clean = clean[clean['reason_cd'].isin(include)][features]
    clean['zip_code'] = clean['zip_code'].astype(int)
    return(clean)

def NC_Dare():
    """
    Read in North Carolina voter registration data for Dare County
    from https://www.ncsbe.gov/results-data/voter-registration-data
    
    Returns
    -------
    a clean pandas dataframe
    
    """
    url = 'https://s3.amazonaws.com/dl.ncsbe.gov/data/ncvoter28.zip'
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    file = z.extract('ncvoter28.txt')
    df = pd.read_csv(file, encoding='cp1252', delimiter = "\t")
    return(NC_clean(df))

def NC_Statewide():
    """
    Read in North Carolina voter registration data for the entire state
    from https://www.ncsbe.gov/results-data/voter-registration-data
    
    Returns
    -------
    a clean pandas dataframe
    
    """
    url = 'https://s3.amazonaws.com/dl.ncsbe.gov/data/ncvoter_Statewide.zip'
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    file = z.extract('ncvoter_Statewide.txt')
    df = pd.read_csv(file, encoding='cp1252', delimiter = "\t")
    return(NC_clean(df))

def NC_Durham():
    """
    Read in North Carolina voter registration data for Durham County
    from https://www.ncsbe.gov/results-data/voter-registration-data
    
    Returns
    -------
    a clean pandas dataframe
    
    """
    url = 'https://s3.amazonaws.com/dl.ncsbe.gov/data/ncvoter32.zip'
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    file = z.extract('ncvoter32.txt')
    df = pd.read_csv(file, encoding='cp1252', delimiter = "\t")
    return(NC_clean(df))

def Flare():
    """
    Read in Solar Flare data (flare.data2) from UCI Machine Learning Repository
    https://archive.ics.uci.edu/ml/datasets/Solar+Flare
    """
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/solar-flare/flare.data2'
    flare_names = ['Zurich','Large_Spot','Spot_Dist','Activity','Evolution','Prev_Activity','Complex','This_Pass','Area','Area_Largest','Common','Moderate','Severe']
    raw = pd.read_csv(url,sep = ' ',skiprows=1,names = flare_names)
    clean = raw.drop(columns=['Area_Largest','Common','Moderate','Severe'])
    return(clean)
    
    
