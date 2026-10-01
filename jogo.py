# ==================================================
# JOGADOR
# ==================================================

x = 100
y = 100

velocidade = 10

jogador = document.querySelector("#jogador")


# ==================================================
# ATUALIZAR JOGADOR
# ==================================================

def atualizar_jogador():
    jogador.style.left = f"{x}px"
    jogador.style.top = f"{y}px"


# ==================================================
# MOEDA
# ==================================================

moeda_x = 300
moeda_y = 200

moeda = document.querySelector("#moeda")


# ==================================================
# MOVER MOEDA
# ==================================================

def mover_moeda():
    global moeda_x, moeda_y

    moeda_x = randint(20, 650)
    moeda_y = randint(20, 410)

    moeda.style.left = f"{moeda_x}px"
    moeda.style.top = f"{moeda_y}px"


# ==================================================
# PONTUAÇÃO
# ==================================================

pontos = 0

placar = document.querySelector("#placar")

mensagem = document.querySelector("#mensagem")


# ==================================================
# VERIFICAR MOEDA
# ==================================================

def verificar_moeda():
    global pontos

    distancia_x = abs(x - moeda_x)
    distancia_y = abs(y - moeda_y)

    if distancia_x < 40 and distancia_y < 40:
        pontos = pontos + 1
        placar.innerText = pontos
        mensagem.innerText = "🪙 Moeda coletada! +1 ponto!"
        mover_moeda()


# ==================================================
# CONTROLE DO JOGADOR
# ==================================================

@when("keydown", document)
def tecla_pressionada(evento):
    global x, y

    # Evita que a tela role para cima/baixo com as setas do teclado
    if evento.key in ["ArrowRight", "ArrowLeft", "ArrowDown", "ArrowUp"]:
        evento.preventDefault()

    if evento.key == "ArrowRight":
        x += velocidade
    elif evento.key == "ArrowLeft":
        x -= velocidade
    elif evento.key == "ArrowDown":
        y += velocidade
    elif evento.key == "ArrowUp":
        y -= velocidade
    else:
        return

    # ==================================================
    # LIMITES
    # ==================================================

    if x < 0:
        x = 0

    if x > 650:
        x = 650

    if y < 0:
        y = 0

    if y > 410:
        y = 410

    # Atualiza o jogador
    atualizar_jogador()

    # Verifica a moeda
    verificar_moeda()


# ==================================================
# INICIALIZAÇÃO
# ==================================================

atualizar_jogador()

mover_moeda()