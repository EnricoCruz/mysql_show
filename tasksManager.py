import xlsxwriter
import os

if __name__ == '__main__':
    print(help(xlsxwriter))

def handleTask(query_result, order="yes"):

    valid = {"yes": True, "y": True, "ye": True,
    "no": False, "n": False}

    if valid[order]:
        print("Would you give a name for the file?")
        file_name = input( 'name = ')
        if file_name  == "":
            file_name = 'untitled_file.xlsx'
        else:
            file_name += '.xlsx'
        #creation of a excel workbook:
        workbook =  xlsxwriter.Workbook(file_name)
        worksheet = workbook.add_worksheet()

        #row :
        row = 0
        for y in query_result:
            #col :

            col = 0
            ###print("===========")
            for x in y:
                ###print(str(x))
                worksheet.write(row, col, str(x))
                col += 1
            row += 1


        workbook.close()
        print("The file has ben created succesfully in " + os.getcwd() + '\\' + file_name )
    else:
        raise ValueError('invalid input.')
