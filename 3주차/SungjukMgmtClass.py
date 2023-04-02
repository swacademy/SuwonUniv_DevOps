import StudentClass, StudentInputClass, StudentCalcClass, StudentOutputClass, StudentSortClass, StudentDatabaseClass
if __name__ == '__main__' : 
    print('Program is starting...')
    list_ = []
    StudentInputClass.student_input(list_)
    StudentCalcClass.student_calc(list_)
    StudentSortClass.student_sort(list_)
    StudentOutputClass.student_output(list_)
    StudentDatabaseClass.student_database(list_)
    print('Program is over...')
