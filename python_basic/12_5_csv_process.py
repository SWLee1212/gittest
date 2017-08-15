# csv 처리 모듈을 활용하여 csv 데이터 처리 하기

import csv

header = []
rownum = 0;
seoung_nam_data = []

with open("korea_floating_population_data.csv","r",encoding="cp949") as p_file:
    csv_data = csv.reader(p_file)
    for row in csv_data:
        if rownum == 0:
            header = row

        location = row[7]

        if location.find(u"성남시") != -1:                 # 한글처리 할때 u 붙여야 함, unicode의 u, -1이면 존재 하지 않는다는 의미
            seoung_nam_data.append(row)                   # -1 존재 하지 않지 않을 때?, 곧 존재할 때

        rownum +=1

# for i in seoung_nam_data :
#     print(i)

with open("seoung_nam_floating_population_data.csv","w",encoding="utf8") as s_p_file:
    writer = csv.writer(s_p_file, delimiter=",",quotechar="'",
    lineterminator="\n", quoting = csv.QUOTE_ALL)

    writer.writerow(header)
    for row in seoung_nam_data:
        writer.writerow(row)
