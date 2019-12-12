f=open("Vibrio_cholerae.txt",'r')
pat="AA"
#text=f.read()
text="AAACATAGGATCAAC"
for i in range(0,len(text)-len(pat)+1):
    if text[i:len(pat)+i]==pat:
        print(i)
    
    
