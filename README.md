# Maxwell Equation Numerical Simulation using Euler and RK4

This project presents a numerical study of electromagnetic wave propagation using simplified Maxwell’s equations in one-dimensional free space.

The electric field (E) and magnetic field (H) are modeled using a coupled system of ordinary differential equations (ODEs):

dE/dt = -H  
dH/dt = E

Two numerical methods are implemented and compared:

- Forward Euler Method
- Fourth-Order Runge-Kutta Method (RK4)

## Project Objectives

- Solve Maxwell’s equations numerically
- Compare Euler and RK4 methods
- Analyze local and global errors
- Study step size sensitivity
- Investigate RK4 stability region
- Visualize electromagnetic wave propagation

## Files Included

### main_simulation.py
Main simulation file containing:

- Euler method
- RK4 method
- Exact solution comparison
- Error analysis
- Electric and magnetic field plots
- 3D electromagnetic wave visualization

### stability_region_rk4.py
Plots the absolute stability region of the classical RK4 method and illustrates the stability radius.

### step_size_analysis.py
Shows the effect of step size selection on RK4 accuracy using small and large step sizes.

## Libraries Used

- NumPy
- Matplotlib

## Author

Numerical Methods for Engineering Project  
Maxwell’s Equations and Runge-Kutta Methods
