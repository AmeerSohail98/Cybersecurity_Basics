a = open('D:\\Sohail\\career\\Cyber_security\\Day-7\\TLD_domain.txt','r')
dm = a.read()
dm_list = dm.split('\n')
print(type(dm))
count=0
for dmn in range(len(dm_list)):
    count+=1
# print(dm_list)
print(count)