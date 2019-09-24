import csv


class CsveReader:
    def read(self, file_path):
        self.list = []
        with open(file_path, 'r') as csvFile:
            self.reader = csv.reader(csvFile)
            for row in self.reader:
                # print(row)
                self.list.append(row)

        csvFile.close()
        return self.list
