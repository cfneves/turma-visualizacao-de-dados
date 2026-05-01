# Guia de Contribuição

Bem-vindo! Este guia explica como enviar seus trabalhos corretamente e manter o repositório organizado.

---

## Índice

1. [Configuração inicial](#1-configuração-inicial)
2. [Criando sua pasta de aluno](#2-criando-sua-pasta-de-aluno)
3. [Fluxo de entrega](#3-fluxo-de-entrega)
4. [Convenção de commits](#4-convenção-de-commits)
5. [Abrindo um Pull Request](#5-abrindo-um-pull-request)
6. [Resolvendo conflitos](#6-resolvendo-conflitos)
7. [Boas práticas em notebooks](#7-boas-práticas-em-notebooks)

---

## 1. Configuração Inicial

Faça isso **uma única vez** no início do curso.

```bash
# Fork o repositório pelo GitHub (botão "Fork" no canto superior direito)

# Clone o SEU fork (substitua SEU_USUARIO)
git clone https://github.com/SEU_USUARIO/turma-visualizacao-de-dados.git
cd turma-visualizacao-de-dados

# Adicione o repositório original como "upstream"
git remote add upstream https://github.com/cfneves/turma-visualizacao-de-dados.git

# Confirme que os dois remotes estão configurados
git remote -v
# origin    https://github.com/SEU_USUARIO/turma-visualizacao-de-dados.git (fetch)
# upstream  https://github.com/cfneves/turma-visualizacao-de-dados.git (fetch)
```

---

## 2. Criando sua Pasta de Aluno

Crie **uma única vez** sua pasta dentro de `alunos/`:

```
alunos/
└── nome-sobrenome/         ← minúsculas, sem espaços, use _
    ├── README.md           ← seu portfólio (use o template!)
    ├── exercicios/         ← uma pasta por exercício
    │   ├── exercicio_01/
    │   └── exercicio_02/
    └── projetos/           ← seus projetos autorais
        └── projeto_01/
```

**Copie o template de portfólio:**

```bash
cp alunos/TEMPLATE_README.md alunos/seu-nome/README.md
```

Edite o `README.md` com suas informações reais — esse arquivo é o seu cartão de visitas.

---

## 3. Fluxo de Entrega

Para **cada entrega** (exercício ou projeto), siga este fluxo:

```bash
# Passo 1: Sincronize com o repositório original
git fetch upstream
git checkout main          # ou master, conforme seu fork
git merge upstream/main

# Passo 2: Crie uma branch para esta entrega
git checkout -b feat/exercicio-01-seu-nome

# Passo 3: Adicione seus arquivos na sua pasta
# (nunca modifique arquivos fora de alunos/seu-nome/)

# Passo 4: Commit
git add alunos/seu-nome/
git commit -m "feat(alunos): adiciona exercício 01 - Seu Nome"

# Passo 5: Push para o seu fork
git push origin feat/exercicio-01-seu-nome

# Passo 6: Abra o Pull Request no GitHub
```

---

## 4. Convenção de Commits

Use o padrão **Conventional Commits**:

```
tipo(escopo): descrição curta em português
```

| Tipo | Quando usar |
|------|-------------|
| `feat` | Nova entrega, exercício ou projeto |
| `fix` | Correção de algo já enviado |
| `docs` | Atualização de README ou documentação |
| `data` | Adição ou atualização de dataset |
| `style` | Formatação, sem mudança de lógica |

**Exemplos:**

```bash
git commit -m "feat(alunos): adiciona exercício 02 - Ana Paula"
git commit -m "fix(alunos): corrige gráfico do exercício 01 - João Silva"
git commit -m "docs(alunos): atualiza portfólio com projeto final - Maria"
git commit -m "data: adiciona dataset vendas_2024.csv"
```

---

## 5. Abrindo um Pull Request

1. Acesse seu fork no GitHub
2. Clique em **"Compare & pull request"** (aparece automaticamente após o push)
3. Verifique que a base é `cfneves/turma-visualizacao-de-dados` → `main`
4. Preencha o template do PR (título + checklist)
5. Clique em **"Create pull request"**

**Título sugerido:**

```
feat(alunos): adiciona [exercício/projeto] - Seu Nome
```

---

## 6. Resolvendo Conflitos

Conflitos acontecem quando outro aluno enviou arquivos depois que você criou o fork. É normal — não é erro seu.

```bash
# 1. Traga as atualizações do repositório original
git fetch upstream

# 2. Vá para sua branch principal
git checkout main

# 3. Integre as mudanças
git merge upstream/main

# 4. Volte para a branch da sua entrega
git checkout feat/seu-exercicio

# 5. Aplique as mudanças do main na sua branch
git rebase main
```

Se aparecer um conflito num arquivo de outro aluno (ex: `alunos/maria_helena/README.md`):

```bash
# Abra o arquivo conflitado e remova os marcadores:
# <<<<<<< HEAD
# (versão do upstream — MANTENHA ESTA)
# =======
# (versão do seu fork — REMOVA ESTA PARTE)
# >>>>>>> sua-branch

# Após resolver:
git add alunos/nome-do-colega/README.md
git rebase --continue

# Atualize seu fork remoto
git push origin feat/seu-exercicio --force-with-lease
```

**Regra de ouro:** em conflito com arquivo de outro aluno, **sempre mantenha a versão do upstream** (a versão do repositório original).

---

## 7. Boas Práticas em Notebooks

- Reinicie o kernel e execute todas as células (`Kernel > Restart & Run All`) antes de commitar
- Sem erros de execução — células com erro **bloqueiam o PR**
- Adicione um título (`# Exercício 01 — Nome`) na primeira célula
- Documente o que cada seção faz com células Markdown
- Dados sensíveis (senhas, tokens) nunca no notebook — use variáveis de ambiente

---

Dúvidas? Abra uma **[Issue](https://github.com/cfneves/turma-visualizacao-de-dados/issues)** com `[dúvida]` no título.
