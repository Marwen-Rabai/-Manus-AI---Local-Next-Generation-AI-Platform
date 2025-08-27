import os
import sys
import pandas as pd

# Ensure project's src/ is on sys.path for tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data.dataset import Dataset


def test_load_synthetic():
    ds = Dataset()
    df = ds.load_data()
    assert isinstance(df, pd.DataFrame)
    assert "target" in df.columns


def test_preprocess_missing_data(tmp_path):
    # create CSV without target column
    p = tmp_path / "nontarget.csv"
    df = pd.DataFrame({"a": [1, None, 3], "b": [4, 5, None]})
    df.to_csv(p, index=False)

    ds = Dataset(str(p))
    df2 = ds.load_data()
    X, y = ds.preprocess_data(df2)
    assert "target" in df2.columns or y is not None
