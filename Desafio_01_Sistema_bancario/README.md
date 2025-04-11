# 🏦 Desafio: Sistema Bancário em Python

Este projeto simula um **sistema bancário** simples com as operações básicas: saque, depósito, extrato e saída. Desenvolvido em Python, ele é executado via terminal/interprete de comandos, oferecendo uma interface interativa baseada em texto.

---

## 📋 Funcionalidades

- **Depósito**: Permite o depósito de valores positivos no saldo da conta.
- **Saque**: Permite até 3 saques diários com limite de R$ 500 por saque.
- **Extrato**: Mostra todas as movimentações (depósitos e saques) e o saldo atual.
- **Sair**: Encerra o programa.

---

## 💡 Lógica do sistema

- O sistema começa com saldo de R$ 100.
- Cada saque verifica se:
  - Há saldo suficiente.
  - O valor não ultrapassa o limite por saque.
  - O limite diário de saques não foi excedido.
- O extrato registra apenas transações bem-sucedidas.
- Mensagens são exibidas para todas as ações, incluindo falhas.

---

## ▶️ Como executar

1. Instale o Python 3 se ainda não tiver:
   - [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Salve o código como `banco.py` (ou outro nome .py).

3. No terminal, execute o arquivo.