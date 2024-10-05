# scripts/analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def make_analysis(path, file):
    # Caminho completo para o arquivo CSV
    csv = os.path.join(path, file)
    
    # Carregar os dados
    df = pd.read_csv(csv)
    
    # Visão geral do conjunto de dados
    num_rows, num_cols = df.shape
    data_types = df.dtypes
    missing_values = df.isnull().sum()
    
    # Diretório para salvar os gráficos
    plots_dir = 'static/plots'
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    else:
        # Limpar o diretório de gráficos antes de cada análise
        for filename in os.listdir(plots_dir):
            file_path = os.path.join(plots_dir, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
    
    # Lista para armazenar informações das variáveis
    variables = []
    
    # Analisar variáveis numéricas
    for col in df.select_dtypes(include=np.number).columns:
        col_safe = col.replace('/', '_').replace('\\', '_')
        stats = df[col].describe().to_frame().to_html()
        plt.figure()
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f'Distribuição de {col}')
        plot_filename = f'{col_safe}_hist.png'
        plot_path = os.path.join(plots_dir, plot_filename)
        plt.savefig(plot_path)
        plt.close()
        variables.append({
            'name': col,
            'type': 'Numérica',
            'stats_table': stats,
            'plot_path': f'/static/plots/{plot_filename}'
        })
    
    # Analisar variáveis categóricas
    for col in df.select_dtypes(include=['object', 'category']).columns:
        stats = df[col].describe().to_frame().to_html()
        plt.figure()
        df[col].value_counts().plot(kind='bar')
        plt.title(f'Contagem de Valores de {col}')
        plot_filename = f'{col}_bar.png'
        plot_path = os.path.join(plots_dir, plot_filename)
        plt.savefig(plot_path)
        plt.close()
        variables.append({
            'name': col,
            'type': 'Categórica',
            'stats_table': stats,
            'plot_path': f'/static/plots/{plot_filename}'
        })
    
    # Gerar matriz de correlação
    corr_matrix = df.select_dtypes(exclude=['object', 'string']).corr()
    plt.figure(figsize=(10,8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Matriz de Correlação')
    plt.tight_layout()
    plot_filename = 'correlation_matrix.png'
    plot_path = os.path.join(plots_dir, plot_filename)
    plt.savefig(plot_path)
    plt.close()
    correlation_plot_path = f'/static/plots/{plot_filename}'
    
    # Gerar mapa de calor de dados ausentes
    plt.figure(figsize=(12,8))
    sns.heatmap(df.isnull(), cbar=False)
    plt.title('Mapa de Calor de Dados Ausentes')
    plt.tight_layout()
    plot_filename = 'missing_data_heatmap.png'
    plot_path = os.path.join(plots_dir, plot_filename)
    plt.savefig(plot_path)
    plt.close()
    missing_data_plot_path = f'/static/plots/{plot_filename}'
    
    # Compilar o relatório HTML
    overview_html = f'''
    <h2>Visão Geral do Conjunto de Dados</h2>
    <p>Número de observações: {num_rows}</p>
    <p>Número de variáveis: {num_cols}</p>
    <h3>Valores Ausentes</h3>
    {missing_values.to_frame('Valores Ausentes').to_html()}
    '''
    
    variable_html = '<h2>Análise de Variáveis</h2>'
    for var in variables:
        variable_html += f'''
        <h3>{var['name']}</h3>
        <p>Tipo: {var['type']}</p>
        <p>Estatísticas:</p>
        {var['stats_table']}
        <p>Gráfico:</p>
        <img src="{var['plot_path']}" alt="Gráfico de {var['name']}" width="600">
        '''
    
    correlation_html = f'''
    <h2>Matriz de Correlação</h2>
    <img src="{correlation_plot_path}" alt="Matriz de Correlação" width="800">
    '''
    
    missing_data_html = f'''
    <h2>Mapa de Calor de Dados Ausentes</h2>
    <img src="{missing_data_plot_path}" alt="Mapa de Calor de Dados Ausentes" width="800">
    '''
    
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Relatório de Análise de Dados</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            h1 {{ text-align: center; }}
            h2 {{ color: #2F4F4F; }}
            table {{ border-collapse: collapse; width: 80%; margin: auto; }}
            th, td {{ text-align: left; padding: 8px; border: 1px solid #ddd; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
            img {{ display: block; margin-left: auto; margin-right: auto; }}
        </style>
    </head>
    <body>
        <h1>Relatório de Análise de Dados</h1>
        {overview_html}
        {variable_html}
        {correlation_html}
        {missing_data_html}
    </body>
    </html>
    '''
    
    # Salvar o relatório HTML
    with open('templates/output.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
