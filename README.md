# 20Fall-CS539-ML
Course project of CS539. Image caption task on Flickr8k and Google Conceptual Caption dataset.
## Environment
The project was moved from Google Colab, you can use jupyter notebook to run the .ipynb files. 
### Dependencies
Keras

Tqdm

Numpy

PIL

Pickle

## How to run
### 1. Download The GCC dataset.

Tools/DownloadGCC.py
### 2. Format Each Dataset
Dataset/Data-img/:All images.

Dataset/Data-text/caption.txt: xxx.jpg,captionscaptions...(Each row)

Dataset/Data-text/train_imgname.txt: xxx.jpg(Each row)

Dataset/Data-text/test_imgname.txt: xxx.jpg(Each row)

Dataset/filter.pkl: {imgname1:captionscaptions,imgname2:captionscaptions...}

The Training program reads 2 txt files first. Then keeps the rows in the filter.pkl. This mechanism helps user easly scale down or split a dataset.

### 3. Train a model
Trainonxxx.ipynb

Hyper-parameters can be set within the file.

Run all.

### 4. Pridict
PridictCCD.ipynb

Set the model name and test data path.

run all.

### 5. Evaluation
eval.ipynb

Prepare output.csv and ref1.csv,ref2.csv...

Captions in the same row are considered as the corresponding y and yhat.

### Datasets
Flicker8k(24 Captions)

https://www.kaggle.com/adityajn105/flickr8k/activity

Google Conceptual Caption (Randomly chose 24K)

https://ai.google.com/research/ConceptualCaptions
