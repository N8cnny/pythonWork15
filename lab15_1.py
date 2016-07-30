from tkinter import *
import InputBox

def exeIt(sql):
    import mysql.connector
    s = "Result:\n"
    conn = mysql.connector.connect(user='tcm159', password='sGkY4651',
    host='localhost', database='customers')

    if conn.is_connected():
        qry = conn.cursor()
        qry.execute(sql)

        tbl = qry.fetchall()
        if len(tbl) > 0:
            for row in tbl:
                s += row[0] + " " + row[1] + " " + row[2] + " " + row[3] + "\n"
        else:
            s = "Not record found."

    conn.close()

    root = Tk()

    root.title('Message Box')
    Label(root, justify=LEFT, text=s).grid()

    root.mainloop()

if __name__ == '__main__':
    InputBox.ShowDialog("Enter an SQL statement:")
    sql = InputBox.GetInput()

    exeIt(sql)
