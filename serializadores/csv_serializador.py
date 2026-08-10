import csv
import io
from typing import Dict, Any


CAMPOS = ["nome", "cpf", "idade", "mensagem"]


def serializar(dados: Dict[str, Any]) -> str:
    """Converte o dicionário para CSV."""
    saida = io.StringIO()
    escritor = csv.DictWriter(
        saida,
        fieldnames=CAMPOS,
        lineterminator="\n",
    )
    escritor.writeheader()
    escritor.writerow(dados)
    return saida.getvalue()


def desserializar(conteudo: str) -> Dict[str, Any]:
    """Converte CSV para dicionário."""
    entrada = io.StringIO(conteudo)
    leitor = csv.DictReader(entrada)
    dados = next(leitor)

    return {
        "nome": dados["nome"],
        "cpf": dados["cpf"],
        "idade": int(dados["idade"]),
        "mensagem": dados["mensagem"],
    }
