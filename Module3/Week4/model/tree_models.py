from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from Module3.Week4.model.preprocessing import preprocessing


def evaluate(y_val, y_pred):
    mae = mean_absolute_error(y_val, y_pred)
    mse = mean_squared_error(y_val, y_pred)
    print('Evaluation results on validation set:')
    print(f'Mean Absolute Error: {mae}')
    print(f'Mean Squared Error: {mse}')


def rf_regressor(df, random_state=1):
    X_train, X_val, y_train, y_val = preprocessing(df)
    regressor = RandomForestRegressor(random_state=random_state)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_val)
    evaluate(y_val, y_pred)


def ada_regressor(df, random_state=1):
    X_train, X_val, y_train, y_val = preprocessing(df)
    regressor = AdaBoostRegressor(random_state=random_state)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_val)
    evaluate(y_val, y_pred)


def gb_regressor(df, random_state=1):
    X_train, X_val, y_train, y_val = preprocessing(df)
    regressor = GradientBoostingRegressor(random_state=random_state)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_val)
    evaluate(y_val, y_pred)
