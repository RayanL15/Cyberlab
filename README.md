# CyberLab — primeiros passos em segurança no Windows

Uma trilha em português para quem está começando em segurança e já conhece
um pouco de lógica, Python ou C. As seis aulas apresentam proteção de dados,
identidade e permissões, validação de entradas, login, logs e recuperação de arquivos.

**Agora há uma área com 21 comandos básicos de CMD e PowerShell**, com busca,
filtro por assunto, explicações do resultado e três práticas com arquivos locais.

## Começar no Windows

1. No GitHub, use **Code → Download ZIP**.
2. Clique com o botão direito no ZIP e escolha **Extrair Tudo**.
3. Entre na pasta extraída.
4. Abra **index.html** no navegador para as aulas.
5. Clique em **Praticar comandos no Windows** para abrir a nova área.

As aulas e a área de comandos funcionam sem servidor, sem Python e sem pacotes.
A página apresenta exemplos: você copia e executa os comandos no seu terminal.
O arquivo **docs/guia-windows.md** reúne o material para consulta.

## Iniciar o servidor no Windows

Para usar também os desafios locais opcionais, instale **Python 3.10 ou superior**
em [python.org](https://www.python.org/downloads/). Reabra o terminal depois de instalar.
Nenhum pacote adicional é necessário.

O jeito mais simples é dar **dois cliques em iniciar.cmd**. Ele procura uma
instalação compatível do Python, inicia o servidor e abre o navegador.

### Pelo CMD

Na pasta extraída:

~~~bat
iniciar.cmd
~~~

Para entrar na pasta, use o caminho real, mantendo as aspas:

~~~bat
cd /d "C:\caminho\Cyberlab-main"
~~~

### Pelo PowerShell

Na pasta extraída:

~~~powershell
.\iniciar.cmd
~~~

Também existe o iniciador nativo:

~~~powershell
.\iniciar.ps1
~~~

Se a política de execução bloquear o arquivo .ps1, use .\iniciar.cmd ou
o comando direto abaixo. Não é necessário mudar a política para usar o laboratório.

### Executar diretamente com Python

Funciona no CMD e no PowerShell:

~~~text
py -3 lab.py --open
~~~

Se py não estiver disponível e python estiver configurado:

~~~text
python lab.py --open
~~~

Para conferir a versão, execute py -3 --version ou python --version.
Mantenha o terminal aberto e pressione **Ctrl+C** para encerrar o servidor.

## Endereços locais

Com o servidor rodando, abra no navegador:

- **http://127.0.0.1:8000** — seis aulas iniciais.
- **http://127.0.0.1:8000/windows** — comandos para CMD e PowerShell.
- **http://127.0.0.1:8000/avancado** — desafios opcionais de SQL, logs e Base64.

127.0.0.1 é o próprio computador. O servidor escuta apenas nesse endereço.
A área avançada contém falhas intencionais e dados fictícios para estudo local.
Pratique em sistemas de outras pessoas somente com autorização.

## O que praticar primeiro

1. **Pastas e arquivos:** cd, dir, mkdir, type e copy; no PowerShell,
   Get-Location, Get-ChildItem, New-Item, Get-Content e Copy-Item.
2. **Rede:** ipconfig, ping e nslookup. Depois observe a porta 8000 com netstat
   ou Get-NetTCPConnection e teste-a com Test-NetConnection.
3. **Sistema:** whoami e tasklist; no PowerShell, Get-Process.
4. **Segurança:** localizar eventos com findstr ou Select-String, comparar
   hashes com SHA256 e consultar permissões com icacls ou Get-Acl.

O arquivo exemplos/acessos.log contém os registros fictícios das práticas.
Uma tentativa que falhou não prova uma invasão. Copiar um arquivo para o mesmo
disco é só demonstração; um backup real também precisa proteger contra perda do aparelho.

## Arquivos do projeto

- **index.html:** seis aulas com exercícios e progresso no navegador.
- **comandos-windows.html:** referência interativa de comandos do Windows.
- **lab.py:** servidor local e desafios opcionais.
- **iniciar.cmd / iniciar.ps1:** iniciadores para Windows.
- **exemplos/acessos.log:** arquivo fictício para treinar leitura de logs.
- **docs/guia-windows.md:** guia de estudo com exemplos.

## Progresso

O navegador tenta salvar o progresso das seis aulas neste computador.
Se o armazenamento estiver bloqueado, elas continuam funcionando enquanto a
página estiver aberta. Não há conta nem sincronização entre dispositivos.

## Problemas comuns

- **Python não encontrado:** instale uma versão compatível, reabra o terminal
  e confira py -3 --version ou python --version.
- **Porta 8000 ocupada:** confira se outra janela já está rodando o CyberLab;
  encerre essa instância com Ctrl+C antes de abrir outra.
- **Arquivo não encontrado:** extraia o ZIP inteiro e confira a pasta atual
  com cd no CMD ou Get-Location no PowerShell.
- **A página não abriu automaticamente:** digite http://127.0.0.1:8000 no navegador.
- **Comando do Windows indisponível:** Get-NetIPConfiguration, Resolve-DnsName e
  Get-NetTCPConnection dependem de módulos do Windows; use ipconfig, nslookup
  e netstat como alternativas.

## Linux e macOS

As aulas continuam abrindo por index.html. Para o servidor:

~~~sh
python3 lab.py
~~~

Os exemplos da área Windows são específicos do Windows.

## Referências oficiais

- [Comandos do Windows](https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/windows-commands)
- [PowerShell](https://learn.microsoft.com/pt-br/powershell/)
- [Python no Windows](https://docs.python.org/3/using/windows.html)
