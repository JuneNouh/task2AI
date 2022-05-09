import pandas as pd

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = pd.read_csv("iris.csv")

df_norm = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].apply(
    lambda x: (x - x.min()) / (x.max() - x.min()))
print(df_norm.sample(n=5))

target = data[['variety']].replace(['Setosa', 'Versicolor', 'Virginica'], [0, 1, 2])
print(target.sample(n=5))

df = pd.concat([df_norm, target], axis=1)
df.sample(n=5)

train, test = train_test_split(df, test_size=0.3)
trainX = train[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
trainY = train.variety
testX = test[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
testY = test.variety
trainX.head(5)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(2), random_state=1, )
clf_three = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3), random_state=1, )
clf_threeLayer_threeNeuron = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 3), random_state=1, )
print(clf.fit(trainX, trainY))
print(clf_three.fit(trainX, trainY))
print(clf_threeLayer_threeNeuron.fit(trainX, trainY))

prediction = clf.predict(testX)
prediction_three = clf_three.predict(testX)
prediction_threeNeuron = clf_threeLayer_threeNeuron.predict(testX)
print(prediction)

print(testY.values)

print('The accuracy is:', metrics.accuracy_score(prediction, testY))
print('The accuracy is:', metrics.accuracy_score(prediction_three, testY))
print('The accuracy is:', metrics.accuracy_score(prediction_threeNeuron, testY))