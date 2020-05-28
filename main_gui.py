from tkinter import *
from new_main import semaphore_algo

window = Tk()
window.title("Timetable Generation OS Project")


class ProvideException(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args):
        try:
            return self._func(*args)
        except ValueError:
            text7 = Label(window, text="Please enter integer values only")
            text7.grid(row=7, column=0)
        except KeyboardInterrupt:
            text7 = Label(window, text="You hit a interrupt key like ' ctrl+c' or 'ctrl+v'. Please rerun the code.")
            text7.grid(row=7, column=0)

@ProvideException
def set_values():
    list_1 = [label3_1.get(), label3_2.get(), label3_3.get(), label3_4.get()]       #Batch 1
    list_2 = [label4_1.get(), label4_2.get(), label4_3.get(), label4_4.get()]       #Batch 2
    list_3 = [label5_1.get(), label5_2.get(), label5_3.get(), label5_4.get()]       #Batch 3
    list_4 = [label6_1.get(), label6_2.get(), label6_3.get(), label6_4.get()]       #Batch 4
    final_list = [list_1, list_2, list_3, list_4]
    print(list_1)
    print(list_2)
    print(list_3)
    print(list_4)
    print(final_list)

    fac_list_1 = []                 # Number of lectures by each batch
    fac_list_2 = []
    fac_list_3 = []
    fac_list_4 = []

    for faculty_no in range(0, 4):
        x = int(final_list[faculty_no][0])
        for hour_cnt in range(0, x):
            fac_list_1.append(faculty_no)

        x1 = int(final_list[faculty_no][1])
        for hour_cnt in range(0, x1):
            fac_list_2.append(faculty_no)

        x2 = int(final_list[faculty_no][2])
        for hour_cnt in range(0, x2):
            fac_list_3.append(faculty_no)

        x3 = int(final_list[faculty_no][3])
        for hour_cnt in range(0, x3):
            fac_list_4.append(faculty_no)

    print(fac_list_1)
    print(fac_list_2)
    print(fac_list_3)
    print(fac_list_4)

    semaphore_algo(fac_list_1, fac_list_2, fac_list_3, fac_list_4)


text1 = Label(window, text="Enter the faculty hours required for each branch")
text1.grid(row=0)

text2 = Label(window, text="Branch Name")
text2_1 = Label(window, text="Faculty 1")
text2_2 = Label(window, text="Faculty 2")
text2_3 = Label(window, text="Faculty 3")
text2_4 = Label(window, text="Faculty 4")
text2.grid(row=1, column=0)
text2_1.grid(row=1, column=1)
text2_2.grid(row=1, column=2)
text2_3.grid(row=1, column=3)
text2_4.grid(row=1, column=4)

text3 = Label(window, text="B.Tech CS")
label3_1 = Entry(window)
label3_2 = Entry(window)
label3_3 = Entry(window)
label3_4 = Entry(window)
text3.grid(row=2, column=0)
label3_1.grid(row=2, column=1)
label3_2.grid(row=2, column=2)
label3_3.grid(row=2, column=3)
label3_4.grid(row=2, column=4)

text4 = Label(window, text="B.Tech IT")
label4_1 = Entry(window)
label4_2 = Entry(window)
label4_3 = Entry(window)
label4_4 = Entry(window)
text4.grid(row=3, column=0)
label4_1.grid(row=3, column=1)
label4_2.grid(row=3, column=2)
label4_3.grid(row=3, column=3)
label4_4.grid(row=3, column=4)

text5 = Label(window, text="MBA.Tech CS")
label5_1 = Entry(window)
label5_2 = Entry(window)
label5_3 = Entry(window)
label5_4 = Entry(window)
text5.grid(row=4, column=0)
label5_1.grid(row=4, column=1)
label5_2.grid(row=4, column=2)
label5_3.grid(row=4, column=3)
label5_4.grid(row=4, column=4)

text6 = Label(window, text="MBA.Tech IT")
label6_1 = Entry(window)
label6_2 = Entry(window)
label6_3 = Entry(window)
label6_4 = Entry(window)
text6.grid(row=5, column=0)
label6_1.grid(row=5, column=1)
label6_2.grid(row=5, column=2)
label6_3.grid(row=5, column=3)
label6_4.grid(row=5, column=4)

button1 = Button(window, text="Submit Request", command=set_values)
button1.grid(row=6, column=2)

window.mainloop()