list = [1,2,3,4,5,6,7,8,9,'on']
print("elave etmek istediyiniz varmi?: ")
print("0 = yes ,,1 = no")
elave = int(input())

if elave==0:
    print("yazin: ")
    deyer2 = input()
    list.append(deyer2)
elif elave == 1:
        print("deyer elave olunmayacaq: ")
        
print("Necenci deyer lazimdi?: ")
deyer = int(input())
print(list[deyer-1])