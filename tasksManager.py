import re
import xlsxwriter

def handleTask(query_result, order="yes"):

    valid = {"yes": True, "y": True, "ye": True,
    "no": False, "n": False}

    if valid[order]:
        print("Would you give a name for the file?")
        file_Name = input( 'name = ')
        if file_Name  == "":
            file_Name = 'untitled_file.xlsx'
        else:
            file_Name += '.xlsx'
        #creation of a excel workbook:
        workbook =  xlsxwriter.workbook(file_Name)
        worksheet = workbook.add_worksheet()

        #row / col:
        row = 0
        col = 0

        #iteration of query result:
        for x in query_result.fetchall():
            for y in x:
                worksheet.write(row, col, x)
                worksheet.write(row, col +1, y)
                row += 1

        workbook.close()
    else:
        raise ValueError('invalid input.')
