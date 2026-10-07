# 🖥️ Interface Gráfica com Python: Sistema de Notas

Projetos de interface gráfica desktop desenvolvidos com **Tkinter** e **Pandas**, com destaque para um sistema de notas escolares com login e controle de acesso por perfil.

## Funcionalidades

- **Tela de login** com validação de usuário e senha
- **Dois perfis de acesso:**
  - 👨‍🏫 **Professor**: vê todos os alunos, cadastra e exclui alunos
  - 🎓 **Aluno**: vê apenas as próprias notas
- **Cálculo automático** da média e da situação do aluno:
  - Média ≥ 7 → Aprovado
  - Média ≥ 5 → Em recuperação
  - Média < 5 → Reprovado
- **Persistência em Excel**: os dados são lidos e salvos em uma planilha `.xlsx` com Pandas
- Tabela com barra de rolagem usando `ttk.Treeview`

## Arquivos

| Arquivo | Descrição |
|---|---|
| `Estrutura de login.py` | Sistema de notas completo com login e perfis de acesso |
| `interface de sistema de notas.py` | Interface do sistema de notas |
| `programa de interface com a bliblioteca pandas.py.py` | Integração da interface com dados via Pandas |
| `desenvolvendo RAD na prática.py` | Exercício de desenvolvimento rápido de aplicações (RAD) |

## Tecnologias

Python · Tkinter · Pandas · OpenPyXL

## Como executar

```bash
pip install pandas openpyxl
python "Estrutura de login.py"
```

> Usuários de teste: `professor`, `aluno` e `aluno2` (senha `1234`). As credenciais são fixas no código, pois o projeto tem fins de estudo.

## Próximos passos

- Guardar usuários em banco de dados com senha criptografada
- Permitir edição de notas pela interface

---
Desenvolvido por **Mateus Fernandes**, estudante de Análise e Desenvolvimento de Sistemas.
