from cvxopt import matrix, solvers

c = matrix([ 0.0, 0.0 ]) # 0*x1 + 0*x2 - objective function
G = matrix([[-1.0, 0.0, -1.0, 1.0, -1.0],[0.0, -1.0, -1.0, 1.0, -2.0]]) #constraint eqtns coefficients
h = matrix([0.0, 0.0, -1.0, 2.0, -2.0]) # constraint eqtns values

sol=solvers.lp( c, G, h )

print( 'PRINT SOLUTION_1' )

print( sol['x'] )

c = matrix([ 2.0, 3.0 ])
G = matrix([[-1.0, 0.0, -1.0, 1.0, -1.0],[0.0, -1.0, -1.0, 1.0, -2.0]])
h = matrix([0.0, 0.0, -1.0, 2.0, -2.0])

sol = solvers.lp(c, G, h)

print( 'PRINT SOLUTION_2' )
print( sol['x'] )



c = matrix([ 2.0, 3.0 ])
G = matrix([[-1.0, 0.0, -1.0, 1.0, -1.0, -1.0],[0.0, -1.0, -1.0, 1.0, -2.0, 1.0]])
h = matrix([0.0, 0.0, -1.0, 2.0, -2.0, 1.0])

sol = solvers.lp(c, G, h)

print( 'PRINT SOLUTION_3' )
print( sol['x'] )

