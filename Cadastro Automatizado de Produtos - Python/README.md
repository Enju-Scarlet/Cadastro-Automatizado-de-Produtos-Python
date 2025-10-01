# 🤖 Automação de Cadastro de Produtos

Este projeto tem como objetivo **automatizar o cadastro de quase 300 produtos em um site da empresa**, utilizando Python para ler os dados de uma planilha e a biblioteca **PyAutoGUI** para interagir com o navegador e preencher os campos automaticamente.  

---

## ✨ Objetivos do Projeto

- Ler a base de dados de produtos a partir de um arquivo CSV  
- Acessar o sistema da empresa via navegador  
- Realizar login automático  
- Preencher os formulários de cadastro de produto (código, marca, tipo, categoria, preço, custo, observações)  
- Repetir o processo para todos os produtos da planilha  

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python 3.x**  
- 📑 **Pandas** – para leitura e manipulação da planilha de produtos  
- 🖱️ **PyAutoGUI** – para automação de teclado e mouse  
- ⏱️ **Time** – para adicionar pausas entre comandos  

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.x instalado  
- Navegador configurado (no código foi usado **Opera**, mas pode ser adaptado)  
- Instalar as bibliotecas necessárias:  

```bash
pip install pandas pyautogui
```

## ⚠️ Observações Importantes

- Os **coordenadas de clique (x, y)** no PyAutoGUI podem variar de acordo com o monitor e resolução.  
- Caso os cliques não funcionem corretamente, utilize o arquivo **auxiliar.py** para capturar as posições corretas do mouse.  
- É importante garantir que o navegador esteja na tela principal e sem elementos inesperados que alterem a posição dos campos.  

---

## 📊 Fluxo da Automação

1. Abrir o navegador e acessar o site da empresa  
2. Realizar login com usuário e senha  
3. Carregar a planilha de produtos (`produtos.csv`)  
4. Iterar sobre cada linha e cadastrar os produtos automaticamente  
5. Confirmar cada cadastro e avançar para o próximo produto  

---

## 📜 Licença

Este projeto está sob a licença MIT.  
Sinta-se livre para usar, modificar e compartilhar!  

---
