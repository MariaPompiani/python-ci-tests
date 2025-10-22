# Projeto de Testes Unitários com CI

Este repositório demonstra um pipeline de Integração Contínua (CI) para uma aplicação Python simples usando GitHub Actions e Pytest.

## Workflow: `tests.yml`

O fluxo de trabalho (`.github/workflows/tests.yml`) é acionado a cada `push` ou `pull_request` e executa os seguintes passos:

1.  **Checkout**: Baixa o código do repositório.
2.  **Setup Python**: Configura o ambiente com a versão 3.11 do Python.
3.  **Cache**: Restaura as dependências do cache para acelerar a instalação.
4.  **Install Dependencies**: Instala as bibliotecas listadas no `requirements.txt`.
5.  **Run Tests**: Executa os testes unitários com `pytest` e gera um relatório de cobertura de código.
6.  **Upload Artifact**: Salva o relatório de cobertura (`coverage.xml`) como um artefato, permitindo a análise posterior da qualidade dos testes.
