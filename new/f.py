import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ── RK4 solver ────────────────────────────────────────────────────────────────
def rk4(f, x0, t):
    x = np.zeros(len(t))
    x[0] = x0
    for i in range(len(t) - 1):
        h = t[i+1] - t[i]
        k1 = f(t[i],        x[i])
        k2 = f(t[i] + h/2,  x[i] + h*k1/2)
        k3 = f(t[i] + h/2,  x[i] + h*k2/2)
        k4 = f(t[i+1],      x[i] + h*k3)
        x[i+1] = x[i] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    return x

# ODE: dx/dt = -3x  →  f(t, x) = -3x
def ode(t, x):
    return -3 * x

t = np.linspace(0, 3, 500)

# ── 4 candidate solutions ─────────────────────────────────────────────────────
candidates = {
    'a) $x(t) = 3e^{-t}$':     (lambda t: 3 * np.exp(-t),          3.0,   False),
    'b) $x(t) = 2e^{-3t}$':    (lambda t: 2 * np.exp(-3*t),        2.0,   True),
    'c) $x(t) = \\frac{3}{2}t^2$': (lambda t: 1.5 * t**2,          0.0,   False),
    'd) $x(t) = 3t^2$':         (lambda t: 3 * t**2,               0.0,   False),
}

colors  = ['#888780', '#185FA5', '#D85A30', '#3B6D11']
rk4_col = '#7F77DD'

fig = plt.figure(figsize=(15, 10))
fig.patch.set_facecolor('#fafaf8')
gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.42, wspace=0.32)

for idx, (label, (func, x0, is_answer)) in enumerate(candidates.items()):
    ax = fig.add_subplot(gs[idx // 2, idx % 2])
    ax.set_facecolor('#fafaf8')

    y_analytical = func(t)

    # RK4: only meaningful when the candidate is the correct ODE solution form
    # We always run RK4 with the *candidate's own x(0)* to show the comparison
    y_rk4 = rk4(ode, x0, t)

    ax.plot(t, y_analytical, color=colors[idx], linewidth=2.5, label=f'Analytical: {label}', zorder=3)
    ax.plot(t, y_rk4, color=rk4_col, linewidth=1.8, linestyle='--', label=f'RK4 (ODE, x₀={x0})', zorder=2)

    # Residual check: plug candidate into ODE symbolically via numerical diff
    h = t[1] - t[0]
    dxdt = np.gradient(y_analytical, h)
    residual = dxdt + 3 * y_analytical
    max_res = np.max(np.abs(residual[5:-5]))   # ignore edge effects

    border_color = '#185FA5' if is_answer else '#D85A30'
    for spine in ax.spines.values():
        spine.set_edgecolor(border_color)
        spine.set_linewidth(2.2 if is_answer else 0.8)

    ax.set_title(
        label + ('  ✓  CORRECT ANSWER' if is_answer else f'  ✗  max residual = {max_res:.3f}'),
        fontsize=11, color=border_color, fontweight='bold' if is_answer else 'normal', pad=8
    )
    ax.set_xlabel('t', fontsize=11)
    ax.set_ylabel('x(t)', fontsize=11)
    ax.legend(fontsize=8.5, loc='upper right')
    ax.grid(True, alpha=0.25, linestyle=':')
    ax.axhline(0, color='gray', linewidth=0.5)

    # Annotation: match/no-match
    match_txt = 'RK4 ≡ Analytical ✓' if is_answer else 'RK4 ≢ Analytical ✗'
    match_col = '#185FA5' if is_answer else '#D85A30'
    ax.text(0.97, 0.55, match_txt, transform=ax.transAxes,
            fontsize=9, color=match_col, ha='right',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=match_col, alpha=0.8))

# ── Master title ──────────────────────────────────────────────────────────────
fig.suptitle(
    "ODE: $\\frac{dx}{dt} + 3x(t) = 0$  —  Analytical candidates vs RK4 solution",
    fontsize=14, fontweight='500', y=1.01, color='#2C2C2A'
)

plt.savefig('ode_rk4_comparison.png', dpi=150, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.show()

# ── Console verification ───────────────────────────────────────────────────────
print("\nResidual check  |dx/dt + 3x(t)| max value:")
print("-" * 45)
for label, (func, x0, is_answer) in candidates.items():
    y = func(t)
    dxdt = np.gradient(y, t[1]-t[0])
    res = np.max(np.abs((dxdt + 3*y)[5:-5]))
    tick = "✓ SOLUTION" if is_answer else "✗"
    print(f"  {label:<30s}  {res:.6f}   {tick}")