import os
import pandas as pd
from sklearn.datasets import make_classification
from urllib.parse import urlparse


class Dataset:
    """Flexible dataset loader.

    Supported input types:
    - Local CSV files (.csv)
    - Local JSON files (.json)
    - Local Parquet files (.parquet)
    - Remote CSV/JSON via http(s) URLs

    Expected schema (recommended): a table where feature columns are numeric and
    the target column is named 'target'. If 'target' is missing, training code
    will create a default target (zeros) but results may be meaningless.
    """

    def __init__(self, file_path: str | None = None):
        self.file_path = file_path
        self.data = None

    def _is_url(self, path: str) -> bool:
        try:
            parsed = urlparse(path)
            return parsed.scheme in ("http", "https")
        except Exception:
            return False

    def load_data(self) -> pd.DataFrame:
        """Load dataset from provided path or generate synthetic data.

        Returns
        -------
        pd.DataFrame
            DataFrame containing features and a 'target' column when available.
        """
        if self.file_path:
            # remote URL
            if self._is_url(self.file_path):
                if self.file_path.endswith(".json"):
                    df = pd.read_json(self.file_path)
                    self.data = df
                    return df
                else:
                    # assume CSV by default
                    df = pd.read_csv(self.file_path)
                    self.data = df
                    return df

            # local file
            if os.path.exists(self.file_path):
                lower = self.file_path.lower()
                if lower.endswith('.csv'):
                    df = pd.read_csv(self.file_path)
                    self.data = df
                    return df
                if lower.endswith('.json'):
                    df = pd.read_json(self.file_path)
                    self.data = df
                    return df
                if lower.endswith('.parquet') or lower.endswith('.pq'):
                    # requires pyarrow or fastparquet installed
                    df = pd.read_parquet(self.file_path)
                    self.data = df
                    return df

        # Fallback: synthetic dataset
        X, y = make_classification(n_samples=200, n_features=10, n_informative=5, random_state=42)
        cols = [f"f{i}" for i in range(X.shape[1])]
        df = pd.DataFrame(X, columns=cols)
        df["target"] = y
        self.data = df
        return df

    def preprocess_data(self, df: pd.DataFrame | None = None, target_column: str = "target") -> tuple:
        """Basic preprocessing: fill NAs, separate features and target, return (X, y).

        Parameters
        ----------
        df : pd.DataFrame | None
            DataFrame to preprocess. If None, uses previously loaded data.
        target_column : str
            Name of the target column to extract.
        """
        if df is None:
            df = self.data
        if df is None:
            raise ValueError("No data available to preprocess")

        df = df.copy()
        df.fillna(0, inplace=True)

        if target_column not in df.columns:
            # Create a default target (all zeros) if missing — caller should replace with real target
            df[target_column] = 0

        X = df.drop(columns=[target_column])
        y = df[target_column]
        return X, y