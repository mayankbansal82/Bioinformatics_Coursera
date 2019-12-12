def main():
    text='TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT'
    k=3
    freqarr=ComputingFrequencies(text,k)
    for i in freqarr:
        print(i,end=' ')
def ComputingFrequencies(text,k):
    freqarr=[]
    for i in range(0,4**k):
        freqarr.append(0)
    for i in range(0,len(text)-k+1):
        pat=text[i:k+i]
        j=PatternToNumber(pat)
        freqarr[j]=freqarr[j]+1
    return(freqarr)

def PatternToNumber(pat):
    l=len(pat)
    k=l
    s=0
    while(l>0):
        pat=pat[0:l]
        c=pat[-1:]
        if c=='A':
            v=0
        elif c=='C':
            v=1
        elif c=='G':
            v=2
        elif c=='T':
            v=3
        s=s+(v*(4**(k-l)))
        l=l-1
    return(s)
if __name__ == '__main__':
    main()     
