#!/usr/bin/env python
# coding: utf-8

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

########################################################################################################################
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
        
####################################################################################################################
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

#####################################################################################################################
#Largest Continuous Sum
def large_cont_sum(arr):
    if len(arr) == 0:
        return 0
    
    max_num = sum = arr[0]# max=sum=arr[0] bug: TypeError: 'int' object is not callable. (Do not use the keyword!)
    
    for n in arr[1:]:
        sum = max(sum+n, n)
        max_num = max(sum, max_num)
    return max_num
    pass

#####################################################################################################################
#Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
def compress(str1):
    final_string=""
    res = [] 
    for i in str1: 
        if i not in res: 
            res.append(i) 
    count=1
    counter=[]
    for i in range(len(str1)-1):
        if str1[i]==str1[i+1]:
            count=count+1
            #print(str1[i])

        else:
            counter.append(count)
            count=1
            #print(str1[i])
    counter.append(count)
    final_string=""
    for k in range(len(res)):
        final_string=final_string+((res[k])+str(counter[k]))
    return(final_string)


