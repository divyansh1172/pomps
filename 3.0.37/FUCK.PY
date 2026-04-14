import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function G(s)H(s) = (s + 3) / (s + 8)^2
# We leave K out, as the root_locus function varies K automatically
numerator = [1, 3]                  # represents 1*s + 3
denominator = [1, 16, 64]           # represents s^2 + 16s + 64

# Create the system model
system = ctrl.TransferFunction(numerator, denominator)

# Set up the plot aesthetics
plt.figure(figsize=(8, 6))
plt.title('Root Locus of G(s)H(s) = K(s+3) / (s+8)²', fontsize=14)
plt.xlabel('Real Axis (Damping)', fontsize=12)
plt.ylabel('Imaginary Axis (Oscillation Frequency)', fontsize=12)
plt.axvline(x=0, color='red', linestyle='--', label='Oscillation Boundary (Marginal Stability)')

# Generate and plot the Root Locus
roots, gains = ctrl.root_locus(system, plot=True, grid=True)

plt.legend()
plt.show()