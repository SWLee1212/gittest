# Excel에서 csv 변환된 파일 처리

line_counter = 0            # 파일의 총 줄수를 세수 변수
data_header = []            # data의 필드값을 저장하는 list
customer_list = []          # customer 개별 list를 저장하는 list
customer_USA_list = []      # 국적이 미국인 사람 리스트
customoer = None

with open("customers.csv") as customer_data : # customers.csv파일을 customer_data객체에 저장
    while True:
        data = customer_data.readline() # customers.csv 파일을 한줄씩 data 변수에 저장
        if not data:                    # data가 없으면 loop를 종료함
            break

        if line_counter == 0:
            data_header = data.split(",")
        else:
            customer_list.append(data.split(","))

        customer = data.split(",")
        if customer[10].upper() == "USA":
            customer_USA_list.append(customer)

        line_counter =1

# print("Header : \t", data_header)
# for i in range(10):
#     print("Data", i, ": ",customer_list[i])

for i in customer_USA_list:
    print(i)
with open("customer_USA_only.csv","w") as customoer_USA_only_csv:
    customoer_USA_only_csv.write(",".join(data_header).strip("\n")+"\n")
    for customer in customer_USA_list :
        print(customer)
        customoer_USA_only_csv.write(",".join(customer).strip("\n")+"\n")
        # ",".join(customer)는 리스트 변수를 ","로 구분되는 string 변수로 변환
