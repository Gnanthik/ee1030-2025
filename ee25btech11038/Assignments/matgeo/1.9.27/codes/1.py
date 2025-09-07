mport sympy as sp

# Define the variable p
p = sp.symbols('p')

# Coordinates
A = (0, 2)
B = (3, p)
C = (p, 5)

# Distance squared from A to B and A to C
dist_AB_sq = (A[0] - B[0])**2 + (A[1] - B[1])**2
dist_AC_sq = (A[0] - C[0])**2 + (A[1] - C[1])**2

# Set up the equation: equidistant
eq = sp.Eq(dist_AB_sq, dist_AC_sq)

# Solve for p
solution = sp.solve(eq, p)

print(f"The value(s) of p for which A(0,2) is equidistant from B(3,p) and C(p,5) is/are: {solution}")
plt.save(jpg.2)

