# xml 변환 예제

from bs4 import BeautifulSoup

with open("books.xml","r", encoding="cp949") as books_file:
    books_xml = books_file.read()           # File을 String으로 읽기

soup = BeautifulSoup(books_xml, "lxml")     # lxml Parser를 이용해서 데이터 분석
                                            # BeautifulSoup는 xml을 파일을 String으로 변환한 파일 lxml이라는 parser를 활용하여
                                            # soup클래스로 반환
# soup는 bs4.BeautifulSoup라는 클래스
# print(type(soup))

# Author가 들어간 모든 element 추출

for book_info in soup.find_all("author"):
    # print(type(book_info))                  # book_info는 bs4.BeautifulSoup라는 클래스 형
    print(book_info)                        # author과 /author 가 들어간 줄을 찾음
    print(book_info.get_text())
