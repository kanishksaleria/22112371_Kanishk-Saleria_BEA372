def content():
    with open("Lab 1/bank.csv",'r') as data:
        content=data.readlines()
        return content
# to read the headers of the given csv file:
def header_list():
    with open("Lab 1/bank.csv",'r') as data:
        header=data.readline()
        coloumn=header.split(';')
        headers = []
        for element in coloumn:
            element = element[1:]
            element = element[:-1]
            headers.append(element)
        return headers
def coloumn():
    print("The coloumn in the given csv file is:")
    lst=header_list()
    for i in lst:
        print(f'>>>>   {i:^29}  ')


def category():
    married=0
    single =0
    divorced=0
    lst0=content()
    for i in lst0:
       coloumn=i.split(';') 
       for j in coloumn:
           if j=='"married"':
               married=married+1
           elif j=='"single"':
               single+=1
           elif j=='"divorced"':
               divorced+=1     
    return married,single,divorced

def martial_status():
    m,s,d=category()  
    print(f"Married:{m}\nSingle:{s}\nDivorced:{d}")


def life():
    lst=[]
    with open('Lab 1/bank.csv') as data:
        for line in data:
            ages = line.split(';')[0] 
            lst.append(ages)
        return lst 
    
def age_bins():
    age=life()
    age=age[1:]
    real=[]
    for j in age:
        k=int(j)
        real.append(k)
    sum=0
    hist=[0,0,0,0,0,0,0,0,0,0]
    for i in real:
        if i>0 and i<=10:
            hist[0] = hist[0]+1 
        if i>11 and i<=20:
            hist[1] = hist[1]+1 
        if i>21 and i<=30:
            hist[2] = hist[2]+1 
        if i>31 and i<=40:
            hist[3] = hist[3]+1 
        if i>41 and i<=50:
            hist[4] = hist[4]+1 
        if i>51 and i<=60:
            hist[5] = hist[5]+1 
        if i>61 and i<=70:
            hist[6] = hist[6]+1 
        if i>71 and i<=80:
            hist[7] = hist[7]+1 
        if i>81 and i<=90:
            hist[8] = hist[8]+1 
        if i>91 and i<=100:
            hist[9] = hist[9]+1 

    ranges = ['000-010','011-020','021-030','031-040','041-050','051-060','061-070','071-080','081-090','091-100',]
    lst=[]
    for i in hist:
        if i<50:
            lst.append("*")
        if i>50 and i<=100:
            lst.append("***")    
        if i>100 and i<=800:
            lst.append("******")  
        if i>800 and i<=1200:
            lst.append("*********")  
        if i>1200:
            lst.append("***************")

    for item,range in zip(lst,ranges):
        print(range,item)
    print("\nDown  is mentioned the age with number that lies in respective bins\n")
    for item,range in zip(hist,ranges):
        print(range,item)

#
#
#
#
print("To view data enter:  'view'\nTo view coloumns enter:  'coloumns'\nTo view martial status enter:  'marriage'\n To view histogram enter:  'graph'")
user=input("Enter your input:")
if user=="view":
    print(content())
if user=="coloumn":
    print(coloumn())
if user=="marriage":
    print(martial_status())
elif user=="graph":
    print(age_bins())