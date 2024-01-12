
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem


import flet as ft

def main(pagina):
    titulo = ft.Text("GregZap", size=30, bold=True, color=ft.colors.BLUE_500)
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_popup)

    def entrar_popup(evento):
        pagina.add(chat)
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(titulo)
        pagina.update()



    pagina.add(titulo)


ft.app(main)