# Lectura de datos
import pandas as pd
# import numpy as np

df = pd.read_csv("../test_data/iris.csv")

# Matriz de features
X = df.iloc[:, :-1].values
# variable output
y = df.iloc[:, -1]
print(" --- Matrices executed ---")

# Creamos la instancia de LabelEncoder
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
y = encoder.fit_transform(y)
print(" --- LabelEncoder executed ---")

# Convertimos o serializamos las clases en formato pickle pkl
import joblib
# import pickle

path = "../models/iris_label_encoder.pkl"
joblib.dump(encoder, open(path, 'wb'))
print(" --- Pickle labelEncoder dump executed ---")

# Train and Test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30,
                                                            random_state=17)
# print(X_train[:10])
print(" --- Train and test executed ---")

# Train model
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors=4, 
                                    metric='minkowski', p=2)
classifier.fit(X_train, y_train)
print(" --- Classifier train executed ---")


# Test model
y_pred = classifier.predict(X_test)
print(" --- Classifier test executed ---")

# Metricas del modelo
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_true = y_test, y_pred = y_pred)
print(f"Accuracy score: {round(accuracy*100,4)}")

# Save model Pickle format pkl
import joblib
path = "../models/iris_knn.pkl"
joblib.dump(classifier, open(path, 'wb'))
print(" --- Pickle classifier dump executed ---")