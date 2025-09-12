import csv
import pandas as pd
import requests
import matplotlib.pyplot as plt
from pathlib import Path
import time


inicio = time.time()


url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url) # pega os dados
comments = response.json() # armazena em uma lista de dicionarios 
print(f"Total de comentários: {len(comments)}") # print pra ver se deu tudo certo


df = pd.DataFrame(comments) # transforma em dataframe do pandas
print(df.head()) # printa o começo pra ver se deu tudo certo


df["body_len"] = df["body"].str.len() # cria uma nova coluna com o tamanho do comentario
# print("Média de caracteres: ", df["body_len"].mean())
# print("Mediana de caracteres: ", df["body_len"].median())
media = df["body_len"].mean() # calcula a média
mediana = df["body_len"].median() # calcula a mediana
max = df["body_len"].max() # calcula o máximo
min = df["body_len"].min() # calcula o mínimo


# Cria o histograma da coluna 'body_len'
plt.figure(figsize=(10, 6)) # Define o tamanho da figura
plt.hist(df["body_len"], bins=20, edgecolor='black', alpha=0.7) # bins define o número de barras

# Adiciona linhas verticais para a média e a mediana
plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Média: {media:.2f}')
plt.axvline(mediana, color='green', linestyle='dashed', linewidth=2, label=f'Mediana: {mediana:.2f}')
plt.axvline(max, color='pink', linestyle='dashed', linewidth=2, label=f'Máximo: {max:.2f}')
plt.axvline(min, color='yellow', linestyle='dashed', linewidth=2, label=f'Mínimo: {min:.2f}')

# Adiciona título e rótulos aos eixos
plt.title('Distribuição do Comprimento dos Comentários')
plt.xlabel('Comprimento do Comentário (número de caracteres)')
plt.ylabel('Frequência')

# Adiciona legenda para média e mediana
plt.legend()

# Exibe o gráfico
plt.grid(axis='y', alpha=0.75) # Adiciona grade ao eixo Y
plt.tight_layout() # Ajusta o layout para evitar sobreposição
plt.show()


def salvar_csv(df, arquivo): # função para salvar o dataframe em csv
    path = Path(arquivo) 
    try:
        # verifica se o diretório existe        
        if not path.parent.exists(): 
            print("Erro: Diretório não encontrado.") 
            return 

        # salva o dataframe em csv
        df.to_csv(path, index=False, encoding='utf-8')
        print(f"Arquivo salvo com sucesso em: {path}")
    except PermissionError:
        print("Erro: Permissão negada para salvar o arquivo.")
    except UnicodeEncodeError:
        print("Erro: Problema de codificação ao salvar o arquivo.")
    except Exception:
        print(f"Ocorreu um erro inesperado: {Exception}")

salvar_csv(df, "comentarios.csv")


fim = time.time()
print(f"Tempo total de execução: {fim - inicio:.2f} segundos")