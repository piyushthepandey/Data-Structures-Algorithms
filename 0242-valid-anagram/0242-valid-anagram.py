class Solution(object):
    def isAnagram(self, s, t):


        #two strings s and t 
        #return True 
        #If t is an anagram of s else false 


        #create a hashmap 
        #key s, t and value will frequency of occurence 

        #if value of s, t % 2 return true else false 
        
        if len(s)==len(t):
            my_dict = {} 
            for i in s: 
                print(i)
                if i in my_dict:
                    my_dict[i]+=1
                else:
                    my_dict[i]=1
            for j in t: 
                if j in my_dict: 
                    my_dict[j] -= 1 
            for k in my_dict.values(): 
                if k != 0:
                    return False
            return True
        else:
            return False
        

               

