import pandas as pd
from Module3.Week4.model.tree_models import rf_regressor, ada_regressor, gb_regressor

dataset_path = '../dataset/Housing.csv'
df = pd.read_csv(dataset_path)

rf_regressor(df)
ada_regressor(df)
gb_regressor(df)
