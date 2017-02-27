from cvxopt import matrix, solvers

c = matrix([ 0.0, 0.0 ])
G = matrix([[-1.0, 0.0, -1.0, 1.0, 1.0],[0.0, -1.0, -1.0, 1.0, 2.0]])
h = matrix([0.0, 0.0, 1.0, 2.0, 2.0])

sol=solvers.lp( c, G, h )

print( 'PRINT SOLUTION_1' )
print( sol )

print( sol['x'] )

'''
Optimal solution found.
{'y': <0x1 matrix, tc='d'>, 'dual infeasibility': 0.0, 'primal infeasibility': 0.0, 'dual slack': 0.0, 'residual as dual infeasibility certificate': None, 'relative gap': None, 'iterations': 0, 'gap': 0.0, 'primal objective': 0.0, 's': <5x1 matrix, tc='d'>, 'z': <5x1 matrix, tc='d'>, 'primal slack': 0.08333333333333326, 'x': <2x1 matrix, tc='d'>, 'residual as primal infeasibility certificate': None, 'status': 'optimal', 'dual objective': -0.0}
[ 8.33e-02]
[ 6.67e-01]
'''

c = matrix([ 2.0, 3.0 ])
G = matrix([[-1.0, 0.0, -1.0, 1.0, 1.0],[0.0, -1.0, -1.0, 1.0, 2.0]])
h = matrix([0.0, 0.0, 1.0, 2.0, 2.0])

sol = solvers.lp(c, G, h)

print( 'PRINT SOLUTION_2' )
print( sol )
print( sol['x'] )

'''
{'primal infeasibility': 1.734357606815213e-16, 'gap': 3.3158635851348936e-09, 'status': 'optimal', 'dual slack': 1.1280084313793751e-10, 'iterations': 6, 'relative gap': None, 'dual objective': -2.532841219589929e-09, 's': <5x1 matrix, tc='d'>, 'residual as dual infeasibility certificate': None, 'dual infeasibility': 1.9066300230478848e-10, 'x': <2x1 matrix, tc='d'>, 'primal slack': 1.5949171549480597e-11, 'z': <5x1 matrix, tc='d'>, 'residual as primal infeasibility certificate': None, 'y': <0x1 matrix, tc='d'>, 'primal objective': 7.83022365717081e-10}
[ 1.59e-11]
[ 2.50e-10]
'''

c = matrix([ 2.0, 3.0 ])
G = matrix([[-1.0, 0.0, -1.0, 1.0, 1.0, -1.0],[0.0, -1.0, -1.0, 1.0, 2.0, 1.0]])
h = matrix([0.0, 0.0, 1.0, 2.0, 2.0, 1.0])

sol = solvers.lp(c, G, h)

print( 'PRINT SOLUTION_3' )
print( sol )
print( sol['x'] )

'''
PRINT SOLUTION_3
{'primal infeasibility': 9.215426956270859e-11, 'gap': 1.5253372598843387e-09, 'status': 'optimal', 'dual slack': 9.535300940129172e-11, 'iterations': 6, 'relative gap': None, 'dual objective': -7.979623889751286e-10, 's': <6x1 matrix, tc='d'>, 'residual as dual infeasibility certificate': None, 'dual infeasibility': 1.252064204215212e-10, 'x': <2x1 matrix, tc='d'>, 'primal slack': 1.0567618718524076e-10, 'z': <6x1 matrix, tc='d'>, 'residual as primal infeasibility certificate': None, 'y': <0x1 matrix, tc='d'>, 'primal objective': 1.3252227837072713e-10}
[ 8.62e-11]
[-1.33e-11]
'''
