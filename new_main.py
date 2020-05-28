from quantum_time_splitter import quantum_splitter
from writing_excel import write

def semaphore_algo(f1,f2,f3,f4):
    fac_list=[]
    faculty_list = [[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                    ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                    ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                    ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                    ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                    ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                    ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
                    ,[[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]]     # [Hour of Day][Day of Week][Faculty]

    fac_list.append(quantum_splitter(f1))
    fac_list.append(quantum_splitter(f2))
    fac_list.append(quantum_splitter(f3))
    fac_list.append(quantum_splitter(f4))

    print('============================   REQUIREMENT HOURS   ==================================')

    for i in range(4):
        print(fac_list[i])

    flag = 0

    print('==============================   ALLOCATED TIMETABLE   ================================')

    for hour in range(0, 8):
        if flag == 1:
            break
        for day in range(0, 5):
            if len(fac_list[0]) == 0 and len(fac_list[1]) == 0 and len(fac_list[2]) == 0 and len(fac_list[3]) == 0:
                flag = 1
                break

            semaphore_list = []

            for i in range(4):
                if len(fac_list[i]) > 0:
                    try:
                        for x in range(0, 4):
                            if fac_list[i][x] not in semaphore_list:
                                faculty_list[hour][day][i] = fac_list[i][x]
                                semaphore_list.append(fac_list[i][x])
                                fac_list[i].pop(x)
                                break
                    except IndexError:
                        pass

    for hour in range(0, 8):
        print(faculty_list[hour])

    write(faculty_list)