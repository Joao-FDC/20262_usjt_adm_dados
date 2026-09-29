from pathlib import Path
RAIZ = Path(__file__).parent # é o caminho do arquivo, sua raiz com base no file desse arquivo
DADOS = RAIZ / "dados"
ENTRADA = DADOS / "entrada"
SAIDAS = DADOS / "saidas"
RAW = DADOS / "raw"
BRONZE = DADOS / "bronze"
SILVER = DADOS / "silver"
GOLD = DADOS / "gold"
ARQUIVO = "dirty_cafe_sales.csv"
SLA_FRESCOR_DADOS = 1 #  FRESCOR é o quao atual é o dado
RETENCAO_DADOS = 6 #meses

def preparar_pastas():
    for pasta in [ENTRADA,SAIDAS,RAW,BRONZE,SILVER,GOLD]:
        pasta.mkdir(parents=True, exist_ok=True) #cria as pasta se elas nao existirem

#12.456,78
def br(numero, casas=0):
    texto =f"{numero:,.{casas}f}"
    return texto.replace(",","_").replace(".",",").replace("_",".") #substituição de . e ,


def moeda(valor):
    return "US$" + br(valor,2) #conversao de moeda

if __name__ == "__main__":
    preparar_pastas()
    print("Pastas criadas em", DADOS)