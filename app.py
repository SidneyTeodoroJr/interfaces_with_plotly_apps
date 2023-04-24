import plotly.graph_objs as go
from plotly.offline import plot

# Dados fictícios de exemplo
labels = ['TikTok', 'WhatsApp', 'Instagram', 'Facebook', 'Snapchat', 'Zoom', 'YouTube', 'Uber', 'Google Maps', 'Spotify', 'Netflix', 'Amazon Shopping', 'Google Chrome', 'Candy Crush Saga', 'Subway Surfers']
values = [200000000, 150000000, 120000000, 100000000, 80000000, 70000000, 50000000, 40000000, 30000000, 25000000, 20000000, 15000000, 10000000, 5000000, 2000000]

# Definindo as barras
data = [go.Bar(
            x=labels,
            y=values,
            marker=dict(
                color='rgb(7, 168, 56)'
            )
        )]

# Definindo o layout
layout = go.Layout(
    title='Dados fictícios dos APPs mais baixados da PlayStory em 2023',
    xaxis=dict(title='Aplicativos'),
    yaxis=dict(title='Download'),
)

# Criando a figura
fig = go.Figure(data=data, layout=layout)

# Renderizando o gráfico em um arquivo HTML
plot(fig, filename='dashboard_app.html')
