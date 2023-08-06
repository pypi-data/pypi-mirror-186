import os
import sys

os.environ["NW_HOME"] = "../"
os.environ["NW_DATASETS"] = "../datasets"
os.environ["NW_DATASET_STORAGE"] = "../datasets"

# sys.path.append("../neural_lib")

import dataset
from torch_helper import TorchDatasetGetter

ds = dataset.Dataset()
ds.load_by_id("ds-9123")
ds.split_dataset(
        train_ratio= 0.8,
        valid_ratio= 0.1,
        test_ratio= 0.1,
        dataset_type=ds.get_dataset_type())
print(ds.dataset_id, ds.get_dataset_type(), ds.get_problem_type())
print(ds.ann.category_id_to_name)
print(dir(ds))
print(dir(ds.ann))
data = ds.train_data()

print(data[0][0]) # image files

print(type(data[1][0][0]))
# bbox : 박스의 좌표 정보. ccwh로 되어 있음.
# ccwh : 현재 뉴럴웍스랩의 내부적인 좌표 체계, center_x, center_y, width, height를 줄인 단어로, 
# 각 박스의 가운데 중심 값(x, y)과 가로/세로의 값으로 이루어져 있음. 절대 좌표가 아닌 상대 좌표임(=scaling된 값임.). 
# 보통 YOLO 모델을 타겟으로 하는 Dataset에서 사용함.
print(data[1][0][0]) # category and bbox of all in the one image

getter = TorchDatasetGetter(ds)
torch_ds = getter.get_dataset(forwhat="train")

