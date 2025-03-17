import os
import sys
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.path_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        """
        Initializes the DataIngestion class with configuration values.

        Args:
            config (dict): Configuration dictionary loaded from YAML.
        """
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_name = self.config["bucket_file_name"]
        self.train_test_ratio = self.config["train_ratio"]

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"Data Ingestion started with bucket: {self.bucket_name}, file: {self.file_name}")

    def download_csv_gcp(self):
        """Downloads CSV file from Google Cloud Storage."""
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.file_name)
            blob.download_to_filename(RAW_FILE_PATH)
            logger.info(f"Raw file successfully downloaded to {RAW_FILE_PATH}")
        except Exception as e:
            logger.error(f"Error while downloading CSV file: {e}")
            raise CustomException(str(e), sys)
        
    def split_data(self):
        """Splits data into training and testing sets and saves them as CSV files."""
        try:
            logger.info("Starting data splitting process")
            data = pd.read_csv(RAW_FILE_PATH)

            train_data, test_data = train_test_split(data, test_size=1 - self.train_test_ratio, random_state=32)
            train_data.to_csv(TRAIN_FILE_PATH, index=False)
            test_data.to_csv(TEST_FILE_PATH, index=False)

            logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data saved to {TEST_FILE_PATH}")

        except Exception as e:
            logger.error(f"Error while splitting data: {e}")
            raise CustomException(str(e), sys)

    def run(self):
        """Runs the complete data ingestion pipeline."""
        try:
            logger.info("Starting data ingestion")
            self.download_csv_gcp()
            self.split_data()

            logger.info("Data ingestion completed successfully")

        except CustomException as ce:
            logger.error(f"Custom Exception: {str(ce)}")
            raise ce

        finally:
            logger.info("Data ingestion process finished")


if __name__ == "__main__":
    config = read_yaml(CONFIG_PATH)    
    print(f"Loaded Config: {config}")  # Debugging step

    data_ingestion = DataIngestion(config)  # Pass dictionary, not string
    data_ingestion.run()
