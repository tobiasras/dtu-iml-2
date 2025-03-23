import pandas as pd
import numpy as np

def clean_data(df):
    """
    Cleans and preprocesses the given DataFrame containing data from the diamonds dataset.
    This function performs the following operations:
    1. Maps ordinal categorical variables ('cut', 'color', and 'clarity') to numerical values 
    based on predefined mappings:
    - 'cut': {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
    - 'color': {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6, 'D': 7}
    - 'clarity': {'I3': 1, 'I2': 2, 'I1': 3, 'SI2': 4, 'SI1': 5, 'VS2': 6, 'VS1': 7, 
                    'VVS2': 8, 'VVS1': 9, 'IF': 10}
    2. Applies a logarithmic transformation to the 'carat' and 'price' columns, creating 
    new columns 'log_carat' and 'log_price'.

    Parameters:
        df (pandas.DataFrame): A DataFrame containing the diamonds dataset with columns 
                            'cut', 'color', 'clarity', 'carat', and 'price'.

    Returns:
        pandas.DataFrame: The modified DataFrame with the 'cut', 'color', and 'clarity' 
                        columns mapped to numerical values, and new columns 'log_carat' 
                        and 'log_price' added.
    """
    
    # Mapping for ordinal categorical variables
    cut_mapping = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
    color_mapping = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6, 'D': 7}
    clarity_mapping = {'I3': 1, 'I2': 2, 'I1': 3, 'SI2': 4, 'SI1': 5, 'VS2': 6, 'VS1': 7, 'VVS2': 8, 'VVS1': 9, 'IF': 10}

    # Apply the mapping
    df['cut'] = df['cut'].map(cut_mapping)
    df['color'] = df['color'].map(color_mapping)
    df['clarity'] = df['clarity'].map(clarity_mapping)
    
    # Log transform, carat and price.
    df['log_carat'] = np.log(df['carat'])
    df['log_price'] = np.log(df['price'])
    
    return df