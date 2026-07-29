# ADR-002 — Utilização de CSV para armazenamento inicial

## Status

Aceito

## Contexto

O projeto precisa registrar o histórico das variáveis lidas do CODESYS.

A primeira versão deve utilizar uma solução simples, de fácil inspeção e que não exija infraestrutura adicional.

## Decisão

Utilizar um arquivo CSV como mecanismo inicial de armazenamento.

## Motivos

- implementação simples;
- não exige servidor ou banco de dados;
- pode ser aberto em editores de texto e planilhas;
- facilita a validação dos dados;
- pode ser utilizado posteriormente por bibliotecas de análise;
- adequado ao volume de dados desta simulação.

## Estrutura registrada

- data e hora;
- estado da máquina;
- contador de produção;
- temperatura;
- estado do alarme.

## Consequências positivas

- rápida implementação;
- facilidade de auditoria;
- portabilidade;
- baixo custo de manutenção;
- integração simples com Python.

## Limitações

- baixa eficiência para grandes volumes;
- ausência de consultas estruturadas;
- risco de crescimento excessivo do arquivo;
- ausência de controle de concorrência;
- ausência de relacionamentos entre dados.

## Alternativas consideradas

### SQLite

Oferece consultas SQL e melhor organização, mas não era necessário para a primeira versão.

### Banco de dados externo

Seria desproporcional ao escopo inicial e exigiria configuração adicional.

## Evolução futura

Migrar o armazenamento para SQLite e manter o CSV apenas como formato de exportação.
