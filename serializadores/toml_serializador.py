from typing import Dict, Any


def _escapar(texto: str) -> str:
    return texto.replace("\\", "\\\\").replace('"', '\\"')


def serializar(dados: Dict[str, Any]) -> str:
    """Converte os quatro campos do projeto para TOML."""
    return (
        f'nome = "{_escapar(str(dados["nome"]))}"\n'
        f'cpf = "{_escapar(str(dados["cpf"]))}"\n'
        f'idade = {int(dados["idade"])}\n'
        f'mensagem = "{_escapar(str(dados["mensagem"]))}"\n'
    )


def desserializar(conteudo: str) -> Dict[str, Any]:
    """Lê o TOML simples usado pela atividade.

    O parser foi mantido pequeno de propósito: os dados da atividade
    possuem apenas strings e um inteiro.
    """
    dados = {}

    for linha in conteudo.splitlines():
        linha = linha.strip()

        if not linha or linha.startswith("#") or "=" not in linha:
            continue

        chave, valor = linha.split("=", 1)
        chave = chave.strip()
        valor = valor.strip()

        if valor.startswith('"') and valor.endswith('"'):
            valor = valor[1:-1]
            valor = valor.replace('\\"', '"').replace("\\\\", "\\")
        elif chave == "idade":
            valor = int(valor)

        dados[chave] = valor

    return dados
