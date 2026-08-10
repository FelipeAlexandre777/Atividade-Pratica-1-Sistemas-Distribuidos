from typing import Dict, Any

import yaml


def serializar(dados: Dict[str, Any]) -> str:
    """Converte o dicionário para YAML."""
    return yaml.safe_dump(
        dados,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    )


def desserializar(conteudo: str) -> Dict[str, Any]:
    """Converte YAML para dicionário."""
    return yaml.safe_load(conteudo)
