import numpy as np
import matplotlib.pyplot as plt

# Grid
x = np.linspace(-4, 2, 1200)
y = np.linspace(-4, 4, 1200)
X, Y = np.meshgrid(x, y)
z = X + 1j*Y

# RK4 stability function
R = 1 + z + (z**2)/2 + (z**3)/6 + (z**4)/24
A = np.abs(R)

# Figure
plt.figure(figsize=(10,8), facecolor='white')

# Filled contour for |R| <= 1
plt.contourf(X, Y, A, levels=[0, 1], colors=[[0.18, 0.18, 0.55]])

# Contour line for |R| = 1
plt.contour(X, Y, A, levels=[1], colors='k', linewidths=3)

# Axis settings
plt.axis('equal')
plt.xlim([-4, 2])
plt.ylim([-4, 4])
plt.grid(True, alpha=0.15)
plt.box(True)

# Labels and title
plt.xlabel('Real(z)', fontsize=16, fontweight='bold')
plt.ylabel('Imag(z)', fontsize=16, fontweight='bold')
plt.title('Absolute Stability Region of Classical RK4', fontsize=18, fontweight='bold')

# Axes lines
plt.plot([-4, 2], [0, 0], 'k--', linewidth=1)
plt.plot([0, 0], [-4, 4], 'k--', linewidth=1)

# r4 marker
r4 = -2.828
plt.plot(r4, 0, 'ro', markersize=10, markerfacecolor='r')
plt.text(r4-0.9, 0.25, r'r$_4 \approx -2.828$', fontsize=14, fontweight='bold')
plt.text(-1.7, 0, 'Stable Region', fontsize=16, fontweight='bold')
plt.text(0.4, 2.8, 'Unstable Region', fontsize=15, fontweight='bold')

# Colorbar off (not needed)
# plt.colorbar()  # not adding

# Annotation
plt.annotate(
    'Stable region satisfies |R(z)| ≤ 1 where z = hλ',
    xy=(0.5, -0.1),
    xycoords='axes fraction',
    ha='center',
    fontsize=13,
    bbox=dict(facecolor='none', edgecolor='none')
)

plt.show()