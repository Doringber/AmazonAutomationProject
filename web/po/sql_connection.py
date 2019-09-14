import sqlite3

result_list = []
list_three = []

try:
    con = sqlite3.connect('/Users/doringber/PycharmProjects/homework/amazon/web/po/test.db')

    # print("open Database !!")
except Exception as e:
    print("The problem: " + str(e))

results_pixel = con.execute("SELECT * FROM Person where NAME = 'Pixel' or NAME = 'redmi 6'")


for row in results_pixel:
    if row is not None:
        result_list.append(row)


for i in result_list:
    list_three.append(i[1])

if list_three[0] == 'Pixel':
    ENTER_TEXT_SQL_PIXEL = list_three[0]
    if list_three[1] == 'redmi 6':
        ENTER_TEXT_SQL_REDMI = list_three[1]
else:
    print("There is a problem with the list text ")

con.close()







