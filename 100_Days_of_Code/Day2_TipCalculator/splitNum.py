#num = input('Two Number to sum:\n')
#num1 = int(num[0])
#print(num1)
#num2 = int(num[1])
#print(num2)
#print('The Sum Is:')
#print(num1 + num2)

n = input('Input Numbers to Sum w/o Space:\n')
num_split = [int(i) for i in n]
num_sum = str(sum(num_split))
print('The Sum of Numbers is:\n' + num_sum)