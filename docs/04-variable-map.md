# Mapa de variáveis e registradores

## Variáveis de processo

| Variável | Tipo | Unidade | Descrição |
|---|---|---|---|
| `MachineRunning` | `BOOL` | — | Estado da máquina |
| `AlarmActive` | `BOOL` | — | Estado do alarme |
| `ProductionCount` | `INT` | peças | Produção acumulada |
| `Temperature` | `REAL` | °C | Temperatura simulada |

## Variáveis auxiliares Modbus

| Variável | Tipo | Origem | Conversão |
|---|---|---|---|
| `MB_MachineRunning` | `WORD` | `MachineRunning` | `FALSE = 0`, `TRUE = 1` |
| `MB_AlarmActive` | `WORD` | `AlarmActive` | `FALSE = 0`, `TRUE = 1` |
| `MB_ProductionCount` | `WORD` | `ProductionCount` | `INT_TO_WORD` |
| `MB_Temperature_x10` | `WORD` | `Temperature` | temperatura × 10 |

## Mapeamento dos Input Registers

| Endereço lógico | Canal CODESYS | Variável | Descrição |
|---:|---|---|---|
| 0 | `Outputs[0]` | `MB_MachineRunning` | Estado da máquina |
| 1 | `Outputs[1]` | `MB_AlarmActive` | Estado do alarme |
| 2 | `Outputs[2]` | `MB_ProductionCount` | Produção acumulada |
| 3 | `Outputs[3]` | `MB_Temperature_x10` | Temperatura multiplicada por 10 |

## Correspondência no Python

```python
registers = client.read_input_registers(0, 4)

machine_running = bool(registers[0])
alarm_active = bool(registers[1])
production_count = registers[2]
temperature = registers[3] / 10.0
