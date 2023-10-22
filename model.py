import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the data from the URL
url = "https://raw.githubusercontent.com/Medlytics2023/Week1/master/Datasets/allhypo.train.data"
data = pd.read_csv(url, header=None)

# Drop non-numeric columns
numeric_data = data.select_dtypes(include='number')

# Check for missing values
missing_values = numeric_data.isnull().sum()
print("Missing Values:")
print(missing_values)

# Impute missing values using mean
imputer = SimpleImputer(strategy='mean')
imputed_data = imputer.fit_transform(numeric_data)
imputed_data = pd.DataFrame(imputed_data, columns=numeric_data.columns)

# Perform one-hot encoding
encoded_data = pd.get_dummies(imputed_data)

print(encoded_data)

# Split the data into features (X) and target variable (y)
X = encoded_data.drop('Class', axis=1)
y = encoded_data['Class']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an instance of the Random Forest Classifier
model = RandomForestClassifier()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)