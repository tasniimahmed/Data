import csv

with open('contacts.csv','w',newline='') as f:
    data=['Name','email', 'mobile','uni','major']
    thewriter=csv.DictWriter(f,fieldnames=data)

    thewriter.writeheader()
    
    while(1):
       
        x=input('')
        if x == 'stop':
            break
        else:
            thewriter.writerow({'Name':x,'email':input(''),'mobile': input(''),'uni':input(''),'major':input('')})