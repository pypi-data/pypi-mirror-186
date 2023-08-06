import pandas as pd
from importlib import resources
from test_datasets_2.utils import read_all_datasets

def DataLoader(dataset_names):
    return read_all_datasets(dataset_names)
