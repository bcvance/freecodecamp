number = input("Number: ")

def luhns_checker(number):
    sum1 = 0
    sum2 = 0
    dist_from_end = 0
    for i in range(len(number)-1, 0, 1):
        if dist_from_end%2 == 0:
            sum2 += int(number[i])
        else:
            sum1 += 2*int(number[i])
        dist_from_end +=1
    

