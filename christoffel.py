import sympy as sp

def christoffel_symbols(g, coords):
    """
    Compute Christoffel symbols Γ^k_{ij} for a given metric tensor g.

    Parameters
    ----------
    g : sympy.Matrix
        Metric tensor
    coords : tuple of sympy.Symbol
        Coordinate variables

    Returns
    -------
    Gamma : list
        3D list with Christoffel symbols Gamma[k][i][j]
    """
    n = len(coords)
    g_inv = g.inv()
    Gamma = [[[0 for j in range(n)] for i in range(n)] for k in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                term = 0
                for l in range(n):
                    term += g_inv[k, l] * (
                        sp.diff(g[j, l], coords[i]) +
                        sp.diff(g[i, l], coords[j]) -
                        sp.diff(g[i, j], coords[l])
                    )
                Gamma[k][i][j] = sp.simplify(sp.Rational(1, 2) * term)
    return Gamma
