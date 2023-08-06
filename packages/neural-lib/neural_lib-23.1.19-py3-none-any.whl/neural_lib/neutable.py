import numpy as np
import pandas as pd
from scipy import stats
import sys
import os

from neuenv import dataset_folder

import logging
logger = logging.getLogger(__name__)


# 차후 리팩토링에 고려사항
# def __init__(self, jsondict={}, dataset_id='', dataset_type='TABLE', problem_type=None, root_path=""):
# assert jsondict != {} or dataset_id != '', f"Table class should have [jsondict] or [dataset_id] value: now is {jsondict} and {dataset_id}."

class Table:
    def __init__(self, dataset_id='', dataset_type='TABLE', problem_type=None, root_path="", table_meta={}):
        self.dataset_id = dataset_id
        self.dataset_type = dataset_type
        self.problem_type = problem_type
        self.root_path = root_path
        self.MAP_NAME_FUNC = {
            "FillMissing": self.FillMissing, 
            "MinMaxScaler": self.MinMaxScaler,
            "StandardScaler": self.StandardScaler,
            "RobustScaler": self.RobustScaler,
            "LogScaler": self.LogScaler,
            "ExpScaler": self.ExpScaler,
            "BoxCoxTransform": self.BoxCoxTransform,
            
            "Carling": self.Carling,
            "Tukey": self.Tukey,
            "ESD": self.ESD,
            
            "LabelEncoder": self.LabelEncoder,
            "OneHotEncoder": self.OneHotEncoder,
            
            "ReplaceValue":self.ReplaceValue, # 값 대체 : 단일값
            "ReplaceRangeValue":self.ReplaceRangeValue, # 값 대체 : 범위값
            "Filtering": self.Filtering,
        }
        self.table_meta = table_meta
        # self.history = []
        '''
        # 결측치 값 채우기 => 2개 컬럼
        self.history = list([
            [{
            'name': 'FillMissing',
            'column_name': 'has_gym',
            'fill_val': 1,
            'nan_vals': [],
            'descriptive': -1,
            'is_test': True,
            'treated_missing_n': 4,
            'remained_missing_n': 0
            },
            {
            'name': 'FillMissing',
            'column_name': 'rent',
            'fill_val': 1,
            'nan_vals': [],
            'descriptive': -1,
            'is_test': True,
            'treated_missing_n': 4,
            'remained_missing_n': 0
            }],
            [{ 
            'name': 'FillMissing',
            'column_name': 'bathrooms',
            'fill_val': 3.0,
            'nan_vals': [],
            'descriptive': -1,
            'treated_missing_n': 4,
            'is_test': True,
            'remained_missing_n': 0
            }]
        ])
        '''

        '''
        # Telecom Chrun Data - 필터링 정수, 실수형 , 문자형
        self.history = list([
            [
                {
                    'name': 'Filtering',
                    'column_name': 'tenure',
                    'is_test': False,
                    'col_dtype': 'int64',
                    'condition': 'X >= 5'
                },
            ],
            [
                {
                    'name': 'Filtering',
                    'column_name': 'MonthlyCharges', 
                    'is_test': False, 
                    'col_dtype': 'float64', 
                    'condition': 'X >= 60 AND X <= 150'
                }
            ],
            [
                {
                    'name': 'Filtering', 
                    'column_name': 'gender', 
                    'is_test': False, 
                    'col_dtype': 'object', 
                    'condition': 'X == Female'
                }
            ]
        ])
        '''

        '''
        # Telecom Chrun Data - 이상치 3종류
        self.history = list([
            [
                {
                    'name': 'Carling', 
                    'column_name': 'tenure', 
                    'is_test': True, 
                    'new_column': ['tenure_Carling'], 
                    'q25': 9.0, 'q50': 30.0, 'q75': 56.0, 
                    'lower': -78.1, 'upper': 138.1, 
                    'outlier_n': 4
                }
            ],
            [
                {
                    'name': 'Carling', 
                    'column_name': 'tenure', 
                    'is_test': False, 
                    'q25': 9.0, 'q50': 30.0, 'q75': 56.0, 
                    'lower': -78.1, 'upper': 138.1, 
                    'outlier_n': 4
                }
            ],
            [
                {
                    'name': 'Tukey', 
                    'column_name': 'tenure', 
                    'is_test': True, 
                    'new_column': ['tenure_Tukey'], 
                    'q25': 9.0, 'q50': 30.0, 'q75': 56.0, 
                    'lower': -61.5, 'upper': 126.5, 
                    'outlier_n': 5
                }
            ],
            [
                {
                    'name': 'Tukey', 
                    'column_name': 'tenure', 
                    'is_test': False, 
                    'q25': 9.0, 'q50': 30.0, 'q75': 56.0, 
                    'lower': -61.5, 'upper': 126.5, 
                    'outlier_n': 5
                }
            ],
            [
                {
                    'name': 'ESD', 
                    'column_name': 'tenure', 
                    'is_test': True, 
                    'new_column': ['tenure_ESD'], 
                    'org_mean': 33.02685050798258, 'stddev': 24.826860637095507, 'cutoff': 74.48058191128652, 
                    'lower': -41.45373140330394, 'upper': 107.5074324192691, 
                    'outlier_n': 5
                }
            ],
            [
                {
                    'name': 'ESD', 
                    'column_name': 'tenure', 
                    'is_test': False, 
                    'org_mean': 33.02685050798258, 'stddev': 24.826860637095507, 'cutoff': 74.48058191128652, 
                    'lower': -41.45373140330394, 'upper': 107.5074324192691, 
                    'outlier_n': 5
                }
            ]
        ])
        '''

        '''
        # Telecom Chrun Data - 스케일러 6종류
        self.history = list([
            [
                {
                    'name': 'MinMaxScaler', 
                    'column_name': 'MonthlyCharges', 
                    'is_test': True, 
                    'org_min': 23.45, 'org_max': 118.75, 'org_mean': 76.85505261248186, 'org_std_dev': 21.927341844209476, 
                    'new_min': 0.0, 'new_max': 1.0, 'new_mean': 0.5603887997112472, 'new_std_dev': 0.23008753246809519
                },
                {
                    'name': 'MinMaxScaler', 
                    'column_name': 'TotalCharges', 
                    'is_test': True, 
                    'org_min': 23.45, 'org_max': 8684.8, 'org_mean': 2729.505406386067, 'org_std_dev': 2355.467366705752, 
                    'new_min': 0.0, 'new_max': 1.0, 'new_mean': 0.31242882534317024, 'new_std_dev': 0.27195152796108596
                }
            ],
            [
                {
                    'name': 'StandardScaler', 
                    'column_name': 'tenure', 
                    'is_test': True, 
                    'org_min': 1, 'org_max': 178, 'org_mean': 33.02685050798258, 'org_std_dev': 24.826860637095507, 
                    'new_min': -1.290008067315973, 'new_max': 5.839366950624565, 'new_mean': 1.4115462548209537e-16, 'new_std_dev': 1.0
                }
            ],
            [
                {
                    'name': 'RobustScaler', 
                    'column_name': 'SeniorCitizen', 
                    'is_test': True, 
                    'org_min': 0, 'org_max': 1, 'org_q25': 0.0, 'org_q50': 0.0, 'org_q75': 0.0, 
                    'new_min': 0, 'new_max': 0, 'new_q25': 0.0, 'new_q50': 0.0, 'new_q75': 0.0
                }
            ],
            [
                {
                    'name': 'LogScaler', 
                    'column_name': 'Partner', 
                    'is_test': True, 
                    'org_min': 0, 'org_max': 1, 
                    'new_min': 0.0, 'new_max': 0.6931471805599453
                }
            ],
            [
                {
                    'name': 'ExpScaler',
                    'column_name': 'Dependents',
                    'is_test': True,
                    'org_min': 0,'org_max': 1,
                    'new_min': 0.0, 'new_max': 1.718281828459045
                }
            ],
            [
                {
                    'name': 'BoxCoxTransform',
                    'column_name': 'OnlineBackup',
                    'is_test': True,
                    'org_min': 0,
                    'org_max': 1,
                    'new_min': -52.99082261763703,
                    'new_max': 2.2204460492503126e-16
                }
            ]
        ])
        '''

        '''
        # Telecom Chrun Data - 값 대체, 값 범위 지정
        self.history = list([
            [
                {
                    'name': 'ReplaceValue',
                    'column_name': 'gender',
                    'is_test': True,
                    'replace_sum': 5512,
                    'missing_num': 0,
                    'org_values': ['Female', 'Male'],
                    'replace_values': ['Female__', 'Male__']
                }
            ],
            [
                {
                    'name': 'ReplaceRangeValue', 
                    'column_name': 'tenure', 
                    'is_test': True, 
                    'range_list': [[0, 20, 'F'], [21, 40, 'D'], [41, 60, 'C'], [61, 80, 'B'], [81, 100, 'A']], 
                    'new_column': ['tenure_ReplaceRangeValue'], 
                    'missing_num': 172, 
                    'replace_sum': 5340
                }
            ]
        ])
        '''

        # Airpassengers.csv
        self.history = list([
        ])

        ''' # manhattan_nan.csv
        self.history = list([
            [{
            "name": "FillMissing",
            "column_name": "bathrooms",
            "nan_vals": [],
            "fill_val": 5,
            },  
            {
            "name": "FillMissing",
            "column_name": "has_gym",
            "nan_vals": [],
            }],

            [{
                "name": "Filtering",
                "column_name": "min_to_subway",
                "condition": "X >= 2",
                "new_column": [
                    "min_to_subway_filter"
                ]
            },
            {
                "name": "Filtering",
                "column_name": "size_sqft",
                "condition": "X >= 300 AND X <= 3200",
                "new_column": [
                    "size_sqft_filter"
                ]
            }]
        ])
        '''
        ''' = boston_housing_scaler_outlier_test.csv
        self.history = list([
            [{
            "name": "StandardScaler",
            "column_name": "NOX",
            "new_column": [
                    "NOX_StandardScaler"
            ],
            "org_max": 450,
            "org_min": 0,
            "org_mean": 206.6666717529297,
            "org_std_dev": 152.93426513671875,
            "new_max": 1.5910974740982056,
            "new_min": -1.3513431549072266
            }],

            [{
            "name": "MinMaxScaler",
            "column_name": "RM",
            "new_column": [
                    "RM_MinMaxScaler"
            ],
            "org_max": 50,
            "org_min": 0,
            "new_max": 1,
            "new_min": 0
            }],

            [{ # 이상치 판단
            "name": "carling",
            "column_name": "B",
            "q25": 375.3775,
            "q50": 391.44,
            "q75": 396.225,
            "lower": 327.42824999999993,
            "upper": 444.1742500000001,
            "new_column": [
                "PTRATIO_carling"
            ]
            },
            { # 이상치 제거
            "name": "carling",
            "column_name": "B",
            "q25": 375.3775,
            "q50": 391.44,
            "q75": 396.225,
            "lower": 327.42824999999993,
            "upper": 444.1742500000001,
            }],

            [{ # 이상치 판단
            "name": "tukey",
            "column_name": "CRIM",
            "q25": 0.08204499999999999,
            "q50": 0.25651,
            "q75": 3.6770825,
            "lower": -5.31051125,
            "upper": 9.06963875,
            "new_column": [
                "CRIM_tukey"
            ]
            },
            { # 이상치 제거
            "name": "tukey",
            "column_name": "CRIM",
            "q25": 0.08204499999999999,
            "q50": 0.25651,
            "q75": 3.6770825,
            "lower": -5.31051125,
            "upper": 9.06963875,
            }]
        ])
        '''
        ''' = manhattan_labelencoder_onehotencoder.csv 
        self.history = list([
            [{
            "name": "LabelEncoder",
            "column_name": "neighborhood",
            "label": [
                'Upper West Side',
                'Upper East Side',
                'Midtown East',
                'Midtown West',
                'Financial District',
                'Chelsea',
                'Flatiron',
                'Midtown',
                'Tribeca',
                'East Village',
                'Battery Park City',
                'Midtown South',
                'Central Harlem',
                'West Village',
                'Greenwich Village',
                'Gramercy Park',
                'Soho',
                'Washington Heights',
                'East Harlem',
                'Lower East Side',
                'Central Park South',
                'Hamilton Heights',
                'Morningside Heights',
                'Inwood',
                'Nolita',
                'Chinatown',
                'Roosevelt Island',
                'Long Island City',
                'Stuyvesant Town/PCV',
                'Little Italy',
                'West Harlem',
                'Manhattanville'
                ],
            "new_column": [
                "neighborhood_LabelEncoder"
            ]
            }],
            [{
            "name": "OneHotEncoder",
            "column_name": "neighborhood",
            "label": [
                'Upper West Side',
                'Upper East Side',
                'Midtown East',
                'Midtown West',
                'Financial District',
                'Chelsea',
                'Flatiron',
                'Midtown',
                'Tribeca',
                'East Village',
                'Battery Park City',
                'Midtown South',
                'Central Harlem',
                'West Village',
                'Greenwich Village',
                'Gramercy Park',
                'Soho',
                'Washington Heights',
                'East Harlem',
                'Lower East Side',
                'Central Park South',
                'Hamilton Heights',
                'Morningside Heights',
                'Inwood',
                'Nolita',
                'Chinatown',
                'Roosevelt Island',
                'Long Island City',
                'Stuyvesant Town/PCV',
                'Little Italy',
                'West Harlem',
                'Manhattanville'],
            "new_column": [
                'neighborhood_Upper West Side',
                'neighborhood_Upper East Side',
                'neighborhood_Midtown East',
                'neighborhood_Midtown West',
                'neighborhood_Financial District',
                'neighborhood_Chelsea',
                'neighborhood_Flatiron',
                'neighborhood_Midtown',
                'neighborhood_Tribeca',
                'neighborhood_East Village',
                'neighborhood_Battery Park City',
                'neighborhood_Midtown South',
                'neighborhood_Central Harlem',
                'neighborhood_West Village',
                'neighborhood_Greenwich Village',
                'neighborhood_Gramercy Park',
                'neighborhood_Soho',
                'neighborhood_Washington Heights',
                'neighborhood_East Harlem',
                'neighborhood_Lower East Side',
                'neighborhood_Central Park South',
                'neighborhood_Hamilton Heights',
                'neighborhood_Morningside Heights',
                'neighborhood_Inwood',
                'neighborhood_Nolita',
                'neighborhood_Chinatown',
                'neighborhood_Roosevelt Island',
                'neighborhood_Long Island City',
                'neighborhood_Stuyvesant Town/PCV',
                'neighborhood_Little Italy',
                'neighborhood_West Harlem',
                'neighborhood_Manhattanville'],
            }]
        ])
        '''


    def read_table(self, table_file):
        """_summary_

        Args:
            table_file (_type_): csv file path

        Raises:
            NotImplementedError: _description_

        Returns:
            _type_: df (Dataframe)
        """
        table_path = os.path.join(dataset_folder(ds_id=self.dataset_id, root_path=self.root_path), table_file)
        logger.info(f"[TABLE] Loading: {table_path}")

        if table_file.endswith('csv'):
            if self.table_meta == {}: # training시
                return pd.read_csv(table_path)
            else: # inference 데이터
                try: # 정상적으로 load
                    csv_df = pd.read_csv(table_path, dtypes=self.table_meta)
                    return csv_df
                except: # 데이터 형 충돌 있을 때 dtypes으로 강제 변환 해줌.
                    csv_df = pd.read_csv(table_path)
                    for col, v in self.table_meta.items():
                        if v == 'int64':
                            csv_df[col] = pd.to_numeric(csv_df[col], errors = 'coerce')
                        elif v == 'float64':
                            csv_df[col] = pd.to_numeric(csv_df[col], errors = 'coerce')
                        elif v == 'object':
                            try:
                                csv_df[col] = csv_df[col].astype('str')
                            except:
                                print('문자열로 변환 될 수 없는 행이 존재합니다')
                                pass
                        elif v == 'bool':
                            try:
                                csv_df[col] = csv_df[col].astype('bool')
                            except:
                                print('논리형으로 변환 될 수 없는 행이 존재합니다')
                                pass


        elif table_file.endswith('parquet'):
            return pd.read_parquet(table_path)
        else:
            raise NotImplementedError(f"[{table_file.split('.')[-1]}] format is not supported yet.")

    def load_data(self, all_data, train_data, valid_data, test_data):
        """_summary_

        Args:
            all_data (_type_): file path
            train_data (_type_): file path
            valid_data (_type_): file path
            test_data (_type_): file path

        Raises:
            ValueError: _description_

        Returns:
            _type_: tuple of Dataframes
        """
        all_table, train_table, valid_table, test_table = None, None, None, None

        if all_data != '' and train_data == '':
            all_table = self.read_table(all_data)
        elif (all_data == '' and train_data != '' and valid_data != '' and test_data != ''):
            train_table = self.read_table(train_data)
            valid_table = self.read_table(valid_data)
            test_table = self.read_table(test_data)
        else:
            raise ValueError("Missing Table field.")

        return all_table, train_table, valid_table, test_table

    def replaceOrAddColumn(self, df, p, newColVal):
        newColName = getattr(p, "new_column", None) # "new_column": ["Price_tukey"]
        if newColName != None:
            df[newColName[0]] = newColVal # ex) Price_StandardScaler 추가
        else:
            df[p.column_name] = newColVal # 새로운 대체 column 추가

    # =========== 데이터 스케일러 변환 ===========
    def StandardScaler(self, df, p):
        """
        Standard 표준화 공식 : X-X.mean() / X.std()
        scikit-learn의  StandardScaler (stddev를 1/N로 구함)
        pandas의 std() 함수는 stddev를 구할 때 1/(N-1)으로 구함
        """
        avg, stddev = p.org_mean, p.org_std_dev
        newColVal = df[p.column_name].map(lambda x: (x - avg)/stddev)
        self.replaceOrAddColumn(df, p, newColVal)
        return df

    def MinMaxScaler(self, df, p):
        """
        MinMax 정규화 공식 : X-X.min() / (X.max() - X.min())
        """
        minv, maxv = p.org_min, p.org_max
        range = maxv - minv
        if range != 0:
            newColVal = df[p.column_name].map(lambda x: (x - minv)/range)
        else:
            newColVal = df[p.column_name].map(lambda x: 0)
        self.replaceOrAddColumn(df, p, newColVal)
        return df

    def RobustScaler(self, df, p):
        """
        Robust 표준화 공식 : X-X_2분위수 / (X_3분위수 - X_1분위수)
        """
        q25, q50, q75 = p.org_q25, p.org_q50, p.org_q75
        range = q75 - q25
        if range != 0:
            newColVal = df[p.column_name].map(lambda x: (x - q50)/range)
        else:
            newColVal = df[p.column_name].map(lambda x: 0)
        self.replaceOrAddColumn(df, p, newColVal)
        return df

    def LogScaler(self, df, p):
        """
        Log 스케일러 공식 : log1p(x)
        https://steadiness-193.tistory.com/224
        """
        newColVal = df[p.column_name].map(lambda x: np.log1p(x))
        self.replaceOrAddColumn(df, p, newColVal)
        return df

    def ExpScaler(self, df, p):
        """
        exp 스케일러 공식 : exp(x)-1
        https://steadiness-193.tistory.com/224
        """
        newColVal = df[p.column_name].map(lambda x: np.exp(x)-1)
        self.replaceOrAddColumn(df, p, newColVal)
        return df

    def BoxCoxTransform(self, df, p):
        """
        BoxCoxTransform : 정규 분포 처럼 바꿔주는 알고리즘
        https://dining-developer.tistory.com/18
        """
        # 전처리 값 계산
        try:
            newColVal = stats.boxcox(df[p.column_name]+sys.float_info.epsilon)[0] # boxcox는 양수에만 적용 가능해서.
        except ValueError as e:
            print("Error: BoxCox는 양수에 대해서만 적용 가능합니다.", e)
        self.replaceOrAddColumn(df, p, newColVal)
        return df

    # =========== 데이터 이상치 변환 ===========
    def Carling(self, df, p):
        """
        Carling 이상치 처리 공식 : q50 - iqr*2.3 < 정상 < q50 + iqr*2.3
        """
        newColName = getattr(p, "new_column", None)
        
        # 이상치 판단 - new_column이 존재.
        if newColName != None: # 이상치 판단 - newColName이 있으면
            def is_outlier_func(x): 
                return not (p.lower <= x and x <= p.upper)
            newColVal = df[p.column_name].map(is_outlier_func)
            self.replaceOrAddColumn(df, p, newColVal)
            return df
        
        # 이상치 제거 - new_column이 없음
        else: # 이상치 제거 - NewColVal이 None이면 생성 안됨.
            df = df.loc[df[p.column_name]>=p.lower]
            df = df.loc[df[p.column_name]<=p.upper]  
            return df

    def Tukey(self, df, p):
        """
        tukey 이상치 처리 공식 : q25 - iqr*1.5 < 정상 < q75 + iqr*1.5
        """
        newColName = getattr(p, "new_column", None) # "new_column": ["Price_tukey"]
        
        # 이상치 판단 - new_column이 존재.
        if newColName != None: # 이상치 판단 - newColName이 있으면
            def is_outlier_func(x): 
                return not (p.lower <= x and x <= p.upper)
            newColVal = df[p.column_name].map(is_outlier_func)
            self.replaceOrAddColumn(df, p, newColVal)
            return df
        
        # 이상치 제거 - new_column이 없음
        else: # 이상치 제거 - NewColVal이 None이면 생성 안됨.
            df = df.loc[df[p.column_name]>=p.lower]
            df = df.loc[df[p.column_name]<=p.upper]  
            return df

    def ESD(self, df, p):
        """
        ESD(Extreme Studentized deviate test)
        ESD 이상치 처리 공식 : 평균 - 표준편차*3 < 정상 < 평균 + 표준편차*3
        """
        newColName = getattr(p, "new_column", None) # "new_column": ["Price_tukey"]
        
        # 이상치 판단 - new_column이 존재.
        if newColName != None: # 이상치 판단 - newColName이 있으면
            def is_outlier_func(x): 
                return not (p.lower <= x and x <= p.upper)
            newColVal = df[p.column_name].map(is_outlier_func)
            self.replaceOrAddColumn(df, p, newColVal)
            return df
        
        # 이상치 제거 - new_column이 없음
        else: # 이상치 제거 - NewColVal이 None이면 생성 안됨.
            df = df.loc[df[p.column_name]>=p.lower]
            df = df.loc[df[p.column_name]<=p.upper]  
            return df

    # =========== 데이터 범주형 변수 변환 ===========
    def LabelEncoder(self, df, p):
        num_labels, labels = p.num_label, p.label

        mapping = {label: num for label, num in zip(labels, num_labels)}
        # mapping = {labels[i]: i for i in range(len(labels))}
        print('===Label Encoder Mapping', mapping)

        newColVal = df[p.column_name].map(mapping)
        self.replaceOrAddColumn(df, p, newColVal)
        return df

    def OneHotEncoder(self, df, p):
        labels = p.label  # give from the history
        for i, label in enumerate(labels):
            newColVal = df[p.column_name].map(lambda x: 1 if x == label else 0)
            newColName = p.new_column[i] # ex) [Name_Pear, Name_Apple..]
            df[newColName] = newColVal
        return df

    # =========== 데이터 결측치 변환 ===========
    # 실제 결측치 유형은 크게 2가지 (값 제거, 값 채우기)
    # 실제 결측치 세부 유형은 3가지(값 제거, 함수로 값 채우기, 특정값으로 채우기)
    # fillVal 여부로만 구분.
    def FillMissing(self, df, p):
        # fill_val
        is_fill_val = getattr(p, "fill_val", None) # "new_column": ["Price_carling"]
        # 결측치 값 채우기
        if is_fill_val != None: 
            newColVal = df[p.column_name].fillna(value=p.fill_val) # 
            # print('=== 2.1 ', df.isna().sum())
            self.replaceOrAddColumn(df, p, newColVal)
            return df
        
        # 결측치 제거
        else: 
            df = df[df[p.column_name].notna()]
            # print('=== 2.1 ', df.isna().sum())
            return df

    # =========== 데이터 핕터링 ===========
    def parseOneExpr(self, df, columnName, col_dtype, flds):
        print("OneExpr", flds) # ['X', '>', '0']
        if col_dtype == 'object':
            print('column이 object 입니다')
            val1 = str(flds[2])
        elif col_dtype == 'bool':
            print('column이 Bool 입니다')
            val1 = bool(flds[2])
        elif col_dtype == 'int64' or col_dtype=='float64':
            print('column이 numerical 입니다')
            val1 = float(flds[2]) # X > 0

        # OP : 연산자
        op = flds[1]
        if (op == ">"): 
            return df[columnName] > val1
        elif (op == ">="):  
            return df[columnName] >= val1
        elif (op == "=="): 
            return df[columnName] == val1
        elif (op == "!="):
            return df[columnName] != val1
        elif (op == "<"):
            return df[columnName] < val1
        elif (op == "<="):
            return df[columnName] <= val1
        else:
            return df

    # 문자열로 되어있는 수식을 파싱하여 DataFrame 리턴
    def parseExpression(self, df, column_name, col_dtype, exprStr):
        flds = exprStr.strip().split(' ')
        # 대소 비교 연산자만 사용
        if len(flds) == 3:
            func = self.parseOneExpr(df, column_name, col_dtype, flds)
            return df[func]
            # return self.parseOneExpr(flds)

        # 대소 비교 연산자 + [AND, OR] 결합
        elif len(flds) == 7:
            boolOp = flds[3].upper()
            func1 = self.parseOneExpr(df, column_name, col_dtype, flds[:3])
            func2 = self.parseOneExpr(df, column_name, col_dtype, flds[4:])
            if (boolOp == "AND"):
                return df[func1 & func2]

            elif (boolOp == "OR"):
                return df[func1 | func2]
        else:
            print("ERROR in", exprStr, '맞지않는 필터 수식입니다')
            return df

    def Filtering(self, df, p):
        col_dtype = str(df[p.column_name].dtypes)
        df = self.parseExpression(df, p.column_name, col_dtype, p.condition)
        # print(df)
        return df

    # =========== 데이터 값 대체 ===========
    # 단일 값 대체
    def ReplaceValue(self, df, p):
        org_values, replace_values = p.org_values, p.replace_values
        mapping = {org_val : replace_val for org_val, replace_val in zip(org_values, replace_values)}
        newColVal = df[p.column_name].replace(mapping)
        self.replaceOrAddColumn(df, p, newColVal)
        return df
    
    # 범위 값 대체
    def ReplaceRangeValue(self, df, p):
        range_list = p.range_list
        # 전처리 값 계산
        cond_list, value_list = [], []
        for min_v, max_v, new_v in range_list:
            filter_df = (df[p.column_name] >= min_v) & (df[p.column_name]<max_v)

            cond_list.append(filter_df)
            value_list.append(new_v)
        
        newColVal = np.select(cond_list, value_list, default=[pd.NA])
        self.replaceOrAddColumn(df, p, newColVal)
        return df

##
class MyJsonObject(object):
    def __init__(self, jsondict):
        for k, v in jsondict.items():
            # print(k, v)
            setattr(self, k, v)

    def print(self):
        for k, v in self.__dict__.items():
            print(k, v)
