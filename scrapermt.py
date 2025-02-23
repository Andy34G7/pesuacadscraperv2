from bs4 import BeautifulSoup
import requests
import csv
import threading
import time
def fetch(st):
    while st<3000:
        no=f"{st:05}"
        sprn=f"PES{c}{y}{no}"
        response=requests.post(url, headers=headers, data={'loginId':sprn})
        # print(response)
        rtext=response.text
        #print(rtext)
        soup=BeautifulSoup(rtext,'html.parser')
        tbody=soup.find('tbody', {'id': 'knowClsSectionModalTableDate'})
        if tbody is None:
            print(f"PRN: {prn} fetch unsuccessful")
            st+=10
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
        st+=10
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
f=open(f"students_{y}_{c}_.csv","w", newline="")
x=csv.writer(f)
x.writerow(["PRN","SRN","Name","Semester","Section","Cycle","Campus","Course"])
url = "https://www.pesuacademy.com/Academy/getStudentClassInfo"
t1 = threading.Thread(target=fetch, args=(1,))
t2 = threading.Thread(target=fetch, args=(2,))
t3 = threading.Thread(target=fetch, args=(3,))
t4 = threading.Thread(target=fetch, args=(4,))
t5 = threading.Thread(target=fetch, args=(5,))
t6 = threading.Thread(target=fetch, args=(6,))
t7 = threading.Thread(target=fetch, args=(7,))
t8 = threading.Thread(target=fetch, args=(8,))
t9 = threading.Thread(target=fetch, args=(9,))
t0 = threading.Thread(target=fetch, args=(10,))
a=time.time()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t0.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t0.join()
f.close()
b=time.time()
print("total time elapsed is ", b-a, "seconds")