# cmd 창에서 실행
#
# activate mypython
#
# conda install lxml
# conda install -c anaconda beautifullsoup4=4.5.1

# python shell에서 실행
from bs4 import beautifullsoup4 as bs
soup = bs(books_xml,"lxml")  #paser를 lxml로 선택

soup.find_all("author")
