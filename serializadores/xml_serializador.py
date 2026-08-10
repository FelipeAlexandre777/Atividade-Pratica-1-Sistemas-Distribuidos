import xml.etree.ElementTree as ET
from typing import Dict, Any


def serializar(dados: Dict[str, Any]) -> str:
    """Converte o dicionário para XML."""
    raiz = ET.Element("mensagem")

    for campo in ("nome", "cpf", "idade", "mensagem"):
        elemento = ET.SubElement(raiz, campo)
        elemento.text = str(dados[campo])

    return ET.tostring(raiz, encoding="unicode")


def desserializar(conteudo: str) -> Dict[str, Any]:
    """Converte XML para dicionário."""
    raiz = ET.fromstring(conteudo)

    return {
        "nome": raiz.findtext("nome"),
        "cpf": raiz.findtext("cpf"),
        "idade": int(raiz.findtext("idade")),
        "mensagem": raiz.findtext("mensagem"),
    }
