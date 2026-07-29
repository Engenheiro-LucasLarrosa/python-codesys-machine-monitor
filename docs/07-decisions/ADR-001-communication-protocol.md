# ADR-001 — Utilização de Modbus TCP

## Status

Aceito

## Contexto

O projeto precisa transmitir variáveis do CODESYS para uma aplicação Python.

## Decisão

Utilizar Modbus TCP na primeira versão.

## Motivos

- protocolo amplamente utilizado na automação;
- configuração relativamente simples;
- disponibilidade de bibliotecas Python;
- adequado ao escopo inicial.

## Consequências

- valores REAL exigem atenção à ordem dos registradores;
- não possui modelagem de informação tão rica quanto OPC UA;
- poderá ser substituído por OPC UA em uma versão futura.

## Alternativas consideradas

### OPC UA

Oferece uma modelagem de informação mais rica e recursos mais modernos, porém aumentaria a complexidade da primeira versão.

### MQTT

Seria adequado para publicação de dados, mas exigiria a utilização de um broker e uma arquitetura diferente.

## Resultado

A decisão foi validada por meio da leitura bem-sucedida de quatro Input Registers pela aplicação Python.
