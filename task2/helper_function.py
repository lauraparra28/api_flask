import os
import pandas as pd

def check_file_exists(filename: str):
    """
    This function helps to check if the file that the user is trying to create
    its already in the folder.
    Args:       file_name (str): file name
    Returns:    bool: True if file exists, False if file doesn't exist.
    """
    if(os.path.exists(filename)):
        return True
    else:
        return False

def filter_range_csv(filename:str, num_n:int, num_m:int):
    """
    Function to filter a csv file by a column and a range of values
    Args:
        filename (str): filename to be filtered
        columns (str): column to be filtered
        value1 (int): lower value to be filtered
        value2 (int): upper value to be filtered
    Returns:
        result: filtered json
    """
   
    data_file = pd.read_csv(filename)
    data_file = data_file.loc[num_n:num_m]
    result = data_file.to_json(orient="split", index=False)

    return result
  
def filter_csv(filename:str, column:str, value:float):
    """
    Function to filter a csv file by a column and a value
    Args:
        filename (str): filename to be filtered
        columns (str): column to be filtered
        value (float): value to be filtered
    Returns:
        result: filtered json
    """
    data_file = pd.read_csv(filename)
    data_file = data_file[data_file[column] <= value and data_file[column] > 60 ]
    result = data_file.to_json(orient="split", index=False)

    return result

def filter_sciFi(filename:str, column:str, tipo:str):
    
    films_sciFi = pd.read_csv(filename)
    films_sciFi = films_sciFi.loc[films_sciFi[column] == tipo]  
    result = films_sciFi.to_json(orient="split", index=False)

    return result

