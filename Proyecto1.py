import yfinance as yf
import pandas as pd


def obtener_mejores_etfs(cantidad=5):
    # Lista de algunos ETFs populares en EE.UU.
    etfs = ["SPY", "QQQ", "VTI", "IVV", "VOO", "DIA", "IWM", "ARKK", "XLK", "XLF"]

    datos = []

    for etf in etfs:
        activo = yf.Ticker(etf)
        hist = activo.history(period="1y")
        if not hist.empty:
            rendimiento = (hist["Close"].iloc[-1] / hist["Close"].iloc[0]) - 1
            datos.append((etf, rendimiento))

    # Ordenar por mejor rendimiento
    datos.sort(key=lambda x: x[1], reverse=True)

    # Convertir a DataFrame para mejor visualización
    df = pd.DataFrame(datos, columns=["ETF", "Rendimiento 1 Año"])

    return df.head(cantidad)


if __name__ == "__main__":
    print("Los mejores ETFs en el último año son:")
    print(obtener_mejores_etfs())
