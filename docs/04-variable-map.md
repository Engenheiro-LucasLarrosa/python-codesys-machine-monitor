| Variável          | Tipo no CODESYS | Modbus             | Unidade | Descrição            |
| ----------------- | --------------- | ------------------ | ------- | -------------------- |
| `MachineRunning`  | `BOOL`          | Coil 0             | —       | Estado da máquina    |
| `AlarmActive`     | `BOOL`          | Coil 1             | —       | Estado do alarme     |
| `ProductionCount` | `INT`           | Holding Register 0 | peças   | Produção acumulada   |
| `Temperature`     | `REAL`          | Registers 1–2      | °C      | Temperatura simulada |
