from bs4 import BeautifulSoup
import requests
import csv
import time

session = requests.Session()
url = 'https://www.pesuacademy.com/Academy/'
response = session.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('meta', attrs={'name': 'csrf-token'})['content']
#print("CSRF Token:", csrf_token)
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Csrf-Token': csrf_token,
    'Referer': url, 
    'Cookie': '; '.join([f"{c.name}={c.value}" for c in session.cookies]),
}
c=int(input("Enter Campus(1 for rr, 2 for ec): "))
y=int(input("Enter Year of batch: "))
a=time.time()
f=open(f"students_{y}_{c}.csv","w", newline="")
x=csv.writer(f)
x.writerow(["PRN","SRN","Name","Semester","Section","Cycle","Campus","Course"])
url = "https://www.pesuacademy.com/Academy/getStudentClassInfo"
number = 1
while number<3000:
    no=f"{number:05}"
    sprn=f"PES{c}{y}{no}"
    response=requests.post(url, headers=headers, data={'loginId':sprn})
    # print(response)
    rtext=response.text
    #print(rtext)
    soup=BeautifulSoup(rtext,'html.parser')
    tbody=soup.find('tbody', {'id': 'knowClsSectionModalTableDate'})
    if tbody is None:
        print(f"PRN: {prn} fetch unsuccessful")
        number+=1
        continue
    # print(tbody)
    first_row = tbody.find('tr')
    prn=first_row.find_all('td')[0].text
    srn=first_row.find_all('td')[1].text
    name=first_row.find_all('td')[2].text
    sem=first_row.find_all('td')[3].text
    sec=first_row.find_all('td')[4].text
    cycle=first_row.find_all('td')[5].text
    campus=first_row.find_all('td')[6].text
    course=first_row.find_all('td')[7].text
    print(f"PRN: {sprn} successfully fetched")
    x.writerow([prn,srn,name,sem,sec,cycle,campus,course])
    number+=1
b=time.time()
print(f"Time taken: {b-a}")
f.close()