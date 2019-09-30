#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters
def anagram(s,n):
    s=s.lower()
    n=n.lower()
    replaced_space_s=(s.replace(" ", ""))
    s_list=[]
    replaced_space_n=(n.replace(" ", ""))
    n_list=[]
    for i in range(len(replaced_space_s)):
        s_list.append(replaced_space_s[i])
        s_list.sort()
    print(s_list)
        
    for i in range(len(replaced_space_n)):
        n_list.append(replaced_space_n[i])
        n_list.sort()
    print(n_list)
    
    for i in range(max(len(s),len(n))):
        if s_list==n_list:
            return True
        else:
            return False


# In[2]:


#Given an integer array, output all the unique pairs that sum up to a specific value k.
#So the input:  pair_sum([1,3,2,2],4)

arr=[1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1]
new_arr=[]
final_list = [] 
count=0
value=10

#finding all possible combinations
for i in range (len(arr)):
    for j in range(i,len(arr)-1):
        #print(i,j)
        #print(arr[i],arr[j+1])
        new_arr.append((arr[i],arr[j+1]))
        
#removing Duplicates
for item in new_arr: 
    if item not in final_list: 
        final_list.append(item) 
#print(final_list) 

#calculating value which satisfies condition
for l in range(len(final_list)):
    if final_list[l][0]+final_list[l][1]==value:
        count=count+1
print(count)    
        


# In[3]:


#Find the Missing Element
def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for i in range (max((len(arr1),len(arr2)))):
        if arr1[i] == arr2[i]:
            continue
        else:
            return(arr1[i])
            pass

#Test finder([5,5,7,7],[5,7,7])


# In[ ]:




