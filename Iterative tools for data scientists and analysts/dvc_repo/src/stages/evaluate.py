import argparse
import itertools
import json

import numpy as np
import pandas as pd
import yaml
from data_split import split
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, f1_score
from visual import plot_confusion_matrix


def evaluate(config_path):
    data = load_iris(as_frame=True)
    
    train_dataset, test_dataset = split(config_path)
    with open(config_path, "r") as f:
        param = yaml.safe_load(f)

    y_train = train_dataset.loc[:, 'target'].values.astype('int32')
    X_train = train_dataset.drop('target', axis=1).values.astype('float32')
    
    
    logreg = LogisticRegression(
        **param['train']['clf_params'], random_state=param['base']['random_state'])
    logreg.fit(X_train, y_train)
    
    y_test = test_dataset.loc[:, 'target'].values.astype('int32')
    X_test = test_dataset.drop('target', axis=1).values.astype('float32')
    
    prediction = logreg.predict(X_test)

    cm = confusion_matrix(prediction, y_test)
    f1 = f1_score(y_true=y_test, y_pred=prediction, average='macro')
    cm_plot = plot_confusion_matrix(cm, data.target_names, normalize=False)
    
    cm=pd.DataFrame(cm)
    cm.columns=data.target_names
    print(cm)
    cm.to_csv(param['reports']['confusion_matrix_data'], index=False)
    metrics = {'f1': f1}
    with open(param['reports']['metrics_file'], 'w') as nf:
        json.dump(obj=metrics, fp=nf, indent=4)
    return cm


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', dest='param',
                        default='params.yaml')
    args = parser.parse_args()
    evaluate(config_path=args.param)
