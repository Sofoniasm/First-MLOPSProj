# 1. **Automating File and Directory Creation in Python**

## Overview

This script automates the creation of a predefined set of files and directories in a project. It ensures that all required project structure components are initialized correctly and avoids errors due to missing files or folders. It also uses logging to provide information about the actions performed during execution.

## Key Features
- Ensures that directories in the file paths exist by creating them if they are missing.
- Creates empty files for all listed file paths if they do not exist or are empty.
- Logs every action taken, such as directory creation and file initialization, for better visibility and debugging.

## How It Works
1. **Define the Project Structure:**  
   A list of file paths (`list_of_files`) specifies the required files and directories for the project.

2. **Check and Create Directories:**  
   For each file path, the script identifies the directory and creates it if it doesn't already exist.

3. **Check and Create Files:**  
   If a file doesn't exist or is empty, it is created as an empty file.

4. **Logging Actions:**  
   The script logs all directory creations and file initializations, providing a detailed execution log.

## Script Snippet

```python
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
