import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#time.sleep(1)

#pyautogui.click(x=770, y=434)

time.sleep(3)
#pyautogui.click(x=295, y=19)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)
pyautogui.click(x=641, y=407)
pyautogui.write("exemplo123@gmail.com")
pyautogui.press("tab") 
pyautogui.write("senha qualquer")
pyautogui.press("tab")
pyautogui.press("enter")

import pandas as pd

tabela = pd.read_csv("produtos.csv")

time.sleep(1)
for linha in tabela.index:
    
    pyautogui.click(x=575, y=290)
    
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "nan":
        pyautogui.write(obs)
        
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    
    
