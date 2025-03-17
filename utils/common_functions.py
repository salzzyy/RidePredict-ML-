import os
import yaml
import sys
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

def read_yaml(file_path):
    """
    Reads a YAML configuration file and returns its content as a dictionary.
    
    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Parsed YAML content.

    Raises:
        CustomException: If the file is not found or cannot be read.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"Successfully read YAML file: {file_path}")
            return config  # Ensure the function returns the parsed YAML data

    except Exception as e:
        logger.error(f"Error while reading YAML file: {e}")
        raise CustomException(str(e), sys)  # Pass sys for traceback info

