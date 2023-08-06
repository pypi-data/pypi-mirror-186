from sklearn.ensemble import RandomForestClassifier
from tabmark.datasets import Heloc, NumpyDataset

def main():
    clf = RandomForestClassifier()
    ds = NumpyDataset(Heloc())
    X_train, X_test, y_train, y_test = ds.split((0.8, 0.2), random_state=0)

    clf.fit(X_train, y_train)
    print(clf.score(X_train, y_train))
    print(clf.score(X_test, y_test))

if __name__ == '__main__':
    main()