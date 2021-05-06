# masters-thesis

This repository contains files related to my 2021 Master's Thesis.

The goal of this project is to find out the effectiveness of various classification models with different features in a hate speech classification task.

To do this, three different dataset were utilised: 
  - Founta et al. (2018) - https://www.dropbox.com/sh/4mapojr85a6sc76/AABYMkjLVG-HhueAgd0qM9kwa?dl=0;
  - Davidson et al. (2017) - https://github.com/t-davidson/hate-speech-and-offensive-language/blob/master/data/labeled_data.csv;
  - Gao & Huang (2017) - https://github.com/sjtuprog/fox-news-comments/blob/master/fox-news-comments.json.

Further, the following models are applied to the datasets:
  - Logistic Regression (LR);
  - Random Forest (RF);
  - Naive Bayes (NB);
  - Support Vector Machine (SVM).

LSTM model was also considered, however, it was rejected to long training time.
Nevertheless, LSTM architecture was used to identify hateful tweets in the Founta et al. (2018) dataset.
Further research could potentially employ this model on other corpora.

Additionally, aspect such as n-grams and sentiment analysis were considered.

The results vary depending on the features and models.
