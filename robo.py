import pyautogui
import time

#tempo de pausa
pyautogui.PAUSE = 1



#entrar navegador 1
pyautogui.click(x=131, y=142)
pyautogui.click(x=380, y=553)
pyautogui.write('carlos')
pyautogui.click(x=348, y=628)

#entrar navegador 2
pyautogui.click(x=880, y=129)
pyautogui.click(x=1419, y=551)
pyautogui.write('joao')
pyautogui.click(x=1292, y=626)

#mandar mensagem  1
pyautogui.click(x=150, y=245)
pyautogui.write('eai')
pyautogui.press("tab")
pyautogui.press("enter")

#mandar mensagem 2
pyautogui.click( x=1074, y=214)
pyautogui.write('oii')
pyautogui.press("tab")
pyautogui.press("enter")


#mandar mensgem 3
pyautogui.click(x=150, y=245)
pyautogui.press("tab")
pyautogui.write('tudo bem?')
pyautogui.press("tab")
pyautogui.press("enter")

#mandar mensgem 4
pyautogui.click( x=1074, y=214)
pyautogui.press("tab")
pyautogui.write('simm e com voce?')
pyautogui.press("tab")
pyautogui.press("enter")


#mandar mensgem 5
pyautogui.click(x=150, y=245)
pyautogui.press("tab")
pyautogui.write('que bom! estou bem!! tchauu')
pyautogui.press("tab")
pyautogui.press("enter")

#mandar mensgem 6
pyautogui.click( x=1074, y=214)
pyautogui.press("tab")
pyautogui.write('que bomm!! tchauuuuu')
pyautogui.press("tab")
pyautogui.press("enter")


