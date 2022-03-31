from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import Flask, render_template,Response, request, url_for
from matplotlib.figure import Figure
import NoiSuy
import stringHandle
from sympy import *
import numpy as np

app = Flask(__name__)

@app.route('/')

def home():
    return render_template("noiSuy.html")

@app.route('/calc' , methods=['POST' , 'GET'])
def calc():
        global X, Y, P_latex, sp
        X = str(request.form['X'])
        Y = str(request.form['Y'])
        pp = str(request.form['choosen'])
        X= stringHandle.split_str(X) 
        Y = stringHandle.split_str(Y)
        if pp == 'Tổng quát':
            P_latex, A =  NoiSuy.TongQuat(X, Y)        
            return render_template('TongQuat.html',A = A, P_latex = P_latex, pp = pp, X= X, Y= Y)
        if pp == 'Newton' or pp == 'Newton Lùi':
            if(NoiSuy.checkCondition(X, Y)):
                P_latex, sp = NoiSuy.Newton(X, Y, pp)
                return render_template('Newton.html',P_latex=P_latex,sp = sp,pp = pp, X= X, Y= Y)
            else:
                return render_template('KhongTM.html')
        # if pp == 'Lagrange':
            # if len(X) == len(Y):
            # return render_template('Lagrange.html', P_latex = P_latex, s1 = s1, s2 = s2, pp = pp)
            # else:
            #     return render_template('KhongTM.html')
        P_latex, s1, s2 = NoiSuy.Lagrange(X, Y)
        return render_template('Lagrange.html', P_latex = P_latex, s1 = s1, s2 = s2, pp = pp, X= X, Y= Y)
if __name__ == '__main__':
    app.run()