from sympy import *
import numpy as np
import array as arr

def TongQuat(X, Y):
    list ( zip(X , Y ) )
    x = symbols('x')
    m = len(X)
    A = [[X[i] ** j for j in range (m) ] for i in range (m) ] 
    kq = np.linalg.solve(A,Y)
    hamSo = ''
    for i in range (len(kq)):
        hamSo += '+%d*(x ** %d)' %(kq[i], i)
    P = lambda x: eval(hamSo )
    f1 = str(P(x))
    f1 = eval(f1)
    f1 = latex(f1)
    return f1, A



def Newton(X, Y, pp):
    X = [0.0,0.5,1.0,1.5,2.0] #mốc nội suy
    Y = [-1.0,0.125,1.0,2.375,5.0]
    n = len(X)
    h = X[1]-X[0]
    x , t = symbols ('x t')
    sp = [ [d(k, i, Y) for i in range(n-k)] for k in range (n)]
    if pp == 'Newton':
        P = Y[0]
        for k in range(1, n): # k chạy từ 1 tới n-1
            prod = d(k, 0,Y)/factorial(k)
            for i in range(k):
                prod *= t - i
            P += prod
        P = P . subs (t , ( x - X [0]) / h) . expand()
    if pp == 'Newton Lùi':
        m = n-1
        P = Y[m]
        for k in range(1, n): 
            prod = d(k, m-k, Y)/factorial(k)
            for i in range(k):
                prod *= t + i
            P += prod
        P = P.subs(t, (x - X[m]) / h).expand()
    print(P)
    f1 = latex(P)
    return f1, sp

def d (k , i, Y ) :
    if k == 0:
        return Y[i]
    return d (k -1,i +1, Y ) - d (k -1 , i, Y )


def checkCondition(X, Y):
    n = len(X)
    h = X[1]-X[0]
    if(len(X) != len(Y)):
        return False
    for i in range(0,n-1):
        if(X[i+1] - X[i] != h):
            return False
    return True

def Lagrange(X,Y):
    n = len(X)
    x = symbols('x')
    P = 0
    for i in range (n) :
        P += Y [i ] * L (i , x, n , X )
    P = P.expand()
    f1 = latex(P)
    print(f1)
    s = []
    s1 = [] 
    for i in range(n):
        a, b = L(i, x, n, X), L(i, x, n , X).expand()
        s.append( latex(a))
        s1.append( latex(b))
    return f1, s, s1
def L (i , x, n, X ) :
    prod = 1
    for j in range (n) :
        if j != i :
            prod *= ( x - X[ j ]) / ( X [ i ] - X [ j ])
    return prod

