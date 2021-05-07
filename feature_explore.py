# -*- coding: utf-8 -*-
"""HW6_lee_chris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RNV2cnABKEJMf7TwbfBB81gOxyOkTsl1
"""

import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn import tree
from matplotlib import pyplot as plt

#A
df = pd.read_csv('mushrooms.csv')

#B
df.head()

df.describe

df.info()

#the dependent variable is class (p = poisonous, e=edible)

#C
df2 = df.drop(['class'], axis=1)
df3 = df.drop(['class'], axis=1)
df2 = pd.get_dummies(df2)

X = df2
y = df['class']

#D
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =.3, random_state=2020, stratify=y)

#E
clf = DecisionTreeClassifier(max_depth = 6, criterion='entropy', random_state=2020)
clf = clf.fit(X_train, y_train)

"""2. Print the confusion matrix. 
Also visualize the confusion matrix using plot_confusion_matrix from sklearn.metrics (3 marks)


"""

pred = clf.predict(X_test)
confusion_matrix(y_test, pred)
plot_confusion_matrix(clf, X_test, y_test)

train_result = clf.score(X_train, y_train)
print(train_result)

test_result = clf.score(X_test, y_test)
print(test_result)

# text decision tree
text_rep = tree.export_text(clf)
print(text_rep)

#determine the feature names
X.columns

print(clf.classes_.tolist())

# Commented out IPython magic to ensure Python compatibility.
#plot tree decision tree
# %matplotlib inline
X.columns
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(clf, 
                   feature_names=X.columns,  
                   class_names=clf.classes_.tolist(),
                   filled=True)

important = pd.DataFrame(zip(X_train.columns, clf.feature_importances_))
important.sort_values(by=[1],ascending=False)
#order_n, bruises_t, stalk-root_c are the top three most important features

#create df with requested features
values_dict = {'cap-shape': ['x'], 'cap-surface': ['s'], 'cap-color' : ['n'],
               'bruises' : ['t'], 'odor' : ['y'], 'gill-attachment' : ['f'], 
               'gill-spacing' : ['c'], 'gill-size' : ['n'], 'gill-color' : ['k'],
               'stalk-shape' : ['e'], 'stalk-root' : ['e'],
               'stalk-surface-above-ring' : ['s'], 'stalk-surface-below-ring' : ['s'],
               'stalk-color-above-ring' : ['w'], 'stalk-color-below-ring' : ['w'], 
               'veil-type' : ['p'], 'veil-color' : ['w'], 'ring-number' : ['o'],
               'ring-type' : ['p'], 'spore-print-color' : ['r'], 'population' : ['s'],
               'habitat' : ['u']}

vf = pd.DataFrame(values_dict)

#concat df with what you have
all = pd.concat([vf, df3], ignore_index=True)

#predict
df4 = pd.get_dummies(all)
print(clf.predict(df4.loc[[0]]))