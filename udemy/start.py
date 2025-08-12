s = "Hi there Sam!"
list = ()
for s in s.split():
    list.append(s)
print(list)

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

def domainGet(email):
    return email.split('@')[1]

def findDog(string):
    return "dog" in string.split() 

def countDog(string):
    count = 0
    for word in string.split():
        if word == "dog":
            count += 1
    return count

seq = ['soup', 'dog', 'salad', 'cat', 'great']
seq = filter(lambda w: w[0] == "s", seq)
print(seq)

def caught_speeding(speed, is_birthday):
    speeds = [60, 80]
    if is_birthday:
        for i in range(len(speeds)):
            speeds[i] += 5
    
    if speed <= speeds[0]:
        return "No Ticket"
    elif speeds[0] < speeds <= speeds[1]:
        return "Small Ticket"
    elif speed > speeds[1]:
        return "Big Ticket"
    