# Sistema de Conforto em Postos de Trabalho - Python

*Aluno:* Vitor reis, sofia, João verardo
*RM:* 562208- Vitor reis 
Rm: 563270- sofia
Rm: 563700- João verardo 
*Disciplina:* Computational Thinking with Python  
*Tema:* Future at Work  

## Descrição do Projeto

Este projeto implementa um sistema em Python para monitorar o conforto térmico em postos de trabalho (mesas, salas, estações).  
O usuário registra leituras de temperatura e umidade, e o programa indica se cada posto está em *conforto* ou *desconforto* com base em uma faixa configurável (20–27 °C).

Os dados são armazenados em memória e também em arquivo de texto, permitindo carregar e salvar leituras.

## Funcionalidades

- Registrar nova leitura (posto, temperatura, umidade)
- Listar todas as leituras registradas
- Remover uma leitura específica
- Calcular resumo de conforto:
  - total de leituras
  - temperatura média
  - quantidade de postos em conforto e desconforto
- Salvar leituras em arquivo (leituras_conforto.txt)
- Carregar leituras do arquivo na inicialização

## Como Executar

1. Certifique-se de ter o *Python 3* instalado.
2. Baixe o arquivo conforto_trabalho.py deste repositório.
3. No terminal, navegue até a pasta onde o arquivo está salvo.
4. Execute:

```bash
python conforto_trabalho.py
