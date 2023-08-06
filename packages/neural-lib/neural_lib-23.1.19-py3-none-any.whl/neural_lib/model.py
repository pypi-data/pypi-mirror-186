"""
"""
import importlib
import sys

"""
model.json 의 필수 필드:
- library
- problem_type
- source_file
model source code 에는  get_model()를 정의해야 함.
  get_model(input_shape, output_shape)
  input_shape, output_shape 은 list 형태임.
"""

import logging
logger = logging.getLogger(__name__)

# Neuralworks Library
from neujson import Json
from neuenv import model_fpath, model_folder

# (dc) @TODO -> 불필요한 함수로 추정됨.
def get_model_from_src(src_name):
    print(f"Import model source code using importlib package... :{src_name}")
    mod = importlib.import_module(src_name)
    print(f"{src_name} import success.\n")
    return mod.get_model()

class Model(Json):
    ## JOB -> 1. Model init
    def __init__(self):
        super().__init__()
        self.model_name: str = ""
        self.compile_fixed = False
        self.pre_check = False
        self.input_shape: list = None# [224, 224, 3]
        self.year = 2021
        self.origin_url = ""

    ## JOB -> 2. load_by_id
    def load_by_id(self, model_id):
        fpath = model_fpath(model_id)
        return self.load(fpath)

    def get_source_file(self):
        source_folder = model_folder(self.model_id)
        fpath = source_folder + "/" + self.source_file
        return fpath

    def model_folder(self):
        return model_folder(self.model_id)

    ## only import model's source code, not calling - @daehee 2022/12/28
    def import_model_module(self):
        """
        model 소스 파일을 import 만 한다.
        """
        try:
            source_folder = model_folder(self.model_id)
            sys.path.append(source_folder)
            module_name = self.source_file.split('.')[0]
            module = importlib.import_module(module_name)
            logger.info(f"imported {source_folder} {module_name}")
            return module

        except Exception as e:
            logger.exception(f"import Failed {source_folder} {module_name} {e}")
            return None
     
     ## import model's source code, and then call Model() or get_model() - @daehee 2022/12/28
    def import_and_get_model(self, job=None, meta={}):
        """
        model 소스 파일을 import 만 한다.
        """
        try:
            source_folder = model_folder(self.model_id)
            sys.path.append(source_folder)
            module_name = self.source_file.split('.')[0]
            module = importlib.import_module(module_name)
            
            ## check get_model() first
            if getattr(module, "get_model", None):
                instance = module.get_model(job=job)
                logger.info(f"get_model() type {type(instance)} from {source_folder} {module_name}")
                
            ## and then, Model()
            elif getattr(module, "Model", None):
                instance = module.Model(job=job, meta=meta)
                logger.info(f"Model() type {type(instance)} from {source_folder} {module_name}")
            
            else:
                instance = None
                logger.info(f"NOT defined: Model class nor get_model() in {source_folder} {module_name}")
            return instance

        except Exception as e:
            logger.exception(f"Model loading failed {source_folder} {module_name} {e}")
            return None

    def get_target_size(self):
        return self.input_shape

    def get_network_type(self):
        try:
            return self.default_hyper_params['network_type']
        except Exception as e:
            return None


    def info(self):
        input_shape = self.input_shape if getattr(self, "input_shape") else "None"
        if getattr(self, "reference"):
            if self.reference['github'] != '' and self.reference['wiki'] == '' and self.reference['docs'] == '':
                reference = self.reference['github']
            elif self.reference['github'] == '' and self.reference['wiki'] != '' and self.reference['docs'] == '':
                reference = self.reference['wiki']
            elif self.reference['github'] == '' and self.reference['wiki'] == '' and self.reference['docs'] != '':
                reference = self.reference['docs']
            else:       # reference is None state
                reference = "None"
        else:
            reference = "None"

        if getattr(self, "paper"):
            if "title" in self.paper.keys():
                title = self.paper['title']
            else:
                title = "None"
        else:
            title = "None"

        print("\n\n   [ MODEL INFORMATION ]")
        print("     - Model Name".ljust(20), " : ", self.model_name.ljust(20))
        print("     - Library".ljust(20), " : ", self.library.ljust(20))
        print("     - Problem type".ljust(20), " : ", self.problem_type.ljust(20))
        print("     - Public Date".ljust(20), " : ", self.paper.get("date", "None").ljust(20))
        print("     - Input Shape".ljust(20), " : ", str(getattr(self, "input_shape", "None")).ljust(20), "\n\n")
        # print("   Reference".ljust(20), " : ", str(reference).ljust(20))
        # print("   Paper".ljust(20), " : ", str(title).ljust(20), "\n\n")
        

###
if __name__ == "__main__":
    model = Model()
    print(dir(model))
    model.load_by_id("m-450")
    # model.print()
    model.info()
    # module = model.import_and_get_model()
    # module.summary()
