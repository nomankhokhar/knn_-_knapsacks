import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, completeness_score, homogeneity_score
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("spam.csv", encoding='latin1')

# Split the dataset into training and testing sets
train_size = int(0.8 * len(df))  # 80% for training, 20% for testing
train_data = df.iloc[:train_size]
test_data = df.iloc[train_size:]

# Preprocess the text data using TF-IDF vectorization
vectorizer = TfidfVectorizer()
train_features = vectorizer.fit_transform(train_data["v2"])
test_features = vectorizer.transform(test_data["v2"])

# Determine the appropriate number of clusters (K) using the elbow method
wcss = []
for k in range(1, 11):
    # Create a K-Means instance
    kmeans = KMeans(n_clusters=k, random_state=42)
    
    # Fit the K-Means model to the training features
    kmeans.fit(train_features)
    
    # Compute the within-cluster sum of squares (WCSS) and add it to the list
    wcss.append(kmeans.inertia_)

# Plot the elbow curve to visualize the optimal K
plt.plot(range(1, 11), wcss)
plt.xlabel("Number of Clusters (5)")
plt.ylabel("WCSS (Within-Cluster Sum of Squares.)")
plt.title("Elbow Method")
plt.show()

# Choose the optimal K based on the elbow curve
k = 5

# Train the K-Means model with the optimal K
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(train_features)

# Assign cluster labels to the testing set
predicted_labels = kmeans.predict(test_features)

# Evaluate the performance of the K-Means model
accuracy = accuracy_score(test_data["v1"], predicted_labels)
completeness = completeness_score(test_data["v1"], predicted_labels)
homogeneity = homogeneity_score(test_data["v1"], predicted_labels)

# Print the evaluation metrics
print("Accuracy:", accuracy)
print("Completeness:", completeness)
print("Homogeneity:", homogeneity)
