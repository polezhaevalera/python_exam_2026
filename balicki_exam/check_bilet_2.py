import numpy as np
import math
import matplotlib.pyplot as plt

with open('final_data/input_bilet_2.txt', 'r') as f:
    content = f.read().strip()
x = np.array([float(num) for num in content.split()])

def damped_oscillation(x):
    return np.sin(x) * np.exp(-0.1 * x)

y = damped_oscillation(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='darkgreen', linewidth=2, label='Затухающие колебания')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График y = sin(x) * e^{-0.1x}')
plt.legend()
plt.savefig('damped_oscillation.png', dpi=300, bbox_inches='tight')
plt.show()