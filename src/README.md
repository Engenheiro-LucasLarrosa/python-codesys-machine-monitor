# Código-fonte Python

Esta pasta contém a aplicação responsável pela leitura dos dados disponibilizados pelo CODESYS e pelo registro do histórico em CSV.

## Arquivos

### `app_machinesimulation.py`

Arquivo principal da aplicação.

Responsabilidades:

- executar o ciclo de leitura;
- interpretar os dados recebidos;
- exibir os valores no terminal;
- solicitar o registro em CSV;
- tratar interrupção pelo usuário.

### `modbus.py`

Módulo de comunicação Modbus TCP.

Responsabilidades:

- configurar o cliente Modbus;
- conectar ao servidor CODESYS;
- ler os Input Registers;
- converter os valores recebidos;
- retornar os dados em uma estrutura organizada.

### `csv_logger.py`

Módulo de armazenamento.

Responsabilidades:

- criar a pasta de dados;
- criar o arquivo CSV;
- escrever o cabeçalho;
- registrar data, hora e valores da máquina;
- preservar o histórico existente.

## Fluxo da aplicação

```text
app_machinesimulation.py
        ↓
modbus.py
        ↓
CODESYS
        ↓
csv_logger.py
        ↓
machine_history.csv
