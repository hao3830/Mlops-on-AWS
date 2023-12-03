import argparse
import joblib
import numpy as np
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

parser = argparse.ArgumentParser()

parser.add_argument("--train-test-ratio", type=float, default=0.25)
parser.add_argument("--model-dir", type=str, default=os.environ.get("SM_MODEL_DIR"))
parser.add_argument("--train", type=str, default=os.environ.get("SM_CHANNEL_TRAIN"))
parser.add_argument("--test", type=str, default=os.environ.get("SM_CHANNEL_TEST"))

args = parser.parse_args()

print("[INFO] Start training...")

train = pd.read_csv(os.path.join(args.train, "iris_train.csv"))
test = pd.read_csv(os.path.join(args.test, "iris_test.csv"))

X_train, X_test, y_train, y_test = train_test_split(
    train.drop(["target"], axis=1), train["target"], test_size=args.train_test_ratio
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))
print(f"[INFO] Model dumped to {os.path.join(args.model_dir, 'model.joblib')}")
y_pred = model.predict(X_test)
print(f"[INFO] Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"[INFO] Log loss: {log_loss(y_test, model.predict_proba(X_test))}")
