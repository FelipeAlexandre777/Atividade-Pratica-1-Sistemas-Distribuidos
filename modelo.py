from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class Mensagem:
    """Representa os dados que serão trocados entre cliente e servidor."""

    nome: str
    cpf: str
    idade: int
    mensagem: str

    def para_dicionario(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def de_dicionario(cls, dados: Dict[str, Any]) -> "Mensagem":
        return cls(
            nome=str(dados["nome"]),
            cpf=str(dados["cpf"]),
            idade=int(dados["idade"]),
            mensagem=str(dados["mensagem"]),
        )
