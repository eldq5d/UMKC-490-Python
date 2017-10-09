import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cross_validation import train_test_split

# Load dataset, using only one feature from x
diabetes = datasets.load_diabetes()
x = diabetes.data[:, np.newaxis, 2]
y = diabetes.target

# Split data for testing and training
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Create linear regression object
model = linear_model.LinearRegression()

# Train model with training sets
model.fit(x_train, y_train)

# Make predictions using the testing set
y_pred = model.predict(x_test)

# Plot
plt.scatter(x_test, y_test,  color='pink')
plt.plot(x_test, y_pred, color='teal', linewidth=2.5)

plt.xticks(())
plt.yticks(())

plt.show()
