import argparse

import yaml
#from src.stages.data_load import data_load
from data_load import data_load
from sklearn.model_selection import train_test_split


def split(config_path):
    with open(config_path, "r") as f:
        param = yaml.safe_load(f)
    dataset = data_load(config_path)
    dataset_train, dataset_test = train_test_split(
        dataset, test_size=param['data']['test_size'], random_state=param['base']['random_state'])
    
        
    dataset_train.to_csv(param['data']['train_dataset_path'], index=False)
    
    dataset_test.to_csv(param['data']['test_dataset_path'], index=False)
    return dataset_train, dataset_test


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', dest='param',
                        default='params.yaml')
    args = parser.parse_args()
    split(config_path=args.param)
