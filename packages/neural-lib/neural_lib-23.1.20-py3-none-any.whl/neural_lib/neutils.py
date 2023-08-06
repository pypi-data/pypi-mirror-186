import json
import os
import numpy as np
import math
from matplotlib import pyplot as plt
import neuenv
from PIL import Image
import re
import cv2
from job import job_status_fpath

import logging
logger = logging.getLogger(__name__)

# Lambda에서 cv2 임포트 에러를 피하기 시도하는 접근.
# Refactor, 어디에 두는게 좋을 지 몰라서 일단 여기에 선언
def module_exists(module_name):
    logger.info(f"Module name to import: [{module_name}]")
    try:
        logger.info(f"Trying import module : [{module_name}]")
        __import__(module_name)
        logger.info(f"module [{module_name}] is imported successfully!")
    except ImportError as E:
        logger.info(E)
        logger.exception(E)
        return False
    else: # lambda가 아닌 다른 환경에서 실행
        from job import job_status_fpath
        return True

module_exists("cv2")


regex_pattern = re.compile("((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))")
class JsonModel:
    @classmethod
    def to_camel(cls, payload: dict):
        def convert(key: str):
            camel_key = "".join(word.capitalize() for word in key.split("_"))
            return camel_key[0].lower() + camel_key[1:]

        if isinstance(payload, dict):
            new_dict = {}
            for key, value in payload.items():
                value = cls.to_camel(value)
                new_dict[convert(key)] = value
            return new_dict

        if isinstance(payload, list):
            new_list = []
            for value in payload:
                new_list.append(cls.to_camel(value))
            return new_list

        return payload

    @classmethod
    def to_snake(cls, payload: dict):
        def convert(key: str):
            snake_key = regex_pattern.sub(r"_\1", key).lower()
            return snake_key

        if isinstance(payload, dict):
            new_dict = {}
            for key, value in payload.items():
                value = cls.to_snake(value)
                new_dict[convert(key)] = value
            return new_dict

        if isinstance(payload, list):
            new_list = []
            for value in payload:
                new_list.append(cls.to_snake(value))
            return new_list

        return payload



class convert_coordinate(object):
    def __init__(
        self, coordinate, img_shape, input_coord, input_type, output_coord, output_type
    ):
        # img_shape = (height, width) 이미지의 세로/가로
        """
        Arguments:
        1) coordinate : bbox coordinate
        2) img_shape = (height, width)
        3) input_coord = ['ccwh', 'xyrb', 'xywh']
        4) input_type = ['relat', 'abs']
        5) output_coord = ['ccwh', 'xyrb', 'xywh']
        6) output_type = ['relat', 'abs']
        return:
        converted coordinate, self.result

        example:
        answer = convert_coordinate(bbox, img_shape=(480, 640),
                                    input_coord='ccwh', input_type='relat',
                                    output_coord='xyrb', output_type='abs')
        """

        self.coord = [
            float(coordinate[0]),
            float(coordinate[1]),
            float(coordinate[2]),
            float(coordinate[3]),
        ]
        self.ih = int(img_shape[0])
        self.iw = int(img_shape[1])
        self.input_coord = input_coord
        self.input_type = input_type
        self.output_coord = output_coord
        self.output_type = output_type

        self.converted_type = self.convert_type(
            self.coord, self.input_type, self.output_type
        )
        self.converted_coord = self.convert_coord(
            self.converted_type, self.input_coord, self.output_coord
        )
        self.result = list(map(float, self.converted_coord)) if output_type == 'relat' else list(map(int, self.converted_coord))

    def __call__(self):
        return self.result

    def convert_type(self, coord, input_type, output_type):
        """
        coordinate type만 변경.
        1) relat(상대 좌표) to abs(절대 좌표)
        2) abs(절대 좌표) to relat(상대 좌표)
        """
        result = []

        if input_type != output_type:
            if input_type == "relat" and output_type == "abs":
                result = [
                    int(coord[0] * self.iw),
                    int(coord[1] * self.ih),
                    int(coord[2] * self.iw),
                    int(coord[3] * self.ih),
                ]
            elif input_type == "abs" and output_type == "relat":
                result = [
                    round(coord[0] / self.iw, 5),
                    round(coord[1] / self.ih, 5),
                    round(coord[2] / self.iw, 5),
                    round(coord[3] / self.ih, 5),
                ]

        elif input_type == output_type:
            result = coord

        return result

    def convert_coord(self, coord, input_coord, output_coord):
        """
        coordinate system을 변경.

        [대상 인자]
        1) ccwh : center_x, center_y, width, height
        2) xyrb : xmin, ymin, xmax, ymax
        3) xywh : xmin, ymin, width, height
        """
        result = []

        if input_coord != output_coord:
            if input_coord == "ccwh":
                center_x = coord[0]
                center_y = coord[1]
                width = coord[2]
                height = coord[3]

                if output_coord == "xywh":
                    result = [
                        center_x - (width / 2),
                        center_y - (height / 2),
                        width,
                        height,
                    ]
                elif output_coord == "xyrb":
                    result = [
                        center_x - (width / 2),
                        center_y - (height / 2),
                        center_x + (width / 2),
                        center_y + (height / 2),
                    ]
            elif input_coord == "xywh":
                xmin = coord[0]
                ymin = coord[1]
                width = coord[2]
                height = coord[3]

                if output_coord == "ccwh":
                    result = [xmin + (width / 2), ymin + (height / 2), width, height]
                elif output_coord == "xyrb":
                    result = [xmin, ymin, xmin + width, ymin + height]

            elif input_coord == "xyrb":
                xmin = coord[0]
                ymin = coord[1]
                xmax = coord[2]
                ymax = coord[3]

                width = xmax - xmin
                height = ymax - ymin

                if output_coord == "ccwh":
                    result = [xmin + (width / 2), ymin + (height / 2), width, height]
                elif output_coord == "xywh":
                    result = [xmin, ymin, width, height]

        elif input_coord == output_coord:
            result = coord

        return result


class CustomGetMetricCallback(object):
    """
    Metric 작성(in job-XXX-status.json)

    - runner_XXXXX.py에서 객체 생성 후(보통 torch가 될 것) fit 당시에 param으로 넘겨주는 형식.
    - 실제 모델 code에서 사용 당시
        epoch = 기록할 epoch 값
        metrics = [[train_metric], [valid_metric]]
        metrics_name = [[train_metric_name], [valid_metric_name]]

    example:
    my_getmetric.save_status(epoch + 1,
                             metrics=[[round(mloss.cpu().numpy().tolist()[3], 4), round(mloss.cpu().numpy().tolist()[0], 4)],   # train metric
                                      [round(loss, 4), round(mAP, 4)]],                                                         # validation metric
                             metrics_name=[['total_loss', 'bbox_loss'],                                                         # train metric name
                                           ['total_loss', 'mAP']])                                                              # validation metric name
    """

    def __init__(self, job):
        self.job = job

    def save_status(self, epoch, metrics=[], metrics_name=[]):
        # train_metrics_name = valid_metrics_name = self.metrics
        # Metrics 정제 과정
        if len(metrics) == 2 and (
            isinstance(metrics[0], list) and isinstance(metrics[1], list)
        ):
            train_metric = metrics[0]
            valid_metric = metrics[1]
        else:
            train_metric = metrics
            valid_metric = []

        train_metric = (
            [train_metric] if not isinstance(train_metric, list) else train_metric
        )
        valid_metric = (
            [valid_metric] if not isinstance(valid_metric, list) else valid_metric
        )

        # Metrics_name 정제 과정
        if len(metrics_name) == 2 and (
            isinstance(metrics_name[0], list) and isinstance(metrics_name[1], list)
        ):
            train_metric_name = metrics_name[0]
            valid_metric_name = metrics_name[1]
        else:
            train_metric_name = valid_metric_name = metrics_name

        train_metric_name = (
            [train_metric_name]
            if not isinstance(train_metric_name, list)
            else train_metric_name
        )
        valid_metric_name = (
            [valid_metric_name]
            if not isinstance(valid_metric_name, list)
            else valid_metric_name
        )

        for index, metric in enumerate(train_metric):
            if math.isnan(metric):
                train_metric[index] = "NaN"
        for index, metric in enumerate(valid_metric):
            if math.isnan(metric):
                valid_metric[index] = "NaN"

        # Dictionary type으로 변경 과정
        my_train_metric = {
            name: value for name, value in zip(train_metric_name, train_metric)
        }
        my_valid_metric = (
            {name: value for name, value in zip(valid_metric_name, valid_metric)}
            if len(valid_metric) != 0
            else {}
        )

        logger.info(
            "Metric Name is changed in [CustomGetMetricCallback function]\n: {}".format(
                (train_metric_name, valid_metric_name)
            )
        )

        self.job.add_train_metric(epoch, my_train_metric, my_valid_metric)
        print(
            " -> Added train metric > Epoch {} metrics [train: {}, valid: {}]".format(
                epoch, my_train_metric, my_valid_metric
            )
        )
        self.job.save_status()
        print(
            " -> {}-status.json is saved in {}".format(
                self.job.job_id, job_status_fpath(self.job.job_id)
            )
        )


class CustomSaveBestWeightCallback(object):
    """
    Best weight(best.pt, best.hdf5) 저장하기 위함

    - runner_XXXXX.py에서 객체 생성 후(보통 torch가 될 것) fit 당시에 param으로 넘겨주는 형식.
    - 실제 모델 code에서 사용 당시
        model = 저장할 model 객체
        model_metric = best epoch임을 판별하기 위해 비교 가능한 변수(val_loss, mAP 등) -> init val : inf / -inf
        compared = 해당 model_metric이 더 작아야 best 인지 더 커야 best 인지 판별하기 위함. ('less'/'more')
        lib = weight 저장 형식이 'KERAS'(=.hdf5) 인지 'TORCH'(=.pt) 인지 알려줌

    example:
    my_savebestweight.save_best_weight(model=self, model_loss=avg_mAP, compared='more', lib='TORCH')
    """

    def __init__(self, job):
        self.job = job
        self.valid_metric = False

    def save_best_weight(self, model=None, model_metric=0.0, compared="less", lib="TORCH"):
        import torch

        # self.valid_metric initializing
        if self.valid_metric == False:
            if compared == "less":
                self.valid_metric = float("inf")
            elif compared == "more":
                self.valid_metric = float("-inf")

        if model is not None:
            self.model = model

        self.save_path = self.job.best_weight_fpath(lib=lib)

        if compared == "less" and model_metric < self.valid_metric:
            logger.info(f"-> The model metric {model_metric} is less than the previous metric {self.valid_metric}")
            print("==========> model weight file(best.pt) is saved in {}\n".format(self.save_path))

            if lib == "KERAS":
                self.model.save_weights(self.save_path)
                if self.job.user_id is not None:
                    save_rootpath = os.path.join("/datasets", "Users", self.job.user_id, "Weights", self.job.job_id, str(self.job.job_id) + "-best.hdf5")
                    save_rootpath_dirname = os.path.dirname(save_rootpath)
                    if not os.path.isdir(save_rootpath_dirname):
                        os.makedirs(save_rootpath_dirname, exist_ok=True)
                    self.mode.save_weights(save_rootpath)
            elif lib == "TORCH":
                # (DC) Old way
                torch.save(self.model, self.save_path)
                if self.job.user_id is not None:
                    save_rootpath = os.path.join("/datasets", "Users", self.job.user_id, "Weights", self.job.job_id, str(self.job.job_id) + "-best.pt")
                    save_rootpath_dirname = os.path.dirname(save_rootpath)
                    if not os.path.isdir(save_rootpath_dirname):
                        os.makedirs(save_rootpath_dirname, exist_ok=True)
                    torch.save(self.model, save_rootpath)

                # (DC) new way
                # torch.save(self.model.state_dict(), self.save_path)
            self.job.add_result_best_weight()
            self.valid_metric = model_metric

        elif compared == "more" and model_metric > self.valid_metric:
            logger.info(f"-> The model metric {model_metric} is greater than the previous metric {self.valid_metric}")
            print("==========> model weight file(best.pt) is saved in {}\n".format(self.save_path))
            
            if lib == "KERAS":
                self.model.save_weights(self.save_path)
                if self.job.user_id is not None:
                    save_rootpath = os.path.join("/datasets", "Users", self.job.user_id, "Weights", self.job.job_id, str(self.job.job_id) + "-best.hdf5")
                    save_rootpath_dirname = os.path.dirname(save_rootpath)
                    if not os.path.isdir(save_rootpath_dirname):
                        os.makedirs(save_rootpath_dirname, exist_ok=True)
                    self.mode.save_weights(save_rootpath)
            elif lib == "TORCH":
                # (DC) old way
                torch.save(self.model, self.save_path)
                if self.job.user_id is not None:
                    save_rootpath = os.path.join("/datasets", "Users", self.job.user_id, "Weights", self.job.job_id, str(self.job.job_id) + "-best.pt")
                    save_rootpath_dirname = os.path.dirname(save_rootpath)
                    if not os.path.isdir(save_rootpath_dirname):
                        os.makedirs(save_rootpath_dirname, exist_ok=True)
                    torch.save(self.model, save_rootpath)

                # (DC) new way
                # torch.save(self.model.state_dict(), self.save_path)
            self.job.add_result_best_weight()
            self.valid_metric = model_metric

        else:
            logger.info(f"The model metric {model_metric} is worse than the previous metric {self.valid_metric}\n")


class CustomEarlyStopping(object):
    def __init__(self, patience=10, verbose=False, delta=0):
        """
        Args:
            patience (int): validation loss가 개선된 후 기다리는 기간
                            Default: 7
            verbose (bool): True일 경우 각 validation loss의 개선 사항 메세지 출력
                            Default: False
            delta (float): 개선되었다고 인정되는 monitered quantity의 최소 변화
                            Default: 0
            path (str): checkpoint저장 경로
                            Default: 'checkpoint.pt'
        """
        self.patience = patience
        self.verbose = verbose
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.val_loss_min = np.Inf
        self.delta = delta

    def __call__(self, val_loss):
        score = -val_loss

        if self.best_score is None:
            self.best_score = score

        elif score < self.best_score + self.delta:
            self.counter += 1
            logger.info(f'-> EarlyStopping counter: now [{self.counter}] out of patience [{self.patience}] | Now Best Score : [{self.best_score}]')

            if self.counter >= self.patience:
                self.early_stop = True

        else:
            self.best_score = score
            self.counter = 0


def get_colormap(count=256, cmap_type="pascal"):
    """Creates a label colormap used in PASCAL VOC segmentation benchmark.
    Returns:
        A colormap for visualizing segmentation results.
    """

    def bit_get(val, idx):
        """Gets the bit value.
        Args:
            val: Input value, int or numpy int array.
            idx: Which bit of the input val.
        Returns:
            The "idx"-th bit of input val.
        """
        return (val >> idx) & 1

    cmap_type = cmap_type.lower()
    if cmap_type == "voc" or cmap_type == "coco":
        cmap_type = "pascal"

    if cmap_type == "pascal":
        colormap = np.zeros((count, 3), dtype=int)
        ind = np.arange(count, dtype=int)

        for shift in reversed(list(range(8))):
            for channel in range(3):
                colormap[:, channel] |= bit_get(ind, channel) << shift
            ind >>= 3

        return colormap

    elif cmap_type == "cityscape":
        colormap = np.zeros((256, 3), dtype=np.uint8)
        colormap[0] = [128, 64, 128]
        colormap[1] = [244, 35, 232]
        colormap[2] = [70, 70, 70]
        colormap[3] = [102, 102, 156]
        colormap[4] = [190, 153, 153]
        colormap[5] = [153, 153, 153]
        colormap[6] = [250, 170, 30]
        colormap[7] = [220, 220, 0]
        colormap[8] = [107, 142, 35]
        colormap[9] = [152, 251, 152]
        colormap[10] = [70, 130, 180]
        colormap[11] = [220, 20, 60]
        colormap[12] = [255, 0, 0]
        colormap[13] = [0, 0, 142]
        colormap[14] = [0, 0, 70]
        colormap[15] = [0, 60, 100]
        colormap[16] = [0, 80, 100]
        colormap[17] = [0, 0, 230]
        colormap[18] = [119, 11, 32]

        return colormap

    elif cmap_type == "ade20k":
        return np.asarray(
            [
                [0, 0, 0],
                [120, 120, 120],
                [180, 120, 120],
                [6, 230, 230],
                [80, 50, 50],
                [4, 200, 3],
                [120, 120, 80],
                [140, 140, 140],
                [204, 5, 255],
                [230, 230, 230],
                [4, 250, 7],
                [224, 5, 255],
                [235, 255, 7],
                [150, 5, 61],
                [120, 120, 70],
                [8, 255, 51],
                [255, 6, 82],
                [143, 255, 140],
                [204, 255, 4],
                [255, 51, 7],
                [204, 70, 3],
                [0, 102, 200],
                [61, 230, 250],
                [255, 6, 51],
                [11, 102, 255],
                [255, 7, 71],
                [255, 9, 224],
                [9, 7, 230],
                [220, 220, 220],
                [255, 9, 92],
                [112, 9, 255],
                [8, 255, 214],
                [7, 255, 224],
                [255, 184, 6],
                [10, 255, 71],
                [255, 41, 10],
                [7, 255, 255],
                [224, 255, 8],
                [102, 8, 255],
                [255, 61, 6],
                [255, 194, 7],
                [255, 122, 8],
                [0, 255, 20],
                [255, 8, 41],
                [255, 5, 153],
                [6, 51, 255],
                [235, 12, 255],
                [160, 150, 20],
                [0, 163, 255],
                [140, 140, 140],
                [250, 10, 15],
                [20, 255, 0],
                [31, 255, 0],
                [255, 31, 0],
                [255, 224, 0],
                [153, 255, 0],
                [0, 0, 255],
                [255, 71, 0],
                [0, 235, 255],
                [0, 173, 255],
                [31, 0, 255],
                [11, 200, 200],
                [255, 82, 0],
                [0, 255, 245],
                [0, 61, 255],
                [0, 255, 112],
                [0, 255, 133],
                [255, 0, 0],
                [255, 163, 0],
                [255, 102, 0],
                [194, 255, 0],
                [0, 143, 255],
                [51, 255, 0],
                [0, 82, 255],
                [0, 255, 41],
                [0, 255, 173],
                [10, 0, 255],
                [173, 255, 0],
                [0, 255, 153],
                [255, 92, 0],
                [255, 0, 255],
                [255, 0, 245],
                [255, 0, 102],
                [255, 173, 0],
                [255, 0, 20],
                [255, 184, 184],
                [0, 31, 255],
                [0, 255, 61],
                [0, 71, 255],
                [255, 0, 204],
                [0, 255, 194],
                [0, 255, 82],
                [0, 10, 255],
                [0, 112, 255],
                [51, 0, 255],
                [0, 194, 255],
                [0, 122, 255],
                [0, 255, 163],
                [255, 153, 0],
                [0, 255, 10],
                [255, 112, 0],
                [143, 255, 0],
                [82, 0, 255],
                [163, 255, 0],
                [255, 235, 0],
                [8, 184, 170],
                [133, 0, 255],
                [0, 255, 92],
                [184, 0, 255],
                [255, 0, 31],
                [0, 184, 255],
                [0, 214, 255],
                [255, 0, 112],
                [92, 255, 0],
                [0, 224, 255],
                [112, 224, 255],
                [70, 184, 160],
                [163, 0, 255],
                [153, 0, 255],
                [71, 255, 0],
                [255, 0, 163],
                [255, 204, 0],
                [255, 0, 143],
                [0, 255, 235],
                [133, 255, 0],
                [255, 0, 235],
                [245, 0, 255],
                [255, 0, 122],
                [255, 245, 0],
                [10, 190, 212],
                [214, 255, 0],
                [0, 204, 255],
                [20, 0, 255],
                [255, 255, 0],
                [0, 153, 255],
                [0, 41, 255],
                [0, 255, 204],
                [41, 0, 255],
                [41, 255, 0],
                [173, 0, 255],
                [0, 245, 255],
                [71, 0, 255],
                [122, 0, 255],
                [0, 255, 184],
                [0, 92, 255],
                [184, 255, 0],
                [0, 133, 255],
                [255, 214, 0],
                [25, 194, 194],
                [102, 255, 0],
                [92, 0, 255],
            ]
        )
    elif cmap_type == "kvasir":
        return np.asarray(
            [
                [0, 0, 0],
                [255, 255, 255]
            ]
        )

    else:
        raise ValueError("Unsupported dataset.")


def _draw_label_and_softmax(image, label, softmax, color=(0, 0, 255)):
    def truncate(num, n):
        intnum, floatnum = str(num).split(".")
        floatnum = floatnum[:n]
        return float(intnum + "." + floatnum)

    total = f"{label} {truncate(softmax, 3)}"
    text_size = cv2.getTextSize(total, 0, fontScale=1, thickness=1)[0][1]

    cv2.putText(
        image,
        text=total,
        org=(0 + 4, 0 + text_size + 4),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1,
        color=color,
        thickness=2,
    )

    return image


def _draw_center(image, center, color=(0, 255, 0)):
    image = cv2.circle(
        image,
        center=(int(center[0]), int(center[1])),
        radius=1,
        color=color,
        thickness=5,
    )

    return image


def _draw_bbox(image, coord, color=(0, 0, 255), conf_score=None, label=None) -> np.ndarray:
    # ccwh -> xyrb
    get_xyrb = convert_coordinate(coord, (image.shape[0], image.shape[1]), 'ccwh', 'relat', 'xyrb', 'abs')
    xyrb = get_xyrb()
    xyrb = list(map(int, xyrb))

    color = tuple(map(int, color))

    # 박스 위에 conf_score 수치나 label 문자열을 출력해줘야 하는 경우.
    if conf_score is not None or label is not None:
        total = ""
        if conf_score is None:              # only [label]
            total = f"{label} "
        elif label is None:                 # only [conf_score]
            conf_score = str(round(conf_score, 2))
            total = f"{conf_score} "
        else:                               # both exist (label + conf_score)
            conf_score = str(round(conf_score, 2))
            total = f"{label} {conf_score}"

        image = cv2.rectangle(  # 실제 boundbox 그려주는 부분
            image,
            (xyrb[0], xyrb[1]),
            (xyrb[2], xyrb[3]),
            color=color,
            thickness=2,
        )

        text_size = cv2.getTextSize(total, 0, fontScale=1, thickness=1)[0]

        point1 = [xyrb[0], xyrb[1]]
        point2 = [xyrb[0] + text_size[0], xyrb[1] - text_size[1] - 21]
        diff = 0
        if point2[1] < 0:
            diff = 0 - point2[1]
            point2[1] = 0
            point1[1] = point1[1] + diff

        cv2.rectangle(  # label + conf_score 데이터 박스 그려주는 부분
            image,
            pt1=tuple(point1),
            pt2=tuple(point2),
            color=(144, 187, 0),
            thickness=-1,
            lineType=cv2.LINE_AA,
        )

        # 배경색의 반대색으로 문자열 색상을 지정함.
        white = (255, 255, 255)
        contrast_color = tuple([int(white[x] - color[x]) for x in range(0, 3)])

        cv2.putText(  # label + conf_score 데이터(수치+문자열) 작성하는 부분
            image,
            text=total,
            org=(xyrb[0], xyrb[1] - 14 + diff),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1,
            color=white,
            thickness=2,
        )

        return image

    else:  # only rounded bndboxes
        image = cv2.rectangle(
            image,
            pt1=(xyrb[0], xyrb[1]),
            pt2=(xyrb[2], xyrb[3]),
            color=color,
            thickness=3,
        )
        # center_x = xyrb[0] + (abs(xyrb[0] - xyrb[2]) / 2)
        # center_y = xyrb[1] + (abs(xyrb[1] - xyrb[3]) / 2)
        # image = _draw_center(image, center=(center_x, center_y), color=(0, 255, 255))
        return image


def DrawLabelAndSoftmax(imagename, label, softmax, workdir="./", save=True):
    """
    Argument:
        1) imagename: image file의 이름(path)
        2) label: label 값(string, 실제 label name 들어감)
        3) softmax: 해당 라벨에 대한 softmax 값이 들어감. label 값으로 참조할 것.
        4) workdir: save 경로
        5) save: 저장 여부

    Return:
        1) if save == True:  -> Save하고 싶은 경우? Default 값은 "True" 임.
               return image_path (Bndbox가 그려진 Image의 Path가 넘어감, string type)
        2) else:
               return image (Bndbox가 그려진 Image의 numpy array가 넘어감, numpy.ndarray type)

    """
    # palette = seaborn.color_palette('husl', 8)

    os.makedirs(f"{workdir}LabelSoftmaxImages", exist_ok=True)
    workdir = f"{workdir}LabelSoftmaxImages/"
    image = cv2.imread(imagename)
    # realname = imagename.split("/")[-1]
    realname = os.path.basename(imagename)

    image = _draw_label_and_softmax(image, label, softmax, color=(0, 0, 255))

    try:
        if save:  # result image를 저장하는 부분.
            cv2.imwrite(f"{workdir}label_softmax_{realname}", image)
            logger.info(
                f"-> [DrawLabelAndSoftmax Processing] Save Image => {workdir}label_softmax_{realname}\n"
            )

            result = f"{workdir}label_softmax_{realname}"
            # print(f"[NeuralWorks] --- INFO --- \n[DrawBoundBox Processing] Save Image => {workdir}bndbox_{realname}")
        else:  # result image를 저장하지 않고 넘어감.
            result = image
    except:
        logger.Error("Cannot Save Drawed Imagefile!")
        # print("[NeuralWorks] --- ERROR --- Cannot Save drawed image!")

    return result


def DrawBndBoxes(imagename, detected, conf_thres=0.4, workdir="./") -> str:
    """
    Argument:
        1) imagename: image file의 이름(path)
        2) detected: detection된 bbox 정보들
        3) conf_thres: confidence score threshold
        4) num_classes: colormap 설정을 위한 값, integer, 개수임.
        5) workdir: save 경로

    Return:
        1) if save == True:  -> Save하고 싶은 경우? Default 값은 "True" 임.
               return image_path (Bndbox가 그려진 Image의 Path가 넘어감, string type)
        2) else:
               return image (Bndbox가 그려진 Image의 numpy array가 넘어감, numpy.ndarray type)

    """
    # palette = seaborn.color_palette('husl', 8)

    workdir = os.path.join(workdir, "BndboxImages")
    os.makedirs(workdir, exist_ok=True)
    image = cv2.imread(imagename, cv2.IMREAD_COLOR)
    # realname = imagename.split("/")[-1]
    realname = os.path.basename(imagename)
    colormap = get_colormap()

    for i, det in enumerate(detected):
        conf_score = det["conf_score"]
        bboxes = det["bbox"]
        label = det["label"]
        colour = colormap[
            int(label) + 1
        ]  # detection이므로 +1 해줌, 왜냐? CUSTOM_COLORMAP은 segmentation용 background(0, 0, 0)이 0번 인덱스에 존재.
        if not isinstance(colour, tuple):
            try:
                colour = tuple(colour)
            except Exception as exception:
                print(
                    f"[Exception] DrawBndBoxes Function : colour variable type\n > {exception}"
                )
                print(f"colour variable is overridden to rgb=(0, 187, 144).\n")
                colour = (144, 187, 0)

        if conf_score > conf_thres:
            image = _draw_bbox(
                image,
                bboxes,
                color=colour,
                conf_score=conf_score,
                label=label,
            )
    try:
        result = os.path.join(workdir, f"bndbox_{realname}")

        cv2.imwrite(result, image)
        logger.info(
            f"-> [DrawBoundBox Processing] Save Image => {workdir}bndbox_{realname}\n"
        )
            # print(f"[NeuralWorks] --- INFO --- \n[DrawBoundBox Processing] Save Image => {workdir}bndbox_{realname}")
    except:
        logger.Error("Cannot Save Drawed Imagefile!")
        # print("[NeuralWorks] --- ERROR --- Cannot Save drawed image!")

    return result


def DrawSegmentedPixel(imagename, polygon, workdir="./", save=True):
    """
    Argument:
        1) imagename: original image file의 이름(path)
        2) polygon: segmentation network colormap
        3) workdir: save 경로
        5) save: 저장 여부

    Return:
        1) if save == True:  -> Save하고 싶은 경우? Default 값은 "True" 임.
               return image_path (SegmentedPixel이 그려진 Image의 Path가 넘어감, string type)
        2) else:
               return image (SegmentedPixel이 그려진 Image의 numpy array가 넘어감, numpy.ndarray type)

    """
    os.makedirs(f"{workdir}CompositedImages", exist_ok=True)
    workdir = f"{workdir}CompositedImages/"

    realname = os.path.basename(imagename)

    if not isinstance(imagename, str) and not isinstance(polygon, str):
        print("original image and polygon(segmented) image should string type.")
        exit(0)

    source1 = cv2.imread(imagename) / 255.0
    source2 = cv2.imread(polygon) / 255.0
    image = source1 + source2

    try:
        if save:
            image = image * 255.0
            result = f"{workdir}composited_{realname}"
            cv2.imwrite(result, image)
            logger.info(
                f"-> [DrawSegmentedPixel Processing] Save Image => {workdir}composited_{realname}\n"
            )
        else:
            result = image
    except:
        logger.Error("Cannot Save Drawed Imagefile!")

    return result


def DrawStatusGraph(job_id, train_metric="", valid_metric=""):
    """
    Argument:
    1) job_id : job id number -> for job-id-status.json
    2) metric = [] : metric name,
        ex) metric=['train_loss', 'mAP']
            -> x = data['train']['train_loss']
               y = data['valid']['valid_loss']
    """

    json_data = f"{neuenv.NW_HOME}/neusite/jobs/{job_id}/{job_id}-status.json"

    with open(json_data, "r") as f:
        data = json.load(f)

    data = data["metrics_on_train"]

    epoch, x, y = [], [], []

    for i in range(len(data)):
        epoch.append(data[i]["epoch"])
        x.append(data[i]["train"][train_metric])
        y.append(data[i]["valid"][valid_metric])

    plt.clf()
    plt.plot(epoch, x, color="blue", label=f"train_{train_metric}")
    plt.plot(epoch, y, color="green", label=f"valid_{valid_metric}")
    plt.xlabel("Epoch")
    plt.ylabel("Metric values")
    plt.title(f"Status values per Epoch")
    plt.xlim([-1, max(epoch) + 1])
    plt.grid(True)
    plt.legend(loc="upper right")
    plt.savefig(f"{neuenv.NW_HOME}/neusite/jobs/{job_id}/{job_id}-status_graph.jpg")


def printShape(*elems):
    for elem in elems:
        if isinstance(elem, list) or isinstance(elem, tuple):
            print(f"Size: {len(elem)} | Type: {type(elem).__name__}")

        else:
            print(f"Size: {elem.shape} | Type: {type(elem).__name__}")


# def point2polygon(point, color='coco'):
#     cmap = get_colormap(color)
#     print("Convert point to polygon")
#     if isinstance(point, list):
#         point = np.array(point, np.int32)

#     img = np.zeros((240, 240, 3), np.uint8)
#     img = cv2.fillPoly(img, [point], tuple(color))
#     cv2.imwrite("polygon.jpg", img)

#     return img


def point2polygon(info: dict, color="coco"):
    nw_home = os.getenv("NW_HOME")
    cmap = get_colormap(cmap_type=color).tolist()
    palette = [value for color in cmap for value in color]

    column = info["width"]
    row = info["height"]
    dataset_path = info["dataset_path"]
    root_path = info["root_path"]
    extra_path = info["extra_path"]
    file_name = info["file_name"]
    segment = info["segment"]

    savepath = os.path.join(dataset_path, root_path, extra_path, file_name)
    rgb = np.zeros((row, column, 3), np.uint8)

    for seg in segment:
        point = seg["points"]
        cat_id = seg["category_id"]
        col = cmap[cat_id]
        unknown = cmap[255]
        if isinstance(point, list):
            try:
                poly = (
                    np.array(point).reshape((int(len(point) / 2), 2)).astype(np.int32)
                )
            except:
                point = point[0]
                poly = (
                    np.array(point).reshape((int(len(point) / 2), 2)).astype(np.int32)
                )
            # print(poly)
            rgb = cv2.fillPoly(rgb, [poly], tuple(col))
            rgb = cv2.polylines(rgb, [poly], True, tuple(unknown), 2)

    rgb = rgb.astype("uint8")
    img_png = np.zeros((row, column), np.uint8)

    for index, val_col in enumerate(cmap):
        img_png[np.where(np.all(rgb == val_col, axis=-1))] = index
    img_png = Image.fromarray(img_png).convert("P")
    img_png.putpalette(palette)
    img_png.save(savepath)


def count_parameters(model):
    n_params = sum(p.numel() for p in model.parameters())

    return n_params


def convert_float(val: float, point: int):
    val = round(val, point)
    integer, fp = str(val).split(".")

    try:
        result = f"{integer}.{fp[:5]}"
    except:
        result = f"{integer}.{fp}"

    return float(result)

def model_summary(model, lib='TORCH'):
    try:
        if lib == 'TORCH':
            summary_string = str(model)
            summary_lines = summary_string.splitlines()
            line_count = len(summary_lines)

            print("\n ========== MODEL ARCHITECTURE ==========\n")

            if line_count < 30:
                for index in range(line_count):
                    print(summary_lines[index])
            else:
                for index in range(0, 10):
                    print(summary_lines[index])

                print("\n...\n")
                for index in range(11, 0, -1):
                    print(summary_lines[-index])

            print("\n ========== MODEL ARCHITECTURE ==========\n")
            model_params = count_parameters(model)
            print(f"\n - Model Params : {model_params} \n")
        elif lib == 'KERAS':
            model.summary()
        else:
            print("\n\n - Model Object :", model, "\n\n")
    except Exception as e:
        print("Model state is Null. Model summary was fail to call.")
        print("Error message :", e)


if __name__ == "__main__":
    # job_id = "job-20210702-1821-Ao9me"
    job_id = "job-20210705-1737-ACtXz"
    DrawStatusGraph(job_id, train_metric="loss", valid_metric="loss")

    # point = [[40, 40], [120, 40], [150, 70], [170, 90], [134, 104], [120, 120], [200, 120], [160, 180], [120,200], [80, 80]]

    # poly = point2polygon(point, (128, 128, 192))

    # image = "/home/clt_dc/neural-framework/neuralPlatform/neusite/datasets/ds-450/sample/00000637_010681_0009.jpg"
    # label = "cat"
    # softmax = 0.991222
    # result = DrawLabelAndSoftmax(image, label, softmax)
    # print(result)
