import time
import requests
import pandas as pd
from estatisticas import calcular_estatisticas, mostrar_emails
from grafico import plotar_histograma
from salvar import salvar_csv

inicio_total = time.time()


url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url)
comments = response.json()
print(f"===== Total de comentários: {len(comments)} =====")

df = pd.DataFrame(comments)
print("\n===== Primeiras linhas do DataFrame: =====")
print(df.head())


df["body_len"] = df["body"].str.len()


estatisticas = calcular_estatisticas(df)
print("\n===== Estatísticas do tamanho dos comentários: =====")
for k, v in estatisticas.items():
    print(f"{k}: {v:.2f}")


mostrar_emails(df, limite=5)


plotar_histograma(df, estatisticas)


salvar_csv(df, "trabalhoapi/comentarios.csv")

fim_total = time.time()
print(f"\n===== Tempo total de execução: {fim_total - inicio_total:.2f} segundos =====")
