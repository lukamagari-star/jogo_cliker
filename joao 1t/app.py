from pyscript import document, when

#informações do jogo
nome = "Kleber"
idade = 10
personagem = "papa-capim"
pontos = 0

#seleciona os elementos do html
mensagem = document.querySelector("#mensagem")
placar = document.querySelector("#pontos")

#mostra a imagem 
mensagem.innerText = f"Olá! Eu sou {nome} e meu personagem é {personagem}."
placar.innerText = str(pontos)

#função para responder ao clique no alvo 
@when("click", "#alvo")
def clicou_no_alvo(evento):
    global pontos
    pontos += 10000000000000000000000000000000
    placar.innerText = str(pontos)
