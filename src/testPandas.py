import pandas as pd
import datetime
def main() :
    print("hellow world")

    to_date = datetime.date.today()

    from_date = to_date - datetime.timedelta(days=1)

    to_date = to_date.strftime("%Y-%m-%d")
    from_date = from_date.strftime("%Y-%m-%d")

    print(to_date)
    print(from_date)

    # create a dataframe
    df = pd.DataFrame({
        'Name': ['John', "None", 'Bob'],
        'Age': [30, 25, None],
        'City': ['New York', 'San Francisco', 'London']
    })

    # iterate over the rows of the dataframe using iterrows()
    for index, row in df.iterrows():
        # check if any element in the row is null
        if row["Name"] is not None :
            print(f"Row {index} contains null values: {row}")





if __name__ == "__main__" :
    main();