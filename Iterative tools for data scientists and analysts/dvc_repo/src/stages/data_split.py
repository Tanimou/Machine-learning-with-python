import yaml
from sklearn.model_selection import train_test_split

from dvc_repo.src.stages.data_load import data_load


def split(config_path):
    with open(config_path, "r") as f:
        param = yaml.safe_load(f)
    dataset = data_load(config_path)
    dataset_train, dataset_test = train_test_split(
        dataset, test_size=param['data']['test_size'], random_state=param['base']['random_state'])
    
        
    dataset_train.to_csv(param['data']['train_dataset_path'], index=False)
    
    dataset_test.to_csv(param['data']['test_dataset_path'], index=False)
    return dataset_train, dataset_test



