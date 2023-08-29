# datapipeline-tvseries

Development of a short project to ETL from a REST API to a SQLite database

data ingestion is modeled as follows. Please check it out for better understanding of the code.

![data pipeline design](model/pipeline_design.jpg)

The data model designed for the project is the following
![data model](model/datamodel_tvseries.jpg)

To install this project you can follow the following steps:
-- previous requierements:
make sure you have already installed python and its version is the same or higher than mine:

```text
Python 3.9.6
```

also consider the need for having installed git on your system

```text
git version 2.39.2
```

## INSTALLING STEPS

1. copy the current repository into your system with

    ```bash
    git clone https://github.com/fsosap/datapipeline-tvseries.git
    ```

2. create a virtual environment to run the project and avoid downloads on your global python environment

    ```bash
    python -m venv <venv_name>
    ```

3. activate your virtual environment so you can start downloading packages

    ```bash
    # for UNIX based systems
    source <venv_name>/bin/activate

    # for windows users
    C:\> <venv_name>\Scripts\activate.bat
    ```

4. download the dependencies from 'requirements.txt' file with the following command

    ```bash
    pip install -r requirements.txt
    ```

5. run the code with

    ```bash
    python src/main.py
    ```
