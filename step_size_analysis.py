import numpy as np
import matplotlib.pyplot as plt

# Constants
w = 2 * np.pi

# Exact solutions
E_exact = lambda t: np.cos(w * t)
H_exact = lambda t: np.sin(w * t)

# Initial conditions
t0 = 0
tf = 2
E0 = 1
H0 = 0

# Step sizes
h_small = 0.01
h_large = 0.2

# Time arrays
t_small = np.arange(t0, tf + h_small, h_small)
t_large = np.arange(t0, tf + h_large, h_large)

# Initialize fields
E_small = np.zeros_like(t_small)
H_small = np.zeros_like(t_small)
E_large = np.zeros_like(t_large)
H_large = np.zeros_like(t_large)

E_small[0] = E0
H_small[0] = H0
E_large[0] = E0
H_large[0] = H0

# RK4 for small step
for n in range(len(t_small) - 1):
    E = E_small[n]
    H = H_small[n]
    
    k1E = -w * H
    k1H =  w * E

    k2E = -w * (H + 0.5 * h_small * k1H)
    k2H =  w * (E + 0.5 * h_small * k1E)

    k3E = -w * (H + 0.5 * h_small * k2H)
    k3H =  w * (E + 0.5 * h_small * k2E)

    k4E = -w * (H + h_small * k3H)
    k4H =  w * (E + h_small * k3E)

    E_small[n+1] = E + (h_small/6) * (k1E + 2*k2E + 2*k3E + k4E)
    H_small[n+1] = H + (h_small/6) * (k1H + 2*k2H + 2*k3H + k4H)

# RK4 for large step
for n in range(len(t_large) - 1):
    E = E_large[n]
    H = H_large[n]
    
    k1E = -w * H
    k1H =  w * E

    k2E = -w * (H + 0.5 * h_large * k1H)
    k2H =  w * (E + 0.5 * h_large * k1E)

    k3E = -w * (H + 0.5 * h_large * k2H)
    k3H =  w * (E + 0.5 * h_large * k2E)

    k4E = -w * (H + h_large * k3H)
    k4H =  w * (E + h_large * k3E)

    E_large[n+1] = E + (h_large/6) * (k1E + 2*k2E + 2*k3E + k4E)
    H_large[n+1] = H + (h_large/6) * (k1H + 2*k2H + 2*k3H + k4H)

# Exact solution for plotting
t_exact = np.linspace(t0, tf, 1000)
E_true = E_exact(t_exact)

# Plotting
plt.figure(figsize=(10,6))
plt.plot(t_exact, E_true, 'k', linewidth=2, label='Exact Solution')
plt.plot(t_small, E_small, 'b--', linewidth=1.8, label='RK4 Small Step (h=0.01)')
plt.plot(t_large, E_large, 'ro-', linewidth=1.8, label='RK4 Large Step (h=0.2)')
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Electric Field E(t)')
plt.title('Effect of Step Size in RK4 for Maxwell Equation')
plt.legend()
plt.show()

# Compute maximum errors
error_small = np.max(np.abs(E_small - E_exact(t_small)))
error_large = np.max(np.abs(E_large - E_exact(t_large)))

print(f'Maximum Error with Small Step = {error_small:.6f}')
print(f'Maximum Error with Large Step = {error_large:.6f}')