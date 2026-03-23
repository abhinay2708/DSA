class Solution:
    def defangIPaddr(self, address: str) -> str:
        new=''
        c=0
        while c<len(address):
            if address[c]=='.':
                new+='[.]'
            else:
                new+=address[c]
            c+=1
        return new
