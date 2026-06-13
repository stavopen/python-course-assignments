import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# -------------------------
# 1. Load data
# -------------------------

tumor = pd.read_csv("data/BC-TCGA-Tumor.txt", sep="\t")
normal = pd.read_csv("data/BC-TCGA-Normal.txt", sep="\t")

# -------------------------
# 2. Add labels
# -------------------------

tumor["label"] = 1
normal["label"] = 0

# -------------------------
# 3. Combine datasets
# -------------------------

df = pd.concat([tumor, normal], axis=0)

print("\nDataset shape:", df.shape)

# -------------------------
# 4. Split features / target
# -------------------------

X = df.drop("label", axis=1)
y = df["label"]

# convert to numeric
X = X.apply(pd.to_numeric, errors="coerce")

# replace inf / nan safely
X = X.replace([np.inf, -np.inf], np.nan)
X = X.fillna(0)

# -------------------------
# 5. Clip extreme values (stable version)
# -------------------------

upper_bounds = X.quantile(0.99)

X = X.apply(lambda col: col.clip(upper=upper_bounds[col.name]))

# -------------------------
# 6. Train / test split
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -------------------------
# 7. Random Forest model
# -------------------------

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# -------------------------
# 8. Predictions
# -------------------------

y_pred = model.predict(X_test)

# -------------------------
# 9. Evaluation
# -------------------------

print("\n====================")
print("TEST RESULTS")
print("====================")

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -------------------------
# 10. Cross-validation
# -------------------------

print("\n====================")
print("CROSS VALIDATION")
print("====================")

cv_model = RandomForestClassifier(n_estimators=200, random_state=42)
scores = cross_val_score(cv_model, X, y, cv=5)

print("CV Scores:", scores)
print("Mean CV Accuracy:", scores.mean())

# -------------------------
# 11. Feature importance
# -------------------------

importances = model.feature_importances_
indices = np.argsort(importances)[-10:]

print("\n====================")
print("TOP FEATURES")
print("====================")

for i in indices:
    print(X.columns[i], importances[i])

plt.figure()
plt.barh(range(len(indices)), importances[indices])
plt.yticks(range(len(indices)), X.columns[indices])
plt.title("Top Predictive Genes")
plt.tight_layout()
plt.savefig("important_genes.png")
plt.show()

# -------------------------
# 12. PCA (HIGH VARIANCE GENES)
# -------------------------

gene_variance = X.var()
top_genes = gene_variance.sort_values(ascending=False).head(50).index
X_high_var = X[top_genes]

# -------------------------
# 13. SAFE log transform
# -------------------------

X_log = np.log1p(np.abs(X_high_var))

# final safety cleanup
X_log = np.nan_to_num(X_log, nan=0.0, posinf=0.0, neginf=0.0)

# -------------------------
# 14. Scaling
# -------------------------

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_log)

# -------------------------
# 15. PCA
# -------------------------

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("\nExplained variance ratio:", pca.explained_variance_ratio_)

# -------------------------
# 16. PCA visualization (DOWNSAMPLED)
# -------------------------

# number of points to plot
n_samples = 3000

# random subset (for visualization only)
sample_idx = np.random.choice(len(X_pca), n_samples, replace=False)

X_plot = X_pca[sample_idx]
y_plot = y.iloc[sample_idx].values

plt.figure()

plt.scatter(
    X_plot[y_plot == 0, 0],
    X_plot[y_plot == 0, 1],
    label="Normal",
    alpha=0.5,
    s=10
)

plt.scatter(
    X_plot[y_plot == 1, 0],
    X_plot[y_plot == 1, 1],
    label="Tumor",
    alpha=0.5,
    s=10
)

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA on High-Variance Genes (Downsampled View)")
plt.legend()

plt.tight_layout()
plt.savefig("pca_downsampled.png")
plt.show()