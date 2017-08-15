import os
from bs4 import BeautifulSoup

patent_info = []
patent_infos = []
file_list = os.listdir("./output")

print(file_list)
for file_name in file_list:
    if ".XML" in file_name :

        # print(file_name)

        with open(file_name,"r", encoding="cp949") as my_file:
            xml_content = "".join(my_file.readlines())                     # file 내용을 string으로 읽어오기

            # print(xml_content)
            soup = BeautifulSoup(xml_content,"lxml")

            #
            invention_title_tag = soup.find("invention-title")
            invention_country_tag = soup.find("country")
            invention_doc_number_tag = soup.find("doc-number")
            invention_kind_tag = soup.find("kind")
            invention_date_tag = soup.find("date")

            print(invention_title_tag.get_text())
            print(invention_country_tag.get_text())
            print(invention_doc_number_tag.get_text())
            print(invention_kind_tag.get_text())
            print(invention_date_tag.get_text())

            patent_info.append(invention_title_tag.get_text())
            patent_info.append(invention_country_tag.get_text())
            patent_info.append(invention_doc_number_tag.get_text())
            patent_info.append(invention_kind_tag.get_text())
            patent_info.append(invention_date_tag.get_text())

            patent_infos.append(patent_info)
