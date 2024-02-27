from scipy.signal import freqz
import matplotlib.pyplot as plt
import numpy as np  # Import NumPy

b = [8]
a = [1, 2]

w, h = freqz(b, a, whole=True)
plt.plot(w, np.abs(h))  # Use np.abs() instead of abs()
plt.title('ROC of $x(z)$')
plt.xlabel('Frequency [rad/sample]')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

