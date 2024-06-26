import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Definir los tickers de los activos del portafolio y del índice
tickers_portafolio = ["WALMEX.MX", "SORIANAB.MX", "LACOMERUBC.MX", "CHDRAUIB.MX"]
ticker_indice = '^MXX'  # Ticker del IPC

# Obtener datos
datos_portafolio = yf.download(tickers_portafolio, start='2023-01-01', end='2024-01-01')['Adj Close']
datos_indice = yf.download(ticker_indice, start='2023-01-01', end='2024-01-01')['Adj Close']

# Calcular los retornos diarios
retorno_diario_portafolio = datos_portafolio.pct_change().dropna()
retorno_diario_indice = datos_indice.pct_change().dropna()

# Calcular los retornos acumulativos
retorno_acum_portafolio = (1 + retorno_diario_portafolio).cumprod()
retorno_acum_indice = (1 + retorno_diario_indice).cumprod()

# Configurar la aplicación Streamlit
st.title('Comparación de rendimiento del portafolio optimizado con índice IPC')

# Mostrar gráfico de los retornos acumulativos
st.pyplot(plt.figure(figsize=(12, 6)))
plt.plot(retorno_acum_portafolio.index, retorno_acum_portafolio.sum(axis=1), label='Portafolio Optimizado')
plt.plot(retorno_acum_indice.index, retorno_acum_indice, label='Índice IPC')
plt.title('Comparación de rendimiento del portafolio optimizado con índice IPC')
plt.xlabel('Fecha')
plt.ylabel('Valor acumulado del retorno')
plt.legend()
plt.grid(True)
