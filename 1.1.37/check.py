import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# ==========================================
# 1. Set your K value here!
# ==========================================
K = -20.0  # Try 10 (stable), -16 (oscillating), or -20 (unstable)

# ==========================================
# 2. Generalized State-Space Definition
# ==========================================
def f1(x1, x2):
    return x2

def f2(x1, x2, u, K_val):
    return -(64 + 3 * K_val) * x1 - (16 + K_val) * x2 + u

# ==========================================
# 3. Simulation Setup
# ==========================================
dt = 0.01
t_end = 5.0
t = np.arange(0, t_end, dt)
n_steps = len(t)

x1 = np.zeros(n_steps)
x2 = np.zeros(n_steps)
y_rk4 = np.zeros(n_steps)

u = 1.0  # Step input

# Initial output
y_rk4[0] = (3 * K) * x1[0] + K * x2[0]

# ==========================================
# 4. RK4 Integration Loop
# ==========================================
for i in range(n_steps - 1):
    curr_x1 = x1[i]
    curr_x2 = x2[i]
    
    k1_1 = f1(curr_x1, curr_x2)
    k1_2 = f2(curr_x1, curr_x2, u, K)
    
    k2_1 = f1(curr_x1 + 0.5*dt*k1_1, curr_x2 + 0.5*dt*k1_2)
    k2_2 = f2(curr_x1 + 0.5*dt*k1_1, curr_x2 + 0.5*dt*k1_2, u, K)
    
    k3_1 = f1(curr_x1 + 0.5*dt*k2_1, curr_x2 + 0.5*dt*k2_2)
    k3_2 = f2(curr_x1 + 0.5*dt*k2_1, curr_x2 + 0.5*dt*k2_2, u, K)
    
    k4_1 = f1(curr_x1 + dt*k3_1, curr_x2 + dt*k3_2)
    k4_2 = f2(curr_x1 + dt*k3_1, curr_x2 + dt*k3_2, u, K)
    
    x1[i+1] = curr_x1 + (dt / 6.0) * (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)
    x2[i+1] = curr_x2 + (dt / 6.0) * (k1_2 + 2*k2_2 + 2*k3_2 + k4_2)
    
    # Generalized output equation
    y_rk4[i+1] = (3 * K) * x1[i+1] + K * x2[i+1]

# ==========================================
# 5. Theoretical Solution (using Scipy)
# ==========================================
num = [K, 3 * K]
den = [1, 16 + K, 64 + 3 * K]
sys = signal.TransferFunction(num, den)
t_theory, y_theory = signal.step(sys, T=t)

# ==========================================
# 6. Plotting
# ==========================================
plt.figure(figsize=(10, 6))

plt.plot(t_theory, y_theory, label='Theoretical Response', linewidth=6, color='orange', alpha=0.5)
plt.plot(t, y_rk4, label='Numerical (RK4 Method)', linestyle='--', linewidth=2, color='navy')

plt.title(f'RK4 Verification for K = {K}', fontsize=14, fontweight='bold')
plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Output Amplitude y(t)', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=12, loc='upper right')

plt.show()