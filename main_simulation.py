import numpy as np
import matplotlib.pyplot as plt

# =============================
# 1. Simulation settings
# =============================

h = 0.01
t_final = 10

t = np.arange(0, t_final + h, h)

# =============================
# 2. Initial conditions
# =============================

E0 = 1
H0 = 0

# =============================
# 3. Simplified Maxwell ODEs
# dE/dt = -H
# dH/dt = E
# =============================

def f(E, H):
    dE_dt = -H
    dH_dt = E
    return dE_dt, dH_dt

# =============================
# 4. Euler Method
# =============================

E_euler = np.zeros(len(t))
H_euler = np.zeros(len(t))

E_euler[0] = E0
H_euler[0] = H0

for i in range(len(t) - 1):
    dE, dH = f(E_euler[i], H_euler[i])

    E_euler[i + 1] = E_euler[i] + h * dE
    H_euler[i + 1] = H_euler[i] + h * dH

# =============================
# 5. RK4 Method
# =============================

E_rk4 = np.zeros(len(t))
H_rk4 = np.zeros(len(t))

E_rk4[0] = E0
H_rk4[0] = H0

for i in range(len(t) - 1):
    E = E_rk4[i]
    H = H_rk4[i]

    k1_E, k1_H = f(E, H)

    k2_E, k2_H = f(
        E + 0.5 * h * k1_E,
        H + 0.5 * h * k1_H
    )

    k3_E, k3_H = f(
        E + 0.5 * h * k2_E,
        H + 0.5 * h * k2_H
    )

    k4_E, k4_H = f(
        E + h * k3_E,
        H + h * k3_H
    )

    E_rk4[i + 1] = E + (h / 6) * (k1_E + 2*k2_E + 2*k3_E + k4_E)
    H_rk4[i + 1] = H + (h / 6) * (k1_H + 2*k2_H + 2*k3_H + k4_H)

# =============================
# 6. Exact solution
# =============================

E_exact = np.cos(t)
H_exact = np.sin(t)

# =============================
# 7. Error calculation
# =============================

error_E_euler = np.abs(E_exact - E_euler)
error_E_rk4 = np.abs(E_exact - E_rk4)

# =============================
# 8. Plot 1: Electric Field using RK4
# =============================

plt.figure()
plt.plot(t, E_rk4, label="Electric Field using RK4")
plt.xlabel("Time")
plt.ylabel("Electric Field E")
plt.title("Electric Field vs Time using RK4")
plt.legend()
plt.grid(True)

# =============================
# 9. Plot 2: Magnetic Field using RK4
# =============================

plt.figure()
plt.plot(t, H_rk4, label="Magnetic Field using RK4")
plt.xlabel("Time")
plt.ylabel("Magnetic Field H")
plt.title("Magnetic Field vs Time using RK4")
plt.legend()
plt.grid(True)

# =============================
# 10. Plot 3: Euler vs RK4 Comparison
# =============================

plt.figure()
plt.plot(t, E_euler, label="Euler Method")
plt.plot(t, E_rk4, label="RK4 Method")
plt.plot(t, E_exact, "--", label="Exact Solution")
plt.xlabel("Time")
plt.ylabel("Electric Field E")
plt.title("Comparison Between Euler and RK4")
plt.legend()
plt.grid(True)

# =============================
# 11. Plot 4: Error Comparison
# =============================

plt.figure()
plt.plot(t, error_E_euler, label="Euler Error")
plt.plot(t, error_E_rk4, label="RK4 Error")
plt.xlabel("Time")
plt.ylabel("Absolute Error")
plt.title("Error Comparison: Euler vs RK4")
plt.legend()
plt.grid(True)

# =============================
# 12. Plot 5: 3D Electromagnetic Wave
# Shows E ⟂ B ⟂ k
# =============================

x = np.linspace(0, 4*np.pi, 200)

# E field is in y-direction
E_wave = np.sin(x)

# B field is in z-direction
B_wave = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Propagation direction k along x-axis
ax.plot(x, np.zeros_like(x), np.zeros_like(x), label="Propagation Direction k")

# Electric field wave along y-axis
ax.plot(x, E_wave, np.zeros_like(x), label="Electric Field E")

# Magnetic field wave along z-axis
ax.plot(x, np.zeros_like(x), B_wave, label="Magnetic Field B")

# Arrows showing field directions
for i in range(0, len(x), 20):
    ax.quiver(
        x[i], 0, 0,
        0, E_wave[i], 0,
        length=1,
        normalize=False
    )

    ax.quiver(
        x[i], 0, 0,
        0, 0, B_wave[i],
        length=1,
        normalize=False
    )

ax.set_xlabel("k direction / Propagation")
ax.set_ylabel("Electric Field E")
ax.set_zlabel("Magnetic Field B")

ax.set_title("3D Electromagnetic Wave: E ⟂ B ⟂ k")
ax.legend()

# Show all graphs
plt.show()
