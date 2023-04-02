# import StudentClass

# def student_input(list_):
#     while True : 
#         hakbun = input('학번 : ')
#         name = input('이름 : ')
#         kor = int(input('국어 : '))
#         eng = int(input('영어 : '))
#         math = int(input('수학 : '))
#         edps = int(input('전산 : '))
#         student = StudentClass.Student(hakbun, name, kor, eng, math, edps)
#         list_.append(student)
#         y_n = input('Again(y/n) ? : ')
#         if y_n.upper() != 'Y' : break
        
# import json, StudentClass 

# def student_input(list_):
#     try:
#         data = open('sungjuk.json').read()
#         sungjuklist_ = json.loads(data)
#         for dict_ in sungjuklist_ :
#             student = StudentClass.Student(dict_['hakbun'], dict_['irum'], dict_['kor'], dict_['eng'], dict_['mat'], dict_['edp'])
#             list_.append(student)
#     except Exception as err :
#         print(err)