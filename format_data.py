# Regan Willis 2020-2021
"""
Data formatting functions.
"""
import os
import pandas as pd
from itertools import combinations


def get_combinations(input_list):
    """
    Description
    -----------
    Gets combinations of input list.

    Parameters
    ----------
    input_list          : list
                        List to get combinations of.

    Returns
    -------
    all_combinations    : list
                        Combinations of input_list.
    """

    all_combinations = []

    for i in range(len(input_list)):
        input_combinations = combinations(input_list, i+1)

        for combination in list(input_combinations):
            all_combinations.append(list(combination))

    return all_combinations


def shrink_to_specified_data(df, search_column, specified_data):
    """
    Description
    -----------
    Restructures dataframe to only include specified_data based
    on the search column.

    Example df
    ----------
    index   search_column
    0       1
    1       1
    2       0
    3       1
    4       0

    Example return df if specified_data is 1
    ----------------------------------------
    index   search_column
    0       1
    1       1
    3       1

    Parameters
    ----------
    df                  : pandas dataframe
                        Dataframe to be reduced.

    search_column       : string
                        Name of the column to search for specified_data in.

    specified_data      : list
                        Data to search for.

    Returns
    -------
    formatted_data      : pandas dataframe
                        Dataframe shrunk according to specified_data.
    """

    formatted_data = pd.DataFrame()

    for idx in specified_data:

        # set up rows and index for new dataframe
        formatted_data_rows = []
        formatted_data_idx = []

        # loop through dataframe looking for matches
        for i, row in df.iterrows():

            # match found
            if row[search_column] == idx:
                formatted_data_rows.append(row.values)  # store the whole row
                formatted_data_idx.append(i)  # store the index

        # dataframe for current idx
        curr_idx = pd.DataFrame(formatted_data_rows, index=formatted_data_idx,
                                columns=list(df.columns))

        # add current idx to return dataframe
        formatted_data = pd.concat([formatted_data, curr_idx])

    return formatted_data


def get_formatted_columns(feature_names):
    """
    Description
    -----------
    Formats columns into readable format.

    Parameters
    ----------
    feature_names       : list
                        List to format into columns.

    Returns
    -------
    columns             : list
                        List of formatted columns.
    """
    column_delimiter = ' & '
    columns = []

    # create column header combinations to match features
    column_names = get_combinations(feature_names)

    # format columns
    for column in column_names:
        column = column_delimiter.join(column)
        columns.append(column)

    return columns


def get_data_name(data, events, paths):
    """
    Description
    -----------
    Gets data name for output spreadsheet.

    Parameters
    ----------
    data            : string
                    Data model was run on.

    events          : list
                    All events, used to know if all events
                    are being used and create special name.

    event_type      : list
                    All event types, used to know if all event types
                    are being used and create special name.

    Returns
    -------
    Data name used for output spreadsheet.
    """

    # special names when using all events or all event_types
    if data == events and len(events) > 1:
        return 'all-loaded-events'
    elif data == paths and len(paths) > 1:
        return 'all-loaded-event-types'
    data = data[0]

    return data


def get_idxname(data, data_type, events, event_type):
    """
    Description
    -----------
    Gets row name for output spreadsheet.

    Parameters
    ----------
    data            : string
                    Data model was run on.

    data_type       : string
                    Type of data model was run on.

    events          : list
                    All events, used to know if all events
                    are being used and create special name.

    event_type      : list
                    All event types, used to know if all event types
                    are being used and create special name.

    Returns
    -------
    idxname         : string
                    Row name used for output spreadsheet
    """

    # create idx name with data type and name
    idxname = data_type + ' - data: '
    data_name = get_data_name(data, events, event_type)

    idxname = idxname + data_name

    return idxname


def save_to_spreadsheet(results, save_file):
    """
    Description
    -----------
    Saves results to a spreadsheet.

    Parameters
    ----------
    results         : pandas dataframe
                    Results to save to spreadsheet.

    save_file       : string
                    Name of file results will be saved to.
    """

    # check if file with that name already exists
    if os.path.exists(save_file):
        overwrite = ''

        # give user choice to overwrite
        while overwrite != "Y" and overwrite != "N":
            overwrite = input(f"{save_file} already exists, would "
                              + "you like to overwrite it? (Y/N)").upper()

        if overwrite == "Y":
            # overwrite existing file with results
            print(f'...saving to {save_file}')
            results.to_csv(save_file)
        else:
            # print results
            print("Data not saved")
            print(results)
    else:
        # overwrite existing file with results
        print(f'...saving to {save_file}')
        results.to_csv(save_file)
