def calcular_estatisticas(df):
    media = df["body_len"].mean()
    mediana = df["body_len"].median()
    minimo = df["body_len"].min()
    maximo = df["body_len"].max()
    return {
        "Média": media,
        "Mediana": mediana,
        "Mínimo": minimo,
        "Máximo": maximo
    }

def mostrar_emails(df, limite=10):
    print(f"\n===== Exibindo até {limite} emails únicos: =====")
    emails = df["email"].unique()[:limite]
    for e in emails:
        print("-", e)
    print(f"===== Total de emails únicos: {df['email'].nunique()} =====")
