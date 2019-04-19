import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

def run(train_file, test_file):
    data = pd.read_csv(train_file)
    test = pd.read_csv(test_file)

    from sklearn.preprocessing import LabelEncoder
    labelencoder=LabelEncoder()
    data["class"] = labelencoder.fit_transform(data["class"])
    for col in data.columns:
        if(col != "class" and col != "Id"):
            data[col] = labelencoder.fit_transform(data[col])
            test[col] = labelencoder.transform(test[col])

    X_train = np.array(data.iloc[:, 1:23])
    y_train = data.iloc[:, 0]
    test_data = np.array(test.iloc[:, 0:22])

    scaler = StandardScaler()
    X_train=scaler.fit_transform(X_train)
    test_data = scaler.transform(test_data)

    mlp = MLPClassifier()
    mlp.fit(X_train,y_train)

    y_prob = mlp.predict_proba(test_data)[:,1] # This will give you positive class prediction probabilities
    y_pred = np.where(y_prob > 0.5, 1, 0) # This will threshold the probabilities to give class predictions.

    result = []
    for i in range(len(y_pred)):
        if(y_pred[i] == 0):
            result.append('e')
        else:
            result.append('p')

    result = np.asarray(result)
    df = pd.DataFrame(test['Id'])
    df['class'] = result
    df.to_csv("test_results.csv", index = False)

if __name__ == "__main__":
    train_file = sys.argv[1]
    test_file = sys.argv[2]
    run(train_file, test_file)