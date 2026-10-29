# CyberLab no Windows

Guia básico de comandos e segurança para iniciantes

Este guia acompanha o repositório RayanL15/Cyberlab. Comece por entender as pastas e os arquivos; depois observe a rede, os processos e os registros. Os exemplos usam CMD e PowerShell no Windows 10 ou 11.

## O que aprender primeiro

| Conceito | O que significa | Exemplo no CyberLab |
| --- | --- | --- |
| Confidencialidade | Limitar quem pode ler os dados. | Consultar permissões de um arquivo. |
| Integridade | Evitar ou identificar alterações indevidas. | Comparar o hash antes e depois de editar. |
| Disponibilidade | Manter dados e serviços acessíveis. | Iniciar o servidor e recuperar cópias. |
| Autenticação e autorização | Conferir identidade e definir permissões. | Diferenciar entrar na conta de poder alterar dados. |
| Validação de entradas | Conferir tipo, tamanho e regras do dado. | Aceitar uma idade somente de 1 a 120. |
| Logs e backups | Registrar eventos e permitir recuperação. | Ler tentativas de login e restaurar um arquivo. |

## CMD e PowerShell

O **terminal** é a janela em que você escreve. **CMD** e **PowerShell** interpretam os comandos. O Windows Terminal pode abrir abas dos dois.

O CMD usa comandos como `dir` e `type`. O PowerShell usa comandos como `Get-ChildItem` e `Get-Content`; seus comandos podem retornar objetos com propriedades, como nome e identificador de processo.

| Detalhe | CMD | PowerShell |
| --- | --- | --- |
| Pasta temporária do usuário | `%TEMP%` | `$env:TEMP` |
| Executar arquivo na pasta atual | `iniciar.cmd` | `.\iniciar.cmd` |
| Consultar ajuda | `dir /?` | `Get-Help Get-ChildItem` |

Abra o menu Iniciar e procure Prompt de Comando ou PowerShell. Use uma linha por vez e confira a pasta atual. **Ctrl+C** interrompe o comando em execução; **Tab** ajuda a completar nomes.

<!-- page -->
## Pastas e arquivos

Um caminho informa onde um arquivo está. `C:\pasta\nota.txt` é um caminho completo. `.\nota.txt` aponta para um arquivo na pasta atual; `..` representa a pasta acima. Use aspas em caminhos com espaços.

| Objetivo | CMD | PowerShell |
| --- | --- | --- |
| Ver a pasta atual | `cd` | `Get-Location` |
| Listar o conteúdo | `dir` | `Get-ChildItem` |
| Entrar em uma pasta | `cd /d "C:\minha pasta"` | `Set-Location "C:\minha pasta"` |
| Voltar uma pasta | `cd ..` | `Set-Location ..` |
| Criar uma pasta | `mkdir treino` | `New-Item -ItemType Directory treino` |
| Ler um arquivo | `type nota.txt` | `Get-Content .\nota.txt` |
| Copiar um arquivo | `copy nota.txt copia.txt` | `Copy-Item .\nota.txt .\copia.txt` |
| Renomear a cópia | `ren copia.txt novo.txt` | `Rename-Item .\copia.txt novo.txt` |
| Remover só a cópia | `del novo.txt` | `Remove-Item .\novo.txt -Confirm` |

No CMD, `/d` permite trocar de unidade junto com a pasta. As opções do CMD e os parâmetros do PowerShell têm sintaxes próprias, mesmo quando existem comandos com nomes parecidos.

## Prática de arquivos

Escolha **um** dos blocos. Ele cria uma pasta de treino nos arquivos temporários do seu usuário, escreve uma nota e faz uma cópia.

**CMD**
```bat
cd /d "%TEMP%"
mkdir CyberLab-Treino
cd CyberLab-Treino
echo Meu primeiro teste> nota.txt
type nota.txt
copy nota.txt copia.txt
```

**PowerShell**
```powershell
Set-Location $env:TEMP
New-Item -ItemType Directory .\CyberLab-Treino -Force
Set-Location .\CyberLab-Treino
Set-Content .\nota.txt "Meu primeiro teste" -Encoding UTF8
Get-Content .\nota.txt
Copy-Item .\nota.txt .\copia.txt
```

**Confira:** os dois arquivos devem existir e ter o mesmo conteúdo. Se a pasta já existir, use-a. `>` e `Set-Content` substituem o conteúdo anterior. Excluir pelo terminal normalmente não envia para a Lixeira; pratique apenas nos arquivos descartáveis.

<!-- page -->
## Rede e programas em execução

**IP** é um endereço de uma interface na rede. **Gateway** é a saída para outras redes, normalmente seu roteador. **DNS** consulta endereços associados a nomes. **Porta** identifica um ponto de comunicação de um serviço; o CyberLab usa a 8000.

| Objetivo | CMD | PowerShell |
| --- | --- | --- |
| Ver IP e gateway | `ipconfig` | `Get-NetIPConfiguration` |
| Testar o próprio computador | `ping -n 4 127.0.0.1` | `ping.exe -n 4 127.0.0.1` |
| Consultar DNS | `nslookup example.com` | `Resolve-DnsName example.com` |
| Ver conexões e PIDs | `netstat -ano` | `Get-NetTCPConnection` |
| Ver processos | `tasklist` | `Get-Process` |
| Ver a conta da sessão | `whoami` | `whoami.exe` |

**PID** é o identificador de um processo. Ele permite relacionar uma conexão ao programa que a utiliza. Uma conexão existente ou um nome desconhecido, isoladamente, não prova um problema de segurança.

## Confira o servidor do CyberLab

Inicie o laboratório conforme a página 5. Deixe o primeiro terminal aberto e faça a consulta em outro terminal.

**CMD**
```bat
netstat -ano | findstr ":8000"
curl.exe -i http://127.0.0.1:8000/artifacts/access.log
```

Procure uma linha com `127.0.0.1:8000` e estado `LISTENING`. O filtro de texto pode mostrar outras linhas que contenham 8000; leia a coluna do endereço local. Na consulta HTTP, `200 OK` indica que a rota respondeu.

**PowerShell**
```powershell
Get-NetTCPConnection -LocalPort 8000 -State Listen
Test-NetConnection 127.0.0.1 -Port 8000
```

`TcpTestSucceeded : True` significa que a conexão TCP funcionou. Isso não verifica o conteúdo da página. `127.0.0.1` é o próprio computador; esse teste não precisa da Internet.

O `ping` verifica resposta ICMP, sem testar uma porta HTTP. Uma resposta não garante que um site está funcionando; uma falha também pode ser causada por bloqueio de ICMP. A consulta DNS depende do acesso ao servidor DNS.

Se um comando de rede do PowerShell não estiver disponível, use `ipconfig`, `nslookup` ou `netstat`, que também podem ser executados nele. `curl.exe` evita a confusão com o apelido `curl` de algumas versões do PowerShell.

<!-- page -->
## Logs integridade e permissões

Um **log** registra acontecimentos. No CyberLab, cada linha fictícia informa horário, IP, ação e resultado. Os horários terminados em `Z` estão em UTC. No exercício de login, `401` representa uma tentativa recusada e `200`, uma resposta bem-sucedida.

Na **pasta do projeto**, procure tentativas recusadas no arquivo que acompanha o laboratório.

**CMD**
```bat
findstr /n /c:"status=401" .\exemplos\acessos.log
```

**PowerShell**
```powershell
Select-String -Path .\exemplos\acessos.log -Pattern "status=401" -SimpleMatch
```

**Resultado esperado:** três linhas. O mesmo IP aparece depois com sucesso e download de backup. Isso merece investigação; os registros sozinhos não identificam a pessoa nem provam uma invasão.

## Ver uma alteração pelo hash

Um **hash** é um resumo calculado a partir do conteúdo. SHA256 é o algoritmo usado aqui. Ele ajuda a comparar versões e verificar integridade; não cifra os dados nem garante que o arquivo seja confiável.

Volte à pasta da prática de arquivos da página 2. Calcule o hash, acrescente uma linha e compare novamente.

**CMD**
```bat
certutil -hashfile nota.txt SHA256
echo Segunda linha>> nota.txt
certutil -hashfile nota.txt SHA256
certutil -hashfile copia.txt SHA256
```

**PowerShell**
```powershell
Get-FileHash .\nota.txt -Algorithm SHA256
Add-Content .\nota.txt "Segunda linha" -Encoding UTF8
Get-FileHash .\nota.txt -Algorithm SHA256
Get-FileHash .\copia.txt -Algorithm SHA256
```

**Confira:** o hash da nota muda e o da cópia continua com o valor anterior. Compare os valores dentro do mesmo exercício: diferentes codificações de texto podem produzir hashes diferentes entre CMD e PowerShell.

Para **consultar permissões** sem alterá-las, use `icacls nota.txt` no CMD ou `Get-Acl .\nota.txt | Format-List` no PowerShell. A permissão efetiva também depende de grupos e regras herdadas.

**Backup:** copie o arquivo antes de editar e teste a restauração. A cópia no mesmo disco é apenas uma demonstração; para proteger contra perda do aparelho, mantenha outra cópia em local separado.

<!-- page -->
## Como usar o CyberLab no Windows

No GitHub, escolha **Code → Download ZIP**, extraia tudo e abra a pasta extraída. Para as seis aulas e a referência de comandos, basta abrir `index.html` no navegador. Essas páginas não exigem Python.

Para os desafios que usam o servidor, instale **Python 3.10 ou superior** em https://www.python.org/downloads/ e reabra o terminal. Não é preciso instalar pacotes adicionais.

## Iniciar pelo CMD

Troque o caminho de exemplo pelo da pasta extraída.

```bat
cd /d "C:\caminho\Cyberlab-main"
iniciar.cmd
```

Você também pode dar dois cliques em `iniciar.cmd`. O iniciador procura o Python, inicia o servidor e tenta abrir o navegador.

## Iniciar pelo PowerShell

```powershell
Set-Location "C:\caminho\Cyberlab-main"
.\iniciar.cmd
```

Há também `.\iniciar.ps1`. Se a política de scripts bloquear esse arquivo, use `.\iniciar.cmd` ou o comando Python abaixo. Não é necessário alterar a política.

## Comando direto nos dois terminais

```text
py -3 lab.py --open
```

Se `py` não estiver disponível, tente `python lab.py --open`. Confira a versão com `py -3 --version` ou `python --version`.

| Endereço no navegador | Conteúdo |
| --- | --- |
| `http://127.0.0.1:8000` | Seis aulas iniciais. |
| `http://127.0.0.1:8000/windows` | Comandos de CMD e PowerShell. |
| `http://127.0.0.1:8000/avancado` | Desafios opcionais de SQL, logs e Base64. |

**Para encerrar:** pressione Ctrl+C no terminal do servidor. Se a porta 8000 estiver ocupada, confira se outra janela já está executando o laboratório. Se o navegador não abrir, digite o endereço manualmente.

O servidor fica restrito ao próprio computador. A área avançada contém falhas intencionais e dados fictícios. Mantenha-a local e pratique em sistemas de terceiros somente com autorização.

<!-- page -->
## Funções para reconhecer no código

Os comandos anteriores são digitados no terminal. As funções abaixo são usadas dentro do programa Python e ajudam a entender os exemplos do CyberLab.

| Função ou método | Para que serve | Atenção no estudo |
| --- | --- | --- |
| `print()` | Exibir uma mensagem. | Mostrar o resultado de um teste. |
| `input()` | Receber texto digitado. | A entrada ainda precisa ser validada. |
| `int()` | Converter um valor para inteiro. | Texto inválido pode gerar ValueError. |
| `Path.read_text()` | Ler um arquivo como texto. | O servidor lê as páginas em UTF-8. |
| `json.loads()` | Transformar texto JSON em dados Python. | Ainda é preciso conferir tipos e campos. |
| `conn.execute()` | Executar SQL no SQLite. | Use parâmetros para dados recebidos. |
| `hmac.compare_digest()` | Comparar valores reduzindo diferenças de tempo. | Não substitui hash de senha apropriado. |
| `do_GET()` e `do_POST()` | Tratar requisições HTTP no servidor. | GET consulta; POST envia dados ao exercício. |

O login da área avançada monta SQL de forma vulnerável de propósito. Para aprender a correção, observe a ideia de usar um marcador e enviar o dado separadamente:

```python
conn.execute("SELECT username FROM users WHERE username = ?", (usuario,))
```

Esse trecho ensina parametrização; um login real também precisa verificar a senha com um algoritmo apropriado. Base64, usado em outro desafio, é uma codificação reversível, sem proteção de confidencialidade.

## Ordem sugerida de estudo

1. Faça as seis aulas iniciais do CyberLab.
2. Pratique pastas, leitura e cópia de arquivos da página 2.
3. Observe a configuração de rede e teste o servidor local.
4. Localize eventos do log e explique o que as linhas mostram.
5. Altere a nota, compare hashes e recupere o conteúdo da cópia.

## Referências para consulta

- Repositório CyberLab: https://github.com/RayanL15/Cyberlab
- Microsoft Learn, comandos do Windows: https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/windows-commands
- Microsoft Learn, PowerShell: https://learn.microsoft.com/pt-br/powershell/
- Microsoft Learn, Get-FileHash: https://learn.microsoft.com/pt-br/powershell/module/microsoft.powershell.utility/get-filehash
- Documentação do Python no Windows: https://docs.python.org/3/using/windows.html

Material de estudo atualizado em 29 de outubro de 2026.
