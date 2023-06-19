from tkinter import messagebox
from tkinter import *

# Days Worked Options
days_options = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7
]

employees_list = []
processed_employees_list = []

# Initialize List of Employees
def InitializeEmployees():

    # Get list of employees from text file
    employees_file = open("PAYROLL\employees.txt", "r")
    for employee in employees_file:
        employees_list.append(employee.strip().split(" "))
    employees_file.close()

    # Initialize employee labels to first employee in alphabetical order
    employees_list.sort(key=lambda x: x[0])
    employeeLastName.config(text=employees_list[0][0])
    employeeFirstName.config(text=employees_list[0][1])

def ProcessEmployee():
    if employees_list:
        if len(dailyRateEntry.get()) != 0:
            if len(overtimeRateEntry.get()) != 0:

                employee = []
                employee.append(employees_list[0][0])
                employee.append(employees_list[0][1])
                employee.append(dailyRateEntry.get())
                employee.append(overtimeRateEntry.get())
                employee.append(daysWorkedVar.get())
                employee.append(overtimeHoursEntry.get())

                processed_employees_list.append(employee)
                employees_list.pop(0)
                dailyRateEntry.delete(0,END)
                overtimeRateEntry.delete(0,END)
                daysWorkedVar.set(0)
                overtimeHoursEntry.delete(0,END)
                overtimeHoursEntry.insert(0, 0)
                if employees_list:
                    employeeLastName.config(text=employees_list[0][0])
                    employeeFirstName.config(text=employees_list[0][1])
                UpdateEmployees()

            else:
                messagebox.showinfo("Error", "Please enter a value for Overtime Rate")
        else:
            messagebox.showinfo("Error", "Please enter a value for Daily Rate")
    else:
        messagebox.showinfo("Error", "All employees have been processed")

def UpdateEmployees():
    currentRow = len(processed_employees_list)
    for currentCol in range(6):
        employeeData = Label(resultFrame)
        employeeData.config(text=processed_employees_list[currentRow-1][currentCol])
        employeeData.grid(row=currentRow, column=currentCol)
        print(processed_employees_list[currentRow-1][currentCol])

# Main GUI Window
window = Tk()
window.title("Vast Solutions Payroll Calculator")
window.configure(background="white smoke", padx=10)
window.geometry("1000x500")

# Payroll Result Frame
resultFrame = Frame(window, bg="white smoke")
resultFrame.grid(row=0, column=0, sticky=NW)
lastNameTitle = Label(resultFrame, text="Last Name", bg="white smoke", fg="black", font="none 12 bold")
lastNameTitle.grid(row=0, column=0, sticky=W)
firstNameTitle = Label(resultFrame, text="First Name", bg="white smoke", fg="black", font="none 12 bold")
firstNameTitle.grid(row=0, column=1, sticky=W)
dailyRateTitle = Label(resultFrame, text="Daily Rate", bg="white smoke", fg="black", font="none 12 bold")
dailyRateTitle.grid(row=0, column=2, sticky=W)
overtimeRateTitle = Label(resultFrame, text="Overtime Rate", bg="white smoke", fg="black", font="none 12 bold")
overtimeRateTitle.grid(row=0, column=3, sticky=W)
daysWorkedTitle = Label(resultFrame, text="Days Worked", bg="white smoke", fg="black", font="none 12 bold")
daysWorkedTitle.grid(row=0, column=4, sticky=W)
overtimeHoursTitle = Label(resultFrame, text="Overtime Hours", bg="white smoke", fg="black", font="none 12 bold")
overtimeHoursTitle.grid(row=0, column=5, sticky=W)


# Employee Processing Frame
employeeProcessingFrame = Frame(window, bg="white smoke", padx=10)
employeeProcessingFrame.grid(row=0, column=1, sticky=E)

# Title Frame
titleFrame = Frame(employeeProcessingFrame, bg="white smoke")
titleFrame.grid(row=0, column=0, sticky=W)
titleLabel = Label(titleFrame, text="Payroll Calculator", bg="white smoke", fg="black", font="none 12 bold")
titleLabel.grid(row=0, column=0, sticky=W)

# Employee Frame
employeeFrame = Frame(employeeProcessingFrame, bg="white smoke")
employeeFrame.grid(row=1, column=0, sticky=W)
employeeLabel = Label(employeeFrame, text="Employee: ", bg="white smoke", fg="black", font="none 10")
employeeLabel.grid(row=0, column=0, sticky=W)
employeeLastName = Label(employeeFrame, anchor=E, textvariable="", bg="white smoke", fg="black", font="none 10")
employeeLastName.grid(row=0, column=1, sticky=W)
employeeFirstName = Label(employeeFrame, anchor=E, textvariable="", bg="white smoke", fg="black", font="none 10")
employeeFirstName.grid(row=0, column=2, sticky=W)

# Daily Rate Input Frame
dailyRateFrame = Frame(employeeProcessingFrame, bg="white smoke")
dailyRateFrame.grid(row=2, column=0, sticky=W)
dailyRateLabel = Label(dailyRateFrame, text="Enter Daily Rate:", bg="white smoke", fg="black", font="none 10")
dailyRateLabel.grid(row=0, column=0, sticky=W)
dailyRateEntry = Entry(dailyRateFrame, width=10, bg="white smoke", fg="black", font="none 8")
dailyRateEntry.grid(row=0, column=1, sticky=W)

# Overtime Hourly Rate Input Frame
overtimeRateFrame = Frame(employeeProcessingFrame, bg="white smoke")
overtimeRateFrame.grid(row=3, column=0, sticky=W)
overtimeRateLabel = Label(overtimeRateFrame, text="Enter Overtime Hourly Rate:", bg="white smoke", fg="black", font="none 10")
overtimeRateLabel.grid(row=0, column=0, sticky=W)
overtimeRateEntry = Entry(overtimeRateFrame, width=10, bg="white smoke", fg="black", font="none 8")
overtimeRateEntry.grid(row=0, column=1, sticky=W)

# Days Worked Input Frame
daysWorkedFrame = Frame(employeeProcessingFrame, bg="white smoke")
daysWorkedFrame.grid(row=4, column=0, sticky=W)
daysWorkedLabel = Label(daysWorkedFrame, text="Enter Days Worked this Week:", bg="white smoke", fg="black", font="none 10")
daysWorkedLabel.grid(row=0, column=0, sticky=W)
daysWorkedVar = IntVar()
daysWorkedVar.set(0)
daysWorkedEntry = OptionMenu(daysWorkedFrame, daysWorkedVar, *days_options)
daysWorkedEntry.grid(row=0, column=1, sticky=W)

# Overtime Hours Input Frame
overtimeHoursFrame = Frame(employeeProcessingFrame, bg="white smoke")
overtimeHoursFrame.grid(row=5, column=0, sticky=W)
overtimeHoursLabel = Label(overtimeHoursFrame, text="Enter Overtime Hours:", bg="white smoke", fg="black", font="none 10")
overtimeHoursLabel.grid(row=0, column=0, sticky=W)
overtimeHoursEntry = Entry(overtimeHoursFrame, width=10, bg="white smoke", fg="black", font="none 8")
overtimeHoursEntry.insert(0, 0)
overtimeHoursEntry.grid(row=0, column=1, sticky=W)

# Submit Button
submitButton = Button(employeeProcessingFrame, text="Submit", command=ProcessEmployee, relief="raised")
submitButton.grid(row=6, column=0, sticky=W)

InitializeEmployees()
window.mainloop()
