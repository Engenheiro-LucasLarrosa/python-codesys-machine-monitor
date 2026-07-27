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
