import os
import sys
import logging
import getpass


logger = logging.getLogger(__name__)

NW_HOME = os.getenv("NW_HOME", None)
NW_LIB = os.path.join(NW_HOME, "neulib")
EXTERNAL_LIBS = os.path.join(NW_LIB, ".ext")

MMCV = os.path.join(EXTERNAL_LIBS, "mmcv")
MMDETECTION = os.path.join(EXTERNAL_LIBS, "mmdetection")
MMSEGMENTATION = os.path.join(EXTERNAL_LIBS, "mmsegmentation")

sys.path.append(NW_HOME)
sys.path.append(NW_LIB)
sys.path.append(EXTERNAL_LIBS)
sys.path.append(MMCV)
sys.path.append(MMDETECTION)
sys.path.append(MMSEGMENTATION)

import datetime
import shortuuid

# NW_HOME = None

##
def get_now_formatted():
    now = datetime.datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted


## job ID, model ID, dataset ID 할당 방안
def get_yyyymmdd():
    now = datetime.datetime.now()
    yyyymmdd = now.strftime("%Y%m%d-%H%M")
    return yyyymmdd


##
def alloc_job_id():
    yyyymmdd = get_yyyymmdd()
    uuid = shortuuid.ShortUUID().random(length=5)
    new_id = f"job-{yyyymmdd}-{uuid}".lower()
    return new_id


##
def alloc_model_id():
    yyyymmdd = get_yyyymmdd()
    uuid = shortuuid.ShortUUID().random(length=5)
    new_id = f"m-{yyyymmdd}-{uuid}"
    return new_id


##
def alloc_dataset_id():
    yyyymmdd = get_yyyymmdd()
    uuid = shortuuid.ShortUUID().random(length=5)
    new_id = f"ds-{yyyymmdd}-{uuid}"
    return new_id


##
def set_nw_env():
    global NW_HOME
    if NW_HOME is not None:
        NW_HOME = os.environ.get("NW_HOME")
        NW_JOBS = os.path.join(NW_HOME, "neusite/jobs")  # json folder
        NW_WEIGHTS = os.path.join(NW_HOME, "neusite/weights")  # weights files folder
        NW_TEMP = os.path.join(NW_HOME, "neusite/temp")
        NW_DATASETS = os.path.join(NW_HOME, "neusite/datasets")  # json folder

        # SEE `neuralworks-model-storage` repo.
        NW_MODELS = os.path.join(NW_HOME, "neusite/models")
        if os.getenv("NEURALWORKS_MODEL_STORAGE", None) is not None:      # dev mode
            NW_MODELS = os.path.join(os.getenv("NEURALWORKS_MODEL_STORAGE"), "models")

        # logger.info(f"debugging: NW_MODELS Value : {NW_MODELS}")
        os.environ["NW_JOBS"] = NW_JOBS
        os.environ["NW_WEIGHTS"] = NW_WEIGHTS
        os.environ["NW_TEMP"] = NW_TEMP
        os.environ["NW_DATASETS"] = NW_DATASETS
        os.environ["NW_MODELS"] = NW_MODELS
    else:
        raise ValueError("The [NW_HOME] environment path does not exist.")
        exit(0)

##
set_nw_env()


def print_envs():
    logger.info(f"NW_DATASET_STORAGE(dataset) : {os.getenv('NW_DATASET_STORAGE')}")
    logger.info(f"NW_MODEL_STORAGE(.py) : {os.getenv('NW_MODEL_STORAGE')}")
    logger.info(f"NW_DATASETS(ds-001.json) : {os.getenv('NW_DATASETS')}")
    logger.info(f"NW_MODELS(m-001.json) : {os.getenv('NW_MODELS')}")
    logger.info(f"NW_PRIVATE_STORAGE : {os.getenv('NW_PRIVATE_STORAGE')}")
    logger.info(f"NW_JOBS : {os.getenv('NW_JOBS')})")
    logger.info(f"NW_WEIGHTS : {os.getenv('NW_WEIGHTS')}")
    logger.info(f"NW_TEMP : {os.getenv('NW_TEMP')}")


##
def dataset_fpath(ds_id):
    set_nw_env()
    fpath = os.path.join(os.environ["NW_DATASETS"], ds_id, ds_id + ".json")
    return fpath


def dataset_folder(root_path: str = None, ds_id: str = None):
    from bson import ObjectId
    set_nw_env()
    # user_id가 있으면, instruction 학습, ds_id면 기존 방식대로 학습
    logger.info(f"neuenv.py dataset_folder() - root_path: {root_path}, ds_id: {ds_id}")
    dataset_folder_path = None
    
    if root_path:  # for service
        logger.info(f" -> Dataset folder [root_path] {root_path}")
        # ex) /datasets/Users/60d41f93b3b2ea017c9088b6/Datasets/63abcde54d76bd7b11ee68f5/annotation.csv
        # old ? -- /datasets/Public/Datasets/<dataset_id>/<dataset_id>.csv, <dataset_id>-0.csv
        dataset_folder_path = os.path.join(os.environ["NW_DATASET_STORAGE"], root_path)
        
    # if ds_id and not ObjectId.is_valid(ds_id):
    elif ds_id: ## 2023-01-10
        logger.info(f" -> Dataset folder [dataset_id] {ds_id}")
        # ex) /usr/src/app/neural-framework/neuralPlatform/neusite/datasets/638da12fc44f78c203cd6b11/annotation.csv
        # 실제 서비스에서는 오류 발생. annotation.csv 존재하지 않음. 638da12fc44f78c203cd6b11.csv 존재
        # exe.sh로 executor.py실행시에는
        # root_path: None, ds_id: ds-913
        # ->Total dataset folder : /home/gpuadmin/devEnv/neural-framework/neuralPlatform/neusite/datasets/ds-913
        dataset_folder_path = os.path.join(os.getenv("NW_DATASETS"), ds_id)
        
    else:
        raise ValueError("ERROR DATASET!!!!!")
    logger.info(f"->Total dataset folder : {dataset_folder_path}")
    return dataset_folder_path


def model_fpath(model_id):
    set_nw_env()
    fpath = "%s/%s/%s.json" % (os.environ["NW_MODELS"], model_id, model_id)
    return fpath


def model_folder(model_id):
    set_nw_env()
    fpath = None
    model_storage_path = os.getenv("NW_MODEL_STORAGE", None)
    if model_storage_path is None:
        fpath = os.path.join(os.getenv("NW_MODELS"), model_id)
    elif model_storage_path is not None:
        fpath = os.path.join(model_storage_path, model_id)
    logger.info(f"model_folder : {fpath}")
    return fpath


def job_fpath(job_id):
    set_nw_env()
    fpath = "%s/%s/%s.json" % (os.environ["NW_JOBS"], job_id, job_id)
    return fpath


def job_folder(job_id):
    set_nw_env()
    fpath = "%s/%s/" % (os.environ["NW_JOBS"], job_id)
    return fpath


def weight_folder(job_id):
    set_nw_env()
    fpath = "%s/%s/" % (os.environ["NW_WEIGHTS"], job_id)
    # os.makedirs(fpath, exist_ok=True)
    return fpath


def result_of_test_fpath(job_id):
    set_nw_env()
    fpath = "%s/%s/%s-test-result.csv" % (os.environ["NW_JOBS"], job_id, job_id)
    return fpath

# inference result path
def result_of_inference_fpath(job_id, is_original=False):
    set_nw_env()
    if is_original: # 원본 + predicted_y
        fpath = "%s/%s/%s-inf-result.csv" % (os.environ["NW_JOBS"], job_id, job_id)
    else: # 원본 + 전처리 + predicted_y
        fpath = "%s/%s/%s-inf-preprocessed-result.csv" % (os.environ["NW_JOBS"], job_id, job_id)
    return fpath

def job_status_fpath(job_id):
    set_nw_env()
    fpath = "%s/%s/%s-status.json" % (os.environ["NW_JOBS"], job_id, job_id)
    return fpath


def best_weight_fpath(job_id, lib="KERAS"):
    set_nw_env()

    if lib == "KERAS":
        fpath = "%s/%s/%s-best.hdf5" % (os.environ["NW_WEIGHTS"], job_id, job_id)
    elif lib == "TORCH":
        fpath = "%s/%s/%s-best.pt" % (os.environ["NW_WEIGHTS"], job_id, job_id)
    elif lib in ["SCIKIT", "ARIMA", "PROPHET", "PYCARET"]:
        fpath = "%s/%s/%s-best.pkl" % (os.environ["NW_WEIGHTS"], job_id, job_id)
    else:
        NotImplementedError
    return fpath


def last_weight_fpath(job_id, lib="KERAS"):
    set_nw_env()

    if lib == "KERAS":
        fpath = "%s/%s/%s-last.hdf5" % (os.environ["NW_WEIGHTS"], job_id, job_id)
    elif lib == "TORCH":
        fpath = "%s/%s/%s-last.pt" % (os.environ["NW_WEIGHTS"], job_id, job_id)
    elif lib in ["SCIKIT", "ARIMA", "PROPHET", "PYCARET"]:
        fpath = "%s/%s/%s-last.pkl" % (os.environ["NW_WEIGHTS"], job_id, job_id)
    # elif lib == "PROPHET_AD":
    #     fpath = "%s/%s/%s-last.json" % (os.environ["NW_WEIGHTS"], job_id, job_id)
    # elif lib == "PROPHET":
    #     fpath = "%s/%s/%s-last.json" % (os.environ["NW_WEIGHTS"], job_id, job_id)
    else:
        NotImplementedError
    return fpath


def fpath_a(job_id):
    set_nw_env()
    fpath = "%s/%s/%s-a.csv" % (os.environ["NW_JOBS"], job_id, job_id)
    return fpath


def fpath_b(job_id):
    set_nw_env()
    fpath = "%s/%s/%s-b.csv" % (os.environ["NW_JOBS"], job_id, job_id)
    return fpath


def fpath_c(job_id):
    set_nw_env()
    fpath = "%s/%s/%s-c.csv" % (os.environ["NW_JOBS"], job_id, job_id)
    return fpath



##
if __name__ == "__main__":
    # print(alloc_job_id())
    # print(get_now_formatted())

    set_nw_env()
    print_envs()
