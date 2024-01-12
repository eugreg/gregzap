
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


    def entrar_popup(evento):
        popup.open = True
        pagina.romove(botao_iniciar)
        pagina.update()

    popup = ft.AlertDialog(title=ft.Text("Digite seu nome"), content=nome_usuario,  actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)], open=False, )

    def entrar_chat(evento):
        popup.open = True
        pagina.dialog = popup
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)


    pagina.add(titulo)
    pagina.add(botao_iniciar)


ft.app(main)