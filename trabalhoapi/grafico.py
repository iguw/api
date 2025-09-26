import matplotlib.pyplot as plt

def plotar_histograma(df, estatisticas):
    plt.figure(figsize=(10, 6))
    plt.hist(df["body_len"], bins=20, color= 'cyan', edgecolor='black', alpha=0.7)

    plt.axvline(estatisticas["Média"], color='red', linestyle='dashed', linewidth=2, label=f"Média: {estatisticas['Média']:.2f}")
    plt.axvline(estatisticas["Mediana"], color='green', linestyle='dashed', linewidth=2, label=f"Mediana: {estatisticas['Mediana']:.2f}")
    plt.axvline(estatisticas["Máximo"], color='purple', linestyle='dashed', linewidth=2, label=f"Máximo: {estatisticas['Máximo']:.2f}")
    plt.axvline(estatisticas["Mínimo"], color='yellow', linestyle='dashed', linewidth=2, label=f"Mínimo: {estatisticas['Mínimo']:.2f}")

    plt.title('Comprimento dos Comentários')
    plt.xlabel('Número de caracteres')
    plt.ylabel('Frequência')
    plt.legend()
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.show()
