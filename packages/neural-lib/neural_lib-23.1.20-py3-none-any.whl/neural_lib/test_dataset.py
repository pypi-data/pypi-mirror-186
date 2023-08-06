import os
import sys

os.environ["NW_HOME"] = "../"
os.environ["NW_DATASETS"] = "../datasets"
os.environ["NW_DATASET_STORAGE"] = "../datasets"

# sys.path.append("../neural_lib")

import dataset
from torch_helper import TorchDatasetGetter

ds = dataset.Dataset()
ds.load_by_id("ds-9125")
ds.split_dataset(
        train_ratio= 0.8,
        valid_ratio= 0.1,
        test_ratio= 0.1,
        dataset_type=ds.get_dataset_type())
print(ds.dataset_id, ds.get_dataset_type(), ds.get_problem_type())
print(ds.ann.category_id_to_name)
print(dir(ds))
print(dir(ds.ann))
for d in zip(*ds.train_data()):
    print(d)
# ds.ann.print()

getter = TorchDatasetGetter(ds)
torch_ds = getter.get_dataset(forwhat="train")

