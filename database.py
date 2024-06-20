import pandas as pd
import os


def check_file(path_to_file):
    is_table = os.path.exists(path_to_file)
    return is_table


def create_table(file_name):
    df = pd.DataFrame({'Date': [],
                       'Score': [],
                       'Total_time': []
                       })
    df.to_csv(file_name, index=False)
    return df


def load_table(file_name):
    dtypes = {'Score': 'Int16'}
    df = pd.read_csv(file_name, index_col=False, dtype=dtypes, parse_dates=['Date'])
    df['Total_time'] = pd.to_timedelta(df['Total_time'])
    return df


def write_to_table(file_name, df, columns_data=None):
    new_df = pd.DataFrame(columns_data, columns=df.columns)
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv(file_name, index=False)
    return df
