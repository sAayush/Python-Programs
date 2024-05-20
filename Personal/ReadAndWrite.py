class ReadPrint:
    def __init__(self):
        self.file = open("data.txt", "r")
        self.text = self.file.read()
        self.file.close()

    def print_text(self):
        print(self.text)


if __name__ == '__main__':
    rp = ReadPrint()
    rp.print_text()