# Sistema de Login - Versão Executável

Bem-vindo à versão portátil do Sistema de Login. Este aplicativo foi compilado para facilitar o uso imediato, eliminando a necessidade de configurações de ambiente.

---

## Instruções de Uso

### 1. Inicialização
* Execute o arquivo `SistemaLogin.exe`.
* **Nota:** O software é totalmente portátil (não requer instalação, Python ou dependências externas). Funciona em qualquer diretório.

### 2. Primeiro Acesso (Cadastro)
Ao executar o sistema pela primeira vez, o banco de dados local será criado automaticamente.
1.  Clique no botão **"Não tem uma conta? Bora criar!"**.
2.  Preencha os campos solicitados: *Nome*, *Email* e *Senha*.
3.  Clique em **"Enviar"**.

### 3. Realizando Login
1.  Insira suas credenciais (Email e Senha) cadastradas anteriormente.
2.  Clique em **"Login"**.

### 4. Armazenamento de Dados
* Seus dados são salvos localmente em um arquivo gerado automaticamente chamado `users.txt`.
* O sistema verifica a existência deste arquivo a cada execução para validar o login.

---

## Informações Importantes & Segurança

> **Aviso de Antivírus:** Ao executar o arquivo `.exe`, o Windows ou seu antivírus pode exibir um alerta de segurança (como o *Windows SmartScreen*).
>
> * **Motivo:** Isso é um comportamento padrão para executáveis criados via *PyInstaller* que não possuem uma assinatura digital corporativa paga.
> * **Ação:** O arquivo é seguro e gerado diretamente do código-fonte. Você pode permitir a execução com segurança.

### Gerenciamento de Dados
* **Limpeza:** Caso deseje resetar o sistema ou apagar todos os usuários, basta excluir o arquivo `users.txt` da pasta onde o executável está localizado. Um novo arquivo será criado na próxima execução.

---

## Requisitos do Sistema

* **Sistema Operacional:** Windows 7, 8, 10 ou 11 (32 ou 64 bits).
* **Dependências:** Nenhuma (O interpretador Python já está embutido no executável).

---

## Como Compartilhar

Para distribuir este software para amigos ou colegas:

1.  Envie o arquivo `SistemaLogin.exe`.
2.  Recomenda-se enviar este arquivo de instruções (`README.md` ou `README.txt`) junto.

### Nota sobre Compartilhamento de Dados
O banco de dados (`users.txt`) é local.
* **Cenário A:** Se você enviar apenas o `.exe` para um amigo, ele criará o próprio banco de dados vazio no computador dele.
* **Cenário B:** Se você enviar o `.exe` **E** o seu arquivo `users.txt`, o seu amigo terá acesso às contas que você criou.

---

## Stack Tecnológico

Este software foi desenvolvido utilizando:
* **Linguagem:** Python 3.x
* **Interface (GUI):** Kivy Framework
* **Compilação:** PyInstaller
