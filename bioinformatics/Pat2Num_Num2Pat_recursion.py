def main():
    pat='TCCGTTATCGACGCTT'
    number=46
    k=3
    ret=NumberToPattern(number,k)
    print(ret)
def PatternToNumber(pat):
    if pat=='':
        return(0)
    symbol=pat[-1:]
    prefix=pat[0:len(pat)-1]
    return(4*PatternToNumber(prefix)+SymbolToNumber(symbol))
def SymbolToNumber(sym):
    if sym=='A':
        return(0)
    elif sym=='C':
        return(1)
    elif sym=='G':
        return(2)
    elif sym=='T':
        return(3)
def NumberToPattern(ind,k):
    if k==1:
        return(NumberToSymbol(ind))
    prefixind=int(ind/4)
    r=ind%4
    symbol=NumberToSymbol(r)
    prefixpat=NumberToPattern(prefixind,k-1)
    return(prefixpat+symbol)
def NumberToSymbol(val):
    if val==0:
        return('A')
    elif val==1:
        return('C')
    elif val==2:
        return('G')
    elif val==3:
        return('T')
if __name__=='__main__':
    main()
