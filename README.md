# Supermarket Sales Dashboard
Este projeto é um dashboard interativo desenvolvido em Python utilizando o Streamlit e o Plotly, com o objetivo de analisar e visualizar as vendas de um supermercado.

O dashboard permite que o usuário explore métricas importantes, como faturamento por dia, tipos de produto mais vendidos, contribuições por filial, desempenho das formas de pagamento e avaliações das filiais.

🚀 Tecnologias Utilizadas
Streamlit: Para criar a interface web interativa.
Pandas: Para manipulação e análise de dados.
Plotly: Para visualização de gráficos interativos.

📊 Funcionalidades
Faturamento por Dia: Exibe o total de vendas por dia, categorizado por cidade.
Faturamento por Tipo de Produto: Mostra quais categorias de produtos geraram mais receita.
Faturamento por Filial: Analisa o desempenho de vendas por cidade/filial.
Faturamento por Tipo de Pagamento: Exibe a contribuição de cada forma de pagamento.
Avaliações por Filial: Mostra a média das avaliações de clientes para cada filial.

📝 Como Executar o Projeto
Pré-requisitos
Python instalado (versão 3.7 ou superior).
Virtualenv ou outro gerenciador de ambientes virtuais (opcional, mas recomendado).
Passos
Clone o repositório:
```shell
git clone https://github.com/seu-usuario/supermarket-sales-dashboard.git
cd supermarket-sales-dashboard
```

(Opcional) Crie e ative um ambiente virtual:
```shell
# Linux e Mac:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate
```
Instale as dependências:

```shell
pip install -r requirements.txt
```

Execute o dashboard:

```shell
streamlit run dashboard.py
```

Acesse o dashboard no navegador:

O Streamlit fornecerá um link (geralmente algo como http://localhost:8501).

```
🗂 Estrutura do Projeto

```shell
supermarket-sales-dashboard/
├── supermarket_sales.csv   # Base de dados com informações de vendas
├── dashboard.py            # Código principal do dashboard
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

📄 Base de Dados
```shell
O arquivo supermarket_sales.csv contém os dados utilizados no projeto.
Principais colunas:
Date: Data da transação.
City: Cidade/filial.
Product line: Categoria do produto.
Total: Faturamento total.
Payment: Tipo de pagamento.
Rating: Avaliação do cliente.
```

💡 Melhorias Futuras
```shell
Adicionar mais filtros (como cidade ou tipo de produto).
Implementar download de relatórios em PDF/Excel.
Personalizar a interface com estilos mais avançados.
```

🧑‍💻 Autor
```shell
Desenvolvido por Junio Chaves. 😊
```
