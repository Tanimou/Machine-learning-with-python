import argparse

import pandas as pd
import yaml
from sklearn.datasets import load_iris


def data_load(config_path):
    data = load_iris(as_frame=True)
    dataset = data.frame
    dataset.head()
    dataset.columns = [colname.strip(' (cm)').replace(' ', '_') for colname in dataset.columns.tolist()]

    with open(config_path, "r") as f:
        param = yaml.safe_load(f)
    dataset.to_csv(param['data']['dataset_csv'], index=False)
    print(f"Dataset saved to {param['data']['dataset_csv']}")
    return dataset

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', dest='param', default='params.yaml')
    args = parser.parse_args()
    data_load(config_path=args.param)