# Monitoramento de máquina industrial com CODESYS, Modbus TCP e Python

Este projeto apresenta uma simulação de máquina industrial desenvolvida no CODESYS, com aquisição de dados realizada por uma aplicação Python por meio do protocolo Modbus TCP.

A máquina simulada possui controle de partida e parada, contador de produção, variação de temperatura e parada automática por alarme. Os dados são disponibilizados pelo CODESYS, lidos pela aplicação Python e registrados em um arquivo CSV para análise posterior.

O projeto faz parte do meu processo de estudo e desenvolvimento profissional em Automação Industrial, integração OT/IT e aplicação de Python no ambiente industrial.

## Arquitetura

![Arquitetura do sistema](docs/diagrams/system-architecture.png)

```text
CODESYS Runtime
      ↓
Modbus TCP
      ↓
Aplicação Python
      ↓
Terminal + arquivo CSV
```

## Funcionalidades

- partida e parada da máquina simulada;
- produção de uma peça a cada dois segundos;
- aumento de temperatura durante o funcionamento;
- redução de temperatura com a máquina parada;
- geração de alarme ao atingir 45 °C;
- parada automática da máquina em condição de alarme;
- liberação do alarme abaixo de 40 °C;
- leitura das variáveis por Modbus TCP;
- exibição dos valores no terminal;
- registro periódico dos dados em CSV;
- interface de visualização desenvolvida no CODESYS.

## Tecnologias utilizadas

- CODESYS;
- Structured Text;
- CODESYS Visualization;
- Modbus TCP;
- Python;
- pyModbusTCP;
- CSV;
- VMware Workstation;
- Visual Studio Code;
- Git e GitHub.

## Variáveis monitoradas

| Variável | Descrição | Unidade |
|---|---|---|
| `MachineRunning` | Estado de funcionamento da máquina | Booleano |
| `AlarmActive` | Estado do alarme de temperatura | Booleano |
| `ProductionCount` | Produção acumulada | peças |
| `Temperature` | Temperatura simulada | °C |

## Mapeamento Modbus

| Input Register | Variável transmitida | Conversão |
|---|---|---|
| 0 | Estado da máquina | `0 = desligada`, `1 = ligada` |
| 1 | Estado do alarme | `0 = normal`, `1 = ativo` |
| 2 | Contador de produção | valor inteiro |
| 3 | Temperatura | valor recebido dividido por 10 |

A temperatura é transmitida como um valor inteiro multiplicado por dez.

Exemplo:

```text
375 → 37,5 °C
```

## Estrutura do repositório

```text
codesys/   Projeto e documentação do CODESYS
data/      Arquivo CSV de exemplo
docs/      Documentação de engenharia
src/       Código-fonte da aplicação Python
tests/     Estrutura destinada aos testes automatizados
```

## Como executar

### Pré-requisitos

- CODESYS com runtime compatível;
- Python 3;
- biblioteca `pyModbusTCP`;
- comunicação de rede entre o runtime CODESYS e a aplicação Python.

### Instalação da dependência Python

```bash
pip install -r requirements.txt
```

### Configuração

No arquivo:

```text
src/app_machinesimulation.py
```

configure o endereço IP do CODESYS:

```python
IP_CODESYS = "192.168.1.100"
```

O endereço deve ser alterado conforme a rede utilizada.

### Execução

Com o CODESYS em modo RUN e o servidor Modbus TCP ativo:

```bash
python src/app_machinesimulation.py
```

Os dados serão exibidos no terminal e registrados em:

```text
data/machine_history.csv
```

## Exemplo de saída

```text
----------------------------------------
Máquina: Ligada
Produção: 10 peças
Temperatura: 34.0 °C
Alarme: Normal
```

## Exemplo de dados registrados

```csv
timestamp,machine_running,production_count,temperature_c,alarm_active
2026-07-29 10:48:38,Ligada,15,43.0,Normal
2026-07-29 10:48:39,Ligada,15,44.0,Normal
2026-07-29 10:48:40,Desligada,16,45.0,Ativo
```

## Documentação

- [Requisitos](docs/01-requirements.md)
- [Visão geral do sistema](docs/02-system-overview.md)
- [Arquitetura](docs/03-architecture.md)
- [Mapa de variáveis](docs/04-variable-map.md)
- [Plano de testes](docs/05-test-plan.md)
- [Resultados dos testes](docs/06-test-results.md)
- [Decisão sobre o protocolo](docs/07-decisions/ADR-001-communication-protocol.md)
- [Decisão sobre armazenamento](docs/07-decisions/ADR-002-data-storage.md)

## Status

Versão inicial concluída:

- [x] simulação da máquina no CODESYS;
- [x] interface de visualização;
- [x] comunicação Modbus TCP;
- [x] leitura em Python;
- [x] registro em CSV;
- [ ] gráficos históricos;
- [ ] dashboard;
- [ ] armazenamento em banco de dados;
- [ ] testes automatizados.

## Próximas evoluções

- geração de gráficos históricos;
- criação de dashboard em Python;
- utilização de SQLite;
- cálculo de indicadores da máquina;
- comunicação bidirecional entre Python e CODESYS;
- comparação entre Modbus TCP e OPC UA.

## Autor

Lucas Larrosa  
Engenheiro Mecatrônico | Analista de Automação Industrial  
Automação Industrial | Integração OT/IT | Python aplicado à indústria
