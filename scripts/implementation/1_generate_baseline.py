import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import pickle

# Dataset Generation: perfectly correlating thrust curves with torque spikes
np.random.seed(42)
n_samples = 1000
# Baseline normal tool behavior
thrust = np.random.uniform(200, 500, n_samples)
torque = (thrust * 0.45) + np.random.normal(0, 5, n_samples)

df = pd.DataFrame({'Thrust': thrust, 'Torque': torque})

# ML Detection Engine: Training an Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df)

with open('isolation_forest.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Realistic dataset generated and model trained.")
