from email.policy import default

# lis = [1,23,4,5,6,1]

default_key = lambda x: x
def bubble(lis,key):
    length = len(lis)
    for i in range(length -1):
        for j in range(length -1):
            if key(lis[j]) > key(lis[j+1]):
                lis[j],lis[j+1] = lis[j+1] ,lis[j]



