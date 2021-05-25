# Regan Willis 2020-2021
"""
Data is used to train a Multilayer Perceptron.

Results are saved to a csv file (save_file).
"""
import format_data
import pandas as pd
import feature_setup
import multilayer_perceptron

# output spreadsheet name
save_file = './results.csv'

# data to load
events = []
event_types = []

# use dataloader to load dataset
df = pd.DataFrame()

# model variables
extract_feature_args = {'feature_1': True, 'feature_2': False,
                        'feature_3': False,
                        'normalize_feature_3': False}


def run(input_list, column_name, count):
    """
    Description
    -----------
    Handles data formatting, running model and
    results storage for given list of data.

    Parameters
    ----------
    input_list      : list of lists
                    Data to run the model on.

    column_name     : string
                    Column in dataframe the data corresponds to.

    count           : integer
                    Keeps track of which data is being run.

    Returns
    -------
    all_results     : pandas dataframe
                    Results of the data on every feature.

    count           : integer
                    Keeps track of which data is being run.
    """

    all_results = pd.DataFrame()

    for idx in input_list:

        # arrange data into features and targets
        formatted_df = format_data.shrink_to_specified_data(df, column_name,
                                                            idx)
        features, target, feature_names = feature_setup.get_features(formatted_df,
                                                                     extract_feature_args)
        feature_combinations = format_data.get_combinations(features)

        # formatting for output spreadsheet
        idxname = format_data.get_idxname(idx, data_type, events, event_types)
        columns = format_data.get_formatted_columns(feature_names)

        # output for user to keep track of what is running
        print(f'\n{count}/{num_combinations}\n{idxname}')
        print(f'Running on {len(columns)} features...')
        count = count + 1

        # run model and store results
        scores = multilayer_perceptron.run_all_features(columns,
                                                        feature_combinations,
                                                        target)
        results = pd.DataFrame([scores], index=[idxname], columns=columns)
        all_results = pd.concat([all_results, results])

    return all_results, count


# format dataframe
df = df.set_index(df['file'])  # set file name as index

# path and event combinations
event_type_combinations = format_data.get_combinations(event_types)
num_combinations = len(event_type_combinations) + len(events)
print('\nRunning', num_combinations, 'combinations of event types and events...')

# run path and event combinations through model and get results
count = 1
event_results, count = run(events, 'event', count)
path_results, _ = run(event_type_combinations, 'event_type', count)

all_results = pd.DataFrame()
all_results = pd.concat([event_results, path_results])

print(f'\nAll {num_combinations} combinations complete')

format_data.save_to_spreadsheet(all_results, save_file)