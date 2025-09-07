import matplotlib.pyplot as plt
import numpy as np

# Given points and solution
p = 1
A = (0, 2)
B = (3, p)
C = (p, 5)

# Plot points
plt.plot(A[0], A[1], 'ro', label='A (0,2)')
plt.plot(B[0], B[1], 'go', label=f'B (3,{p})')
plt.plot(C[0], C[1], 'bo', label=f'C ({p},5)')

# Plot the distances from A to B and A to C
plt.plot([A[0], B[0]], [A[1], B[1]], 'g--', label='|AB|')
plt.plot([A[0], C[0]], [A[1], C[1]], 'b--', label='|AC|')

# Annotate the points
plt.text(A[0] + 0.1, A[1] + 0.1, 'A(0,2)', color='r')
plt.text(B[0] + 0.1, B[1], f'B(3,{p})', color='g')
plt.text(C[0] - 0.7, C[1] + 0.2, f'C({p},5)', color='b')

# Set plot properties
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.title('Points A, B, C with A Equidistant from B and C')
plt.legend()
plt.xlim(-1, 4)
plt.ylim(0, 6)
plt.savefig('2.jpg')
plt.show()

