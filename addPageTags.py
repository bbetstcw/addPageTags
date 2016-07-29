from os import listdir
from os.path import isfile, join
from FileReader import FileReader
from TagFinder import TagFinder
from LinkSearcher import LinkSearcher
mypath = "./input/articles/"
outputPath = "./output/articles/"

for f in listdir(mypath):
    fileReader = FileReader()
    linkSearcher = LinkSearcher()
    tagFinder = TagFinder()
    print("processing file: "+f)
    if isfile(join(mypath,f)):
        lines = fileReader.readLines(mypath+f)
        (lines, links) = linkSearcher.getLinks(lines)
        lines = tagFinder.replaceTags(links, lines)
        file = open(outputPath+f, 'w', encoding="utf8")
        file.writelines(lines)
        file.close()