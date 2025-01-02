# Import necessary libraries
import pandas as pd  # For data manipulation
import numpy as np  # For numerical computations
import matplotlib.pyplot as plt  # For data visualization
from sklearn.linear_model import LinearRegression  # For linear regression modeling
from sklearn.metrics import mean_squared_error  # For error metrics

# Load preprocessed data
# Specify the file path to your CSV dataset
file_path = '../data/belén,-medellín-air-quality.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Clean column names by stripping leading and trailing whitespace
data.columns = data.columns.str.strip()

# Convert the 'date' column from string to datetime for easier manipulation
data['date'] = pd.to_datetime(data['date'])

# Sort the data by the 'date' column to ensure chronological order
data = data.sort_values(by='date')

# Prepare data for regression
# Calculate the number of days since the start date
data['days'] = (data['date'] - data['date'].min()).dt.days
# Reshape the 'days' column for use as the independent variable (X) in regression
X = data['days'].values.reshape(-1, 1)
# Use the 'pm25' column as the dependent variable (y)
y = data['pm25'].values

# Fit a linear regression model to the data
model = LinearRegression()
model.fit(X, y)

# Predict PM2.5 values using the fitted model
y_pred = model.predict(X)

# Calculate error metrics
mse = mean_squared_error(y, y_pred)  # Mean Squared Error
rmse = np.sqrt(mse)  # Root Mean Squared Error

# Print model details and error metrics
print(f"Linear model: PM2.5 = {model.coef_[0]:.4f} * days + {model.intercept_:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

# Visualization of the results
plt.figure(figsize=(10, 6))  # Set the figure size

# Scatter plot of the observed data
plt.scatter(data['days'], y, label='Observed Data', alpha=0.5)

# Plot the linear regression fit
plt.plot(data['days'], y_pred, color='red', label='Linear Fit')

# Add text box with error metrics (MSE and RMSE)
textstr = f'MSE: {mse:.2f}\nRMSE: {rmse:.2f}'
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes,
         fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

# Add labels, title, legend, and grid
plt.xlabel('Days since start')  # X-axis label
plt.ylabel('PM2.5 Concentration')  # Y-axis label
plt.title('Linear Regression - PM2.5 Trend')  # Plot title
plt.legend()  # Display legend
plt.grid()  # Add grid lines

# Display the plot
plt.show()
