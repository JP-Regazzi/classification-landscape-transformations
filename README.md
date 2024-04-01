# 2EL1730 Machine Learning Project - Jan. 2024

Welcome to the repository for our participation in the Kaggle competition: **2EL1730 Machine Learning Project - Jan. 2024**. Our team has developed various machine learning models to classify geographical areas into one of six man-made features based on multi-date remote sensing data.

## Overview

This project involves the use of machine learning techniques to process and classify geographical features obtained from satellite images. The challenge is to classify a given geographical area into one of six classes: Demolition, Road, Residential, Commercial, Industrial, and Mega Projects.

## Data

The dataset includes geographical features represented as irregular polygons, with categorical values describing the status of the polygon on different dates and neighborhood urban and geographical features. The dataset is divided into training and testing sets, provided as `train.geojson` and `test.geojson`.

## Code

This repository contains all the code used in our submission, including data preprocessing, feature engineering, model training, and evaluation scripts. Our primary models include:

- **Random Forest**: Our main approach, providing a balanced trade-off between accuracy and computational efficiency.
- **Logistic Regression**: A baseline model for comparison.
- **XGBoost**: An advanced gradient boosting model for higher accuracy.
- **Neural Network**: A deep learning approach for capturing complex patterns.
- **k-NN (k-Nearest Neighbors)**: A simple yet effective model for benchmarking.

## Models

Each model directory contains the following:

- Preprocessing and training scripts.
- Hyperparameter tuning configurations.
- Evaluation and cross-validation scripts.

## Discussion

We have explored various strategies for feature engineering, including one-hot encoding of multi-valued categorical columns and geometric property extraction from polygons. Dimensionality reduction techniques were also employed to enhance model performance.

## Leaderboard

Our team's performance on the Kaggle leaderboard is a testament to our rigorous model tuning and evaluation process. The final evaluation metric is the Mean F1-Score.

## References

This project builds upon the dataset and challenge outlined by Sagar Verma et al. in their paper on the QFabric: Multi-Task Change Detection Dataset.

## How to Use

1. Clone this repository.
2. Install required libraries using `requirements.txt`.
3. Explore individual model directories for specific instructions on training and evaluation.

For more details about the challenge, visit the [Kaggle competition page](https://kaggle.com/competitions/2el1730-machine-learning-project-january-2024).

---

©2024 Team Feature Innovators. For questions or feedback, please contact us at joao-pedro.regazzi-ferreira-da-silva@student-cs.fr.
