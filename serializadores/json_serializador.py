import json
from typing import Dict, Any


def serializar(dados: Dict[str, Any]) -> str:
    """Converte o dicionário para JSON."""
    return json.dumps(
        dados,
        ensure_ascii=False,
        indent=2,
    )


def desserializar(conteudo: str) -> Dict[str, Any]:
    """Converte JSON para dicionário."""
    return json.loads(conteudo)
