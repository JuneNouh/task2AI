from sklearn import tree
from sklearn.model_selection import train_test_split
import pandas as pd


df = pd.read_csv("iris.csv")

all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
all_classes = df['variety'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)


myTree = tree.DecisionTreeClassifier()
classifier = myTree.fit(train_inputs, train_classes)

print("The accuracy is ", myTree.score(test_inputs, test_classes) * 100, "%")

for root in tree.plot_tree(classifier):
    print(root)
