# Regan Willis 2020-2021
"""
This script restructures a dataframe.
It creates the labels that go with the data and extracts the
features the user wants out of three feature options.
"""
import numpy as np
import pandas as pd
from scipy.signal import correlate
from sklearn.preprocessing import StandardScaler

feature_names = []


def get_features(df, extract_features_args):
    """
    Description
    -----------
    Access point for other scripts to sort data
    and extract features. Data will enter in
    the form of a pandas dataframe and be returned
    as a list of features, a list of targets,
    and a list of the feature names.

    Parameters
    ----------
    df                      : pandas dataframe
                            Data to get features for.

    extract_features_args   : list
                            Features the user wants to extract.

    Returns
    -------
    features        : list
                    Features to train on.

    target          : list
                    Target that matches data.

    names           : list
                    Feature names.
    """

    data, target = sort_data(df)
    features, names = extract_features(data,
                                       **extract_features_args)

    return features, target, names


def sort_data(loaded_df):
    """
    Description
    -----------
    Reformats dataframe.
    The majority of this function was
    removed because it contains sensitive information.

    Parameters
    ----------
    loaded_df           : pandas dataframe
                        Data sorted with a file column
                        and a data column.

    Returns
    -------
    avg_data            : list
                        One column of data.

    target              : list
                        Labels that go with data taken from
                        the file name.
    """

    # set up new dataframe
    files = list(loaded_df['file'].unique())
    data = pd.DataFrame(index=list(files), columns=col)

    # create data and target
    target = []
    data = list(data[''])

    events = []

    for idx in list(data.index):
        split = str(idx).split('_')
        events.append(split[1])
    target = [char[0] for char in events]

    return data, target


def extract_features(data, feature_1=True, feature_2=False,
                     feature_3=False, normalize_feature_3=False):
    """
    Description
    -----------
    Extracts features from data and gets spreadsheet column headers.

    Parameters
    ----------
    data                        : list
                                Data all features will be extracted from.

    feature_1                   : boolean
                                Include feature_1 data as a feature.

    feature_2                   : boolean
                                Include feature_2 data as
                                a feature.

    feature_3                   : boolean
                                Include feature_3 data as a feature.

    normalize_feature_3         : boolean
                                Normalize feature_3 data with
                                standard scalar.

    Returns
    -------
    features                    : list
                                Features to train a multilayer perceptron.

    feature_names               : list
                                Feature names.
    """

    feature_names = []
    features = []

    if feature_1:
        features.append(data)
        feature_names.append('Feature 1')

    if feature_2:
        # transform data to feature 2
        features.append(data)
        feature_names.append('Feature 2')

    if feature_3:
        # transform data to feature 3

        if normalize_feature_3:
            scaler = StandardScaler()
            normalized_feature_3 = scaler.fit_transform(data)
            features.append(normalized_feature_3)
        else:
            features.append(data)
        feature_names.append('Feature 3')
    elif normalize_feature_3:
        print("Include feature 3 as a feature to normalize it.")

    return features, feature_names
