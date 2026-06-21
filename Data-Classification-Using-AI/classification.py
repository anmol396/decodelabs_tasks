import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    # 2. Load Iris dataset
    iris = load_iris()
    
    # 3. Convert dataset to pandas DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    
    # 4. Dataset Understanding
    print("DATASET UNDERSTANDING")
    print(f"Dataset Shape: {df.shape}")
    print(f"Feature Names: {iris.feature_names}")
    print(f"Target Classes: {iris.target_names}")
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nDataset Info:")
    df.info()
    print("\nStatistical Summary:")
    print(df.describe())
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # 5. EDA
    print("\nEDA")
    print("Class Counts:")
    counts = df['target'].value_counts()
    for idx, count in counts.items():
        print(f"{iris.target_names[idx]} → {count}")
    print("\nCorrelation Matrix:")
    print(df[iris.feature_names].corr())
    print("\nShort Insights:")
    print("* Dataset is balanced.")
    print("* Petal features are most informative.")
    print("* Setosa appears easiest to classify.")
    
    # 6. Visualization
    os.makedirs('graphs', exist_ok=True)
    df_visual = df.copy()
    df_visual['species'] = df_visual['target'].map(lambda x: iris.target_names[x])
    
    # Histogram
    plt.figure(figsize=(10, 8), dpi=300)
    for i, col in enumerate(iris.feature_names):
        plt.subplot(2, 2, i + 1)
        sns.histplot(data=df_visual, x=col, hue='species', kde=True, multiple='stack', palette='Set2')
        plt.title(f'Distribution of {col}', fontsize=10, pad=10)
        plt.xlabel(col, fontsize=8)
        plt.ylabel('Count', fontsize=8)
    plt.tight_layout(pad=3.0)
    plt.savefig('graphs/histogram.png', dpi=300)
    plt.close()
    
    # Boxplot
    plt.figure(figsize=(10, 8), dpi=300)
    for i, col in enumerate(iris.feature_names):
        plt.subplot(2, 2, i + 1)
        sns.boxplot(data=df_visual, x='species', y=col, hue='species', palette='Set2', legend=False)
        plt.title(f'{col} by Species', fontsize=10, pad=10)
        plt.xlabel('Species', fontsize=8)
        plt.ylabel(col, fontsize=8)
    plt.tight_layout(pad=3.0)
    plt.savefig('graphs/boxplot.png', dpi=300)
    plt.close()
    
    # Heatmap
    plt.figure(figsize=(8, 6), dpi=300)
    sns.heatmap(df[iris.feature_names].corr(), annot=True, cmap='coolwarm', fmt='.2f', square=True, linewidths=0.5)
    plt.title('Feature Correlation Heatmap', fontsize=12, pad=15)
    plt.tight_layout()
    plt.savefig('graphs/heatmap.png', dpi=300)
    plt.close()
    
    # Pairplot
    sns.set_theme(style='ticks')
    pp = sns.pairplot(df_visual.drop(columns=['target']), hue='species', palette='Set2')
    pp.fig.suptitle('Pairwise Relationships of Iris Features', y=1.02, fontsize=14)
    pp.savefig('graphs/pairplot.png', dpi=300)
    plt.close()
    
    # Scatterplot
    plt.figure(figsize=(8, 6), dpi=300)
    sns.scatterplot(data=df_visual, x='petal length (cm)', y='petal width (cm)', hue='species', style='species', palette='Set2', s=100)
    plt.title('Petal Length vs Petal Width', fontsize=12, pad=15)
    plt.xlabel('Petal Length (cm)', fontsize=10)
    plt.ylabel('Petal Width (cm)', fontsize=10)
    plt.legend(title='Species', title_fontsize='10', loc='best')
    plt.tight_layout()
    plt.savefig('graphs/scatterplot.png', dpi=300)
    plt.close()
    
    print("\nGraphs generated successfully.")
    print("Saved inside graphs/ folder.")
    
    # 7. Data Preparation
    print("\nMODEL TRAINING")
    X = df[iris.feature_names]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 8. Model Training
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X_train, y_train)
    
    # 9. Evaluation
    y_pred = model.predict(X_test)
    print("\nMODEL EVALUATION")
    acc = accuracy_score(y_test, y_pred) * 100
    print(f"Accuracy Score: {acc:.2f}%")
    
    train_accuracy = model.score(X_train, y_train)
    test_accuracy = model.score(X_test, y_test)
    
    print("\nOVERFITTING CHECK")
    print(f"Training Accuracy: {train_accuracy:.2%}")
    print(f"Testing Accuracy : {test_accuracy:.2%}")
    
    if train_accuracy - test_accuracy > 0.10:
        print("Possible overfitting detected.")
    else:
        print("No significant overfitting detected.")
        
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # 10. Sample Predictions
    print("\nSAMPLE PREDICTIONS")
    for i in range(5):
        actual = iris.target_names[y_test.iloc[i]]
        pred = iris.target_names[y_pred[i]]
        print(f"Prediction {i+1}")
        print(f"Actual: {actual}")
        print(f"Predicted: {pred}")
        if i < 4:
            print()
        
    # 11. Feature Importance
    print("\nFEATURE IMPORTANCE")
    importances = model.feature_importances_
    feat_imp = pd.Series(importances, index=iris.feature_names).sort_values(ascending=False)
    for feat, imp in feat_imp.items():
        print(f"{feat}: {imp:.4f}")
        
    # 12. Final Output
    print("\nProject completed successfully.")

if __name__ == '__main__':
    main()
