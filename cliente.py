import socket

from modelo import Mensagem
from protocolo import enviar_mensagem
from serializadores import (
    csv_serializador,
    json_serializador,
    xml_serializador,
    yaml_serializador,
    toml_serializador,
)



HOST = "127.0.0.1"
PORTA = 5000


def main() -> None:
    mensagem = Mensagem(
        nome="Fulano da Silva",
        cpf="10326709722",
        idade=45,
        mensagem="segue comprovante de endereço",
    )

    serializadores = [
        ("CSV", csv_serializador.serializar),
        ("JSON", json_serializador.serializar),
        ("XML", xml_serializador.serializar),
        ("YAML", yaml_serializador.serializar),
        ("TOML", toml_serializador.serializar),
    ]

    print("=" * 60)
    print("CLIENTE - SISTEMAS DISTRIBUÍDOS")
    print("=" * 60)
    print(f"Conectando em {HOST}:{PORTA}...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORTA))
        print("Conexão estabelecida.")
        print()

        for numero, (nome_formato, serializar) in enumerate(
            serializadores, start=1
        ):
            conteudo = serializar(mensagem.para_dicionario())

            print(f"[{numero}/5] Enviando em {nome_formato}...")
            print("Conteúdo serializado:")
            print(conteudo)
            print("-" * 60)

            enviar_mensagem(sock, conteudo)

        print("As 5 mensagens foram enviadas com sucesso.")

    print("Conexão encerrada.")


if __name__ == "__main__":
    main()
