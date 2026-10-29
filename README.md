# CyberLab — primeiros passos em cibersegurança

Laboratório em português para iniciantes, com três desafios, dicas e validação
de respostas. É uma aplicação pequena em Python, inspirada no formato de CTF.

## O que você vai praticar

1. **SQL injection:** explorar uma falha proposital no formulário de login.
2. **Análise de logs:** identificar um acesso suspeito em registros fictícios.
3. **Base64:** entender por que codificar uma informação não é criptografá-la.

Uma **flag** é a resposta de um desafio, no formato `LAB{alguma_coisa}`.
Ao encontrá-la, digite no campo da missão e clique em **Validar flag**.
O progresso fica salvo no navegador usado para estudar.

## Primeiro: baixar os arquivos

1. Na página deste repositório no GitHub, clique no botão **Code**.
2. Clique em **Download ZIP**.
3. Extraia o ZIP. No Windows, clique com o botão direito e escolha **Extrair tudo**.
4. Abra a pasta extraída que contém o arquivo `lab.py`.

O GitHub guarda os arquivos. Para abrir os desafios, execute o programa no seu
computador seguindo os passos abaixo.

## No Windows

1. Instale o Python pelo site oficial: https://www.python.org/downloads/ .
   Se o instalador mostrar a opção **Add Python to PATH**, marque-a.
2. Na pasta que contém `lab.py`, clique na barra de endereço do Explorador de
   Arquivos, digite `powershell` e pressione Enter. Isso abre uma janela para
   digitar comandos nessa pasta.
3. Digite o comando abaixo e pressione Enter:

```powershell
py lab.py
```

Se `py` não for reconhecido, tente `python lab.py`. Se nenhum dos dois funcionar,
conclua a instalação do Python e abra uma nova janela do PowerShell.

## No macOS ou Linux

Use Python 3.10 ou superior. No Terminal, entre na pasta extraída usando `cd`
seguido do caminho da pasta e execute:

```sh
python3 lab.py
```

## Abrir os desafios

Com o programa rodando, abra seu navegador **no mesmo computador** e digite
`127.0.0.1:8000` na barra de endereço. Esse endereço aponta para seu próprio
computador. Mantenha a janela do terminal aberta enquanto pratica.

Comece pela missão 01. Leia o objetivo, teste o formulário e abra as dicas se
precisar. Para encerrar o laboratório, volte ao terminal e pressione **Ctrl+C**.

Se aparecer que a porta 8000 já está em uso, confira se você já iniciou o
laboratório em outra janela. Se o navegador não abrir a página, veja se o
terminal mostrou algum erro e se você está acessando pelo mesmo computador.

## Como o laboratório funciona

- Requer somente Python 3.10 ou superior, sem instalação de pacotes adicionais.
- O servidor escuta apenas em `127.0.0.1:8000`.
- O banco SQLite é descartável e recriado em memória a cada tentativa de login.
- Os registros, endereços IP, senhas e segredos dos desafios são fictícios.
- A aplicação tem uma vulnerabilidade SQL proposital. Mantenha-a local e não
  publique o servidor na Internet. Pratique apenas em sistemas autorizados.
- As soluções estão no código para permitir auditoria. Para aprender, tente
  resolver os desafios pelo painel antes de ler `lab.py`.

Este projeto é uma primeira trilha local, sem contas de usuário ou VPN.
O ambiente de onboarding na nuvem não oferece prévia web deste laboratório.
