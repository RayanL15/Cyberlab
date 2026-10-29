# Compativel com Windows PowerShell 5.1 e PowerShell 7 no Windows.
# Se a politica de scripts bloquear este arquivo, use .\iniciar.cmd.
$ErrorActionPreference = 'Stop'
$pythonCommand = $null
$pythonArgs = @()

foreach ($candidate in @('py', 'python')) {
    $command = Get-Command $candidate -CommandType Application -ErrorAction SilentlyContinue
    if (-not $command) { continue }
    $arguments = @()
    if ($candidate -eq 'py') { $arguments = @('-3') }
    try {
        & $command.Source @arguments -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)' 2>$null
        if ($LASTEXITCODE -eq 0) {
            $pythonCommand = $command.Source
            $pythonArgs = $arguments
            break
        }
    } catch { continue }
}

if (-not $pythonCommand) {
    Write-Host 'Python 3.10 ou superior nao encontrado. Instale em https://www.python.org/downloads/.'
    Write-Host 'Sem Python, abra index.html diretamente no navegador.'
    exit 1
}

# Caminho absoluto: funciona mesmo quando o terminal esta em outra pasta.
& $pythonCommand @pythonArgs (Join-Path $PSScriptRoot 'lab.py') --open
exit $LASTEXITCODE
