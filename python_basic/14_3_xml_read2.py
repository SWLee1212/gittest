import urllib.request
from bs4 import BeautifulSoup

with open("US08621662-20140107.xml", "r", encoding="cp949") as patent_xml:
    xml = patent_xml.read()         # file 내용을 string으로 읽어오기

soup = BeautifulSoup(xml,"lxml")

invention_title_tag = soup.find("invention-title")
# print(invention_title_tag.get_text())


publication_reference_tag = soup.find("publication-reference")
# print(publication_reference_tag.get_text())
p_document_id_tag = publication_reference_tag.find("document-id")
p_country = p_document_id_tag.find("country").get_text()
p_doc_number= p_document_id_tag.find("doc-number").get_text()
p_kind = p_document_id_tag.find("kind").get_text()
p_date = p_document_id_tag.find("date").get_text()

# print(p_document_id_tag)
print(p_doc_number)
print(p_country)
print(p_kind)
print(p_date)
