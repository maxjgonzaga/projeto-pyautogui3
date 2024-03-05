'''
# DESAFIO 
Crie um programa que vai ate onde seu bloco de notas estiver aberto e digite a frase
"Automação é Incrivel!" 
'''
import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.click(678,209,duration=2)
escrever_frase('Automação é Incrível!')