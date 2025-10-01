# pyautogui -> Fazer automações com python
# pip install pyautogui (Instala o pyautogui)

# importando o pyautogui para usar-mos ele
import pyautogui

# importando a biblioteca time
import time

# Delay de segundos (Para que o programa "respire" entre cada comando) 
pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


# Passo 2: Fazer Login
# Fazer o computador esperar 3 segundos (Para esperar o site carregar)
time.sleep(3)

# Clicar e digitar no campo de email
pyautogui.click(x=730, y=395)
pyautogui.write("esseemailnaoexiste@gmail.com")

# Clicar e digitar no campo de senha
pyautogui.press("tab")
pyautogui.write("12345")

# Entrando no Login
pyautogui.press("enter")


# Passo 3: Importar a base de dados
# Importando Pandas (Foco em base de dados)
import pandas

tabela = pandas.read_csv("produtos.csv")


# Passo 4: Cadastrar 1 Produto
# Fazer o computador esperar 3 segundos (Para esperar o site carregar)
time.sleep(3)

# Clicar e digitar nos campos de texto
# pyautogui.click(x=712, y=352)

# Categorias dos Produtos
# codigo = "MOLO000251"
# pyautogui.write(codigo)

# pyautogui.press("tab")
# marca = "Logitech"
# pyautogui.write(marca)

# pyautogui.press("tab")
# tipo = "Mouse"
# pyautogui.write(tipo)

# pyautogui.press("tab")
# categoria = "1"
# pyautogui.write(categoria)

# pyautogui.press("tab")
# preco_unitario = "25.95"
# pyautogui.write(preco_unitario)

# pyautogui.press("tab")
# custo = "6.50"
# pyautogui.write(custo)

# pyautogui.press("tab")
# obs = ""
# pyautogui.write(obs)

# Dando enter para cadastrar o produto
# pyautogui.press("enter")


# Passo 5: Repetir para todos os produtos
# Fechar o pop-up de "salvar a senha"
pyautogui.click(x=1848, y=132)

for linha in tabela.index: # "Para cada linha da minha tabela..."
    
    # Clicar e digitar nos campos de texto
    pyautogui.click(x=712, y=280)

    # Categorias dos Produtos
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"]) # string = texto -> str()
    pyautogui.write(categoria) # .write só consegue escrever texto e não números (a não ser que o número esteja formatado como texto)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    # Dando enter para cadastrar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

