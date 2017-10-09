from sklearn import datasets, metrics
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split

# Load dataset
digitdataset = datasets.load_digits()

x = digitdataset.data[:, :2]
y = digitdataset.target

# Split data for training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# First model for testing accuracy
# model = SVC(kernel='linear')

# Other model for testing:
model = SVC(kernel='rbf')

# Fit the model and run prediction using test data
model.fit(x_train, y_train)
pred = model.predict(x_test)

# Check the accuracy of the model
print(metrics.accuracy_score(pred, y_test))
