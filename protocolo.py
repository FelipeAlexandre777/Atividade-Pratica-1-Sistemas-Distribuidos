import socket
import struct


TAMANHO_CABECALHO = 4


def enviar_mensagem(sock: socket.socket, conteudo: str) -> None:
    """Envia o tamanho da mensagem e depois seu conteúdo em UTF-8."""
    dados = conteudo.encode("utf-8")
    cabecalho = struct.pack("!I", len(dados))
    sock.sendall(cabecalho + dados)


def receber_exatamente(sock: socket.socket, quantidade: int) -> bytes:
    """Lê exatamente a quantidade de bytes solicitada."""
    partes = []
    recebidos = 0

    while recebidos < quantidade:
        parte = sock.recv(quantidade - recebidos)

        if not parte:
            raise ConnectionError(
                "A conexão foi encerrada antes da mensagem terminar."
            )

        partes.append(parte)
        recebidos += len(parte)

    return b"".join(partes)


def receber_mensagem(sock: socket.socket) -> str:
    """Lê o cabeçalho e depois o conteúdo completo da mensagem."""
    cabecalho = receber_exatamente(sock, TAMANHO_CABECALHO)
    tamanho = struct.unpack("!I", cabecalho)[0]

    if tamanho == 0:
        raise ValueError("Mensagem vazia recebida.")

    dados = receber_exatamente(sock, tamanho)
    return dados.decode("utf-8")
