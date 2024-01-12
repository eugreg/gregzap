
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem


import flet as ft

def main(pagina):
    titulo = ft.Text("GregZap")
    nome_usuario = ft.TextField(label="Escreva seu nome")
    campo_mensagem = ft.TextField(label="Digite uma mensagem")
    chat = ft.Column()



    def enviar_mensagem(evento):
        chat.controls.append(ft.Text(f"{nome_usuario.value}: { campo_mensagem.value}"))
        # limpar o campo de mensagem
        campo_mensagem.value = ""
        pagina.update()

    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    def entrar_chat(evento):
        popup.open = False
        pagina.remove(botao_iniciar)
        linha = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(chat)
        pagina.add(linha)
        pagina.update()
        

    popup = ft.AlertDialog(title=ft.Text("Digite seu nome"), content=nome_usuario,  actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)], open=False, )

    def entrar_popup(evento):
        popup.open = True
        pagina.dialog = popup
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_popup)


    pagina.add(titulo)
    pagina.add(botao_iniciar)


ft.app(main)