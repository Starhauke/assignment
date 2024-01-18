import matplotlib.pyplot as plt
import numpy as np

n = np.arange(0, 10, 1)
x_n = 8 - 2 * n

plt.stem(n, x_n, label=r'$x(n) = 8 - 2n$')
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.title('Plot of $x(n)$')
plt.legend()
plt.grid(True)
plt.show()

