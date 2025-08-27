import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.ai.model import AIModel

X = np.random.RandomState(0).randn(40, 10)
y = (X[:, 0] > 0).astype(int)
model = AIModel()
model.train_model(X, y)
print('Model trained; prediction for "hello":', model.predict('hello'))
