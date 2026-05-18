import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def piecewise_function(x):
    return np.where(x <= 1,
                    np.cos(x) * np.exp(-x**2),
                    np.log(x + 1) - np.sqrt(4 - x**2))

def derivative_second_part(x):
    return 1/(x + 1) + x / np.sqrt(4 - x**2)

x1 = np.linspace(0, 1, 200)
x2 = np.linspace(1, 2, 200)

x0 = 1.5
y0 = float(piecewise_function(x0))
k = derivative_second_part(x0)

x_tangent = np.linspace(1.2, 1.8, 100)
y_tangent = y0 + k * (x_tangent - x0)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 7))

sns.lineplot(x=x1, y=piecewise_function(x1), color='blue', linewidth=2, label=r'$f(x)=\cos(x)e^{-x^2}, 0 \leq x \leq 1$')
sns.lineplot(x=x2, y=piecewise_function(x2), color='green', linewidth=2, label=r'$f(x)=\ln(x+1)-\sqrt{4-x^2}, 1 < x \leq 2$')
sns.lineplot(x=x_tangent, y=y_tangent, color='red', linestyle='--', linewidth=2.5, label=f'Касательная в x={x0:.1f} (k={k:.2f})')

sns.scatterplot(x=[x0], y=[y0], color='red', s=100, zorder=5)

plt.title('Кусочно-заданная функция и касательная к ней (Seaborn)', fontsize=16, fontweight='bold')
plt.xlabel('Ось X', fontsize=14)
plt.ylabel('Ось Y', fontsize=14)
plt.legend(loc='best')

plt.annotate(f'Точка касания\n({x0:.1f}, {y0:.2f})\nk={k:.2f}',
             xy=(x0, y0), xytext=(x0 + 0.1, y0 + 0.1),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
             bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
             fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('function_with_tangent_sns.png', dpi=300, bbox_inches='tight')
plt.show()