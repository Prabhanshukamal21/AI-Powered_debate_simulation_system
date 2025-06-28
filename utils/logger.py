"""# utils/logger.py
import logging

def setup_logger(filepath):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=filepath,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s",
    )"""
import logging
from pathlib import Path

def setup_logger(filepath: str):
    filepath = Path(filepath)  # Convert string to Path object
    filepath.parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists

    logging.basicConfig(
        filename=str(filepath),  # Convert back to string for logging
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger()

