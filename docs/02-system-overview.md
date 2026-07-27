# Visão Geral do Sistema

- Esse sistema irá gerar um arquivo CSV atravéz dos dados enviados por um runtime virtual do codesys em unidade de engenharia. Esses dados podem ser utilizados como log para gerar relatórios ou pra fazer análise comportamental da máquina simulada.
- O sistema consiste em um CLP virtual (Codesys) e um programa desenvolvido em Python atravéz da plataforma VS code.
- A comunicação entre o Codesys e o Python é feita com a utilização do protocolo Modbus TCP.
- O escopo do projeto será dividido entre o desenvolvimento da simulação de uma máquina industrial com variação de valores de algumas variaveis desenvolvida em texto estruturado e ladder, configuração da omunicação via Modbus TCP programada em Python pelo VS code e geração de arquivo CSV também atravès de programação em Python pelo VS code.
