import FileOperation

file_operation = FileOperation.FileOperation('file.xlsx')
file_operation.write_columns_and_rows(['Name', 'Age'], [['John', 25], ['Doe', 30]])

data = file_operation.read_excel()
print(data)

if 'John' in data.values:
    print('John exists')

# file_operation = FileOperation.FileOperation('data.csv')
# data = file_operation.read_csv()
# print(f"{data}\n")

# if file_operation.append_file("Hello World! Append data from main.py"):
#     print("[i] Data appended successfully")
# else:
#     print("[i] Failed to append data")
# print(f"{file_operation.read_file()}")

# Verinin üstünü yeniden yazar.
# text_data ="Hello World! 2 - #edited from main.py"
# if file_operation.write_file(text_data):
#    print('File written successfully')
# else:
#    print('Something went wrong')

