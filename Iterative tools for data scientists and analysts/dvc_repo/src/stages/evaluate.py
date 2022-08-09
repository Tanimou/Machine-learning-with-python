import itertools
import json

import matplotlib as plt
import numpy as np
import yaml
from sklearn.metrics import confusion_matrix, f1_score


def evaluate(test_dataset, logreg, config_path,data):
    with open(config_path, "r") as f:
        param = yaml.safe_load(f)
    y_test = test_dataset.loc[:, 'target'].values.astype('int32')


    X_test = test_dataset.drop('target', axis=1).values.astype('float32')
    prediction = logreg.predict(X_test)


    cm = confusion_matrix(prediction, y_test)
    f1 = f1_score(y_true=y_test, y_pred=prediction, average='macro')

    metrics = {'f1': f1}
    with open(param['reports']['metrics_file'], 'w') as nf:
        json.dump(obj=metrics, fp=nf, indent=4)
    return cm
