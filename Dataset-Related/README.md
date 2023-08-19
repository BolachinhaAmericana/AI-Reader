# AI Reader - Dataset Related Code

## Files Description

- `./Deslant` :\
Directory containg the de-slant algoritm taken from [pytorch-handwritingCTC](https://github.com/jc639/pytorch-handwritingCTC) repository

- `./Creation/` :\
Directory containing the main script and the .csv file with the rows of some clinical analysis and their abreviation.

- `./Fonts/` :\
Dir containing everything related to the fonts used to create the dataset. If you wish by any reason to change any font you can do this by installing the new font and by editing the `FONTS` dictionary on the code. Take note that the name of the font migth not always be the font file name. To check this  you can run the command:
```
$ fc-list
```
## Deslanting Algoritm

### Preparation
- Installing Packages
> opencv - v4.6.0\
pandas - v2.0.3\
Pillow - v9.4.0\
pytorch - v2.0.1\
scikit-image - v0.20.0\
torchvision - v0.15.2

### Running Deslant Algoritm

Just follow along de-slanting.ipynb after the completion of these 2 steps:\
1 - place your input image at .root_dir/ \
2 - change "uploaded" variable with the name of your image.

## Dataset Creation

### Preparation

- Installing Fonts
> You will need to install all fonts in `/Fonts/FontFiles` on your sistem. If you are using ubuntu or WSL you can achieve this simply by inserting the .ttf files in `~/.local/share/fonts`. If the fonts directory doesn't exist feel free to simply create it.

- Installing Packages
> cairocffi - v1.4.0\
Pillow - v9.4.0


### Running Dataset Creation

1. Run `/Creation/script.py`:

```#!/bin/bash
$ cd Creation/
$ python3 dataset_creator.py
```

Depending on yout computer, this will take around 10 minutes ultil the code has finished running. The final output should be:
- the file `./words.txt`\
This file contains all information in `./dataset.csv` formated and ready for training.\
This file is responsable for making the connection of the image name to the image content.

- the directory `./Data/` :\
This directory contains all uncropped images. The images in this dir are unfit for training and can be deleted after the process is finished.

- the directory `./Crop_Data/`:\
This directory contains all cropped data applying the bounding boxes algorithm to the images in `./Data/`. 




