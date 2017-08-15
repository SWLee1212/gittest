import json
import os
from bs4 import BeautifulSoup

patent_document = {}
patent_info = {}
patent_infos = {}
path = "./output"
file_list = os.listdir(path)

#print(file_list)
for file_name in file_list:
    if ".csv" in file_name :

        full_filename = path+"./"+file_name
        # print(full_filename)
        with open(full_filename,"r", encoding="cp949") as my_file:
            xml_content = "".join(my_file.readlines())                     # file 내용을 string으로 읽어오기
            soup = BeautifulSoup(xml_content,"lxml")

            publication_reference_tag = soup.find("publication-reference")
            p_documment_id_tag = publication_reference_tag.find("document-id")
            p_doc_number = p_documment_id_tag.find("doc-number").get_text()
            p_country = p_documment_id_tag.find("country").get_text()
            p_kind = p_documment_id_tag.find("kind").get_text()
            p_date = p_documment_id_tag.find("date").get_text()

            patent_document["doc-number"] = p_doc_number
            patent_document["country"] = p_country
            patent_document["kind"] = p_kind
            patent_document["date"] = p_date


            application_reference_tag = soup.find("application-reference")
            a_documment_id_tag = application_reference_tag.find("document-id")
            a_doc_number = a_documment_id_tag.find("doc-number").get_text()
            a_country = a_documment_id_tag.find("country").get_text()
            a_date = a_documment_id_tag.find("date").get_text()

            patent_document["applicaton-country"] = a_country
            patent_document["application-date"] = a_date

            patent_key_value = a_doc_number
            patent_info[patent_key_value] = patent_document

            # print(patent_info)
        # patent_infos.append
print(patent_info)

full_filename = path+"./"+"patent_info.json"
with open(full_filename, "w") as f:
    json.dump(patent_info,f)
