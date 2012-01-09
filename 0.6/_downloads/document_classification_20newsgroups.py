"""
======================================================
Classification of text documents using sparse features
======================================================

This is an example showing how the scikit-learn can be used to classify
documents by topics using a bag-of-words approach. This example uses
a scipy.sparse matrix to store the features instead of standard numpy arrays.

The dataset used in this example is the 20 newsgroups dataset which will be
automatically downloaded and then cached.

You can adjust the number of categories by giving there name to the dataset
loader or setting them to None to get the 20 of them.

This example demos various linear classifiers with different training
strategies.

To run this example use::

  % python examples/document_classification_20newsgroups.py [options]

Options are:

  --report
      Print a detailed classification report.
  --confusion-matrix
      Print the confusion matrix.

"""
print __doc__

# Author: Peter Prettenhofer <peter.prettenhofer@gmail.com>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Mathieu Blondel <mathieu@mblondel.org>
# License: Simplified BSD

from time import time
import os
import sys

from scikits.learn.datasets import load_files
from scikits.learn.feature_extraction.text.sparse import Vectorizer
from scikits.learn.svm.sparse import LinearSVC
from scikits.learn.linear_model.sparse import SGDClassifier
from scikits.learn import metrics

# parse commandline arguments
argv = sys.argv[1:]
if "--report" in argv:
    print_report = True
else:
    print_report = False
if "--confusion-matrix" in argv:
    print_cm = True
else:
    print_cm = False

################################################################################
# Download the data, if not already on disk
url = "http://people.csail.mit.edu/jrennie/20Newsgroups/20news-18828.tar.gz"
archive_name = "20news-18828.tar.gz"

if not os.path.exists(archive_name[:-7]):
    if not os.path.exists(archive_name):
        import urllib
        print "Downloading data, please Wait (14MB)..."
        print url
        opener = urllib.urlopen(url)
        open(archive_name, 'wb').write(opener.read())
        print

    import tarfile
    print "Decompressiong the archive: " + archive_name
    tarfile.open(archive_name, "r:gz").extractall()
    print


################################################################################
# Load some categories from the training set
categories = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]
# Uncomment the following to do the analysis on all the categories
#categories = None

print "Loading 20 newsgroups dataset for categories:"
print categories

data = load_files('20news-18828', categories=categories, shuffle=True, rng=42)
print "%d documents" % len(data.filenames)
print "%d categories" % len(data.target_names)
print

# split a training set and a test set
filenames = data.filenames
y = data.target

n = filenames.shape[0]
filenames_train, filenames_test = filenames[:-n/2], filenames[-n/2:]
y_train, y_test = y[:-n/2], y[-n/2:]

print "Extracting features from the training dataset using a sparse vectorizer"
t0 = time()
vectorizer = Vectorizer()
X_train = vectorizer.fit_transform((open(f).read() for f in filenames_train))
print "done in %fs" % (time() - t0)
print "n_samples: %d, n_features: %d" % X_train.shape
print

print "Extracting features from the test dataset using the same vectorizer"
t0 = time()
X_test = vectorizer.transform((open(f).read() for f in filenames_test))
print "done in %fs" % (time() - t0)
print "n_samples: %d, n_features: %d" % X_test.shape
print


################################################################################
# Benchmark classifiers
def benchmark(clf):
    print 80 * '_'
    print "Training: "
    print clf
    t0 = time()
    clf.fit(X_train, y_train)
    train_time = time() - t0
    print "train time: %0.3fs" % train_time

    t0 = time()
    pred = clf.predict(X_test)
    test_time = time() - t0
    print "test time:  %0.3fs" % test_time

    score = metrics.f1_score(y_test, pred)
    print "f1-score:   %0.3f" % score

    nnz = clf.coef_.nonzero()[0].shape[0]
    print "non-zero coef: %d" % nnz
    print

    if print_report:
        print "classification report:"
        print metrics.classification_report(y_test, pred,
                                            class_names=categories)

    if print_cm:
        print "confusion matrix:"
        print metrics.confusion_matrix(y_test, pred)

    print
    return score, train_time, test_time

for penalty in ["l2", "l1"]:
    print 80*'='
    print "%s penalty" % penalty.upper()
    # Train Liblinear model
    liblinear_results = benchmark(LinearSVC(loss='l2', penalty=penalty, C=1000,
                                        dual=False, eps=1e-3))

    # Train SGD model
    sgd_results = benchmark(SGDClassifier(alpha=.0001, n_iter=50,
                                          penalty=penalty))

# Train SGD with Elastic Net penalty
print 80*'='
print "Elastic-Net penalty"
sgd_results = benchmark(SGDClassifier(alpha=.0001, n_iter=50,
                                      penalty="elasticnet"))
