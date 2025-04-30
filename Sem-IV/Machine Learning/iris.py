import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load local iris dataset
df = pd.read_csv('Iris.csv')  # replace with the path to your local file

# Encode target labels if they are strings (for KNN)
le = LabelEncoder()
df['species_encoded'] = le.fit_transform(df['Species'])

# ----------- KNN Classification -----------
# Features and target
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]#change accordig to your dataset
y = df['species_encoded']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# Evaluate KNN
print("=== KNN Classification Report ===")
print(classification_report(y_test, y_pred_knn, target_names=le.classes_))


# ----------- K-Means Clustering -----------
# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means model (3 clusters for 3 species)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)
cluster_labels = kmeans.labels_

# Add cluster labels to DataFrame for comparison
df['cluster'] = cluster_labels

# Visualize clusters using first two principal components (or original features)
plt.figure(figsize=(8, 5))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=cluster_labels, cmap='viridis', s=50)
plt.title("K-Means Clustering (Standardized Features)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
