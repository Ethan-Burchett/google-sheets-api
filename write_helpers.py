import pandas as pd
import pickle


def write_helper(dataframe, file_name):
    """
    Write a Pandas DataFrame to a text file.

    Parameters:
        dataframe (pandas.DataFrame): The DataFrame to be written to the text file.
        file_name (str): The name of the text file (with or without extension).

    Returns:
        None
    """
    try:
        # Check if the file name has the .txt extension, if not, add it
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        # Write DataFrame to the text file
        dataframe.to_csv(file_name, sep="\t", index=False)
        print("Data written to", file_name)
    except Exception as e:
        print("Error:", e)


import os


def write_helper_csv(dataframe, file_name):
    """
    Append tabular data from a Pandas DataFrame to a CSV file or create a new one if it doesn't exist.

    Parameters:
        dataframe (pandas.DataFrame): The DataFrame whose data will be appended to the CSV file.
        file_name (str): The name of the CSV file (with or without extension).

    Returns:
        None
    """
    try:
        # Check if the file name has the .csv extension, if not, add it
        if not file_name.endswith(".csv"):
            # file_name += '.csv'
            file_name = "output/" + file_name + ".csv"

        # Check if the file exists
        file_exists = os.path.isfile(file_name)

        # # If the file didn't exist before, write the header
        # if not file_exists:
        dataframe.to_csv(file_name, mode="a")
        # else:
        #     # Append the data without header
        # dataframe.to_csv(file_name, mode='a', header=False, index=False)

        print("Data appended to", file_name)
    except Exception as e:
        print("Error:", e)