"""
dataset.json 파일에는 메타정보만. 실제 이미지 파일들의 목록, label값 목록은 annotation.json 파일에 있다.

Example of annotation json file

ds-9123-all_anno.json 
------------------
{
  "type": "image_detection",
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
  "images": [
    {
      "id": 0,
      "file_name": "data/CHO-1_0_0.jpg",
      "width": 816,
      "height": 612
    },
    {
      "id": 1,
      "file_name": "data/CHO-1_0_1.jpg",
      "width": 816,
      "height": 612
    },
    ...
    "annotations": [
    {
      "id": 0,
      "image_id": 0,
      "category_id": 0,
      "bbox": [
        0.8492647058823529,
        0.39705882352941174,
        0.03676470588235294,
        0.049019607843137254
      ]
    },
    {
      "id": 1,
      "image_id": 0,
      "category_id": 1,
      "bbox": [
        0.9950980392156863,
        0.5310457516339869,
        0.03676470588235294,
        0.049019607843137254
      ]
    },
------------------    
"""
import collections
import random
import math
import os
import numpy as np
import pandas as pd
from neuenv import dataset_folder, job_folder
from neujson import load_json, save_json

import logging
logger = logging.getLogger(__name__)


class Annotation:
    def __init__(
        self,
        dataset_id,
        dataset_type='IMAGE',
        problem_type=None,
        root_path='',
        annotation_path: str = None,
    ):
        self.dataset_id = dataset_id
        self.dataset_type = dataset_type
        self.problem_type = problem_type
        self.root_path = root_path
        self.annotation_path = annotation_path

    def read_annotation_file(self, annotation_file_name: str = None):
        """
        annotation.json 파일을 읽어서 json 파싱하여 attribute 값만 설정. 본격전인 파싱은 아님
        neujson.py의 load_json() 이용.

        annotation.json 파일의 주요 필드들:
            "category"
            "images"
            "annotations" (label 정보, bbox 정보 등)
        """
        data_path = None

        if not annotation_file_name:
            annotation_file_name = "annotation.json"
        if self.annotation_path:
            data_path = os.path.join(self.annotation_path, annotation_file_name)
        else:
            data_path = os.path.join(
                dataset_folder(ds_id=self.dataset_id), annotation_file_name
            )
        logger.info(f"Annotation file : {os.path.basename(data_path)}")
        return load_json(data_path)
    
    def load_data(self, all_anno_file, train_anno_file, valid_anno_file, test_anno_file):
        """
        all_anno_file, train_anno_file, valid_anno_file, test_anno_file: 파일 이름.
        dataset.json 안의 필드 중에 아래 필드들의 값.
            "all_annotation": "ds-9123-all_anno.json",
            "train_annotation": "",
            "valid_annotation": "",
            "test_annotation": "",
        """
        all_annotation, train_annotation, valid_annotation, test_annotation = None, None, None, None

        if all_anno_file != '' and train_anno_file == '':
            all_annotation = self.read_annotation_file(all_anno_file)
        elif (all_anno_file == '' and train_anno_file != '' and valid_anno_file != '' and test_anno_file != ''):
            train_annotation = self.read_annotation_file(train_anno_file)
            valid_annotation = self.read_annotation_file(valid_anno_file)
            test_annotation = self.read_annotation_file(test_anno_file)
        else:
            raise ValueError("Missing Annotation field.")

        return all_annotation, train_annotation, valid_annotation, test_annotation

    ######################## parse function #################################
    def parse_images(self, images: list):
        """ dataset spec: "images" part 
        
       #### annotation for DETECTION
        "images": [
            {
            "id": 0,
            "file_name": "data/CHO-1_0_0.jpg",
            "width": 816,
            "height": 612
            },
            {
            "id": 1,
            "file_name": "data/CHO-1_0_1.jpg",
            "width": 816,
            "height": 612
            },
        
        #### annotation for CLASSIFICATION                        
        "images": [
            {
            "id": 0,
            "category_id": 0,
            "file_name": "alive/b_76934.jpg",
            "width": 40,
            "height": 40
            },
            {
            "id": 1,
            "category_id": 0,
            "file_name": "alive/b_56577.jpg",
            "width": 40,
            "height": 40
            },
                
        """

        # Return Image file's full path
        self.image_file_paths = [os.path.join(self.root_path, imginfo["file_name"]) for imginfo in images]
        self.image_file_ids = [imginfo["id"] for imginfo in images]
        
        width_list = [imginfo["width"] for imginfo in images]
        height_list = [imginfo["height"] for imginfo in images]
        self.image_sizes = list(zip(width_list, height_list))
        
        # dict: image id to image file path
        self.image_id_to_path = dict(zip(self.image_file_ids, self.image_file_paths))
        # dict: image path to image size (width, height)
        self.image_path_to_size = dict(zip(self.image_file_paths, self.image_sizes))
      

        if self.problem_type == "CLASSIFICATION":   
            self.image_label_ids = [imginfo["category_id"] for imginfo in images]
            self.image_label_names = [
                self.category_id_to_name[label_id] for label_id in self.image_label_ids
            ]
        
            return self.image_file_paths, self.image_label_names, width_list, height_list
        
        elif self.problem_type in ["DETECTION", "INSTANCE_SEGMENTATION", "SEGMENTATION", "GENERATION", "POSE"]:
            return self.image_file_paths
        
        else:
            raise ValueError(f"problem_type={self.problem_type} is not supported.")

    def parse_sounds(self, sounds):
        sound_files = [soundinfo["file_name"] for soundinfo in sounds]
        sound_ids = [soundinfo["id"] for soundinfo in sounds]
        sound_labels = []

        self.sound_dict = {
            soundid: soundfname for soundid, soundfname in zip(sound_ids, sound_files)
        }
        if self.problem_type == "CLASSIFICATION":
            sound_labels = [
                self.category_id_to_name[soundinfo["category_id"]] for soundinfo in sounds
            ]
        else:
            raise ValueError(f"problem_type={self.problem_type} is invalid.")
        return sound_files, sound_labels

    def parse_category(self, category_list):
        """ dataset spec: "category" part 
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
        ]
        
        --> self.category_id_to_name 에 저장
        """
        self.n_classes = len(category_list)
        # dict: category(label) id to name
        self.category_id_to_name = {
            cate["id"]: cate["name"] for cate in category_list
        }
        
        # dict: label name to id
        self.category_name_to_id = { cname: cid for cid, cname in self.category_id_to_name.items() }
        
        # id 값순으로 소트
        self.category_ids = sorted(self.category_id_to_name.keys())
        self.category_names = [self.category_id_to_name[cid] for cid in self.category_ids]
        

        if self.problem_type == "SEGMENTATION":
            self.colormap = [tuple(cate["colormap"]) for cate in category_list]
            self.colormap_dict = {
                color: name for color, name in zip(self.colormap, self.category_names)
            }

    def df_for_classification(self, data_files, data_labels, data_width=None, data_height=None, dataset_type='IMAGE'):
        if dataset_type == 'IMAGE':
            if data_width is None or data_height is None:
                raise ValueError(f"data_width=[{data_width}] or data_height=[{data_height}] value should be not None.")
            dataframe = pd.DataFrame(
                data=zip(data_files, data_labels, data_width, data_height),
                columns=["imgfpath", "label", "width", "height"],
            )
            return dataframe
        elif dataset_type == 'SOUND':
            dataframe = pd.DataFrame(
                        data=zip(data_files, data_labels), columns=["soundfpath", "label"]
                    )
            return dataframe
        else:
            raise ValueError(f"dataset_type={dataset_type} is not supported.")

    def parse_dataset(self, json_parsed, problem_type, dataset_type='IMAGE'):
        if problem_type == 'CLASSIFICATION':
            func = self.parse_for_classification
        elif problem_type == 'DETECTION':
            func = self.parse_for_detection
        elif problem_type == 'SEGMENTATION':
            func = self.parse_for_segmentation
        elif problem_type == 'INSTANCE_SEGMENTATION':
            func = self.parse_for_instance_segmentation
        elif problem_type == 'POSE':
            func = self.parse_for_pose
        elif problem_type == 'GENERATION':
            func = self.parse_for_generation
        
        data = func(json_parsed)

        return data

    def parse_for_classification(self, json_parsed, dataset_type='IMAGE'):
        if dataset_type == 'IMAGE':
            image_file_paths, image_label_names, width_list, height_list = self.parse_images(json_parsed["images"])
            return [image_file_paths, image_label_names, width_list, height_list]
        
        elif dataset_type == "SOUND":
            sound_files, sound_labels = self.parse_sounds(json_parsed["sounds"])
            dataframe = self.df_for_classification(sound_files, sound_labels, dataset_type=self.dataset_type)
            return dataframe
        
        else:
            raise ValueError(f"dataset_type={dataset_type} is invalid.")

    def parse_for_detection(self, json_parsed):
        image_file_paths = self.parse_images(json_parsed["images"])

        filenames, annotations, width_list, height_list = [], [], [], []
        annotation_dict = collections.defaultdict(list)

        for anno in json_parsed["annotations"]:
            imgfname = self.get_imgfname(anno["image_id"])

            category_id = anno["category_id"]
            val = [category_id, *list(map(float, anno["bbox"]))]

            annotation_dict[imgfname].append(val)
        filenames = [filename for filename in list(annotation_dict.keys())]
        annotations = list(annotation_dict.values())
        width_list = [
            self.get_imgsize(filename)[0] for filename in list(annotation_dict.keys())
        ]
        height_list = [
            self.get_imgsize(filename)[1] for filename in list(annotation_dict.keys())
        ]

        return (filenames, annotations, width_list, height_list)

    def parse_for_instance_segmentation(self, json_parsed):         # Only use COCO Dataset format
        image_file_paths = self.parse_images(json_parsed["images"])

        filenames, annotations, width_list, height_list = [], [], [], []
        annotation_dict = collections.defaultdict(list, {k: {"detection": [], "segmentation": []} for k in image_file_paths})

        # Detection
        for anno_det in json_parsed['annotations']['detection']:
            imgfname = self.get_imgfname(anno_det["image_id"])

            category_id = anno_det['category_id']
            detval = [category_id, *list(map(float, anno_det['bbox']))]

            annotation_dict[imgfname]['detection'].append(detval)
        
        for anno_seg in json_parsed['annotations']['segmentation']:
            imgfname = self.get_imgfname(anno_seg['image_id'])
            annotation_dict[imgfname]['segmentation'] = os.path.join(self.root_path, anno_seg['file_name'])
 
        filenames = [filename for filename in list(annotation_dict.keys())]
        # print(filenames)
        annotations = list(annotation_dict.values())
        width_list = [
            self.get_imgsize(filename)[0] for filename in list(annotation_dict.keys())
        ]
        height_list = [
            self.get_imgsize(filename)[1] for filename in list(annotation_dict.keys())
        ]

        """
        print(self.all_list[0][index])                    # filename : data/abc.jpg
        print(self.all_list[1][index]['detection'])       # bbox values : [[0, 0.1, 0.1, 0.2, 0.2], [14, 0.5, 0.5, 0.25, 0.25]]
        print(self.all_list[1][index]['segmentation'])    # segmentation colormap file : annotations/abc.png
        """

        return (filenames, annotations, width_list, height_list)

    def parse_for_segmentation(self, json_parsed):
        image_file_paths = self.parse_images(json_parsed["images"])

        filenames, annotations, width_list, height_list = [], [], [], []

        for anno in json_parsed["annotations"]:
            filenames.append(self.get_imgfname(anno["image_id"]))
            annotations.append(os.path.join(self.root_path, anno['file_name']))
            width_list.append(
                self.get_imgsize(self.get_imgfname(anno["image_id"]))[0]
            )
            height_list.append(
                self.get_imgsize(self.get_imgfname(anno["image_id"]))[1]
            )

        return (filenames, annotations, width_list, height_list)

    # @TODO
    def parse_for_pose(self, json_parsed):
        image_file_paths = self.parse_images(json_parsed["images"])

        filenames, annotations, width_list, height_list = [], [], [], []

        for anno in json_parsed["annotations"]:
            filenames.append(self.get_imgfname(anno["image_id"]))
            # annotations.append(os.path.join(self.))

    def parse_for_generation(self, json_parsed):
        image_file_paths = self.parse_images(json_parsed["images"])

        filenames = []
        # annotations = []
        width_list = []
        height_list = []

        for anno in json_parsed["images"]:
            filenames.append(self.get_imgfname(anno["id"]))
            # annotations.append(self.root_path + '/' + anno['file_name'])
            width_list.append(self.get_imgsize(self.get_imgfname(anno["id"]))[0])
            height_list.append(self.get_imgsize(self.get_imgfname(anno["id"]))[1])

        return (filenames, width_list, height_list)

    ############################### get function ##################################
    def annotation_list(self):
        return [(imgfname, vals) for imgfname, vals in self.annotation_dict.items()]

    def get_category_id(self, category_name):
        return self.category_name_to_id.get(category_name, -1)
    
    def get_colormap(self):
        return self.colormap

    def get_colormap_dict(self):
        return self.colormap_dict

    def get_imgfname(self, imgid):
        return self.image_id_to_path.get(imgid, -1)

    def get_imgsize(self, imgfname):
        return self.image_path_to_size.get(imgfname, (0,0))

    def get_num_of_class(self):
        return self.n_classes

    def get_name_of_class(self, type='list'):
        if type == 'list':
            return self.category_names
        elif type == 'dict':
            return self.category_id_to_name
        else:
            raise ValueError(f"Call type {type} is invalid value.")

    def get_json_file_path(self):
        return self.json_file_path

    def print(self):
        print(self.dataset_id, self.dataset_type, self.problem_type)
        print(self.category_name_to_id)
        print(self.annotation_path)
        
        if self.problem_type == "CLASSIFICATION":
            for path, label in zip(self.image_file_paths, self.image_label_names):
                print(path, label)
        
        
#####
def get_filelist_from_df(df):
    f_list = []
    for index, row in df.iterrows():
        f_list.append(row["soundfpath"])

    return f_list


#####
def get_sound_feature_from_df(df, root_folder):
    import librosa
    from keras.utils.np_utils import to_categorical
    from sklearn.preprocessing import LabelEncoder

    X = []
    Y = []
    lb = LabelEncoder()

    for index, row in df.iterrows():
        print("row", root_folder + "/" + row["soundfpath"])
        X2, sample_rate = librosa.load(
            root_folder + "/" + row["soundfpath"], res_type="kaiser_fast"
        )
        # extraccting Mel-Frequeny Cepstral Coeficients feature from data
        # y -> accepts time-series audio data; sr -> accepts sampling rate
        # n_mfccs -> no. of MFCCs to return
        mfccs = np.mean(librosa.feature.mfcc(y=X2, sr=sample_rate, n_mfcc=40).T, axis=0)
        X.append(mfccs)
        Y.append(row["label"])

    x = np.asarray(X)
    y = np.asarray(to_categorical(lb.fit_transform(Y)))

    # print(x.shape)
    # print(y.shape)

    return (x, y)


###########
if __name__ == "__main__":
    ann1 = Annotation("ds-9123", dataset_type="IMAGE", problem_type="DETECTION")
    all_data, train_data, valid_data, test_data = ann1.load_data("ds-9123-all_anno.json", "", "", "")
    data1 = all_data if all_data is not None else train_data
    ann1.parse_category(data1['category'])
    
    ann1.print()
