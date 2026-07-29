# Resultados dos testes

## Resumo

| ID | Resultado | Evidência |
|---|---|---|
| CT-001 | Aprovado | Máquina iniciou desligada a 25 °C |
| CT-002 | Aprovado | Partida realizada pela IHM |
| CT-003 | Aprovado | Produção incrementada a cada dois segundos |
| CT-004 | Aprovado | Temperatura aumentou 1 °C por segundo |
| CT-005 | Aprovado | Parada manual interrompeu a produção |
| CT-006 | Aprovado | Temperatura reduziu 0,5 °C por segundo |
| CT-007 | Aprovado | Temperatura limitada a 25 °C |
| CT-008 | Aprovado | Alarme ativado em 45 °C |
| CT-009 | Aprovado | Máquina parou automaticamente |
| CT-010 | Aprovado | Produção permaneceu em 16 peças |
| CT-011 | Aprovado | Alarme liberado abaixo do limite de histerese |
| CT-012 | Aprovado | Registradores lidos pelo Python |
| CT-013 | Aprovado | Valor 400 interpretado como 40,0 °C |
| CT-014 | Aprovado | CSV recebeu leituras periódicas |
| CT-015 | Aprovado | Histórico preservado entre execuções |
| CT-016 | Pendente | Teste formal ainda não documentado |

## Evidência do alarme

Trecho do histórico:

```csv
2026-07-29 10:48:38,Ligada,15,43.0,Normal
2026-07-29 10:48:39,Ligada,15,44.0,Normal
2026-07-29 10:48:40,Desligada,16,45.0,Ativo
2026-07-29 10:48:41,Desligada,16,44.5,Ativo
