# APP QUE VAI ABRIR O "A FUNÇÃO WINDOS WINDOWS + R"
# VAI ABRIR O EXECUTADOR E PROCURAR POR "TEMP"
# VAI SELECIONAR TUDO DENTRO DO TEMP, E APÓS ISSO DELETAR. 
from tempfile import tempdir
import pyautogui
pyautogui.alert('O Auto Cleaner Começou a Operação.')
pyautogui.hotkey('win', 'r')
#time.pause(0.2)
pyautogui.write('temp')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
pyautogui.press('enter')
