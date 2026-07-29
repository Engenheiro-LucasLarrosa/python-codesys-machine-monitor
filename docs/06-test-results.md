# Plano de testes

## Objetivo

Validar o comportamento da máquina simulada, a comunicação Modbus TCP, a aplicação Python e o registro em CSV.

## Casos de teste

| ID | Teste | Procedimento | Resultado esperado |
|---|---|---|---|
| CT-001 | Estado inicial | Iniciar a aplicação com a máquina parada | Máquina desligada, temperatura em 25 °C e alarme normal |
| CT-002 | Partida | Acionar o botão Start | `MachineRunning` deve ficar verdadeiro |
| CT-003 | Produção | Manter a máquina ligada | Contador deve aumentar a cada dois segundos |
| CT-004 | Aquecimento | Manter a máquina ligada | Temperatura deve subir 1 °C por segundo |
| CT-005 | Parada manual | Acionar Stop | Máquina e produção devem parar |
| CT-006 | Resfriamento | Manter a máquina parada | Temperatura deve cair 0,5 °C por segundo |
| CT-007 | Limite mínimo | Manter a máquina parada | Temperatura não deve ficar abaixo de 25 °C |
| CT-008 | Alarme | Atingir 45 °C | Alarme deve ser ativado |
| CT-009 | Parada por alarme | Atingir 45 °C | Máquina deve parar automaticamente |
| CT-010 | Bloqueio da produção | Manter alarme ativo | Contador deve permanecer constante |
| CT-011 | Liberação do alarme | Reduzir temperatura até 40 °C | Alarme deve ser liberado |
| CT-012 | Leitura Modbus | Executar aplicação Python | Quatro registradores devem ser lidos |
| CT-013 | Conversão da temperatura | Comparar CODESYS e Python | Valores devem ser equivalentes |
| CT-014 | Registro CSV | Executar por alguns segundos | Arquivo deve receber uma linha por ciclo |
| CT-015 | Reinicialização | Executar novamente o Python | Novas linhas devem ser adicionadas sem apagar as anteriores |
| CT-016 | Falha de comunicação | Parar o runtime | Python deve informar falha de leitura |
