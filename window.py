import tkinter as tk;

bgColor = '#ece3e1'
fontXL = ("Tw Cen MT", 32 )
fontBig = ("Tw Cen MT", 20 )
fontMedium = ("Tw Cen MT", 15 )
fontSmall = ("Tw Cen MT", 10 )

def makeWindow (title):
    containerOfWindow = tk.Tk()
    containerOfWindow.title(title)
    containerOfWindow.geometry("900x400")
    containerOfWindow.configure(bg=bgColor)
    return containerOfWindow

def addLabel_XL(window, name, place):
    label = tk.Label(window, text=name, font = fontXL ,bg=bgColor, fg='black')
    label.place(**place)
    return label

def addLabel(window, name, place):
    label = tk.Label(window, text=name, font = fontBig ,bg=bgColor, fg='black')
    label.place(**place)
    return label

def addLabel2(window, name, place):
    label = tk.Label(window, text=name, font = fontMedium ,bg=bgColor, fg='black')
    label.place(**place)
    return label

def addLabel3(window, name, place):
    label = tk.Label(window, text=name, font = fontSmall ,bg=bgColor, fg='black')
    label.place(**place)
    return label
    
def addButton(window, name, place, command):
    button = tk.Button(window, text=name, font = fontMedium, bg='#dcb274',fg='black' , padx=20, command=command)
    # button.pack(padx=100)
    button.place(**place)
    return button

def addButton2(window, name, place, command):
    button = tk.Button(window, text=name, font = fontMedium, bg='#dcb274',fg='black' , padx=10, pady=0, command=command)
    # button.pack(padx=100)
    button.place(**place)
    return button
def addButton3(window, name, place, command):
    button = tk.Button(window, text=name, font = fontSmall, bg='#dcb274',fg='black' , padx=10, pady=0, command=command)
    # button.pack(padx=100)
    button.place(**place)
    return button

def addInput2(window, place):
    input = tk.Entry(window,font =fontMedium, fg='black')
    # input.insert(0, 0)
    input.place(**place)
    return input

def addImage(window, imagePath, place, scale=1):
    image = tk.PhotoImage(file=imagePath)
    def scaleImage(image, size):
        oldWidth = image.width()
        oldHeight = image.height()
        newWidth = int(oldWidth*size)
        newHeight = int(oldHeight*size)
        newPhotoImage = tk.PhotoImage(width=newWidth, height=newHeight)
        for x in range(newWidth):
            for y in range(newHeight):
                xOld = int(x*oldWidth/newWidth)
                yOld = int(y*oldHeight/newHeight)
                rgb = '#%02x%02x%02x' % image.get(xOld, yOld)
                newPhotoImage.put(rgb, (x, y))
        return newPhotoImage    
    label = tk.Label(window, image=image)
    label.image = image
    label.place(**place)
    return label
    
def addGroup(window, place):
    group = tk.Frame(window, height="200px", width="200px")  
    group.pack(padx=10, pady=10, expand=True)
    return group