from tkinter import*
from selenium import webdriver
import time
# from time import strftime


root = Tk()
root.title("Masud Search Box")
root.geometry("1600x1600")
root.configure(background = "#C1B2AF")


x = StringVar()

def query():

    PATH = 'C:\drivers/chromedriver.exe'

    driver = webdriver.Chrome(PATH)

    driver.get('https://www.'+x.get()+".com")


    time.sleep(5)

    driver.close()



topframe = Frame(root, width=1600, bg="#C1B2AF")
topframe.pack(side=TOP)



e1 = Entry(root, width = 30, font = "Algerian 30 bold", textvariable = x)
e1.pack()

searchbtn = Button(root, text="Search",font = "Algerian 20 bold", command = query)
searchbtn.pack()


# def time(): 
#     string = strftime('%H:%M:%S %p') 
#     lbl.config(text = string) 
#     lbl.after(1000, time) 
  
# # Styling the label widget so that clock 
# # will look more attractive 
lbl = Label(topframe, text="Masud Search Engine", font = ('calibri', 90, 'bold'), 
           
            foreground = '#A054D4',  bg="#C1B2AF") 
  
# # Placing clock at the centre 
# # of the tkinter window 
lbl.pack(pady=(0,100))
# time()

root.mainloop()