import numpy as np
import plotly.graph_objects as go

def piecewise_function(x):
    return np.where(x <= 1,
                    np.cos(x) * np.exp(-x**2),
                    np.log(x + 1) - np.sqrt(4 - x**2))

def derivative_second_part(x):
    return 1/(x + 1) + x / np.sqrt(4 - x**2)

x1 = np.linspace(0, 1, 200)
x2 = np.linspace(1, 2, 200)

x0 = 1.5
y0 = piecewise_function(x0)
k = derivative_second_part(x0)

x_tangent = np.linspace(1.2, 1.8, 100)
y_tangent = y0 + k * (x_tangent - x0)

fig = go.Figure()

fig.add_trace(go.Scatter(x=x1, y=piecewise_function(x1), 
                         mode='lines', name='f(x) (0 ≤ x ≤ 1)', 
                         line=dict(color='blue', width=2)))

fig.add_trace(go.Scatter(x=x2, y=piecewise_function(x2), 
                         mode='lines', name='f(x) (1 < x ≤ 2)', 
                         line=dict(color='green', width=2)))

fig.add_trace(go.Scatter(x=x_tangent, y=y_tangent, 
                         mode='lines', name=f'Касательная (k={k:.2f})', 
                         line=dict(color='red', width=2.5, dash='dash')))

fig.add_trace(go.Scatter(x=[x0], y=[y0], 
                         mode='markers', name='Точка касания', 
                         marker=dict(color='red', size=10)))

fig.add_annotation(x=x0, y=y0,
                   text=f"<b>Точка касания</b><br>({x0:.1f}, {y0:.2f})<br>k={k:.2f}",
                   showarrow=True, arrowhead=1, ax=60, ay=-60,
                   bgcolor="yellow", opacity=0.8, bordercolor="black")

fig.update_layout(title='Интерактивная кусочно-заданная функция и касательная',
                  xaxis_title='Ось X',
                  yaxis_title='Ось Y',
                  template='plotly_white',
                  hovermode="x unified")

html_filename = "interactive_plot.html"
fig.write_html(html_filename)
print(f"Интерактивный график сохранен в файл: {html_filename}")

fig.show()