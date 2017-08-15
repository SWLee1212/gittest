import json

with open("json_example.json","r",encoding="utf8") as f:

    contents = f.read()                 #json 파일을 String 형태로 읽어드림
    json_data = json.loads(contents)    # String 파일을 json 형식의 클래스 화함
    # print(json_data["employees"])       # dict type employees json 데이터를 리스트 형으로 불러드림

    print(json_data["employees"][0]["firstName"])
    for content in json_data["employees"]:
        print(content)
        print(content["firstName"], content["lastName"])


    # print(json_data.keys())
