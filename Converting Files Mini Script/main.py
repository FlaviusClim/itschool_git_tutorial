import os
import pandas as pd
from pandas.errors import EmptyDataError


def check_if_file_exists(file_path):
    """Check if the file from the path given by the user exists."""

    try:
        if os.path.exists(file_path):
            print('Well done! File exists')
        else:
            print('The file does not exist or the path is not correct!')
    except (FileNotFoundError, IOError) as e:
        print(f'An error occurred: {e}')


def check_file_type(file_path):
    """Check the extension of the file."""

    accepted_ext_list = ['.txt', '.csv', '.xlsx']

    try:
        result = os.path.splitext(file_path)
        extension = result[1]
        if extension.lower() in [ext.lower() for ext in accepted_ext_list]:
            print(f'The file you choose is a {extension} file')
            return extension
        else:
            print(f'This mini script does not accept {extension} file')
            raise ValueError('Invalid file extension')
    except ValueError as e:
        print(f'An error occurred: {e}')


def read_specific_file_format(file_path, extension):
    """Read the file with the corresponding extension and return the DataFrame."""

    try:
        if extension == '.txt':
            df = pd.read_table(file_path, sep=" ")
        elif extension == '.csv':
            df = pd.read_csv(file_path, encoding='latin-1')
        else:
            df = pd.read_excel(file_path)
        # print(df)
        return df
    except EmptyDataError:
        print('The file is empty or does not contain valid data.')

        return None


def write_specific_file(df, extension):
    """Write a file with a different extension than the original one."""

    try:
        if extension == '.txt':
            df.to_csv('rezultat.csv', index=False)
            new_df_extension = os.path.splitext('rezultat.csv')[1]
        elif extension == '.csv':
            df.to_excel('rezultat.xlsx', index=False)
            new_df_extension = os.path.splitext('rezultat.xlsx')[1]
        else:
            df.to_csv('rezultata_din_excel.csv', index=False)
            new_df_extension = os.path.splitext('rezultat.csv')[1]
        print(f'The {extension} file has been converted successfully to {new_df_extension}')
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == "__main__":
    # C:\Users\flavi\Downloads\SampleCSVFile_11kb.csv
    # C:\Users\flavi\Downloads\WhatsApp Image 2024-01-09 at 19.10.45.jpeg
    # C:\Users\flavi\Downloads\test.txt
    user_input_file_path = input("Enter the file path here: ")
    check_if_file_exists(user_input_file_path)
    file_extension = check_file_type(user_input_file_path)
    df = read_specific_file_format(user_input_file_path, file_extension)

    if df is not None:
        write_specific_file(df, file_extension)