# Visão geral do sistema

## Objetivo

O objetivo deste projeto é demonstrar uma integração simples entre uma aplicação de automação industrial e uma aplicação de software.

A máquina é simulada no CODESYS. Seus dados são disponibilizados por Modbus TCP, lidos por uma aplicação Python e armazenados em um arquivo CSV.

## Problema abordado

Em ambientes industriais, frequentemente é necessário retirar dados do nível de controle e disponibilizá-los para sistemas de monitoramento, histórico, análise ou gestão.

Este projeto representa uma versão reduzida desse fluxo, utilizando uma máquina virtual e dados simulados.

## Componentes

### CODESYS Runtime

Responsável por:

- executar a lógica da máquina;
- simular produção e temperatura;
- controlar estados e alarmes;
- disponibilizar os dados pelo servidor Modbus TCP.

### Aplicação Python

Responsável por:

- atuar como cliente Modbus;
- ler os registradores do CODESYS;
- interpretar os dados;
- exibir o estado atual no terminal;
- registrar o histórico em CSV.

### Arquivo CSV

Responsável por:

- manter o histórico das leituras;
- registrar data e hora;
- permitir análises futuras;
- servir como entrada para gráficos e dashboards.

## Fluxo operacional

1. O operador inicia a máquina pela visualização do CODESYS.
2. A produção é incrementada a cada dois segundos.
3. A temperatura aumenta durante o funcionamento.
4. O CODESYS disponibiliza os valores em Input Registers.
5. A aplicação Python realiza a leitura a cada segundo.
6. Os valores são exibidos no terminal.
7. Os dados são adicionados ao arquivo CSV.
8. Ao atingir 45 °C, o alarme é ativado e a máquina para.
9. A temperatura começa a diminuir.
10. Ao atingir 40 °C ou menos, o alarme é liberado.

## Escopo atual

A versão atual contempla apenas a leitura dos dados do CODESYS pelo Python.

A escrita de comandos do Python para o CODESYS será avaliada em uma versão futura.
