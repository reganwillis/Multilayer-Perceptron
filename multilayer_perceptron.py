# Regan Willis 2020-2021
"""
Runs the multilayer perceptron model.
"""
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def run_all_features(columns, features, target):
    """
    Description
    -----------
    Fits MLP to data and evaluates model performance.

    Parameters
    ----------
    df          : pandas dataframe
                Structure holding data.

    columns     : list
                Column name used to display user output.

    features    : list
                Features to run the model on.

    target      : list
                Targets corresponding to features.

    Returns
    -------
    scores      : list
                Model scores.
    """

    scores = []

    for i in range(len(features)):
        print(f'Running model on {columns[i]}...')

        # train test split on features and target
        feature = np.column_stack(features[i])
        X_train, X_test, y_train, y_test = train_test_split(feature,
                                                            target,
                                                            test_size=TESTSET_SIZE,
                                                            random_state=SPLIT_RS,
                                                            stratify=target)

        # run model on training and testing data
        score = run_model(X_train, X_test, y_train, y_test)
                
        # fit model
        clf = MLPClassifier(hidden_layer_sizes=(100, 100, 100), max_iter=EPOCHS,
                            activation='', solver='', random_state=FIT_RS)
        clf = clf.fit(X_train, y_train)

        # make predictions
        pred = clf.predict(X_test)

        # evaluate model
        score = clf.score(X_test, y_test)
        print('\nModel Evaluation: ', score, '\n')
        print(classification_report(y_test, pred), '\n')

        scores.append(score)

    return scores
