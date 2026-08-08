import pandas as pd, numpy as np, pickle
from sklearn.ensemble import IsolationForest

np.random.seed(42)
thrust = np.random.uniform(200, 500, 1000)
torque = (thrust * 0.45) + np.random.normal(0, 5, 1000)
df = pd.DataFrame({'Thrust': thrust, 'Torque': torque})

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df)
with open('isolation_forest.pkl', 'wb') as f:
    pickle.dump(model, f)
