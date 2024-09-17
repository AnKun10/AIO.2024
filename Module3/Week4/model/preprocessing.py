import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.model_selection import train_test_split


def preprocessing(df):
    # Process categorical features
    categorical_cols = df.select_dtypes(include=['object']).columns.to_list()
    ordinal_encoder = OrdinalEncoder()
    encoded_categorical_cols = ordinal_encoder.fit_transform(
        df[categorical_cols]
    )
    encoded_categorical_df = pd.DataFrame(
        encoded_categorical_cols,
        columns=categorical_cols
    )
    numerical_df = df.drop(categorical_cols, axis=1)
    encoded_df = pd.concat(
        [numerical_df, encoded_categorical_df], axis=1
    )

    # Normalize
    normalizer = StandardScaler()
    dataset_arr = normalizer.fit_transform(encoded_df)

    # Split the dataset
    X, y = dataset_arr[:, 1:], dataset_arr[:, 0]
    test_size = 0.3
    random_state = 1
    is_shuffle = True
    X_train, X_val, y_train, y_val = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        shuffle=is_shuffle
    )

    return X_train, X_val, y_train, y_val
