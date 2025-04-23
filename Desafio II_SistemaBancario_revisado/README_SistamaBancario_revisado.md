
# 🏦 Sistema Bancário em Python — Versão Revisada

Este projeto é uma simulação de um sistema bancário simples, desenvolvido em Python, que permite ao usuário realizar operações como depósito, saque, visualização de extrato, cadastro de usuários e criação de contas bancárias.

---

## 🚀 Funcionalidades

- 📥 **Depósito**: Realiza depósitos no saldo da conta.
- 💸 **Saque**: Permite saques com controle de limite e número de operações por dia.
- 📄 **Extrato**: Exibe o histórico de movimentações e o saldo atual.
- 👤 **Cadastro de Usuário**: Registra novos usuários por CPF, nome, nascimento e endereço.
- 🏦 **Criação de Conta**: Gera uma conta bancária vinculada a um usuário existente.
- 📃 **Listagem de Contas**: Exibe todas as contas criadas com seus respectivos titulares.

---

## 🧱 Estrutura do Código

- `menu()` – Interface de texto para seleção de operações
- `depositar()` – Realiza e valida depósitos
- `sacar()` – Processa saques com verificação de saldo, limite e quantidade
- `exibir_extrato()` – Mostra extrato das movimentações
- `criar_usuario()` – Cadastra novo usuário
- `filtrar_usuario()` – Busca usuário existente pelo CPF
- `criar_conta()` – Cria nova conta atrelada a um usuário
- `listar_contas()` – Mostra todas as contas registradas
- `main()` – Loop principal com controle de fluxo do sistema

---

---

## ✍️ Autor

Desenvolvido como parte de um desafio de aprendizagem para praticar funções, controle de fluxo, listas e dicionários em Python.