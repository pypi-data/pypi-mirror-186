import pandas as pd
from importlib import resources


def read_all_datasets(DATASET_NAMES_2018) -> pd.DataFrame:
    datasets_dict = {}

    for dataset_name in DATASET_NAMES_2018:
        with resources.path("test_datasets_1.data." + dataset_name, dataset_name + "_TRAIN.tsv") as df:
            df_train =  pd.read_csv(df, sep='\t', header=None)
        with resources.path("test_datasets_1.data." + dataset_name, dataset_name + "_TEST.tsv") as df:
            df_test =  pd.read_csv(df, sep='\t', header=None)

        y_train = df_train.values[:, 0]
        y_test = df_test.values[:, 0]
        
        x_train = df_train.drop(columns=[0])
        x_test = df_test.drop(columns=[0])
        
        x_train.columns = range(x_train.shape[1])
        x_test.columns = range(x_test.shape[1])
        
        x_train = x_train.values
        x_test = x_test.values
        
        # znorm
        std_ = x_train.std(axis=1, keepdims=True)
        std_[std_ == 0] = 1.0
        x_train = (x_train - x_train.mean(axis=1, keepdims=True)) / std_
        
        std_ = x_test.std(axis=1, keepdims=True)
        std_[std_ == 0] = 1.0
        x_test = (x_test - x_test.mean(axis=1, keepdims=True)) / std_
        
        datasets_dict[dataset_name] = (x_train.copy(), y_train.copy(), x_test.copy(), y_test.copy())

    return datasets_dict