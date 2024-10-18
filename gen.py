import random as r
import string as s
import time as t
import pyperclip as pc
import webbrowser as wb
import pyfiglet as pf

def g(b='EKpmI8gNvJ'):
    c = s.ascii_letters + s.digits
    return ''.join(r.choice(c) for _ in range(len(b)))

def b(seg):
    v = "\033[38;5;76m"  # Cor verde (#42f563)
    r = "\033[0m"  # Reseta a cor
    print("[+]  Gerando códigos, por favor, aguarde...")

    for i in range(seg * 10):
        t.sleep(0.1)
        print(f"\r{v}[{'#' * (i // 2)}{' ' * (10 - (i // 2))}] {((i + 1) / (seg * 10)) * 100:.0f}%{r}", end='', flush=True)

    print("\n[!]  Geração concluída!")

def s(c):
    with open("codigos_gerados.txt", "w") as f:
        for code in c:
            f.write(code + "\n")
    print("[+]  Os códigos foram salvos no arquivo 'codigos_gerados.txt'.")

def cp(c):
    cs = '\n'.join(c)
    pc.copy(cs)
    print("[+]  Os códigos foram copiados para a área de transferência.")

def ob(c):
    h = """
    <html>
    <head>
        <title>pecinha'1533</title>
        <style>
            body {
                background-color: black;
                color: white;
                font-family: Arial, sans-serif;
            }
            h1 {
                color: #42f563;
                font-size: 3.0em; /* Tamanho grande do título */
            }
            a {
                color: #42f563;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>Spotify gen</h1>
        <ul>
    """
    for code in c:
        u = url.replace("substituir_code", code)
        h += f"<li><a href='{u}' target='_blank'>{u}</a></li>"

    h += """
        </ul>
    </body>
    </html>
    """

    with open("codigos_gerados.html", "w") as f:
        f.write(h)

    wb.open("codigos_gerados.html")
    print("[+]  Pagina aberta no navegador e salva.")

# URL base com o local onde o código deve ser inserido
url = "https://www.spotify.com/br-pt/ppt/microsoft/?code=substituir_code"

# Título do console com pyfiglet
t = pf.figlet_format("Spotify Gen", font="slant")
print("\033[1;32m" + t + "\033[0m")

# Menu inicial
while True:
    print("\n>  Escolha uma opção:")
    print("[1] Gerar códigos Spotify Premium 3 meses")
    print("[2] Discord do criador")
    print("[3] Sair")
    
    o = int(input(">  Escolha uma opção (1/2/3): "))

    if o == 1:
        qtd = int(input("[+]  Quantos códigos deseja gerar? "))
        b(2)
        cg = [g() for _ in range(qtd)]

        print("\n[+]  Códigos gerados:")
        for code in cg:
            print(url.replace("substituir_code", code))

        print("\n>  O que deseja fazer com os códigos?")
        print("[1]  Salvar em um arquivo .txt")
        print("[2]  Copiar para a área de transferência")
        print("[3]  Abrir em uma página local no navegador")

        e = int(input(">  Escolha uma opção (1/2/3): "))

        if e == 1:
            s(cg)
        elif e == 2:
            cp(cg)
        elif e == 3:
            ob(cg)
        else:
            print("[+]  Opção inválida.")

    elif o == 2:
        wb.open("https://discord.com")
    
    elif o == 3:
        print("[+]  Saindo do gerador.")
        break
    
    else:
        print("[+]  Opção inválida. Tente novamente.")
