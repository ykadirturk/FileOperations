import pandas as pd

class FileOperation:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def write_file(self, data):
        with open(self.file_path, 'w') as file:
            file.write(data)
        return True

    def append_file(self, data):
        with open(self.file_path, 'a') as file:
            file.write(data + '\n')
        return True

    def read_csv(self):
        return pd.read_csv(self.file_path)

    def write_csv(self, data):
        data.to_csv(self.file_path, index=False)
        return True

    def create_excel(self):
        pd.DataFrame().to_excel(self.file_path, index=False)
        return True

    def write_columns_and_rows(self, columns, rows):
        data = pd.DataFrame(columns = columns)
        for row in rows:
            data = data._append(pd.Series(row, index = columns), ignore_index = True)
        data.to_excel(self.file_path, index=False)
        return True

    def read_excel(self):
        return pd.read_excel(self.file_path)

    def read_only_columns(self, columns):
        return pd.read_excel(self.file_path, usecols=columns)

    def read_only_rows(self, rows):
        return pd.read_excel(self.file_path, nrows=rows)

    def write_excel(self, data):
        data.to_excel(self.file_path, index=False)
        return True
