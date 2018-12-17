#!/usr/python
import read_input
import numpy as np

# import pandas as pd
# x = pd.get_dummies(pd.Series(list('abc')), dtype=float)
# print(x)

passenagers = read_input.read_input()

features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
embarked = ['C', 'Q', 'S']

x = []
for i in range(len(passenagers)):
	x1 = []
	for key in features:
		if key == "Sex":
			x1.append(1.0 if passenagers[i][key] == 'male' else 0.0)
		elif key == "Embarked":
			#FIXME how to deal with missing data?
			x1 = x1 + [0.0, 0.0, 0.0]
			for idx, e in enumerate(embarked):
				if passenagers[i][key] == e:
					x1[idx + 6] = 1.0
		else:
			#FIXME how to deal with missing data?
			try:
				x1.append(float(passenagers[i][key]))
			except:
				x1.append(0.0)
	x.append(x1)

X = np.vstack(x)
# ["Pclass", "Sex (M)", "Age", "SibSp", "Parch", "Fare", "Embarked (C)", "Embarked (Q)", "Embarked (S)"]
print((X[2,:]))
print(X.shape)