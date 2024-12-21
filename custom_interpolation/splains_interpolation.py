""" Function for interpolation using splains.

    Parameters
    ----------
    x : ndarray-like of shape n
        x coordinates of points to interpolate

    y : ndarray-like of shape n
        y coordinates of points to interpolate

    verbose : bool, default = False
        Verbosity mode
        
    Returns
    -------
    
    Splains(cubics) : Splains
        A class made of dictionary of cubic polynomials interpolating given points

    Examples
    --------

    x, y = ([1, 2, 3], [1, 2, 3])
    result = splains_interpolation(x, y, verbose = True)
    points = x, y
    result.plot(points = points)
    
    x = np.linspace(-1, 1, 11)
    y = 1/(1+25*x**2)
    result = splains_interpolation(x, y, verbose = False)
    points = x, y
    result.plot(points = points)
"""

def splains_interpolation(x, y, verbose = False):
    n = len(x)
    if verbose:
        print(f"n={n}, expected number of equations = {4*n-4}")
    cubics = {}
    A = np.zeros((4*n-4, n-1, 4))
    b = np.zeros(4*n-4)
    
    if verbose:
            print(f"0-th condition for 0-th splain's coefficients:")
            print(f"{np.array([0, 0, 2, 6*x[0]])}*[p_0, p_1, p_2, p_3]=0")
    A[0, 0, :]   = np.array([0, 0, 2, 6*x[0]])

    if verbose:
            print(f"1-th condition for {n-2}-th splain's coefficients:")
            print(f"{np.array([0, 0, 2, 6*x[n-1]])}*[p_0, p_1, p_2, p_3]=0")
    A[1, n-2, :] = np.array([0, 0, 2, 6*x[n-1]])
    if verbose:
            print(f"Code successfully entered into the main loop.")
        
    for i in range(n-1):
        if verbose:
            print(f"{2+i}-th condition for {i}-th splain's coefficients:")
            print(f"{np.array([x[i]**j for j in range(4)])}*[p_0, p_1, p_2, p_3]={y[i]}")
        A[2+i, i, :] = np.array([x[i]**j for j in range(4)])
        b[2+i] = y[i]
    for i in range(n-1):
        if verbose:
            print(f"{i+n+1}-th condition for {i}-th splain's coefficients:")
            print(f"{np.array([x[i+1]**j for j in range(4)])}*[p_0, p_1, p_2, p_3]={y[i+1]}")
        A[i+n+1, i, :] = np.array([x[i+1]**j for j in range(4)])
        b[i+n+1] = y[i+1]

    for i in range(n-2):
        if verbose:
            print(f"{i+2*n}-th condition for coefficients of {i}-th  and {i+1}-th splains (named p and q):")
            print(f"{np.array([0, 1, 2*x[i+1], 3*x[i+1]**2])}*[p_0, p_1, p_2, p_3]+{np.array([0, -1, -2*x[i+1], -3*x[i+1]**2])}*[q_0, q_1, q_2, q_3]=0")
        A[i+2*n, i, :] = np.array([0, 1, 2*x[i+1], 3*x[i+1]**2])
        A[i+2*n, i+1, :] = np.array([0, -1, -2*x[i+1], -3*x[i+1]**2])
        
    for i in range(n-2):
        if verbose:
            print(f"{i+3*n-2}-th condition for coefficients of {i}-th  and {i+1}-th splains (named p and q):")
            print(f"{np.array([0, 0, 2, 6*x[i+1]])}*[p_0, p_1, p_2, p_3]+{np.array([0, 0, -2, -6*x[i+1]])}*[q_0, q_1, q_2, q_3]=0")
        A[i+3*n-2, i, :] = np.array([0, 0, 2, 6*x[i+1]])
        A[i+3*n-2, i+1, :] = np.array([0, 0, -2, -6*x[i+1]])

    A_matrix = A.reshape((A.shape[0], -1))
    if verbose:
            print(f"Reshaped tensor A into matrix:\n{A_matrix}")
    coef_list = np.linalg.solve(A_matrix, b)
    if verbose:
            print(f"Found list of coefficients:\n{coef_list}")
    for i in range(n-1):
        cubics[(x[i], x[i+1])] = Polynomial(coef_list[4*i:4*i+4])
    return Splains(cubics)
