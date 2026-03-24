import math
import matplotlib.pyplot as plt

def nested_sqrt_sequence(x, steps=15):
    values = []
    val = 0
    for _ in range(steps):
        val = math.sqrt(x + val)
        values.append(val)
    return values

x = 2
iterations = list(range(1, 16))
values = nested_sqrt_sequence(x, 15)
S_exact = (1 + math.sqrt(1 + 4*x)) / 2

# Enhanced Plotting
plt.figure(figsize=(8, 5))
plt.plot(iterations, values, marker='o', color='royalblue', linewidth=2, label=r'Numerical Sequence $S_n$')
plt.axhline(S_exact, color='crimson', linestyle='--', linewidth=2, label=r'Exact Limit ($L=2$)')

# Labels, title, and styling
plt.xlabel('Iteration Step ($n$)', fontsize=12)
plt.ylabel(r'Value of $S_n$', fontsize=12)
plt.title('Convergence of Nested Radicals for $x=2$', fontsize=14)
plt.legend(loc='lower right', fontsize=11, frameon=True, shadow=True)
plt.grid(True, linestyle=':', alpha=0.7)

# Annotation for convergence


plt.tight_layout()
plt.savefig('ques_1.png')
plt.show()