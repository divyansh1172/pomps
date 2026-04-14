import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

# ─── 1. Binomial Distribution for a Single Student ───────────────────────────
n = 3    # Number of guesses
p = 0.5  # Probability of guessing correctly (T/F)
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Colors: Red for Fail (0 correct), Green for Pass (1, 2, or 3 correct)
colors1 = ['crimson' if val == 0 else 'mediumseagreen' for val in x]
ax1.bar(x, pmf, color=colors1, edgecolor='black', zorder=3)
ax1.set_xticks(x)
ax1.set_xlabel('Number of Correct Guesses (out of 3)', fontsize=11)
ax1.set_ylabel('Probability', fontsize=11)
ax1.set_title('Binomial Distribution (Single Student)', fontsize=13)
ax1.grid(axis='y', linestyle=':', alpha=0.7, zorder=0)

# Add fraction labels above the bars
fractions1 = ['1/8', '3/8', '3/8', '1/8']
for i, val in enumerate(x):
    ax1.text(val, pmf[i] + 0.01, fractions1[i], ha='center', fontweight='bold')

# ─── 2. Joint Probability Scenarios for Two Students ─────────────────────────
p_fail = 1/8
p_pass = 7/8

scenarios = ['Both Fail', 'Only A Passes', 'Only B Passes', 'Both Pass']
probs = [
    p_fail * p_fail,  # 1/64
    p_pass * p_fail,  # 7/64
    p_fail * p_pass,  # 7/64
    p_pass * p_pass   # 49/64
]

# Colors: Target scenarios in Blue, others in gray/red
colors2 = ['crimson', 'royalblue', 'royalblue', 'lightslategray']
bars = ax2.bar(scenarios, probs, color=colors2, edgecolor='black', zorder=3)
ax2.set_ylabel('Probability', fontsize=11)
ax2.set_title('Combined Outcomes (Students A & B)', fontsize=13)
ax2.grid(axis='y', linestyle=':', alpha=0.7, zorder=0)

# Add exact fraction labels above the bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.02, 
             f"{int(probs[i]*64)}/64", ha='center', fontweight='bold')

plt.suptitle("Visualizing the Probability Model", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()