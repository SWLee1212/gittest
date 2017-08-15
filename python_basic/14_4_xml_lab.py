def WriteToFile(PatentDoc, Filename):
    import os
    if not os.path.exists("output"):
         os.makedirs("output")

    Filename = Filename.replace("XML","csv")
    Filefullname = "output/" + Filename
    with open(Filefullname,"w", encoding="utf8") as my_file:
        for content in PatentDoc:
            my_file.write(content)

def getPatentNumber(patent_document):
    import re

    for line in patent_document:
        if "file=" in str(line):
            file_name_pattern = re.search(r"(US)([0-9])+(A1-)([0-9])+(.)(XML|xml)", line)
            file_name = file_name_pattern.group()
            return file_name

    return 0

with open("ipa110106.XML", "r", encoding="utf8") as patent_xml:
    line = patent_xml.readlines()         # file 내용을 string으로 읽어오기

    StartLineNum = 0
    Counter = 0
    PatentDoc = []

    for index in line:

        if "xml version" in index and Counter != 0:
            PatentDoc = line[StartLineNum:Counter-1]
            StartLineNum = Counter
            filename = getPatentNumber(PatentDoc)
            WriteToFile(PatentDoc, filename)
        Counter += 1

    PatentDoc = line[StartLineNum:Counter-1]
    filename = getPatentNumber(PatentDoc)
    WriteToFile(PatentDoc, str(filename))
