# Relatório — Atividade Teórica e Prática 1

## 1. Introdução

O objetivo desta atividade foi desenvolver uma aplicação simples de comunicação entre um cliente e um servidor em um sistema distribuído, utilizando sockets TCP e diferentes formatos de serialização baseados em texto.

A aplicação troca uma mesma estrutura de dados utilizando CSV, JSON, XML, YAML e TOML. Dessa forma, foi possível observar que a informação pode ser representada de maneiras diferentes, mesmo mantendo os mesmos valores.

## 2. Tecnologias utilizadas

Foi utilizada a linguagem Python por possuir suporte multiplataforma e uma biblioteca padrão com recursos para sockets, CSV, JSON e XML.

Para YAML foi utilizada a biblioteca PyYAML.

| Biblioteca/módulo | Utilização |
|---|---|
| `socket` | Comunicação TCP |
| `csv` | CSV |
| `json` | JSON |
| `xml.etree.ElementTree` | XML |
| `yaml` / PyYAML | YAML |
| `serializadores/toml_serializador.py` | TOML |

## 3. Arquitetura

O sistema possui:

- `cliente.py`: cria, serializa e envia.
- `servidor.py`: recebe, desserializa e imprime.
- `modelo.py`: representa a mensagem.
- `protocolo.py`: controla o tamanho das mensagens TCP.
- `serializadores/`: possui uma biblioteca/módulo separado para cada formato.

## 4. Comunicação por sockets

Foi utilizado TCP para realizar a comunicação confiável entre os processos.

O cliente inicia a conexão e envia cinco mensagens consecutivas. O servidor recebe cada mensagem, aplica o desserializador correspondente e recupera os quatro campos originais.

## 5. Controle do tamanho

TCP é um fluxo contínuo de bytes. Portanto, uma chamada de `recv()` não deve ser tratada como se representasse necessariamente uma mensagem inteira.

O projeto utiliza um cabeçalho de 4 bytes antes de cada conteúdo. Esse cabeçalho informa o tamanho da mensagem.

O servidor primeiro lê o tamanho e depois chama uma função que continua recebendo até obter todos os bytes da mensagem.

## 6. Dados utilizados

```text
Nome: Fulano da Silva
CPF: 10326709722
Idade: 45
Mensagem: segue comprovante de endereço
```

O CPF foi tratado como texto porque é um identificador e não um valor usado para cálculo.

## 7. Formatos

### CSV

```text
nome,cpf,idade,mensagem
Fulano da Silva,10326709722,45,segue comprovante de endereço
```

Arquivo:

```text
serializadores/csv_serializador.py
```

### JSON

```json
{
  "nome": "Fulano da Silva",
  "cpf": "10326709722",
  "idade": 45,
  "mensagem": "segue comprovante de endereço"
}
```

Arquivo:

```text
serializadores/json_serializador.py
```

### XML

```xml
<mensagem>
  <nome>Fulano da Silva</nome>
  <cpf>10326709722</cpf>
  <idade>45</idade>
  <mensagem>segue comprovante de endereço</mensagem>
</mensagem>
```

Arquivo:

```text
serializadores/xml_serializador.py
```

### YAML

```yaml
nome: Fulano da Silva
cpf: '10326709722'
idade: 45
mensagem: segue comprovante de endereço
```

Arquivo:

```text
serializadores/yaml_serializador.py
```

### TOML

```toml
nome = "Fulano da Silva"
cpf = "10326709722"
idade = 45
mensagem = "segue comprovante de endereço"
```

Arquivo:

```text
serializadores/toml_serializador.py
```

## 8. Funcionamento do cliente

O cliente cria um objeto `Mensagem` e monta uma lista contendo os cinco serializadores.

Para cada formato, ele:

1. serializa os dados;
2. mostra a representação no terminal;
3. envia o texto pelo socket.

## 9. Funcionamento do servidor

O servidor possui a ordem dos cinco desserializadores.

Para cada mensagem:

1. recebe o texto;
2. desserializa;
3. cria novamente o objeto `Mensagem`;
4. imprime nome, CPF, idade e mensagem.

## 10. Resultado

O servidor deve apresentar:

```text
[1/5] FORMATO RECEBIDO: CSV
[2/5] FORMATO RECEBIDO: JSON
[3/5] FORMATO RECEBIDO: XML
[4/5] FORMATO RECEBIDO: YAML
[5/5] FORMATO RECEBIDO: TOML
```

Em todos os cinco casos, os valores recuperados devem ser iguais.

## 11. Capturas de tela

Adicionar:

**Figura 1 — Estrutura do projeto no VS Code.**

Mostrar os arquivos e a pasta `serializadores`.

**Figura 2 — Servidor aguardando conexão.**

Mostrar:

```text
Aguardando conexão na porta 5000...
```

**Figura 3 — Cliente enviando as cinco serializações.**

Mostrar CSV, JSON, XML, YAML e TOML.

**Figura 4 — Servidor recebendo as mensagens.**

Mostrar os cinco blocos recebidos.

**Figura 5 — Código dos serializadores.**

Mostrar a pasta `serializadores` e pelo menos dois arquivos.

**Figura 6 — Protocolo de tamanho da mensagem.**

Mostrar `protocolo.py`, principalmente `struct.pack`, `struct.unpack` e `receber_exatamente`.

## 12. Conclusão

A atividade permitiu colocar em prática conceitos de Sistemas Distribuídos por meio da comunicação entre cliente e servidor utilizando sockets TCP.

Também foi possível observar a diferença entre os formatos de serialização. A mesma informação foi enviada cinco vezes, em CSV, JSON, XML, YAML e TOML, e em todas as situações o servidor conseguiu recuperar os quatro campos originais.

A organização em módulos separados deixou o código mais simples de estudar, testar e apresentar.
