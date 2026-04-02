class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}

        for word in strs:
            count=[0]*26

            for ch in word:
                index=ord(ch)-ord('a')
                count[index]+=1
            
            key=tuple(count)

            if key in result:
                result[key].append(word)
            else:
                result[key]=[word]
            
        return list(result.values())
