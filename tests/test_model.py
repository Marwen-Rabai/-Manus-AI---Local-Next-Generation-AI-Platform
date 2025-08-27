import os
import sys
import numpy as np

# Ensure project's src/ is on sys.path for tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.ai.model import AIModel


def test_train_and_predict():
    X = np.random.RandomState(0).randn(50, 10)
    y = (X[:, 0] > 0).astype(int)
    model = AIModel()
    model.train_model(X, y)
    pred = model.predict(X[:5])
    assert len(pred) == 5


def test_predict_without_train():
    model = AIModel()
    try:
        model.predict("hello")
        assert False, "Expected RuntimeError for predict without training"
    except RuntimeError:
        pass
