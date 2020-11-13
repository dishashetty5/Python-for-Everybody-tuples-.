#Exercise 1: Revise a previous program as follows: Read and parse the
#“From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
#After all the data has been read, print the person with the most commits
#by creating a list of (count, email) tuples from the dictionary. Then
#sort the list in reverse order and print out the person who has the most
#commits.
#Sample Line:
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5
#Enter a file name: mbox.txt
#zqian@umich.edu 195
filename=input("enter a file name: ")
fhand=open(filename)
days={}
for line in fhand:
    if line.startswith("From "):
        day=line.split()[1]
        days[day]=days.get(day,0)+1
list=[]
for key,value in days.items():
    list.append((value,key))
list.sort(reverse=True)
tuple=list[0]
print(tuple[1],tuple[0])
