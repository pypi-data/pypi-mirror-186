"""
neuralworks' json

이것은 Json 클래스를 정의하는 것입니다.
그리고 기존의 Model, Dataset, Job 클래스는 Json 클래스를 상속합니다.

Json 클래스는 json file 을 load, save 하는 기본 기능을 담당합니다. 멤버 세팅 등.
"""
import json
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

##
def load_json(jsonfile):
    with open(jsonfile, encoding="UTF-8") as fp:
        lines = fp.readlines()
        cleaned = []
        for line in lines:
            line = line.strip()
            cleaned.append(line)
        cleaned = [line for line in cleaned if line and len(line)]
        txt = "\n".join(cleaned)
        # print(txt)
        parsed = json.loads(txt.encode("UTF-8"))
        return parsed

''' 구 .json에 주석 사용을 위한 ver
def load_json(jsonfile):
    """
    json 파일 내에 '#' 가 있으면 코멘트 처럼 간주하여 제거하고
    깨끗한 json 파일 상태로 만든 다음에 파싱을 하여 리턴한다.
    """
    print("Jsonfile Loading >", jsonfile)
    with open(jsonfile) as fp:
        lines = fp.readlines()
        cleaned = []
        for line in lines:
            pos = line.find("#")
            if pos != -1:
                line = line[:pos]
            line = line.strip()

            cleaned.append(line)

        cleaned = [line for line in cleaned if line and len(line)]
        txt = "\n".join(cleaned)
        # print(txt)
        parsed = json.loads(txt)
        return parsed
'''
def save_json(json_file, data):
    pdir = os.path.split(json_file)[0]
    if not os.path.exists(pdir):
        # os.mkdir(pdir)
        os.makedirs(pdir, exist_ok=True)
    with open(json_file, "w") as f:
        json_str = json.dumps(data, indent=4)
        f.write(json_str)
    # print("save json : " + json_file)


###
class Json(object):
    ##
    class JsonEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Json):
                return obj.get_dict()
            else:
                # return json.JSONEncoder.encode(self, obj)
                # return obj
                return super().default(obj)

    ##
    def __init__(self):
        self.excludes_when_dump = {}
        self.exclude(["excludes_when_dump", "jsondict"])

    ##
    def exclude(self, attr):
        """
        exclude the given 'attr' when we export this json(self) to a file
        """
        if isinstance(attr, list):
            for a in attr:
                self.excludes_when_dump[a] = True
        else:
            self.excludes_when_dump[attr] = True

    ## model.json / datast.json ==> setattr 
    def load(self, jsonfile, verbose=False):
        self.jsonfpath = jsonfile
        logger.info(f"[Load json file] > {jsonfile}")
        self.jsondict = load_json(jsonfile)

        # print()
        for i, (key, val) in enumerate(self.jsondict.items()):
            setattr(self, key, val)
            if verbose:
                logger.info("Neujson [{}] loaded in [{}.{}]".format(val, self.__class__.__name__, key))
        # print()

    ##
    def get(self, keyname):
        return self.jsondict.get(keyname)

    ##
    def load_dict(self, jsondata):
        self.jsondict = jsondata

        for k, v in self.jsondict.items():
            setattr(self, k, v)

    ##
    def get_dict(self):
        data = {
            attr: value
            for attr, value in self.__dict__.items()
            if not self.excludes_when_dump.get(attr)
        }
        return data

    ##
    def save(self, outfile):
        logger.info(f"[Save json file] > {outfile}")
        
        with open(outfile, "w", encoding="UTF-8") as out:
            json.dump(self.get_dict(), out, indent=2, cls=Json.JsonEncoder, ensure_ascii=False)

    def print(self):
        print(json.dumps(self.get_dict(), indent=2, cls=Json.JsonEncoder, ensure_ascii=False,
                         default=None))


###
if __name__ == "__main__":
    a = {"name": "handol", "obj": {"age": 10}}
    print(json.dumps(a, indent=2))

    l = Json()
    l.a = 10
    l.b = "BB"
    l.c = ["X", 10]

    k = Json()
    k.a = 10
    k.b = "BB"
    k.c = ["X", 100]
    k.l = l

    j = Json()
    j.a = 10
    j.b = "BB"
    j.c = ["X", 1000]
    j.k = k

    print(j.__dict__)
    print(j.get_dict())

    j.print()
    j.save("saved.json")
    kor = Json()
    fname = "/home/gpuadmin/devEnv/neural-framework/neuralPlatform/neusite/jobs/job-20221228-1304-vpfxt/job-20221228-1304-vpfxt-status.json"
    kor.load(fname)
    kor.print()
