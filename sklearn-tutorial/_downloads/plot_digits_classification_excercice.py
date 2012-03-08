from scikits.learn import datasets, neighbors, linear_model

digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target

n_samples = len(X_digits)

X_train = X_digits[:.9*n_samples]
y_train = y_digits[:.9*n_samples]
X_test = X_digits[.9*n_samples:]
y_test = y_digits[.9*n_samples:]

knn = neighbors.NeighborsClassifier()
logistic = linear_model.LogisticRegression()

print 'KNN score:', knn.fit(X_train, y_train).score(X_test, y_test)
print 'LogisticRegression score:', logistic.fit(X_train, y_train).score(X_test, y_test)

