"""
Projeto: Sistema de Monitoramento de Conforto em Postos de Trabalho
Tema: Future at Work - Conforto térmico em ambientes de trabalho

Aluno: Vitor Reis, Sofia, Joao verardo 
RM: 562208- Vitor 
Rm: 563270 - sofia 
Rm: 563700- João verardo
Disciplina: Computational Thinking with Python

Descrição geral:
Este programa permite registrar leituras de temperatura e umidade
de diferentes postos de trabalho (mesas/salas) e analisar se estão
em faixa de conforto térmico. Os dados são armazenados em memória
(usando listas e dicionários) e também em arquivo de texto.

Requisitos atendidos:
- Variáveis, tipos básicos, if/elif/else, while, for
- Listas e strings
- Funções com parâmetros e retorno
- Estruturas de dados: listas e dicionários
- Manipulação de arquivos (leitura e escrita)
- Tratamento de exceções
"""

# -----------------------------
# CONFIGURAÇÕES DO SISTEMA
# -----------------------------

FAIXA_CONFORTO_MIN = 20.0  # temperatura mínima de conforto (°C)
FAIXA_CONFORTO_MAX = 27.0  # temperatura máxima de conforto (°C)
ARQUIVO_DADOS = "leituras_conforto.txt"

# Estrutura de dados principal:
# Uma lista de dicionários, cada dicionário representa uma leitura.
leituras = []  # exemplo de item: {"posto": "Mesa 1", "temp": 24.5, "umid": 50.0}


# -----------------------------
# FUNÇÕES AUXILIARES
# -----------------------------

def eh_confortavel(temperatura: float) -> bool:
    """
    Retorna True se a temperatura estiver dentro da faixa de conforto.
    Exemplo de uso da estrutura de decisão if/else.
    """
    return FAIXA_CONFORTO_MIN <= temperatura <= FAIXA_CONFORTO_MAX


def formatar_leitura(leitura: dict) -> str:
    """
    Recebe um dicionário com os dados da leitura e devolve
    uma string formatada para exibição na tela.
    Usa manipulação de strings.
    """
    posto = leitura["posto"]
