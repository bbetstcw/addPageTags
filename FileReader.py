class FileReader(object):
    def __init__ (self):
        return

    def readLines(self, filename):
        file = open(filename, "r", encoding="utf8")
        lines = file.readlines()
        file.close()
        wholeFile = ""
        for line in lines:
            wholeFile+=line
        return wholeFile


