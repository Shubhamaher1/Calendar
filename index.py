from tkinter import *
import calendar

def Calendar_See():
    window=Tk()
    window.config(background="black")
    window.title("Calendar")
    window.geometry("560x680")
    get_year=int(year_entry.get())
    window_content= calendar.calendar(get_year)
    year_calender=Label(window,text=window_content,font=("Arial",12,"bold"))
    year_calender.grid(row=5,column=1)
    window.mainloop()



if __name__=="__main__":
    root=Tk()
    root.config(background="yellow")
    root.title("Calender")
    root.geometry("270x270")
    name=Label(root,text="         Calendar         ",bg="pink",font=("Arial",20,"bold"))
    name.grid(row=1, column=1)
    year=Label(root,text="Year", bg="yellow",font=("Arial",15,"bold"))
    year.grid(row=2,column=1)
    year_entry=Entry(root,font=("Arial",15,"bold"))
    year_entry.grid(row=3,column=1)

    show_button=Button(root,text="Show Calendar",fg="pink", bg="black",
                    command=Calendar_See)
    show_button.grid(row=4,column=1)
    root.mainloop()