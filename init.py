import pandas as pd
import numpy as np

def create_dataframe(n):
    names = []
    for _ in range(n):
        name = input("Enter a name: ")
        names.append(name)
    
    df = pd.DataFrame(names, columns=['Name'])
    return df

def read_settledf(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print(f"The file at {file_path} is empty.")
    except pd.errors.ParserError:
        print(f"Error parsing the file at {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

        