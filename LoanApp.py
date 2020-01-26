print("Python code starting.")
print("This application developed in Python by Galen Schatzman.")
from tkinter import *
from tkinter import messagebox
from decimal import *


HEIGHT=350
WIDTH=360

root = Tk()
root.title("Auto Loan Calculator")
root.iconbitmap = (r'.\icons8carbadge.ico')
#Car Badge icon by Icons8

def calculate(entryLA, entryIR, entryLT):

    #print("Calculate Button Pressed " + entryLA + " " + entryIR + " " + entryLT)

    try:
    #Convert String Value to Decimal Below
        entryLA = Decimal(entryLA)
        entryIR = Decimal(entryIR)
        entryLT = Decimal(entryLT)
    

        interestRate = (entryIR / 100)
        interestRate = Decimal(interestRate)
        monthCalc = (entryLT * 12)
        monthCalc = Decimal(monthCalc)
        interestXComp = (interestRate / 1)
        interestXComp = Decimal(interestXComp)
        a = (1 + interestXComp)
        b = (1 * entryLT)
        #POW = pow(a,b) Line 23 is also a exponential expression
        POW = (a**b)
        totalCost = (entryLA * POW)
        tc = round(totalCost, 2)
        interestCost = (totalCost - entryLA)
        ic = round(interestCost, 2)
        monthly = (totalCost / monthCalc)
        m = round(monthly, 2)

        #Below line prevents users from using decimal format loan term in years and getting back decimal formatted months of loan term
        monthCalc = round(monthCalc, 0)

        #Convert above decimal values to strings in order to print below
        tc = str(tc)
        ic = str(ic)
        m = str(m)
        monthCalc = str(monthCalc)
        entryLA = str(entryLA)

        print(tc + " " + ic + " " + m)

        labelar['text'] = "Amount Requested: $" + entryLA
        labeltc['text'] = "Total Cost of Loan: $" + tc
        labelic['text'] = "Interest on this loan will cost you: $" + ic
        labelmc['text'] = "Minimum Monthly Payment: $" + m
        labelm['text'] = "You will pay this loan off in " + monthCalc + " months"
    except:
        messagebox.showwarning("Auto Loan Calculator", "Please Enter Numbers and Number Formats only.")
        



canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(root, bg="#B2ACAC")
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

labelLA = Label(frame, text="Enter Loan Amount Below", bg="#B2ACAC")
labelLA.place(x = 110, y = 5)

entryLA = Entry(frame, justify='center')
entryLA.place(x = 120, y = 30)

labelIR = Label(frame, text="Enter Interest Rate Below (i.e. 4.49)", bg="#B2ACAC")
labelIR.place(x = 88, y = 55)

entryIR = Entry(frame, justify='center')
entryIR.place(x = 120, y = 80)

labelLT = Label(frame, text="Enter Term of Loan in Years Below", bg="#B2ACAC")
labelLT.place(x = 88, y = 105)

entryLT = Entry(frame, justify='center')
entryLT.place(x = 120, y = 130)

calcButton = Button(frame, text="Calculate Loan", bg='green', fg='white', command=lambda: calculate(entryLA.get(), entryIR.get(), entryLT.get()))
#alcButton = Button(frame, text="Calculate Loan", bg='orange', fg='white', command=lambda: calculate(entryLA.get(), entryIR.get(), entryLT.get()))
calcButton.place(x = 138, y = 155)

labelar = Label(frame, bg="#B2ACAC")
labelar.place(x = 88, y = 180)

labeltc = Label(frame, bg="#B2ACAC")
labeltc.place(x = 88, y = 205)

labelic = Label(frame, bg="#B2ACAC")
labelic.place(x = 88, y = 230)

labelmc = Label(frame, bg="#B2ACAC")
labelmc.place(x = 88, y = 255)

labelm = Label(frame, bg="#B2ACAC")
labelm.place(x = 88, y = 280)


root.mainloop() 