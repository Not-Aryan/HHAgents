import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.impute import SimpleImputer

# Download the data from the URL
url = "cleaned_data_real.csv"
data = pd.read_csv(url)

# Convert columns to numeric type
# data = data.apply(pd.to_numeric, errors='coerce')

# Split the data into input features (X) and the target variable (y)
X = data.iloc[:, :-1]  # Input features (all columns except the last one)
y = data.iloc[:, -1]   # Target variable (last column)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the imputer on the training data and transform both training and testing data
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Create a Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

print(y_pred, y_test)

# # Calculate the accuracy of the model
# accuracy = accuracy_score(y_test, y_pred)
# print("Model accuracy:", accuracy)

# # Calculate precision, recall, and F1-score
# precision = precision_score(y_test, y_pred)
# recall = recall_score(y_test, y_pred)
# f1 = f1_score(y_test, y_pred)

# print("Precision:", precision)
# print("Recall:", recall)
# print("F1-score:", f1)

# # Save the results to a CSV file
# results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
# results.to_csv('model_results.csv', index=False)