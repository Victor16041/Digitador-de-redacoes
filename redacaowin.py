import time
import keyboard
import tkinter as tk
from tkinter import simpledialog
from google.genai import types
from google import genai

root = tk.Tk()
root.withdraw()

client = genai.Client(api_key="Coloque a chave api aqui") # coloque sua chave da api do gemini

# pede pra pessoa digitar o tema
redacao = simpledialog.askstring("Sua redação MANEIRA", "Digite o tema da sua redação")

# gera o texto da ia
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[redacao],
    config=types.GenerateContentConfig(
        system_instruction="O seu proposito vai ser escrever uma redação de no minimo 160 palavras e maximo de 200 palavras sobre o tema que eu pedir. Ela sempre terá que ser em português brasileiro, e de forma totalmente formal."
    )
)

# tenta extrair o texto da resposta
try:
    texto = response.candidates[0].content.parts[0].text
except Exception as e:
    print("Texto bugou e deu erro:", e)
    texto = ""

rodando = True

print("Assim que clicar 'F3', irá começar a escrever")
keyboard.wait('f3')

paragrafos = texto.strip().split('\n\n')

for paragrafo in paragrafos:
    for letra in paragrafo:
        if keyboard.is_pressed('f2'):
            rodando = False
            break
        keyboard.write(letra)
        time.sleep(0.01)
    if not rodando:
        break
    keyboard.write('\n\n')
    time.sleep(0.3)