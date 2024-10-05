
# Automatic Analysis v1.0

## Descrição do Projeto

O **Automatic Analysis v1.0** é uma aplicação web desenvolvida em Flask que permite aos usuários fazer upload de arquivos CSV e realizar análises automáticas dos dados contidos nesses arquivos. A aplicação gera gráficos e estatísticas descritivas, exibindo os resultados através de uma interface web.

## Funcionalidades

- **Upload de arquivos CSV**: Permite que os usuários façam upload de seus próprios arquivos de dados.
- **Análise automática**: Realiza uma análise básica dos dados, incluindo a identificação de tipos de dados, valores ausentes e outras estatísticas.
- **Geração de gráficos**: Cria visualizações dos dados, que são exibidas e armazenadas localmente.
- **Interface web**: Utiliza Flask para oferecer uma interface amigável para interação com o usuário.

## Estrutura do Projeto

- **app.py**: Ponto de entrada da aplicação. Configura o servidor Flask, diretórios para upload e plots, e define as rotas para upload e análise.
- **scripts/analysis.py**: Script que realiza a análise dos dados utilizando bibliotecas como pandas, numpy, e matplotlib.
- **templates/**: Contém os arquivos HTML para renderização das páginas.
- **static/**: Diretório onde são salvos os gráficos gerados.
- **uploads/**: Diretório onde os arquivos CSV enviados são armazenados.
- **requirements.txt**: Lista de dependências necessárias para a execução do projeto.

## Como Executar

1. Clone este repositório para sua máquina local.
   
   ```bash
   git clone https://github.com/GN0Ber/2024-CP05-DATA-SCIENCE
   ```

2. Instale as dependências usando o `pip`.

   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação.

   ```bash
   python app.py
   ```

4. Acesse a aplicação no navegador via `http://127.0.0.1:5000`.

## Dependências

- Flask
- pandas
- numpy
- matplotlib
- seaborn

5. Grupo

- Caíque Walter Silva - RM550693
- Gabriela Marsiglia - RM551237
- Guilherme Nobre Bernardo - RM98604
- Matheus José de Lima Costa - RM551157