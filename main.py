
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem


import flet as ft

def main(pagina):
    #nome da aplicação
    titulo = ft.Text("GregZap")
    #campo de texto para escrever o nome
    nome_usuario = ft.TextField(label="Escreva seu nome")
    #campo de texto para escrever a mensagem
    campo_mensagem = ft.TextField(label="Digite uma mensagem")
    #chat
    chat = ft.Column()

    #função para enviar a mensagem online
    def tunel_mensagem(mensagem):

        #adiciona a mensagem no chat
        chat.controls.append(ft.Text(mensagem))
        #atualiza a página
        pagina.update()

    #inscreve a função no pubsub
    pagina.pubsub.subscribe(tunel_mensagem)

    #função para enviar a mensagem
    def enviar_mensagem(evento):
        #texto da mensagem
        texto = f'{nome_usuario.value}: {campo_mensagem.value}'
        #envia a mensagem para o pubsub
        pagina.pubsub.send_all(texto)
        # limpar o campo de mensagem
        campo_mensagem.value = ""
        #atualiza a página
        pagina.update()

    #botão de enviar mensagem
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    #função para entrar no chat
    def entrar_chat(evento):
        #fecha o popup
        popup.open = False
        #remove o botão iniciar chat
        pagina.remove(botao_iniciar)
        #linha com o campo de mensagem e o botão enviar
        linha = ft.Row(
            [campo_mensagem, botao_enviar]
        )   
        #texto da mensagem de entrada
        texto = f'{nome_usuario.value} entrou no chat'
        #envia a mensagem para o pubsub
        pagina.pubsub.send_all(texto)
        #adiciona o chat na página
        pagina.add(chat)
        #adiciona a linha na página
        pagina.add(linha)
        #atualiza a página
        pagina.update()
        
    #popup para entrar no chat
    popup = ft.AlertDialog(title=ft.Text("Digite seu nome"), content=nome_usuario,  actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)], open=False, )

    #função para abrir o popup
    def entrar_popup(evento):
        #abre o popup
        popup.open = True
        #atualiza a página
        pagina.dialog = popup
        pagina.update()

    #botão de iniciar chat
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_popup)


    pagina.add(titulo)
    pagina.add(botao_iniciar)


ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
# ft.app(main)