from sklearn.model_selection import cross_val_predict, GroupKFold
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer, StandardScaler


def cv_predict(X, y, groups):
    mlpr = MLPRegressor(random_state=1337, hidden_layer_sizes=(100, 20))
    imp = Imputer(strategy='mean')
    scl = StandardScaler()
    pipeline = Pipeline([('imp', imp), ('scl', scl), ('mlp', mlpr)])

    cv = GroupKFold(n_splits=10)

    y_pred = cross_val_predict(pipeline, X, y,
                               cv=cv, groups=groups,
                               verbose=True, n_jobs=-1)
    return y_pred
