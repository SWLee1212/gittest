with open("i_have_a_dream.txt","r") as my_file :
    contents = my_file.read()
    word_list = contents.split(" ")
    line_list = contents.split("\n")

for index in line_list:
    if index != '\n' and index != "":
        print(index.strip())
    #line_list.remove(" ")
    #print(len(contents), len(word_list), len(line_list))
