#Write a program that reads a file and prints the letters
#in decreasing order of frequency. Your program should convert all the
#input to lower case and only count the letters a-z. Your program should
#not count spaces, digits, punctuation, or anything other than the letters
#a-z. Find text samples from several different languages and see how
#letter frequency varies between languages. Compare your results with
#the tables at https://wikipedia.org/wiki/Letter_frequencies
inp="abcdefghijklmnopqrstuvwxyz"
filename=input("enter a file name: ")
fhand=open(filename)
text=fhand.read()
count=0
f_dict={}
for ch in text.lower():
    if ch in inp:
        f_dict[ch]=f_dict.get(ch,0)+1
list=[]
for key,value in f_dict.items():
    list.append((value,key))
list.sort(reverse=True)
for f,l in list:
    print(l,f)

