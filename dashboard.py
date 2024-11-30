import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Com uma visão mensal
# faturamento por unidade…
# tipo de produto mais vendido, contribuição por filial,
# Desempenho das forma de pagamento…
# Como estão as avaliações das filiais?

# Carregando e processando os dados
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%B de %Y")
df = df.sort_values("Date")

# Filtros
month = st.sidebar.selectbox("Mês", df["Month"].unique())
city = st.sidebar.selectbox("Cidade", ["Todas"] + list(df["City"].unique()))

df_filtered = df[df["Month"] == month]
if city != "Todas":
    df_filtered = df_filtered[df_filtered["City"] == city]

# KPIs
col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
col_kpi1.metric("Faturamento Total", f"R$ {df_filtered['Total'].sum():,.2f}")
col_kpi2.metric("Vendas Totais", df_filtered.shape[0])
col_kpi3.metric("Avaliação Média", f"{df_filtered['Rating'].mean():.2f}")

# Gráficos
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(
    df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia"
)
col1.plotly_chart(fig_date, use_container_width=True)

prod_total = df_filtered.groupby("Product line")[["Total"]].sum().reset_index()
fig_prod = px.bar(
    prod_total,
    x="Total",
    y="Product line",
    color="Product line",
    title="Faturamento por tipo de produto",
    orientation="h",
)
col2.plotly_chart(fig_prod, use_container_width=True)

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(
    df_filtered,
    values="Total",
    names="Payment",
    title="Faturamento por tipo de pagamento",
)
col4.plotly_chart(fig_kind, use_container_width=True)

city_ratings = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(
    city_ratings, x="City", y="Rating", title="Avaliação Média por Filial"
)
col5.plotly_chart(fig_rating, use_container_width=True)
