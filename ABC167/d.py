N, K = map(int,input().split())
A = [0] + list(map(int,input().split()))
#1 6 2 5 3 2 5 3 2 5 3
tmp = 1
list_tmp = [1]
set_tmp = set([1])
for n in range(K):
    #n回
    tmp = A[tmp]
    #print(tmp)
    if not tmp in set_tmp:
        set_tmp.add(tmp)
        list_tmp.append(tmp)
        ans = tmp
    else:
        
        list_loop = list_tmp[list_tmp.index(tmp):]
        ans = list_loop[(K-n-1)%len(list_loop)]
        break

print(ans)