import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import pickle

df = pd.read_csv("salary_data.csv")

X = df.drop(["Salary_Annual_USD", "Salary_Monthly_USD"], axis=1)
y = df["Salary_Annual_USD"]

categorical_cols = ["Education", "JobRole", "Location", "Country"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ],
    remainder='passthrough'
)

model = RandomForestRegressor(n_estimators=150, random_state=42)

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", model)
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline.fit(X_train, y_train)

pred = pipeline.predict(X_test)
print("R2 Score:", r2_score(y_test, pred))

with open("model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print(" Model saved after training")