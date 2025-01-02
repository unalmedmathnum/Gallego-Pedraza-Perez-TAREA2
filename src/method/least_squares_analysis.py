import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load preprocessed data
file_path = '../data/belén,-medellín-air-quality.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Ensure column names are stripped
data.columns = data.columns.str.strip()

# Convert 'date' column to datetime
data['date'] = pd.to_datetime(data['date'])

# Sort by date
data = data.sort_values(by='date')

# Prepare data for regression
data['days'] = (data['date'] - data['date'].min()).dt.days  # Days since the start date
X = data['days'].values.reshape(-1, 1)
y = data['pm25'].values

# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict values
y_pred = model.predict(X)

# Calculate errors
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

# Print model information
print(f"Linear model: PM2.5 = {model.coef_[0]:.4f} * days + {model.intercept_:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(data['days'], y, label='Observed Data', alpha=0.5)
plt.plot(data['days'], y_pred, color='red', label='Linear Fit')

# Add text for MSE and RMSE
textstr = f'MSE: {mse:.2f}\nRMSE: {rmse:.2f}'
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes,
         fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

plt.xlabel('Days since start')
plt.ylabel('PM2.5 Concentration')
plt.title('Linear Regression - PM2.5 Trend')
plt.legend()
plt.grid()
plt.show()