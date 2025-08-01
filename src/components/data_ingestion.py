import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.Data_Ingestion = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Data Ingestion Process is Initiated")
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the datasets as dataframe")
            os.makedirs(os.path.dirname(self.Data_Ingestion.train_data_path),exist_ok=True)
            df.to_csv(self.Data_Ingestion.raw_data_path,index=False,header=True)

            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            logging.info("Train Test Split initiated")
            train_set.to_csv(self.Data_Ingestion.train_data_path,index=False,header=True)
            test_set.to_csv(self.Data_Ingestion.test_data_path,index=False,header=True)
            logging.info("Data Ingestion Process is completed")

            return(
                self.Data_Ingestion.train_data_path,
                self.Data_Ingestion.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == '__main__':
    obj= DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)