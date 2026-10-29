#!/usr/bin/env python3
"""Laboratório educativo local. Não exponha esta aplicação à Internet."""
import base64
import hmac
import json
import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

FLAGS = {"sqli": "LAB{consulta_sem_parametros}", "logs": "LAB{203.0.113.42}", "secret": "LAB{base64_nao_e_criptografia}"}
LOGS = '''2026-01-15T10:00:00Z ip=192.0.2.10 POST /login status=200 user=ana
2026-01-15T10:01:00Z ip=203.0.113.42 POST /login status=401 user=admin
2026-01-15T10:01:01Z ip=203.0.113.42 POST /login status=401 user=admin
2026-01-15T10:01:02Z ip=203.0.113.42 POST /login status=401 user=admin
2026-01-15T10:01:03Z ip=203.0.113.42 POST /login status=200 user=admin
2026-01-15T10:02:00Z ip=203.0.113.42 GET /backup.zip status=200 user=admin
2026-01-15T10:03:00Z ip=192.0.2.10 GET /profile status=200 user=ana'''

HTML = '''<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>CyberLab • Primeira missão</title><style>
body{background:#0c1220;color:#dfe9f8;font:17px system-ui;max-width:950px;margin:40px auto;padding:0 20px}h1,h2{color:#70e1c1}article{background:#172237;padding:24px;border-radius:14px;margin:20px 0}button,input{font:inherit;padding:10px;border-radius:6px;border:1px solid #56647b;margin:5px 0}button{background:#70e1c1;color:#0c1220;cursor:pointer}input{background:#0c1220;color:white;max-width:90%}pre{overflow:auto;background:#0c1220;padding:15px}summary{cursor:pointer}a{color:#70e1c1}.muted{color:#b2c1d8}.ok{color:#70e1c1}</style>
<h1>CyberLab</h1><p>Primeira missão: investigue um portal comprometido.</p><p class="muted">Ambiente educativo local. Dados e credenciais são fictícios. Pratique somente neste laboratório ou em sistemas com autorização.</p>
<p id="progress"></p><button onclick="localStorage.removeItem('cyberlab-v1');location.reload()">Reiniciar progresso</button>
<article><h2>01 · Um login suspeito</h2><p>Objetivo: entrar como <code>admin</code> sem conhecer a senha. Teste como o formulário lida com entradas que alteram uma consulta SQL.</p>
<form id="login"><input name="user" placeholder="Usuário" aria-label="Usuário" required><input name="password" placeholder="Senha" aria-label="Senha"><button>Entrar</button></form><pre id="login-result">O portal aguarda seu login.</pre>
<details><summary>Dica 1</summary><p>Uma aspa simples pode revelar como o servidor monta a consulta.</p></details><details><summary>Dica 2</summary><p>No SQLite, dois hífens iniciam um comentário. Pense em como remover a verificação da senha da consulta.</p></details>
<p>Envie a flag exibida após o acesso.</p><form class="flag" data-id="sqli"><input name="flag" aria-label="Flag do login" placeholder="LAB{...}" required><button>Validar flag</button><output></output></form>
<details><summary>Depois do desafio: correção</summary><p>Use consultas parametrizadas, hash de senha com algoritmo apropriado e mensagens de erro que não revelem SQL.</p></details></article>
<article><h2>02 · Rastros de uma invasão</h2><p>Analise o <a href="/artifacts/access.log" target="_blank" rel="noopener">registro de acesso</a>. Qual IP combina tentativas de senha, acesso bem-sucedido e download de backup? Envie <code>LAB{IP}</code>.</p>
<details><summary>Dica</summary><p>Correlacione códigos 401 e 200 para o mesmo usuário e IP. Os endereços usados aqui são reservados para documentação.</p></details>
<form class="flag" data-id="logs"><input name="flag" aria-label="Flag dos logs" placeholder="LAB{...}" required><button>Validar flag</button><output></output></form>
<details><summary>Depois do desafio: defesa</summary><p>Limite tentativas de autenticação, use MFA e gere alertas para downloads sensíveis após falhas repetidas.</p></details></article>
<article><h2>03 · Segredo disfarçado</h2><p>Um desenvolvedor publicou um <a href="/artifacts/config.json" target="_blank" rel="noopener">arquivo de configuração</a>. Recupere o segredo de treinamento.</p>
<details><summary>Dica</summary><p>Base64 é uma codificação reversível. No Python, investigue o módulo <code>base64</code>.</p></details>
<form class="flag" data-id="secret"><input name="flag" aria-label="Flag da configuração" placeholder="LAB{...}" required><button>Validar flag</button><output></output></form>
<details><summary>Depois do desafio: defesa</summary><p>Remova segredos de arquivos públicos, use um gerenciador de segredos e revogue credenciais expostas. Codificação não protege confidencialidade.</p></details></article>
<script>
let solved;try{solved=JSON.parse(localStorage.getItem('cyberlab-v1')||'[]');if(!Array.isArray(solved))solved=[]}catch{solved=[]}
function progress(){document.querySelector('#progress').textContent=`Progresso: ${['sqli','logs','secret'].filter(x=>solved.includes(x)).length}/3 missões concluídas`;document.querySelectorAll('.flag').forEach(f=>{if(solved.includes(f.dataset.id))f.querySelector('output').textContent=' ✓ Concluída'})}progress();
async function post(path,data){const r=await fetch(path,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});if(!r.ok)throw Error('Solicitação recusada');return r.json()}
document.querySelector('#login').onsubmit=async e=>{e.preventDefault();try{const r=await post('/api/login',Object.fromEntries(new FormData(e.target)));document.querySelector('#login-result').textContent=r.message}catch{document.querySelector('#login-result').textContent='Falha na comunicação com o laboratório.'}};
document.querySelectorAll('.flag').forEach(f=>f.onsubmit=async e=>{e.preventDefault();try{const r=await post('/api/flag',{id:f.dataset.id,flag:new FormData(f).get('flag')});f.querySelector('output').textContent=r.ok?' ✓ Correta!':' Tente novamente.';if(r.ok&&!solved.includes(f.dataset.id)){solved.push(f.dataset.id);localStorage.setItem('cyberlab-v1',JSON.stringify(solved));progress()}}catch{f.querySelector('output').textContent=' Falha na comunicação.'}});
</script></html>'''


class Handler(BaseHTTPRequestHandler):
    def reply(self, status, body, content_type="application/json"):
        data = (json.dumps(body, ensure_ascii=False) if content_type == "application/json" else body).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type + "; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            self.reply(200, HTML, "text/html")
        elif path == "/artifacts/access.log":
            self.reply(200, LOGS, "text/plain")
        elif path == "/artifacts/config.json":
            self.reply(200, {"encoding": "base64", "training_secret": base64.b64encode(FLAGS["secret"].encode()).decode()})
        else:
            self.reply(404, {"error": "Não encontrado"})

    def do_POST(self):
        # Only same-origin browser requests and local CLI clients are accepted.
        if self.headers.get("Origin") not in (None, "http://127.0.0.1:8000", "http://localhost:8000"):
            return self.reply(403, {"error": "Origem recusada"})
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 < size <= 8192:
                raise ValueError()
            data = json.loads(self.rfile.read(size))
            if not isinstance(data, dict) or any(not isinstance(v, str) for v in data.values()):
                raise ValueError()
        except (ValueError, UnicodeDecodeError):
            return self.reply(400, {"error": "JSON inválido"})
        if self.path == "/api/flag":
            expected = FLAGS.get(data.get("id"))
            return self.reply(200, {"ok": expected is not None and hmac.compare_digest(data.get("flag", "").strip().encode(), expected.encode())})
        if self.path != "/api/login":
            return self.reply(404, {"error": "Não encontrado"})
        conn = sqlite3.connect(":memory:")
        try:
            conn.execute("CREATE TABLE users (username TEXT, password TEXT)")
            conn.execute("INSERT INTO users VALUES (?, ?)", ("admin", "ficticia-8af92e31"))
            # Intentionally vulnerable: the exercise is confined to a disposable DB.
            query = "SELECT username FROM users WHERE username = '%s' AND password = '%s'" % (data.get("user", ""), data.get("password", ""))
            row = conn.execute(query).fetchone()
            message = "Acesso negado."
            if row and row[0] == "admin":
                message = "Acesso autorizado. " + FLAGS["sqli"]
            self.reply(200, {"message": message})
        except sqlite3.Error as exc:
            self.reply(200, {"message": "Erro SQL de treinamento: " + str(exc) + "\nConsulta: " + query})
        finally:
            conn.close()


if __name__ == "__main__":
    print("CyberLab iniciado em loopback, porta 8000. Ctrl+C encerra.", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
