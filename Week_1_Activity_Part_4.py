    
n = int(input( "enter a integer: " ))
sum_of_range = 0

for i in range(1, n+1):
    if i % 3 or 5:
        sum_of_range += i
        print(sum_of_range)