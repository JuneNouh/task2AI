from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


df = pd.read_csv('diabetes.csv')

X = df[
    ['pregnant-times', 'glucose-concentr', 'blood-pressure', 'skin-thickness', 'insulin', 'mass-index', 'pedigree-func',
     'age']].values
y = df['class'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1)

myTree = tree.DecisionTreeClassifier()
classifier = myTree.fit(X_train, y_train)

print("The accuracy of decision tree classifier is ", myTree.score(X_test, y_test) * 100, "%")

for root in tree.plot_tree(classifier):
    print(root)


for k in [1, 3, 5, 11]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_predict1 = knn.predict(X_test)
    print('The score of knn algorithm with k=', k, ' is:', accuracy_score(y_test, y_predict1) * 100, '%')
