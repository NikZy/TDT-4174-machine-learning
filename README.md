# tdt7143-2020

This repository contains material used in NTNU's machine learning course.

# Folder structure
* data: contains data in different formats
* models: contains persisted models used
* results: contains persisted results
* notebooks: contains Jupyter notebooks.
* source: .....

# Installation
It is recommended to use install the necessary requirements in a
virtual environment

Create virtual env
`python -m venv ./venv`

Activate virtual env
`source ./venv/bin/activate`

Install requirements
`pip install -r requirements.txt`

# Usage
## Run and process data:
All the data files in the "data" folder are generatedt form "kc_house_data-csv" by running "load_and_process_data.py" in the source folder:
`cd source && python load_and_process_data.py` 

## Train linear regression (self made):
The self made linear regression model is trained by running "linear_regression_from_scratch.py" in the source folder, the regression strarts with coeficients retreived from the "Linear.txt" in the models folder and saves the results to the same file on completion. This means that by default the model is already fitted and the coefficients in "Linear.txt" must be reset to train the model again form scratch. One thing to note however is that pythons maximum recurcion depth is 1000, this mens that if the model is refitted we wuold recomend doing it step by steps for a gradually smaller epsilon on line 74:
`cd source && python linear_regression_from_scratch.py` 

## Evaluating linear regression (self made):
The self made linear regression model is trained by running "Linear_Evaluate.py" in the source folder, the regression strarts with coeficients retreived from the "Logistic.txt" in the models folder
`cd source && python Linear_Evaluate.py` 

## Train logistic regression (self made):
The self made linear regression model is trained by running "logistic_regression_from_scratch.py" in the source folder, the regression strarts with coeficients retreived from the "Logistic.txt" in the models folder and saves the results to the same file on completion. This means that by default the model is already fitted and the coefficients in "Logistic.txt" must be reset to train the model again form scratch. One thing to note however is that pythons maximum recurcion depth is 1000, this mens that if the model is refitted we wuold recomend doing it step by steps for a gradually smaller epsilon on line 87:
`cd source && python logistic_regression_from_scratch.py` 

## Evaluating logistic regression (self made):
The self made logistic regression model is trained by running "Logistic_Evaluate.py" in the source folder, the regression strarts with coeficients retreived from the "Logistic.txt" in the models folder
`cd source && python Logistic_Evaluate.py` 



