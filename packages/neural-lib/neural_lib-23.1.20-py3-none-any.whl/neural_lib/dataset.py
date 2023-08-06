"""
dataset 메타 정보를 담은 json 파일을 로딩.
이미지 dataset의 경우, 실제적인 로딩은 neuannotation.py - Annotation class 이용

dataset.json 파일에는 메타정보만. 실제 이미지 파일들의 목록, label값 목록은 annotation.json 파일에 있다.

Example of dataset json file: IMAGE -- datasets/ds-9123/ds-9123.json

____________________________
{
  "dataset_id": "ds-9123",
  "dataset_name": "(need to write)",
  "description": "(need to write)",
  "dataset_type": "IMAGE",
  "problem_type": "DETECTION",
  "all_annotation": "ds-9123-all_anno.json",
  "train_annotation": "",
  "valid_annotation": "",
  "test_annotation": "",
  "root_path": "dataset",
  "category": [
    {
      "id": 0,
      "name": "Dead",
      "supercategory": ""
    },
    {
      "id": 1,
      "name": "Alive",
      "supercategory": ""
    }
  ],
  "sample": 0
}
------------------

Example of dataset json file: TABLE(CSV)
{
  "dataset_id": "ds-913",
  "dataset_name": "Iris LabelEncoding data",
  "description": "Iris LabelEncoding data",
  "dataset_type": "TABLE",
  "problem_type": "CLASSIFICATION",
  "all_table": "iris_label.csv",
  "train_table": "",
  "valid_table": "",
  "test_table": "",
  "date_columns":[],
  "input_columns": ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"],
  "output_columns": ["Species_LabelEncoder"]
}
"""

import os
import random
import math
import collections
import numpy as np
import pandas as pd
import copy

import numpy
import logging

logger = logging.getLogger(__name__)
from neuannotation import (
    Annotation,
    get_sound_feature_from_df,
    get_filelist_from_df,
)
from neutable import Table
from neuenv import dataset_fpath, dataset_folder, job_folder
from neujson import Json, save_json


def calculate_class_weights(labels):
    class_list = np.unique(labels)
    class_list.sort()

    class_weight = {}
    for i, _class in enumerate(class_list):
        class_weight[i] = len(labels) / (len(class_list) * collections.Counter(labels)[_class])

    return class_weight


### Dataset에 대한 정의
# 1) init -> 2) load_by_id -> load_data -> 3) CSV or Annotation
# 4) split_dataset -> 5) save_dataset



"""
v)	[Data 구성] : 각각의 XXX_data는 모두 동일한 규칙을 가지고 있습니다.
(1)	각 변수는 
> TorchRunner의 경우 모두 길이 4의 list 구조입니다. 
   (len(train_data) = 4)
> KerasRunner의 경우 모두 길이 2의 list 구조입니다.
(2)	각 index에는 해당되는 data의 개수만큼 들어있습니다. 
(학습 이미지가 10000장일 경우 : len(train_data[0]) = 10000)
(3)	0번 index에는 입력 X 값(image path)이 들어있습니다.
Keras Runner에서는 Image file을 읽은 채로 출력되기 때문에, numpy.ndarray 형태의 raw image array가 출력됩니다.
(4)	1번 index에는 라벨 Y값(bbox, segmented label color map 등)이 들어있습니다.
(a)	case. Detection : [category_id,  center_x(relat), center_y(relat), width(relat), height(relat)] 순으로 구성됩니다. 
여기서 relat은 상대 좌표(relative coordinate)를 의미합니다.
(5)	2번 index에는 width 값(이미지의 가로 길이, column 수)이 들어있습니다.
> Keras Runner에서는 존재하지 않습니다!
(6)	3번 index에는 height 값(이미지의 세로 길이, row 수)이 들어있습니다.
> Keras Runner에서는 존재하지 않습니다!

"""
class Dataset(Json): # JSON 파일 상속 받으면서, Setattr 를 다 해줌. => ds-300.json 등의 것을
    def __init__(self):
        super().__init__()
        self.user_id: str = None
        self.annotation_id: str = None
        
        self.root_folder: str = ""
        self.dataset_name: str = ""
        self.description: str = ""

        self.text: str = ""

        self.all_df, self.train_df, self.valid_df, self.test_df = \
            None, None, None, None 
        self.all_list, self.train_list, self.valid_list, self.test_list = \
            None, None, None, None


    def load_by_id(self, dataset_id, root_path=None):
        """dataset.py의 핵심적인 함수.
        [1] TABLE (neutable)
        - all_table, train_table, valid_table, test_table : 입력 데이터의 경로(string)
        - all_df, train_df, valid_df, test_df : load_data의 출력. 실제 데이터 정보가 들어있음.

        [2] Image (neuannotation)
        - all_annotation, train_annotation, valid_annotation, test_annotation : 입력 데이터의 경로(string)
        - all_list, train_list, valid_list, test_list : load_data의 출력. 실제 데이터 정보가 들어있음.
        """
        all_data, train_data, valid_data, test_data = None, None, None, None
        
        fpath = dataset_fpath(dataset_id)
        self.load(fpath) # get attr load
        
        # 2023-01-10: dataset json 파일에는 dataset_id 존재하지 않음
        # job (instruction) 에서 주어진 값으로 설정한다
        self.dataset_id = dataset_id # mongodb object ID

        # path 기반 데이터 로드
        if self.get_dataset_type() == "TABLE":
            self.table = Table(dataset_id,
                             self.get_dataset_type(),
                             self.get_problem_type(),
                             root_path=getattr(self, "root_path", ""),
                             table_meta = {})
            # TABLE - load_Data - 경로가지고 load_data 함.
            all_data, train_data, valid_data, test_data = \
                self.table.load_data(getattr(self, "all_table", ''), # path
                                     getattr(self, "train_table", ''),
                                     getattr(self, "valid_table", ''),
                                     getattr(self, "test_table", ''))
            # all data가 
            assert (type(all_data).__name__ == 'DataFrame' or \
                   (type(train_data).__name__ == 'DataFrame' and 
                    type(valid_data).__name__ == 'DataFrame' and 
                    type(test_data).__name__ == 'DataFrame')
                   ) is True, f"[dataset.load_by_id] is loaded None state."

        elif self.get_dataset_type() in ["IMAGE", "SOUND"]:
            if self.user_id and self.annotation_id:  # for service
                self.root_folder = dataset_folder(root_path=root_path)
                self.ann = Annotation(
                    dataset_id,
                    self.get_dataset_type(),
                    self.get_problem_type(),
                    self.root_folder,
                    annotation_path=os.path.split(fpath)[0],
                )
            else:  # for engineer
                self.root_folder = os.path.join(
                    dataset_folder(ds_id=self.dataset_id), self.root_path
                )
                self.ann = Annotation(
                    dataset_id,
                    self.get_dataset_type(),
                    self.get_problem_type(),
                    self.root_folder,
                    annotation_path=os.path.split(fpath)[0],
                )

            all_data, train_data, valid_data, test_data = \
                self.ann.load_data(getattr(self,"all_annotation", ''),
                                   getattr(self, "train_annotation", ''),
                                   getattr(self, "valid_annotation", ''),
                                   getattr(self, "test_annotation", ''))
            assert (type(all_data).__name__ == 'dict' or \
                   (type(train_data).__name__ == 'dict' and
                    type(valid_data).__name__ == 'dict' and
                    type(test_data).__name__ == 'dict')
                   ) is True, f"[dataset.load_by_id] is loaded None state."

            _temporary = all_data if all_data is not None else train_data

            if 'info' in list(_temporary.keys()) and 'licenses' in list(_temporary.keys()) and _temporary['info']['description'] == 'NeuralWorks_COCODataset':
                self.ann.parse_category(_temporary['categories'])
            else:
                self.ann.parse_category(_temporary['category'])
        elif self.get_dataset_type() == "TEXT":
            root_path = getattr(self, "root_path", None) # 실제 환경에는 존재. mongoDB
            folder = dataset_folder(root_path=root_path, ds_id=self.dataset_id)
            filename = f"{self.dataset_id}.txt"
            filepath = os.path.join(folder, filename)
            logger.info(f"[TEXT] Loading: {filepath}")
            try:
                with open(filepath) as fp:
                    self.text = fp.read()
            except:
                logger.error(f"[TEXT] failed: {filepath}")
                self.text = ""
            return
        else:
            raise ValueError(f"dataset_type={self.get_dataset_type()} is invalid.")

        # csv 데이터 로드
        self.load_data(all_data, train_data, valid_data, test_data)

    def load_by_dict(self, json_data):
        return self.load_dict(json_data)

    def load_data(self, all_data=None, train_data=None, valid_data=None, test_data=None):
        problem_type = self.get_problem_type()
        dataset_type = self.get_dataset_type()
        assert all_data is not None or (train_data is not None and test_data is not None), \
            f"You should have [all dataset] or [train/test dataset]."

        if self.get_dataset_type() == 'IMAGE':
            if all_data and not train_data:
                self.all_list = self.ann.parse_dataset(all_data, problem_type=problem_type, dataset_type=dataset_type)
            elif not all_data and train_data and valid_data:
                self.train_list = self.ann.parse_dataset(train_data, problem_type=problem_type, dataset_type=dataset_type)
                self.valid_list = self.ann.parse_dataset(valid_data, problem_type=problem_type, dataset_type=dataset_type)
                self.test_list = self.ann.parse_dataset(test_data, problem_type=problem_type, dataset_type=dataset_type)

        elif self.get_dataset_type() == 'TABLE':
            self.all_df = all_data
            self.train_df = train_data
            self.valid_df = valid_data
            self.test_df = test_data

        else:
            raise NotImplementedError(f"[{self.get_dataset_type()}] is not supported yet.")

    ############################ set, get function #############################

    def get_root_folder(self):
        return self.root_folder

    def get_data(self):
        return self.data_id
    
    def get_dataset_id(self):
        return getattr(self, "dataset_id")

    def get_data_path(self):
        return self.data_path
    
    def dataset_folder(self):
        # 2023-01-10: dataset json 파일에는 dataset_id 존재하지 않음
        # job (instruction) 에서 주어진 값으로 설정됨 -- dataset.py load_by_id() 
        dataset_id =  getattr(self, "dataset_id")
        return dataset_folder(ds_id = dataset_id) 

    def get_dataset_type(self):
        return getattr(self, "dataset_type", "UNKNOWN").upper()

    def get_problem_type(self):
        return getattr(self, "problem_type", "UNKNOWN").upper()

    def get_class_weights(self, labels):
        return calculate_class_weights(labels)

    def get_num_of_class(self):
        return self.ann.n_classes

    def get_name_of_class(self, type='list'):
        if type == 'list':
            return self.ann.category_names
        elif type == 'dict':
            return self.ann.category_id_to_name
        else:
            raise ValueError(f"Call type {type} is invalid value.")

    def get_colormap(self, type='list'):
        if type == 'list':
            return self.ann.colormap
        elif type == 'dict':
            return self.ann.colormap_dict
        else:
            raise ValueError(f"Call type {type} is invalid value.")

    def set_shapes(self, width, height):
        self.img_height = height
        self.img_width = width

    # === job -> set/get csv columns method ===
    def set_columns(self, input_columns, output_columns):
        self.input_columns = input_columns
        self.output_columns = output_columns

    def get_columns(self):
        return self.date_columns + self.input_columns + self.output_columns
    
    ##
    def get_label_index(self, label_name):
        """_summary_
        Args:
            label_name (_type_): _description_
        Returns:
            _type_: int. label_index
        """
        try:
            return self.ann.get_category_id(label_name)
        except:
            return 0
        

    ############################ return data ###################################
    def train_data(self):
        if self.get_dataset_type() == 'IMAGE':
            return self.train_list
            
        elif self.get_dataset_type() == 'TABLE':
            try:
                result_DF = pd.concat([self.train_df[self.date_columns],
                                       self.train_df[self.input_columns],
                                       self.train_df[self.output_columns]],
                                      axis=1)
                return result_DF
            except:
                return self.train_df

        elif self.get_dataset_type() == 'TEXT':
            return self.text

        elif self.get_dataset_type() == 'SOUND':
            pass

    def valid_data(self):
        if self.get_dataset_type() == 'IMAGE':
            return self.valid_list
        elif self.get_dataset_type() == 'TABLE':
            try:
                result_DF = pd.concat([self.valid_df[self.date_columns],
                                       self.valid_df[self.input_columns],
                                       self.valid_df[self.output_columns]],
                                      axis=1)
                return result_DF
            except:
                return self.valid_df
        elif self.get_dataset_type() == 'TEXT':
            return ""
        elif self.get_dataset_type() == 'SOUND':
            pass

    def test_data(self):
        if self.get_dataset_type() == 'IMAGE':
            return self.test_list
        elif self.get_dataset_type() == 'TABLE':
            try:
                result_DF = pd.concat([self.test_df[self.date_columns],
                                       self.test_df[self.input_columns],
                                       self.test_df[self.output_columns]],
                                      axis=1)
                return result_DF
            except:
                return self.test_df
        elif self.get_dataset_type() == 'TEXT':
            return ""
        elif self.get_dataset_type() == 'SOUND':
            pass

    # Timeseries - DL Create Window sliding Data
    def create_window_dataset(self, data, label, window_size):
        feature_list, label_list = [], []
        for i in range(len(data) - window_size):
            feature_list.append(np.array(data[i:i+window_size]))
            label_list.append(np.array(label[i+window_size]))
        return np.array(feature_list), np.array(label_list)

    # Timeseries - DL Create Window Sliding Data - for predict
    def create_window_dataset_for_predict(self, data, window_size):
        feature_list = []
        for i in range(len(data) - window_size):
            feature_list.append(np.array(data[i:i+window_size]))
        return np.array(feature_list)

    ############################ Split data & Save dataset ######################
    def split_dataset(self, train_ratio, valid_ratio, test_ratio, dataset_type='IMAGE', problem_type='', random_seed=None):
        # Image or CSV 
        if (self.all_list is not None and (self.train_list is None and self.valid_list is None and self.test_list is None)) or \
           (self.all_df is not None and (self.train_df is None and self.valid_df is None and self.test_df is None)): # CSV 
            
            is_shuffle = True if problem_type != "TIMESERIES" else False
            all_data = self.all_list if dataset_type == 'IMAGE' else self.all_df

            print(" -> Split Dataset...")
            print(f"\n -> Dataset type : {dataset_type} | Model problem type : {problem_type}")
            print(f" -> Want to shuffle? : {is_shuffle}")
            print(f" -> train_ratio: {train_ratio} | valid_ratio: {valid_ratio} | test_ratio: {test_ratio}\n")

            train_data, valid_data, test_data = None, None, None

            if dataset_type == 'IMAGE':
                datafield_count = len(all_data)
                # shuffle routine ==========================================================
                new_dataset = []
                for datazip in zip(*[all_data[i] for i in range(0, datafield_count)]):
                    new_dataset.append(list(datazip))

                if is_shuffle:     # shuffle 선택 시: shuffle 동작 수행.
                    if random_seed is not None:
                        random.seed(random_seed)
                    random.shuffle(new_dataset)

                elems = []
                for _ in range(0, datafield_count):
                    elems.append([])

                for dataset in new_dataset:
                    for idx in range(0, datafield_count):
                        elems[idx].append(dataset[idx])

                # ==========================================================================
                assert int(sum([len(elems[x]) for x in range(0, datafield_count)]) / datafield_count) == len(elems[0]), \
                    f"Some of Dataset field was missed! The list {[len(elems[x]) for x in range(0, datafield_count)]} should has same number."

                N = len(elems[0])
                trainset = math.floor(N * train_ratio)
                validset = trainset + math.floor(N * valid_ratio)

                train_data = [elems[x][:trainset] for x in range(0, datafield_count)]
                valid_data = [elems[x][trainset:validset] for x in range(0, datafield_count)]
                test_data = [elems[x][validset:] for x in range(0, datafield_count)]

            elif dataset_type == 'TABLE':
                train_data, valid_data, test_data = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
                if is_shuffle:
                    all_data = all_data.sample(frac=1, random_state=random_seed).reset_index(drop=True)

                trainset = int(len(all_data) * train_ratio)
                validset = int(len(all_data) * valid_ratio)
                testset = int(len(all_data) - (trainset + validset))

                train_data = all_data.iloc[0:trainset, :]

                if validset != 0:
                    valid_data = all_data.iloc[trainset:trainset + validset, :]

                test_data = all_data.iloc[trainset + validset:, :]
            
            all_data_size = [len(all_data[0]), len(all_data)] if dataset_type == 'IMAGE' else len(all_data)
            train_data_size = [len(train_data[0]), len(train_data)] if dataset_type == 'IMAGE' else len(train_data)
            valid_data_size = [len(valid_data[0]), len(valid_data)] if dataset_type == 'IMAGE' else len(valid_data)
            test_data_size = [len(test_data[0]), len(test_data)] if dataset_type == 'IMAGE' else len(test_data)

            logger.info(f"-> FUNCTION: [split_dataset] - dataset_type: [{dataset_type}]")
            logger.info(f"-> All Dataset shape : {all_data_size}")
            logger.info(f"-> train, valid, test shape : {train_data_size}, {valid_data_size}, {test_data_size}")

            # split dataset 
            if dataset_type == 'IMAGE':
                self.train_list, self.valid_list, self.test_list = train_data, valid_data, test_data

            elif dataset_type == 'TABLE':
                self.train_df, self.valid_df, self.test_df = train_data, valid_data, test_data
            else:
                raise NotImplementedError(f"Dataset type: [{dataset_type}] is not supported yet.")
        else:
            logger.info("-> You don't have to split dataset. Your dataset is already splitted [train/valid/test].")

    def save_dataset(self, job_id, split_type):
        if split_type == 'list':
            save_list_dataset(self.train_list, self.valid_list, self.test_list, job_id,
                              problem_type=self.get_problem_type(),
                              category_dict=self.get_name_of_class(type='dict'),
                              dataset_type=self.get_dataset_type(),
                              root_path=self.get_root_folder())
        elif split_type == 'dataframe':
            save_dataframe_dataset(self.train_df, self.valid_df, self.test_df, job_id, dataset_type=self.get_dataset_type())
        else:
            # raise ValueError(f"split_type={split_type} is not supported.")
            # TEXT의 경우 split_type 정의되지 않음. 이 경우 그냥 통과 -- @daehee 2023-01-06
            pass

    def info(self):
        print("\n\n   [ DATASET INFORMATION ]")
        print("     - Dataset Name".ljust(20), " : ", self.dataset_name.ljust(20))
        print("     - Dataset Type".ljust(20), " : ", self.dataset_type.ljust(20))
        print("     - Problem Type".ljust(20), " : ", self.problem_type.ljust(20))
        print("     - Description".ljust(20), " : ", self.description.ljust(20), "\n\n")


############################ Save data ###################################
def save_list_dataset(train_list, valid_list, test_list, job_id, problem_type, category_dict, dataset_type='IMAGE', root_path=''):
    assert len(train_list[0]) == len(train_list[1]) == len(train_list[2]), \
        f"Train Data count is different: {len(train_list[0])} {len(train_list[1])} {len(train_list[2])}."
    assert len(valid_list[0]) == len(valid_list[1]) == len(valid_list[2]), \
        f"Validation Data count is different: {len(valid_list[0])} {len(valid_list[1])} {len(valid_list[2])}."
    assert len(test_list[0]) == len(test_list[1]) == len(test_list[2]), \
        f"Test Data count is different: {len(test_list[0])} {len(test_list[1])} {len(test_list[2])}."

    train_datacount, valid_datacount, test_datacount = len(train_list[0]), len(valid_list[0]), len(test_list[0])

    logger.info(
        "\n -> Total dataset count: %i\n -> train count: %i | valid count: %i | test count: %i\n"
        % (train_datacount + valid_datacount + test_datacount, train_datacount, valid_datacount, test_datacount)
    )
    inv_category_dict = {v: k for k, v in category_dict.items()}

    save_list = []
    for elem in ['train', 'valid', 'test']:
        save_list.append(os.path.join(job_folder(job_id), f"{job_id}-{elem}.json"))

    for data_list, save_path in zip([train_list, valid_list, test_list], save_list):
        res_file, data, category = {}, [], []
        annotations = [] if problem_type != 'INSTANCE_SEGMENTATION' else {"detection": [],  "segmentation": []}

        if problem_type == "CLASSIFICATION":
            for i, elems in enumerate(zip(*data_list)):
                image_dict = {}
                image_dict["id"] = i
                image_dict["category_id"] = inv_category_dict[elems[1]]
                image_dict["file_name"] = elems[0].replace(root_path if root_path[-1] == '/' else root_path + '/', '')
                image_dict["width"] = elems[2]
                image_dict["height"] = elems[3]
                data.append(image_dict)

        elif problem_type == "DETECTION":
            for i, elems in enumerate(zip(*data_list)):
                image_dict = {}
                image_dict["id"] = i
                image_dict["file_name"] = elems[0].replace(root_path if root_path[-1] == '/' else root_path + '/', '')
                image_dict["width"] = elems[2]
                image_dict["height"] = elems[3]
                data.append(image_dict)

                for annot in elems[1]:
                    annot_dict = {}
                    annot_dict["id"] = len(annotations)
                    annot_dict["image_id"] = i
                    annot_dict["category_id"] = annot[0]
                    annot_dict["bbox"] = annot[1:]
                    annotations.append(annot_dict)

        elif problem_type == 'INSTANCE_SEGMENTATION':           # Only support COCO Dataset
            for i, elems in enumerate(zip(*data_list)):
                image_dict = {}
                image_dict["id"] = i
                image_dict["file_name"] = elems[0].replace(root_path if root_path[-1] == '/' else root_path + '/', '')
                image_dict["width"] = elems[2]
                image_dict["height"] = elems[3]
                data.append(image_dict)

                annot_det = elems[1]['detection']
                annot_seg = elems[1]['segmentation']

                for _d in annot_det:
                    detection_dict = {}
                    detection_dict['id'] = len(annotations['detection'])
                    detection_dict['image_id'] = i
                    detection_dict['category_id'] = _d[0]
                    detection_dict['bbox'] = _d[1:]
                    annotations['detection'].append(detection_dict)

                segmentation_dict = {}
                segmentation_dict['id'] = len(annotations['segmentation'])
                segmentation_dict['image_id'] = i
                segmentation_dict['file_name'] = annot_seg.replace(root_path if root_path[-1] == '/' else root_path + '/', '')
                annotations['segmentation'].append(segmentation_dict)

        elif problem_type == "SEGMENTATION":
            for i, elems in enumerate(zip(*data_list)):
                image_dict = {}
                annot_dict = {}

                image_dict["id"] = i
                image_dict["file_name"] = elems[0].replace(root_path if root_path[-1] == '/' else root_path + '/', '')
                image_dict["width"] = elems[2]
                image_dict["height"] = elems[3]
                data.append(image_dict)                

                annot_dict["id"] = i
                annot_dict["image_id"] = i
                annot_dict["file_name"] = elems[1].replace(root_path if root_path[-1] == '/' else root_path + '/', '')
                annotations.append(annot_dict)

        elif problem_type == "GENERATION":
            for i, elems in enumerate(zip(*data_list)):
                image_dict = {}
                image_dict["id"] = i
                image_dict["file_name"] = elems[0].replace(root_path if root_path[-1] == '/' else root_path + '/', '')
                image_dict["width"] = elems[1]
                image_dict["height"] = elems[2]
                data.append(image_dict)

        # Parsing - Category
        for k, v in category_dict.items():
            cat_dict = {}
            cat_dict["id"] = k
            cat_dict["name"] = v
            cat_dict["super_category"] = ""
            category.append(cat_dict)

        # Dump - Json file
        res_file["dataset_type"] = dataset_type
        res_file["category"] = category
        if dataset_type == 'IMAGE':
            res_file["images"] = data
        else:
            raise ValueError(f"dataset_type={dataset_type} is not supported.")
        res_file["annotations"] = annotations

        save_json(save_path, res_file)

def save_dataframe_dataset(train_df, valid_df, test_df, job_id, dataset_type='TABLE'):
    save_list = []
    for elem in ['train', 'valid', 'test']:
        save_list.append(os.path.join(job_folder(job_id), f"{job_id}-{elem}.csv"))

    for dataframe, save_path in zip([train_df, valid_df, test_df], save_list):
        dataframe.to_csv(save_path, index=False) # 원래 False


###
def get_pytorch_dataset():
    """
    neulib Dataset (dataset.py) 으로부터 pytorch Dataset class의 instance 만들어서 리턴해야 함
    """

###
if __name__ == "__main__":
    dataset = Dataset()
    dataset.load_by_id("ds-9123")
    dataset.print()  # JSON 정보 출력함. 그냥 JSON string으로 출력한다고 보면 됨.
    print(dir(dataset))  # dataset의 멤버 함수 같은것들 종류 알기위해서.
