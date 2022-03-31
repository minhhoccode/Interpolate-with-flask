import array as arr
def split_str(X):
    X=X.replace(' ','')
    b = [float(s) for s in X.split(",")]
    return b