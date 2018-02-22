#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Giannis
#
# Created:     22/02/2018
# Copyright:   (c) Giannis 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import urllib.request
import json
import datetime

today=datetime.datetime.now()


for i in range(10):
    L=[0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    L[i]=input("Διαλέξτε τους αριθμούς με τους οποίους θα παίξετε:")


def compare_lists(l1,l2):
    s=0
    for i in range(10):
        if int(l1[i]) in l2:
            s+=1
    return s
max=0
for i in range(31):

    today = today - datetime.timedelta(days=1)
    date_str= today.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
        tmp=k["results"]
        r.append(compare_lists(L,tmp))



    if int(r[0])>4:
        max=r[0]
        max_day=today.strftime("%d-%m-%Y")


if max==0 :
    print("Δεν είχατε επιτυχίες")
else:
    print("H μέρα που είχατε τις περισσότερες επιτυχίες είναι",max_day)






