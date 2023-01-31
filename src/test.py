from openpyxl import load_workbook

file_name = 'C:/Users/jrmachado/Downloads/Ford GVOSS PDP Configurator Sub Builds 2023 DESAI pricing 10-6-22 (1).xlsx'
sheet_name = '400A CPDP'
work_book = load_workbook(file_name, data_only=False)
work_sheet = work_book[sheet_name]
test = work_sheet["B4:B201"]
for x in test:
    if(x[0].value is None):
        continue
    print(x[0].value)