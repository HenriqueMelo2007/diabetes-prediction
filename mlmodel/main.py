import pandas as pd  # type: ignore
from sklearn.ensemble import RandomForestClassifier  # type: ignore
from sklearn.model_selection import StratifiedKFold, RandomizedSearchCV, cross_validate  # type: ignore
from sklearn.metrics import f1_score, make_scorer  # type: ignore
from scipy.stats import randint  # type: ignore
import joblib  # type: ignore


train_df = pd.read_csv("diabetes-dataset.csv")
X = train_df.drop(columns=["Outcome"])
y = train_df["Outcome"]


cv_outer = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
custom_scorer = make_scorer(f1_score, average="macro", greater_is_better=True)


rf_model = RandomForestClassifier(random_state=42)


param_dist = {
    "n_estimators": [100, 500, 1000],
    "max_depth": [None, 15, 20],
    "min_samples_split": [2, 5, 10, 15],
    "min_samples_leaf": randint(1, 10),
    "bootstrap": [True, False],
    "max_features": ["sqrt", "log2"],
}


search = RandomizedSearchCV(
    estimator=rf_model,
    param_distributions=param_dist,
    n_iter=300,
    scoring=custom_scorer,
    cv=5,
    verbose=1,
    n_jobs=-1,
    random_state=42,
)


results = cross_validate(
    search, X, y, cv=cv_outer, scoring=custom_scorer, return_estimator=True, n_jobs=-1
)


print("F1-macro for each extern fold:", results["test_score"])
print("F1-macro average:", results["test_score"].mean())


best_index = results["test_score"].argmax()
best_search_model = results["estimator"][best_index]
best_params = best_search_model.best_params_

print("\nBest Params:")
print(best_params)


final_model = RandomForestClassifier(**best_params, random_state=42)
final_model.fit(X, y)


joblib.dump(final_model, "ml_model_random_forest_diabetes.pkl")
print("\nFinal ML model trained and saved as 'ml_model_random_forest_diabetes.pkl'")

# Best Params {'bootstrap': False, 'max_depth': None, 'max_features': 'sqrt', 'min_samples_leaf': 2, 'min_samples_split': 10, 'n_estimators': 1000}
