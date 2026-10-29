# CyberLab — primeiros passos em segurança de software

Uma trilha de cibersegurança para quem conhece lógica e já escreveu um pouco de
Python ou C, mas ainda não estudou segurança. Os exemplos conectam conceitos de
segurança a condições, entradas de dados e registros de um programa.

**Abra `index.html` no navegador para começar. A trilha não exige instalação de pacotes nem servidor.**

## Executar

1. No GitHub, use **Code → Download ZIP**.
2. Extraia o ZIP e abra a pasta do projeto.
3. Abra **index.html** no navegador e comece pelo módulo 1.

Se você já baixou a versão anterior, baixe o ZIP novamente. Você também pode
usar seu checkout local atualizado e abrir o mesmo arquivo.

## O que você vai aprender

1. **O que proteger em um programa.** Confidencialidade é limitar quem pode ler
   informações; integridade é impedir alterações indevidas; disponibilidade é
   manter o serviço e os dados acessíveis quando necessários.
2. **Autenticação e autorização.** O login verifica quem você é; a permissão
   determina o que você pode fazer. O módulo também apresenta senhas exclusivas
   e a verificação em duas etapas, uma confirmação extra além da senha.
3. **Validar entradas.** Um exemplo em Python converte uma entrada com `int` e
   verifica o intervalo de 1 a 120. Um exemplo em C explica o limite de leitura
   com `fgets` em relação ao tamanho de um array. O objetivo é reconhecer dados
   inesperados e limites, sem exercícios de exploração.
4. **Observar um login fictício.** Compare uma tentativa com senha incorreta e
   outra com a senha fornecida, relacionando o resultado a uma condição em
   Python. A simulação ensina o fluxo de decisão; não é um modelo de
   autenticação para produção.
5. **Interpretar registros de um programa.** Leia um histórico simples de
   tentativas de entrada, conecte os eventos ao código Python e diferencie
   falhas de sucessos. Uma tentativa que falhou não prova uma invasão.
6. **Recuperar dados.** Entenda como cópias de segurança e testes de recuperação
   ajudam a manter a disponibilidade depois de uma falha.

Cada módulo explica o conceito antes do exercício. Você pode consultar dicas e
tentar novamente sem penalidade; as respostas incluem uma explicação.
Os dados e as credenciais apresentados são fictícios.

## Progresso

O navegador tenta salvar seu progresso neste computador. Se o armazenamento
estiver bloqueado, a trilha continua funcionando e mantém o progresso enquanto a
página estiver aberta. O progresso não é sincronizado entre navegadores ou
dispositivos. Não é necessário criar uma conta.

## Opcional: servir a página com Python

Se preferir usar um servidor local, o projeto requer apenas Python 3.10 ou
superior, sem pacotes adicionais. Na pasta do projeto, execute:

```sh
python3 lab.py
```

No Windows, você também pode usar `py lab.py`. Com o processo rodando, digite
`127.0.0.1:8000` no navegador do mesmo computador. Para encerrar, pressione
**Ctrl+C** no terminal.

## Para depois: exercícios de exploração

Os exercícios anteriores de SQL injection, análise de registros e Base64 ficam
em `127.0.0.1:8000/avancado` quando o servidor Python estiver rodando. Eles são
opcionais e podem ficar para depois da trilha inicial.

A área avançada contém falhas intencionais para estudo e usa dados fictícios.
O servidor escuta apenas no próprio computador; mantenha-o assim, sem publicá-lo
na Internet. Pratique em sistemas de outras pessoas somente com autorização.
