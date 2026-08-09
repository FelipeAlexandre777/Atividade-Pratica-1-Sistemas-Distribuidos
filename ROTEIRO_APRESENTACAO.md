# Roteiro para apresentação ao professor

## 1. Introdução

"Eu escolhi Python porque ele é multiplataforma e possui suporte para sockets TCP. A ideia foi deixar o projeto simples o suficiente para rodar em Windows, Linux e macOS."

## 2. Estrutura

Mostrar:

```text
cliente.py
servidor.py
modelo.py
protocolo.py
serializadores/
```

Explicar:

"Eu fiz um módulo separado para cada serialização. Assim, CSV, JSON, XML, YAML e TOML ficam independentes."

## 3. Modelo

Abrir `modelo.py`.

"Essa classe representa a mensagem que vai circular entre cliente e servidor. Ela tem exatamente os quatro campos pedidos na atividade."

"Eu deixei CPF como string porque ele é um identificador."

## 4. Cliente

Abrir `cliente.py`.

"Eu crio a mensagem uma vez e depois passo pelos cinco serializadores. Cada resultado vira texto e é enviado pelo socket."

## 5. Servidor

Abrir `servidor.py`.

"O servidor faz o processo inverso: recebe o texto, usa o desserializador correspondente e recupera os mesmos quatro valores."

## 6. Protocolo TCP

Abrir `protocolo.py`.

Falar:

"TCP é um fluxo de bytes. Por isso, eu não posso depender de um único recv para representar uma mensagem inteira."

Mostrar:

```python
cabecalho = struct.pack("!I", len(dados))
```

e:

```python
tamanho = struct.unpack("!I", cabecalho)[0]
```

Explicar:

"Os primeiros quatro bytes informam o tamanho. Depois o servidor lê exatamente aquele tamanho."

## 7. Execução

Terminal 1:

```powershell
py servidor.py
```

Terminal 2:

```powershell
py cliente.py
```

Mostrar no servidor:

```text
[1/5] FORMATO RECEBIDO: CSV
[2/5] FORMATO RECEBIDO: JSON
[3/5] FORMATO RECEBIDO: XML
[4/5] FORMATO RECEBIDO: YAML
[5/5] FORMATO RECEBIDO: TOML
```

## 8. Fechamento

"Então a aplicação tem um cliente e um servidor via sockets, envia a mesma mensagem cinco vezes usando os cinco formatos pedidos e o servidor recebe, desserializa, manipula e imprime os dados em todas as cinco situações."
