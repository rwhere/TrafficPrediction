from sklearn import svm
import numpy as np

input_set = [[10, 0, 1, 8], [10, 0, 2, 9], [10, 1, 1, 13], [5, 0, 1, 15], [5, 1, 5, 16], [5, 1, 6, 18]]
output_set = [8, 7, 5, 6, 9, 9]
clf = svm.SVC(C=100.0, gamma=0.001)
clf.fit(np.array(input_set), output_set)
print(clf.predict([[10, 1, 4, 10]]))
