def merge(array, l, m, r):
    p_f = len(array[l:m])+1 #m-l + 1 
    p_s = len(array[m:r]) #r-m
    print('{}-{}-{}={}={}'.format(l,m,r, p_f, p_s))
    F = []
    S = []
    
    for i in range(0,p_f):
        F.append(array[l+i])

    for j in range(0,p_s):
        S.append(array[m+1+j])
    i = 0
    j = 0
    k = l
    
    while(p_f > i and p_s > j):
        if F[i] <= S[j]:
            array[k] = F[i]
            i += 1
        else:
            array[k] = S[j]
            j += 1
        k += 1
	
	while i < p_f: 
       array[k] = F[i] 
       i += 1
       k += 1
    
    while j < p_s: 
       array[k] = S[j] 
       j += 1
       k += 1
		
def mergeSortHelper(array, l, r):
    if l < r:
        m = (l+(r-1))//2
        
        mergeSortHelper(array, l, m)
        mergeSortHelper(array, m+1, r)
        merge(array, l, m, r)
def mergeSort(array):
    mergeSortHelper(array, 0, len(array)-1)
	return array