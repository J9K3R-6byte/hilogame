import random
from window import addButton, addButton2, addButton3, addGroup, addImage, addInput2, addLabel2, addLabel3, addLabel_XL, makeWindow, addLabel

class HiLoGame:
    def __init__(self):
        self.window = makeWindow("Hi Lo Game")
        self.money = 1000
        self.bet = 0
        self.cardValues = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            "jack",
            "queen",
            "king",
        ]
        self.cardTypes = [
            "heart",
            "spade",
            "clover",
            "diamond",
        ]
        
    def run(self):
        self.openMenu()
        self.window.mainloop()
        
    def resetScreen(self):
        def destroyAttr(name):
            if(hasattr(self, name)):
                for key in getattr(self, name).keys():
                    if key in getattr(self, name):
                        getattr(self, name)[key].destroy()
                delattr(self, name)
        destroyAttr("menu")
        destroyAttr("placeBetWindow")
        destroyAttr("hiloselectioWindow")
            
    def openMenu(self):
        self.resetScreen()
        title = addLabel(self.window, "Click 'Play' To Start The Game", {"relx":0.5, "rely":0.3, "anchor":"center"})
        buttonToStart = addButton(self.window, "Play", {"relx":0.5, "rely":0.5, "anchor":"center"}, self.placeBet)
        self.menu = {
            "title": title, 
            "buttonToStart": buttonToStart
        }
        
    def placeBet(self):
        self.resetScreen()
        backToMenu = addButton3(self.window, "< Back", {"x":5, "y":5}, self.openMenu)
        currentMoney = addLabel3(self.window, f"Current Money: {self.money}", {"x":75, "y":5})
        title = addLabel2(self.window, "Place A Bet", {"relx":0.5, "rely":0.3, "anchor":"center"})
        def buttonStartCheck():
            if(self.bet > 0):
                self.money -= self.bet
                self.hiloselection()
        buttonToStart = addButton(self.window, "Bet", {"relx":0.5, "rely":0.5, "anchor":"center"}, buttonStartCheck)
        betInput = addInput2(self.window, {"relx":0.5, "rely":0.4, "anchor":"center"})
        def onInput(event):
            try:   
                self.bet = int(betInput.get())
            except ValueError:
                True
        betInput.bind("<KeyRelease>", onInput)
        
        self.placeBetWindow = {
            "backToMenu": backToMenu,
            "currentMoney": currentMoney, 
            "title": title,
            "buttonToStart": buttonToStart,
            "betInput":betInput,
        }
        
    def hiloselection(self):
        self.resetScreen()
        currentMoney = addLabel3(self.window, f"Current Money: {self.money}", {"x":75, "y":5})
        buttonHigh = addButton(self.window, "High", {"relx":.45, "rely":.7, "anchor":"center"}, lambda: result(self, "high"))
        buttonLow = addButton(self.window, "Low", {"relx":.55, "rely":.7,"anchor":"center"}, lambda: result(self, "low"))
        cardValueIndex = random.randint(0, 12)
        cardTypeIndex = random.randint(0, 3)
        imageLink1 = f"cards/{self.cardTypes[cardTypeIndex]}_{self.cardValues[cardValueIndex]}.png"
        
        image1 = addImage(self.window, imageLink1, {"relx":.4, "rely":.4,"anchor":"center"})
        middleMan = addLabel_XL(self.window, "X", {"relx":.5, "rely":.4,"anchor":"center"})
        image2 = addImage(self.window, "cards/back_card.png", {"relx":.6, "rely":.4,"anchor":"center"})
        
        self.hiloselectioWindow = {
            "currentMoney":currentMoney,
            "buttonHigh": buttonHigh, 
            "buttonLow": buttonLow,
            "image1":image1,
            "image2":image2,
            "middleMan":middleMan,
        }
        def result(self, highOrLow):
            next_cardValueIndex = random.randint(0, 12)
            next_cardTypeIndex = random.randint(0, 3)
            imageLink2 = f"cards/{self.cardTypes[next_cardTypeIndex]}_{self.cardValues[next_cardValueIndex]}.png"
            image2.destroy()
            self.hiloselectioWindow["image2"] = addImage(self.window, imageLink2, {"relx":.6, "rely":.4,"anchor":"center"})
            buttonHigh.destroy()
            buttonLow.destroy()
            isWin = False
            if ((next_cardValueIndex > cardValueIndex) and highOrLow == "high") or ((next_cardValueIndex < cardValueIndex) and highOrLow == "low"):
                isWin = True
            if isWin:
                amountToAdd = self.bet*2
                self.money += amountToAdd
                self.hiloselectioWindow["labelResult"] = addLabel_XL(self.window, f"You Won {amountToAdd}", {"relx":.5, "rely":.65,"anchor":"center"})
            else:
                amountToLose = self.bet*2
                self.money -= amountToLose
                self.hiloselectioWindow["labelResult"] = addLabel_XL(self.window, f"You Lose {amountToLose}", {"relx":.5, "rely":.65,"anchor":"center"})
                
            self.hiloselectioWindow["buttonDone"] = addButton(self.window, "Bet Again", {"relx":0.5, "rely":0.8, "anchor":"center"}, self.placeBet)
            
        
