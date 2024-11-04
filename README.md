# Sistema de Controle de Biblioteca

Um sistema para gerenciar o acervo de uma biblioteca, ideal para controle de empréstimos e devoluções de livros.

## Funcionalidades
- **Cadastro de Livros, Autores e Categorias**: Mantenha o registro dos livros com status de disponibilidade.
- **Controle de Usuários e Empréstimos**: Registre empréstimos e devoluções de livros por usuários cadastrados.
- **Lembrete de Devolução**: Envia automaticamente um lembrete por e-mail para devolução.
- **Relatório de Livros Mais Emprestados**: Gere relatórios dos livros mais populares.

## Pré-requisitos
- Python 3.x
- Redis
- Django

### Configuração do Redis (Windows)
Redis precisa estar configurado para executar o Celery no gerenciamento de tarefas assíncronas. [Instruções para instalação no Windows](https://github.com/microsoftarchive/redis/releases).

# Library Management System

A system to manage a library's collection, ideal for tracking book loans and returns.

## Features
- **Book, Author, and Category Registration**: Keep records of books with availability status.
- **User and Loan Management**: Register book loans and returns for registered users.
- **Return Reminder**: Automatically sends an email reminder for overdue returns.
- **Most Borrowed Books Report**: Generates reports of the most popular books.

## Requirements
- Python 3.x
- Redis
- Django

### Redis Setup (Windows)
Redis is required to run Celery for asynchronous task management. [Instructions for installing on Windows](https://github.com/microsoftarchive/redis/releases).

