#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

# Inicializa o mixer

pygame.mixer.init()

#Carrega a música

pygame.mixer.music.load("teste.mp3")

print ("mini player")
print("comandos disponiveis:play, pause, resume, stop, sair")

while True:
    comando = input("Digite um comando: ").strip().lower()

    if comando == "play":
        pygame.mixer.music.load()
        print("Tocando a musica...")
    elif comando == "pause":
        pygame.mixer.music.pause()
        print("Musica será pausada")
    elif comando == "resume":
        pygame.mixer.music.unpause()
        print("Musica será retomada")
    elif comando == "stop":
        pygame.mixer.music.stop()
        print("⏹️ Música parada.")
    elif comando == "sair":
        pygame.mixer.music.stop()
        print("👋 Encerrando player.")
        break
    else:
        print("Comando inválido! Use: play, pause, resume, stop, sair")

#SE VOCE NÃO TIVER UM ARQUIVO EM MP3, PODE BAIXAR NO YOUTUBE
#CLIQUE CONTA CLIENTE NA SUA FOTO >>> YOUTUBE STUDIO >>>BIBLIOTECA DE AUDIO>>> ESCOLHA A MUSICA DISPONIVEL E BAIXE
#APANHEI PARA CARREGAR A MUSICA PORQUE SALVEI NA PASTA ERRADA E QUANDO FUI RENOMEAR SALQUE COM MP3 DUAS VEZES
#SE ATENDE COM A VERSÃO DO PYTHON VOCÊ ESTÁ USANDO PORQUE DEPENDENDO ESSE CÓDIGO PODE NÃO RODAR


