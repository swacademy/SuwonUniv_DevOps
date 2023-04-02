def student_sort(list_):
    list_.sort( 
        key = lambda student : student.tot, 
        reverse=True
    )