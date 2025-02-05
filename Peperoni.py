
#Ejemplo 1
d=10
print(d)

import yfinance as yf


def get_nvidia_stock_data():
    # El símbolo de NVIDIA en Yahoo Finance es "NVDA"
    ticker_symbol = "NVDA"

    try:
        # Descargamos los datos del ticker
        nvidia = yf.Ticker(ticker_symbol)

        # Información general sobre el ticker
        info = nvidia.info
        print(f"Nombre: {info['shortName']}")
        print(f"Sector: {info['sector']}")
        print(f"Industria: {info['industry']}")
        print(f"Precio actual: ${info['currentPrice']}")
        print(f"Rango de 52 semanas: {info['fiftyTwoWeekLow']} - {info['fiftyTwoWeekHigh']}")

        # Opcional: Obtener datos históricos
        hist = nvidia.history(period="1mo")  # Último mes de datos
        print("\nDatos históricos del último mes:")
        print(hist)
    except Exception as e:
        print(f"Error al obtener los datos: {e}")


# Llamamos a la función
get_nvidia_stock_data()

#Tarea: Sintaxys, ciclos, classes
