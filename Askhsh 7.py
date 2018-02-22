#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Giannis
#
# Created:     20/02/2018
# Copyright:   (c) Giannis 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import datetime
now = datetime.datetime.today()
days=0
for i in range(now.year + 1,now.year + 11):
    hmera=datetime.date(i,now.month,now.day)
    if hmera.strftime("%A")==now.strftime("%A"):
        days= days + 1
print("Θα υπάρξουν",days,"μέρα/ες τα επόμενα 10 χρόνια που θα είναι",now.day,"του",now.month,"μήνα.")