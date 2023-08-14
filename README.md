# datapipeline-tvseries
Development of a short project to ETL from a REST API to a SQLite database

data ingestion is modeled as the model which you can find on "model/tvseries-project_ingestion design.pdf". Please check it out for better understanding of the code. 

To install this project you can follow the following steps:
-- previous requierements:
make sure you have already installed python and its version is the same or grather than mine:
```
Python 3.9.6
```
also consider the need for having installed git on your system
```
git version 2.39.2
```
to avoid any mistake, also create on the folders: json, db, data  at the same level inside the project

1. copy the current repository into your system with 

```
git clone https://github.com/fsosap/datapipeline-tvseries.git
```

2. create a virtual environment to run the project and avoid downloads on your global python environment.
```
python -m venv << venv_path >>
```

3. activate your virtual environment so you can start downloading packages
```
# for UNIX based systems
source venv/bin/activate

# for windows users
C:\> <venv>\Scripts\activate.bat

```

4. download the dependencies from 'requirements.txt' file with the following command
```
pip install -r requirements.txt
```

5. run the code with
```
python src/main.py
```