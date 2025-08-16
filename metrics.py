import sympy as sp

def polar_metric():
    r, θ = sp.symbols('r θ')
    coords = (r, θ)
    g = sp.Matrix([[1, 0],
                   [0, r**2]])
    return g, coords, ['r', 'θ']

def cartesian_metric():
    x, y = sp.symbols('x y')
    coords = (x, y)
    g = sp.Matrix([[1, 0],
                   [0, 1]])
    return g, coords, ['x', 'y']
