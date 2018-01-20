import math
from collections import defaultdict
from operator import itemgetter
 
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import precision_score
 
 
# Calculate Euclidean distance for point A and B (https://en.wikipedia.org/wiki/Euclidean_distance)
def euclidean_distance(A, B):
    C2 = 0
    for i in xrange(len(A)):
        C2 += pow(float(A[i]) - B[i], 2)
    return math.sqrt(C2)
 
 
# Find k smallest values among calculated Euclidean distances
def k_smallest(list, k):
    smallest = min(list)
    if k == 1:
        return [list.index(smallest)]
    sorted_distances = sorted(list)
    return [list.index(sorted_distances[i]) for i in xrange(0, k)]
 
 
# Count which category is more popular among neighboring points
def max_occurrences(list):
    occurance = defaultdict(int)
    for key in list:
        occurance[key] += 1
    category, count = max(occurance.iteritems(), key=itemgetter(1))
    return category
 
 
# Run knn on one row in test data
def knn_one_test(X_train, y_train, test_row, k):
    test_eucl_distance = [euclidean_distance(train_row, test_row) for train_row in X_train]
    k_neighbor_indices = k_smallest(test_eucl_distance, k)
    k_neighbor_labels = [y_train[x] for x in k_neighbor_indices]
    return max_occurrences(k_neighbor_labels)
 
 
# Calculate knn for all the test rows (https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
def knn(X_train, y_train, X_test, k=1):
    if k > len(X_train):
        return []
    return [knn_one_test(X_train, y_train, test_row, k) for test_row in X_test]
 
 
# Some handmade train/test data
X_train = [
    [1, 1],
    [1, 2],
    [2, 4],
    [3, 5],
    [1, 0],
    [0, 0],
    [1, -2],
    [-1, 0],
    [-1, -2],
    [-2, -2]
]
 
y_train = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
 
X_test = [
    [5, 5],
    [0, -1],
    [-5, -5]
]
 
y_test = [1, 2, 2]
 
print "------------------------Handmade dataset---------------------"
test_prediction = knn(X_train=X_train, y_train=y_train, X_test=X_test, k=1)
print "Original:  ", y_test
print "Prediction:", test_prediction
print precision_score(y_test, test_prediction, average='binary')
 
print "------------------------The Iris dataset---------------------"
iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
test_prediction = knn(X_train=X_train, y_train=y_train, X_test=X_test, k=3)
print "Original:  ", list(y_test)
print "Prediction:", test_prediction
print precision_score(y_test, test_prediction, average='micro')
 
print "------------------------The Digits dataset---------------------"
digits = datasets.load_digits()
X = digits.data
y = digits.target
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
test_prediction = knn(X_train=X_train, y_train=y_train, X_test=X_test, k=5)
print "Original:  ", list(y_test)
print "Prediction:", test_prediction
print precision_score(y_test, test_prediction, average='micro')
