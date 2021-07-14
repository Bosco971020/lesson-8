apple=0
bapplem=0
m=0
summ=0
sum=0
start=0
sapple=0
sapplenn=0
ssapple_list=[]
bapple_list=[]
apple_list=[]
sapple_list=[]
applesm=0
print('在系統開始前請先設定基本資料')
apple=int(input('目前有幾顆蘋果呢?'))
m=int(input('今天的蘋果要賣多少錢?'))
while start==0:
    if apple==0:
        print('已經沒有蘋果了!')
    x=input('你要系統協助什麼事情呢?')
    if x == '設定' or x== 'gk42u/4':
        m=int(input('今天的蘋果要賣多少錢?'))
        print('設定完成')
    elif x == '進貨' or x== 'rup4cji4':
        y=int(input('今天新進了幾顆蘋果呢?'))
        apple=apple+y
        bapplem=int(input('進的每一顆蘋果花了多少錢呢?'))
        print('你共花了',bapplem*y,'元')
        bapple_list.append(bapplem*y)
        apple_list.append(bapplem)
        applesm=applesm-bapplem
        sapplenn=sapplenn+1
        print('交易完成')
    elif x == '出貨' or x== 'tj cji4':
        sum=int(input('今天賣出了幾顆蘋果呢?'))
        summ=sum*m
        if sum>apple:
            print('你的庫存不夠喔!')
        else:
            print('以上的買賣要收',summ,'元')
            sapple=sapple+sum
            sapple_list.append(summ)
            ssapple_list.append(sum)
            applesm=applesm+summ
            sapplenn=sapplenn+1
            apple=apple-sum
            print('交易完成')
    elif x == '營業額統計' or x == 'u/6u,4k6wj/3ru4':
         print('今天有',sapplenn,'筆交易呢')
         print('賣蘋果的交易金額紀錄為',sapple_list,'/元')
         print('進貨蘋果的交易金額紀錄為',bapple_list,'/元')
         print('進貨蘋果的交易顆數為',apple_list)
         print('賣蘋果的交易顆數為',ssapple_list)
         print('目前營業額為',sum(sapple_list))
         print('目前利潤為',applesm)
    elif x == '庫存統計' or x == 'dj4hjp6wj/3ru4':
         print('你的庫存內還有', apple ,'顆蘋果')
         print('統計完成')
    elif x == '離開系統' or x == 'xu6d9 vu4wj/3':
         print('你已離開系統')
         start=1
    else:
         print('此功能尚開發中')