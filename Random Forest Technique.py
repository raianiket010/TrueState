import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
from sklearn.ensemble import RandomForestClassifier


data = pd.DataFrame({
    'housing_price': [250000, 450000, 350000, 600000, 275000, 320000, 500000, 410000],
    'rate_of_return': [5.0, 6.5, 5.5, 7.0, 5.2, 5.8, 6.8, 6.0],
    'expected_holdingPeriod': [5, 7, 6, 8, 5, 6, 7, 6], 
    'similarity_score': [0.8, 0.95, 0.85, 0.9, 0.75, 0.82, 0.92, 0.88],
    
    'deal_secured': [1, 1, 0, 1, 0, 0, 1, 1]
})
features = ['housing_price', 'rate_of_return', 'expected_holdingPeriod', 'similarity_score']
X = data[features]
y = data['deal_secured']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline that scales features and trains a Logistic Regression model
pipeline_lr = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(solver='liblinear'))
])


pipeline_lr.fit(X_train, y_train)


y_pred_lr = pipeline_lr.predict(X_test)
y_pred_proba_lr = pipeline_lr.predict_proba(X_test)[:, 1]



pipeline_rf = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(random_state=42))
])


param_grid = 
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [None, 5, 10]
}

grid_search = GridSearchCV(pipeline_rf, param_grid, cv=3, scoring='roc_auc')
grid_search.fit(X_train, y_train)
print("\nRandomForest Best Parameters:", grid_search.best_params_)

y_pred_rf = grid_search.predict(X_test)
y_pred_proba_rf = grid_search.predict_proba(X_test)[:, 1]

print("RandomForest Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("AUC-ROC:", roc_auc_score(y_test, y_pred_proba_rf))
print("Classification Report:\n", classification_report(y_test, y_pred_rf))
