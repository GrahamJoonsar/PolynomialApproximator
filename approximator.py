import numpy as np
import scipy.integrate as integrate

import math

# returns the coefficients of a polynomial from 
# the degree specified that minimizes the area between
# it and the function you want to approximate across the 
# interval that was specified
def get_approx(f, degree, interval):
    M = np.zeros((degree+1, degree+1))
    for y in range(degree+1):
        for x in range(degree+1):
            M[y][degree-x] = (interval[1]**(x+y+1) - interval[0]**(x+y+1))/(x+y+1)
    
    V = np.zeros((degree+1, 1))
    for y in range(degree+1):
        integrand = lambda x: f(x) * (x**y)
        V[y][0] = integrate.quad(integrand, interval[0], interval[1])[0]

    return np.reshape(np.dot(np.linalg.inv(M), V), (1, degree+1)).tolist()[0]

def get_polynomial(coefficients):
    txt = ""
    for i in range(len(coefficients)):
        txt += str(coefficients[i]) + "x^" + str(len(coefficients)-i-1) + " + "
    return txt[:len(txt)-3]

print(get_polynomial(get_approx(lambda x: math.sin(x), 5, (0, 2*math.pi))))


