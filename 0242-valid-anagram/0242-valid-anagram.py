class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict={}
        for i in s:
            if i not in my_dict:
                my_dict[i]=1
            else:
                my_dict[i]+=1

        for i in t:
            if i not in my_dict:
                my_dict[i]=1
            else:
                my_dict[i]-=1
                
        flag = all(value == 0 for value in my_dict.values())
        return flag
