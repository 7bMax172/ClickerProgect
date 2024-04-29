from customtkinter import *
from tkinter import  messagebox
from random import randint as rn, choice as ch
import json


def read(fileName: str) -> dict:
    with open(fileName, "r") as f:
        return json.load(f)

def __save_data_in_json(data) -> None:
    data = json.dumps(data)
    data = json.loads(str(data))
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

dataRead = read("data.json")
clickCount = dataRead["click"]
cristalCount = dataRead["cristal"]
cristalChanse = dataRead["cristalChanse"]
clickBoost = dataRead["clickBoost"]
cristalBoost = dataRead["cristalBoost"]
shopClickCount = dataRead["shopClickCount"]
cristalClickCount = dataRead["cristalClickCount"]

clickCost = clickBoost * 100
cristalCost = cristalBoost * 20

root = CTk()
root.title("clicker")
root.geometry("800x600")
root.resizable(False, False)

clickCountLabel = CTkLabel(root, text=f"Clicks - {clickCount}")
cristalCountLabel = CTkLabel(root, text=f"Cristal - {cristalCount}")

def updateSafeData():
    dataSafe = {
         "click": clickCount,
         "cristal": cristalCount,
         "cristalChanse": cristalChanse,
         "clickBoost": clickBoost,
         "cristalBoost": cristalBoost,
         "shopClickCount": shopClickCount,
         "cristalClickCount": cristalClickCount
        }
    __save_data_in_json(dataSafe)
updateSafeData()

def clickAdd():
    global clickCount, cristalChanse, clickBoost, cristalCount, cristalBoost
    clickCount += clickBoost
    if rn(1, cristalChanse) == 10:
        cristalCount += cristalBoost

    updateSafeData()
    clickCountLabel.configure(text=f"Clicks - {clickCount}")
    cristalCountLabel.configure(text=f"Cristal - {cristalCount}")

def shopWin():
    clickCountLabel.destroy()
    cristalCountLabel.destroy()
    clickBtn.destroy()
    shopOpen.destroy()

    shopClickBtn.place(x=200, y=170)
    shopCristalBtn.place(x=350, y=170)
    exitBtn.place(x=300, y=560)

def clickShop():
    global clickCost, clickBoost, clickCount, shopClickCount
    if clickBoost < 2 ** 48:
        if clickCost <= clickCount:
            clickBoost *= 2
            clickCount -= clickCost
            shopClickCount += 1

            clickCountLabel.configure(text=f"Clicks - {clickCount}")
            cristalCountLabel.configure(text=f"Cristal - {cristalCount}")
            shopClickBtn.configure(text=f"Click - {shopClickCount}/50 \n {clickCost}")

    else:
        messagebox.showerror("Max boost", "You buy all 50 click boost!")

    updateSafeData()

def cristalShop():
    global cristalCost, clickBoost, cristalCount, cristalClickCount
    if clickBoost < 2 ** 48:
        if cristalCost <= cristalCount:
            clickBoost *= 2
            cristalCount -= cristalCost
            cristalClickCount += 1

            clickCountLabel.configure(text=f"Clicks - {cristalCount}")
            cristalCountLabel.configure(text=f"Cristal - {cristalCount}")
            shopClickBtn.configure(text=f"Click - {cristalClickCount}/50 \n {cristalCount}")

    else:
        messagebox.showerror("Max boost", "You buy all 50 click boost!")

    updateSafeData()

def exit():
    shopClickBtn.destroy()
    shopCristalBtn.destroy()
    exitBtn.destroy()

    main_window()

clickBtn = CTkButton(root, text="Click", command=clickAdd)
shopClickBtn = CTkButton(root, text=f"Click - {shopClickCount}/50 \n {clickCost}", command=clickShop)
shopCristalBtn = CTkButton(root, text=f"Cristal - {cristalClickCount}/20 \n {cristalCost}")

shopOpen = CTkButton(root, text="Shop", command=shopWin)
exitBtn = CTkButton(root, text="Exit", command=exit)

def main_window():
    clickCountLabel.place(x=0, y=150)
    cristalCountLabel.place(x=0, y=170)
    clickBtn.place(x=300, y=560)
    shopOpen.place(x=650, y=170)

main_window()

if __name__ == "__main__":
    root.mainloop()