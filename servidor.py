import socket

from modelo import Mensagem
from protocolo import receber_mensagem
from serializadores import (
    csv_serializador,
    json_serializador,
    xml_serializador,
    yaml_serializador,
    toml_serializador,
)


HOST = "0.0.0.0"
PORTA = 5000


FORMATOS = [
    ("CSV", csv_serializador.desserializar),
    ("JSON", json_serializador.desserializar),
    ("XML", xml_serializador.desserializar),
    ("YAML", yaml_serializador.desserializar),
    ("TOML", toml_serializador.desserializar),
]


def imprimir_mensagem(mensagem: Mensagem) -> None:
    print(f"Nome      : {mensagem.nome}")
    print(f"CPF       : {mensagem.cpf}")
    print(f"Idade     : {mensagem.idade}")
    print(f"Mensagem  : {mensagem.mensagem}")


def main() -> None:
    print("=" * 60)
    print("SERVIDOR - SISTEMAS DISTRIBUÍDOS")
    print("=" * 60)
    print(f"Aguardando conexão na porta {PORTA}...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORTA))
        servidor.listen(1)

        conexao, endereco = servidor.accept()

        with conexao:
            print(f"Cliente conectado: {endereco[0]}:{endereco[1]}")
            print()

            for numero, (nome_formato, desserializar) in enumerate(
                FORMATOS, start=1
            ):
                conteudo = receber_mensagem(conexao)
                dados = desserializar(conteudo)
                mensagem = Mensagem.de_dicionario(dados)

                print("=" * 60)
                print(f"[{numero}/5] FORMATO RECEBIDO: {nome_formato}")
                print("=" * 60)
                imprimir_mensagem(mensagem)
                print()
                print("Conteúdo recebido:")
                print(conteudo)
                print()

            print("=" * 60)
            print("As 5 mensagens foram recebidas e processadas.")
            print("=" * 60)


if __name__ == "__main__":
    main()
