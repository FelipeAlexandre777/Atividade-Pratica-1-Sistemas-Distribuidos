# Atividade Teórica e Prática 1 — Sistemas Distribuídos

Projeto desenvolvido para demonstrar a troca de mensagens entre **1 cliente e 1 servidor usando sockets TCP**, utilizando cinco formatos de serialização baseados em texto:

- CSV
- JSON
- XML
- YAML
- TOML

A mesma mensagem é enviada cinco vezes, uma vez em cada formato. O servidor recebe, desserializa, manipula e imprime os dados.

## Dados enviados

- Nome
- CPF
- idade
- mensagem

Exemplo:

```text
Nome: Fulano da Silva
CPF: 10326709722
Idade: 45
Mensagem: segue comprovante de endereço
```

## Estrutura

```text
sistemas_distribuidos_serializacao/
├── cliente.py
├── servidor.py
├── modelo.py
├── protocolo.py
├── requirements.txt
├── README.md
├── RELATORIO.md
├── ROTEIRO_APRESENTACAO.md
└── serializadores/
    ├── __init__.py
    ├── csv_serializador.py
    ├── json_serializador.py
    ├── xml_serializador.py
    ├── yaml_serializador.py
    └── toml_serializador.py
```

Cada formato possui seu próprio módulo, para facilitar a comparação e a explicação durante a apresentação.

## Requisitos

- Python 3.9 ou superior
- Windows, Linux ou macOS

Dependência externa:

- PyYAML — usada somente pelo módulo YAML.

CSV, JSON, XML e sockets usam a biblioteca padrão do Python. O módulo TOML deste projeto também não exige pacote externo.

## Instalação no Windows

No PowerShell ou Prompt de Comando, dentro da pasta:

```powershell
py -m pip install -r requirements.txt
```

ou:

```powershell
python -m pip install -r requirements.txt
```

## Executando

### Terminal 1 — servidor

```powershell
py servidor.py
```

### Terminal 2 — cliente

```powershell
py cliente.py
```

O cliente envia automaticamente:

1. CSV
2. JSON
3. XML
4. YAML
5. TOML

O servidor recebe e imprime os quatro campos cinco vezes.

## Como funciona

```text
CLIENTE                         SERVIDOR
   |                                |
   |---- conexão TCP -------------->|
   |                                |
   |---- mensagem CSV ------------->|
   |                                | desserializa
   |                                | imprime
   |---- mensagem JSON ------------>|
   |                                | desserializa
   |                                | imprime
   |---- mensagem XML ------------->|
   |                                | desserializa
   |                                | imprime
   |---- mensagem YAML ------------>|
   |                                | desserializa
   |                                | imprime
   |---- mensagem TOML ------------>|
   |                                | desserializa
   |                                | imprime
   |                                |
```

### Por que existe `protocolo.py`?

TCP é um fluxo de bytes. Uma chamada de `recv()` não garante que uma mensagem completa será recebida de uma vez.

Por isso, antes de cada mensagem o cliente envia **4 bytes informando o tamanho do conteúdo**. O servidor lê esses 4 bytes e depois lê exatamente a quantidade de bytes indicada.

Assim, as cinco mensagens ficam corretamente separadas.

## Rodando em dois computadores

No servidor, descubra o IPv4:

```powershell
ipconfig
```

Se o servidor tiver, por exemplo, `192.168.0.15`, altere no `cliente.py`:

```python
HOST = "192.168.0.15"
```

No mesmo computador, use:

```python
HOST = "127.0.0.1"
```

As máquinas precisam estar na mesma rede e a porta 5000 deve estar liberada no firewall do computador servidor.

## Resultado esperado

No servidor:

```text
[1/5] FORMATO RECEBIDO: CSV
Nome      : Fulano da Silva
CPF       : 10326709722
Idade     : 45
Mensagem  : segue comprovante de endereço

[2/5] FORMATO RECEBIDO: JSON
Nome      : Fulano da Silva
CPF       : 10326709722
Idade     : 45
Mensagem  : segue comprovante de endereço

[3/5] FORMATO RECEBIDO: XML
Nome      : Fulano da Silva
CPF       : 10326709722
Idade     : 45
Mensagem  : segue comprovante de endereço

[4/5] FORMATO RECEBIDO: YAML
Nome      : Fulano da Silva
CPF       : 10326709722
Idade     : 45
Mensagem  : segue comprovante de endereço

[5/5] FORMATO RECEBIDO: TOML
Nome      : Fulano da Silva
CPF       : 10326709722
Idade     : 45
Mensagem  : segue comprovante de endereço
```
