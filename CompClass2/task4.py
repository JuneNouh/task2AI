from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='white', color_codes=True)

iris = pd.read_csv('iris.csv')

X = iris.iloc[:, :4]
y = iris.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1)

for k in [1, 3, 5, 11]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_predict1 = knn.predict(X_test)

    print('The score of knn algorithm with k=', k, ' is:', accuracy_score(y_test, y_predict1) * 100, '%')

sns.FacetGrid(iris, height=5, hue="variety").map(plt.scatter, "sepal.length", "sepal.width").add_legend()
sns.FacetGrid(iris, height=5, hue="variety").map(plt.scatter, "petal.length", "petal.width").add_legend()
plt.show()

# They have all the same accuracy and it is better than task3
