# pip install mysql-connector-python
import mysql.connector

def student_database(list_):
    host = ''
    port = 3306
    user = 'root'
    password = 'pythonmysql'
    database = 'mycompany'
    try:
        dbconn = mysql.connector.connect(host=host, port=port, user=user, password=password, database=database)
        cursor = dbconn.cursor()
    #     sql = """
    # CREATE TABLE Student(
    #     hakbun CHAR(4)  PRIMARY KEY,
    #     name  VARCHAR(20)  NOT NULL,
    #     korean TINYINT  NOT NULL,
    #     english TINYINT  NOT NULL,
    #     math   TINYINT   NOT NULL,
    #     edps   TINYINT   NOT NULL,
    #     tot    SMALLINT,
    #     avg    FLOAT(5, 2),
    #     grade  CHAR(1)
    # )
    #     """
        for student in list_ : 
            sql = "INSERT INTO mycompany.Student(hakbun, name, korean, english, math, edps, tot, avg, grade) " + \
                f"VALUES('{student.hakbun}, {student.name}', {student.kor}, {student.eng}, {student.math}, {student.edps}, {student.tot}, {student.avg}, '{student.grade}')"
            cursor.execute(sql)
        dbconn.commit()
        print('Insert Students Successfully')
    except Exception as error : 
        print(f'error = {error}')
    else : dbconn.close()
    
