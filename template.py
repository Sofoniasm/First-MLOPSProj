import os
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent  # Get the directory part of the path
    filename = filepath.name   # Get the file name part

    # Create directory if it doesn't exist
    if filedir != Path("."):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    # Create file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            logging.info(f"Creating empty file: {filepath}")
