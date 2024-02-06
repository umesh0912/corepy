import pandas as pd
from re import search
def main():
    # Example DataFrames
    df1 = pd.DataFrame({'columnA': [1, 2, 3],
                        'system.columnB': [4, 5, 6],
                        'columnC': [7, 8, 9]})

    df2 = pd.DataFrame({'columnX': [1, 2, 3],
                        'columnY': [4, 5, 6],
                        'columnB': [5, 1, 6]})

    # Get the list of substring column names from 'df2'
    substring_columns = df2.columns.tolist()

    # Filter and compare columns in 'df1' based on substring matches
   # matching_columns = [col for col in df1.columns if any(sub_col in col for sub_col in substring_columns)]
    matching_columns = list()
    for col in df1.columns.tolist():
        for sub_col in substring_columns :
            if sub_col in col:
                matching_columns.append(sub_col)


    # Perform the comparison
   # comparison_result = df1[matching_columns] == df2[matching_columns]

    # Print the comparison result
    print(matching_columns)


if __name__ == "__main__" :
    main();