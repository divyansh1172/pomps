import math
import matplotlib.pyplot as plt

def nested_sqrt_sequence(x, steps=50):
    values = []
    val = 0
    for _ in range(steps):
        val = math.sqrt(x + val)
        values.append(val)
    return values

x = 2
values = nested_sqrt_sequence(x)

# Analytical solution
S_exact = (1 + math.sqrt(1 + 4*x)) / 2

plt.plot(values, label="Numerical")
plt.axhline(S_exact, color='red', linestyle='--', label="Exact")

plt.title("Numerical vs Exact Solution")
plt.legend()
plt.grid()

plt.show()
