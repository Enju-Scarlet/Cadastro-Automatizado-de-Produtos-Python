# 🤖 Automated Product Registration

This project aims to **automate the registration of nearly 300 products on the company's website**, using Python to read the data from a spreadsheet and the **PyAutoGUI** library to interact with the browser and automatically fill in the fields.  

---

## ✨ Project Goals

- Read the product database from a CSV file  
- Access the company's system via browser  
- Perform automatic login  
- Fill in the product registration forms (code, brand, type, category, price, cost, notes)  
- Repeat the process for all products in the spreadsheet  

---

## 🛠️ Technologies Used

- 🐍 **Python 3.x**  
- 📑 **Pandas** – for reading and manipulating the product spreadsheet  
- 🖱️ **PyAutoGUI** – for keyboard and mouse automation  
- ⏱️ **Time** – for adding pauses between commands  

---

## 🚀 How to Run the Project

### Requirements
- Python 3.x installed  
- Configured browser (the code uses **Opera**, but it can be adapted)  
- Install the required libraries:  

```bash
pip install pandas pyautogui
```

---

## ⚠️ Important Notes

- The **click coordinates (x, y)** in PyAutoGUI may vary depending on the monitor and resolution.  
- If the clicks do not work correctly, use the **auxiliar.py** file to capture the correct mouse positions.  
- Make sure the browser is on the main screen and no unexpected elements shift the field positions.  

---

## 📊 Automation Flow

1. Open the browser and access the company's website  
2. Perform login with user and password  
3. Load the product spreadsheet (`produtos.csv`)  
4. Iterate over each row and register the products automatically  
5. Confirm each registration and proceed to the next product  

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share!  

---