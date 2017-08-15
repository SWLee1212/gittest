# 예제 파일 검색 프로그램

def fk(SearchKey):              #FindKeyword
    import os
    os.system('cls')  # on windows

    PyFiles = []
    
    for root, dirs, files in os.walk("./"):
        for name in files:
            if ".py" in name and ".pyc" not in name:
                PyFiles.append(os.path.join(root, name))

    for PyFile in PyFiles :
        SearchResult = []

        with open(PyFile ,"rt", encoding="utf8") as my_file :
            contents = my_file.read()
            line_list = contents.split("\n")

        i=1
        KeyMatch = False

        for line in line_list:
            if SearchKey in line:
                SearchResult.append([i, line.strip()])
            i+=1
        else:
            if SearchResult != []: KeyMatch = True

        if KeyMatch == True:
            print("\n\n",PyFile)
            for line in SearchResult:
                print(line[0],"line: ", line[1])
