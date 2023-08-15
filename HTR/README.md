# AI Reader - SimpleHTR

> If you face any issues that we fail to explain please try to understand the source code [here](https://github.com/githubharald/SimpleHTR).

## Files Description

- `./data/` :\
This directory contain the chorus.txt file.
- `./datasets/` :\
This is where we store our datasets. If you wish to add a new one just make sure your dataset folder's content is the **gt** and **img** dirs. The **gt** dir should have the *words.txt* file, making the connection `image-name -> word` and the **img** dir should have the images of our dataset.
- `./model/` :\
This is where the model goes, you can either place trained models here or create new files training a new one with your data.
- `/src/` :\
This is the main directory containing all scripts. **When running the scripts** this should be your *cwd*.

- `/TrainedModel/` :\
Dir containing some pre-trained models that can be placed in `./model/` and be used immediately.\
There are two types of models. *line-models* and *word-models*. At the time of this commit, there are only pre-trained *line-models* available.\
on the path `/TrainedModel/{model_type}/*` there are the dirs containing the actual model files. Distinguished by the data they where trained on, you should move or copy these dirs content to `./model/`.

### Going more in depth at  `./src/`

- create_lmdb.py:\
Responsible for creating a ligth memory database from a dataset.

- dataloader_iam.py:\
Responsible for properly loading the data train our model

- main.py:\
Responsible for putting everything together. This is the main script.
- model.py:\
Responsible for trainig the model
- preprocessor:\
Responsible for preprocessing the images before they go to training and before they are read by the model.
- testing.py:\
Responsible for writting the test on a instance basis
- testing.sh:\
Responsible for filthering the output for the test and for managing all test instances to testing.py .

## Running the scripts

### Preparation

- Installing Packages
> editdistance v0.6.2\
lmdb v1.0.0\
matplotlib v3.7.1\
numpy v1.23.5\
opencv-python v4.7.0.72\
path v16.6.0\
tensorflow v2.11.0

### About the scripts
You can run this program in 2 major ways:
1. Training the model
2. Running a model that has already been trained.

To shift between these two modes just change the running command but please pay attention to `/model/` dir content as if you try to train a model with this dir not empty you migth change you model permanentely or you can face an error.

### Running Commands

- Run a model on an image
```#!/bin/bash
$ cd ./src/
$ python3 main.py --img_file {path_to_image}
```
- Training a new model

Training to read lines:
```#!/bin/bash
$ cd ./src/
$ python3 main.py --mode train --line_mode --data_dir {path_to_data_dir}
```
Training to read words:
```#!/bin/bash
$ cd ./src/
$ python3 main.py --mode train --data_dir {path_to_data_dir}
```
- Running tests:
```#!/bin/bash
$ cd ./src/
$ ./testing.sh
```
## Viewing test results

When `/SimpleHTR-Harald/src/testing.sh` is executed. The `/quick-access/Tests/results.csv` file is formated and rewritten with the new test results. In order for you to save the results you should manually copy-paste 'model-x-result' and 'model-x-prob' columns to `/quick-access/Tests/fixed_results.csv` .
> You can also have a small statistic view of a collumn running `/quick-access/Tests/checker.py` by manually editing *file_path* and *collumn_index* variables.
