n = input()
k = int(input())


def find_lucky_number(n: str, k: int):
   
    lst1 = list(n)
    m = ""
    index = 0

    while len(lst1) > 0:
        index = (index + k - 1) % len(lst1)

        m = m + lst1[index]
        
        new_lst = []
        for i in range(len(lst1)):
            if i != index:  
                new_lst.append(lst1[i])
      
        lst1 = new_lst
        

    

    if int(m) % 3 == 0:
        result = "YES"
    else:
        result = "NO"
    return m, result, lst1

lst1, m, result = find_lucky_number(n, k)
print(result)
print(m)
print(lst1)
