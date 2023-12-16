def valid_anagram(s,t):
    if len(s)!=len(t):
        return False
    k=set(s)
    for i in k:
        if s.count(i)!=t.count(i):
            return False
    return True

strs = ["eat","tea","tan","ate","nat","bat"]
big_list=[]
i=0
while len(strs)!=0:
    chunk_list=[]
    chunk_list.append(strs[i])
    for j in range(i+1,len(strs)):
        x=valid_anagram(strs[i],strs[j])
        if(x):
            chunk_list.append(strs[j])
    print(strs)
    strs=[x for x in strs if x not in chunk_list]
    print(strs)
    big_list.append(chunk_list)
    i=0
print(big_list)