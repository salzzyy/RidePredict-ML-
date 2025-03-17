import os
from pathlib import Path

########################### DATA INGESTION ############

# Define directories
RAW_DIR = Path("artifacts/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist

# Define file paths
RAW_FILE_PATH = RAW_DIR / "raw.csv"
TRAIN_FILE_PATH = RAW_DIR / "train.csv"
TEST_FILE_PATH = RAW_DIR / "test.csv"

# Config file path
CONFIG_PATH = Path("config/config.yaml")

# Print paths to verify
print(f"Raw Data Path: {RAW_FILE_PATH}")
print(f"Train Data Path: {TRAIN_FILE_PATH}")
print(f"Test Data Path: {TEST_FILE_PATH}")
print(f"Config Path: {CONFIG_PATH}")
