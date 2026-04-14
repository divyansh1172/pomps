import numpy as np
import matplotlib.pyplot as plt

# 1. Define the time array for plotting
t = np.linspace(0, 2, 100)

# 2. Define the four options given in the problem
opt_a = 3 * np.exp(-t)
opt_b = 2 * np.exp(-3 * t)
opt_c = 1.5 * t**2
opt_d = 3 * t**2

# 3. Define the differential equation for RK4
# dx/dt = -3x
def dxdt(t, x):
    return -3 * x

# 4. Implement the Runge-Kutta 4th Order (RK4) method
def rk4(func, x0, t_array):
    n = len(t_array)
    x = np.zeros(n)
    x[0] = x0
    
    for i in range(n - 1):
        h = t_array[i+1] - t_array[i]
        
        k1 = h * func(t_array[i], x[i])
        k2 = h * func(t_array[i] + h/2, x[i] + k1/2)
        k3 = h * func(t_array[i] + h/2, x[i] + k2/2)
        k4 = h * func(t_array[i] + h, x[i] + k3)
        
        x[i+1] = x[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        
    return x

# To verify option (b), we use its initial condition at t=0, which is x(0) = 2
rk4_solution = rk4(dxdt, x0=2, t_array=t)

# 5. Plot everything
plt.figure(figsize=(10, 6))

# Plot the 4 options as continuous lines
plt.plot(t, opt_a, label="Option A: $3e^{-t}$", color='blue', linestyle='--')
plt.plot(t, opt_b, label="Option B: $2e^{-3t}$", color='green', linewidth=2)
plt.plot(t, opt_c, label="Option C: $\\frac{3}{2}t^2$", color='orange', linestyle='--')
plt.plot(t, opt_d, label="Option D: $3t^2$", color='red', linestyle='--')

# Plot the RK4 numerical solution as scatter points to show it overlaps with Option B
plt.scatter(t[::4], rk4_solution[::4], color='black', marker='o', label="RK4 Solution (IC: $x(0)=2$)", zorder=5)

# Formatting the plot
plt.title("Comparison of Options and RK4 Solution for $\\frac{dx}{dt} + 3x = 0$")
plt.xlabel("Time (t)")
plt.ylabel("x(t)")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.ylim(0, 4) # Adjust y-limits for better visibility

# Show the plot
plt.show()