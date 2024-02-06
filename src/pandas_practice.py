
import pandas as pd
from pprint import  pp
def main():
    print('in main')
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 28, 22],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
    }

    df = pd.DataFrame(data)

    df.set_index('Name', inplace=True)
    pp(df)
    pp("_____print alice info_____")
    pp(df.loc['Alice', 'Age'])
    pp(df.loc[['Alice', 'Charlie'], ['Age', 'City']])
    pp(df.loc[(df['Age'] >= 25) & (df['City'] == 'New York')])

    pp(df.loc['Alice':'Charlie'])
    pp(df.loc['Alice':'Charlie', 'Age':'City'])

    pp(df.loc[df['Age'] < 30])

if __name__ == "__main__":
    main()