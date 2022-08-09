import joblib
import yaml
from sklearn.linear_model import LogisticRegression


def train(config_path,train_dataset):
    with open(config_path, "r") as f:
        param = yaml.safe_load(f)
    y_train = train_dataset.loc[:, 'target'].values.astype('int32')
    X_train = train_dataset.drop('target', axis=1).values.astype('float32')
    logreg = LogisticRegression(
        **param['train']['clf_params'], random_state=param['base']['random_state'])
    logreg.fit(X_train, y_train)
    joblib.dump(logreg, param['train']['model_path'])
    return logreg
