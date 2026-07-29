# Requisitos do sistema

## Requisitos funcionais

| ID | Requisito | Status |
|---|---|---|
| RF-001 | Permitir ligar a máquina simulada. | Implementado |
| RF-002 | Permitir parar a máquina simulada. | Implementado |
| RF-003 | Permitir zerar o contador de produção. | Implementado |
| RF-004 | Incrementar a produção a cada dois segundos durante o funcionamento. | Implementado |
| RF-005 | Aumentar a temperatura durante o funcionamento. | Implementado |
| RF-006 | Reduzir a temperatura com a máquina parada. | Implementado |
| RF-007 | Ativar um alarme ao atingir 45 °C. | Implementado |
| RF-008 | Parar a máquina automaticamente quando o alarme for ativado. | Implementado |
| RF-009 | Liberar o alarme quando a temperatura atingir 40 °C ou menos. | Implementado |
| RF-010 | Disponibilizar as variáveis por Modbus TCP. | Implementado |
| RF-011 | Ler os dados do CODESYS por meio de uma aplicação Python. | Implementado |
| RF-012 | Exibir os dados no terminal. | Implementado |
| RF-013 | Registrar os dados em arquivo CSV. | Implementado |

## Requisitos não funcionais

| ID | Requisito | Status |
|---|---|---|
| RNF-001 | Separar a aplicação Python em módulos com responsabilidades distintas. | Implementado |
| RNF-002 | Utilizar nomes de variáveis compreensíveis. | Implementado |
| RNF-003 | Apresentar mensagens compreensíveis em caso de falha de leitura. | Implementado |
| RNF-004 | Preservar o histórico existente ao reiniciar a aplicação. | Implementado |
| RNF-005 | Não utilizar dados ou códigos confidenciais de clientes. | Implementado |
| RNF-006 | Documentar arquitetura, mapeamento e testes do sistema. | Em andamento |
| RNF-007 | Permitir alteração do endereço IP conforme o ambiente. | Implementado |

## Fora do escopo da versão atual

- controle da máquina pelo Python;
- autenticação de usuários;
- criptografia da comunicação;
- armazenamento em banco de dados;
- dashboard em tempo real;
- cálculo de OEE;
- aplicação em equipamento físico.
