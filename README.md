# Genetic Algorithm for Knapsack Problem and Text Clustering using K-Means

This repository contains Python scripts implementing a genetic algorithm for solving the knapsack problem and text clustering using the K-Means algorithm.

## Knapsack Problem

The genetic algorithm aims to optimize the selection of items to be placed in a knapsack to maximize the total value without exceeding its weight capacity. It includes the following components:

- `Item` class: Defines an item with weight and value attributes.
- `generate_population`: Creates a population of chromosomes, where each chromosome represents a possible selection of items.
- `fitness`: Calculates the fitness (total value) of a chromosome while considering the knapsack's weight constraint.
- `selection`: Selects parent chromosomes based on tournament selection.
- `crossover`: Performs crossover between parent chromosomes to generate offspring.
- `mutate`: Introduces random mutations in chromosomes based on a mutation rate.
- `genetic_algorithm`: Executes the genetic algorithm by evolving populations over generations to find the best solution.

## Text Clustering using K-Means

This section utilizes the K-Means algorithm to cluster text data from the SMS Spam Collection dataset. It includes the following steps:

- Preprocesses text data using TF-IDF vectorization.
- Determines the optimal number of clusters using the elbow method by plotting within-cluster sum of squares (WCSS) against the number of clusters.
- Chooses the optimal number of clusters based on the elbow point.
- Trains the K-Means model with the optimal number of clusters.
- Assigns cluster labels to the testing set and computes evaluation metrics (accuracy, completeness, homogeneity).

## Dependencies

- `random`: For generating random numbers.
- `pandas`: For data manipulation.
- `scikit-learn`: For machine learning functionalities including TF-IDF vectorization, K-Means clustering, and evaluation metrics.
- `matplotlib`: For data visualization.

## Usage

1. Ensure you have the required dependencies installed (`pip install pandas scikit-learn matplotlib`).
2. Place the dataset file `spam.csv` in the same directory as the script.
3. Run the script to execute both the genetic algorithm and text clustering tasks.

## Authors

- [@nomankhokhar](https://www.github.com/nomankhokhar)

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## 🚀 About Me

I'm a full Stack Developer...
