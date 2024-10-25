import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# Load dataset
data = pd.read_csv('uber_dataset.csv')

# Splitting the dataset into features (X) and target (y)
data_x = data.iloc[:, 0:-1].values
data_y = data.iloc[:, -1].values

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.3, random_state=0)

# Linear Regression Model
reg_linear = LinearRegression()
reg_linear.fit(X_train, y_train)
print("Linear Regression Train Score:", reg_linear.score(X_train, y_train))
print("Linear Regression Test Score:", reg_linear.score(X_test, y_test))

# Random Forest Regressor Model
reg_rf = RandomForestRegressor(n_estimators=100, random_state=0)
reg_rf.fit(X_train, y_train)
print("Random Forest Train Score:", reg_rf.score(X_train, y_train))
print("Random Forest Test Score:", reg_rf.score(X_test, y_test))

# Gradient Boosting Regressor Model
reg_gbr = GradientBoostingRegressor(n_estimators=100, random_state=0)
reg_gbr.fit(X_train, y_train)
print("Gradient Boosting Regressor Train Score:", reg_gbr.score(X_train, y_train))
print("Gradient Boosting Regressor Test Score:", reg_gbr.score(X_test, y_test))

# Saving the models using pickle
pickle.dump(reg_linear, open('model_linear.pkl', 'wb'))
pickle.dump(reg_rf, open('model_rf.pkl', 'wb'))
pickle.dump(reg_gbr, open('model_gbr.pkl', 'wb'))

# Loading a model to make predictions
model = pickle.load(open('model_linear.pkl', 'rb'))
print("Linear Regression Prediction:", model.predict([[80, 1770000, 6000, 85]]))

model_rf = pickle.load(open('model_rf.pkl', 'rb'))
print("Random Forest Prediction:", model_rf.predict([[80, 1770000, 6000, 85]]))

model_gbr = pickle.load(open('model_gbr.pkl', 'rb'))
print("GBR Prediction:", model_gbr.predict([[80, 1770000, 6000, 85]]))
