from pathlib import Path
import time

def salvar_csv(df, arquivo):
    path = Path(arquivo)
    try:
        inicio = time.time()

        if not path.parent.exists():
            print("Erro: Diretório não encontrado.")
            return

        df.to_csv(path, index=False, encoding='utf-8')

        fim = time.time()
        print(f"\n===== Arquivo salvo com sucesso em: {path} =====")
        print(f"===== Tempo para salvar: {fim - inicio:.4f} segundos =====")

    except PermissionError:
        print("Erro: Permissão negada para salvar o arquivo.")
    except UnicodeEncodeError:
        print("Erro: Problema de codificação ao salvar o arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
