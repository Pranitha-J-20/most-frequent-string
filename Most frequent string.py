def most_frequent(string):
    d ={}
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d
x=input("Please enter a string ")  
print(most_frequent(x))   
