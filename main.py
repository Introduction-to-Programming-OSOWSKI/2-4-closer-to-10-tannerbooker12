def close10(x,y):
    if 10-x>10-y: 
        return(x)
    elif 10-y>x-10:
            return(y)
    else:
        x=y 
        return("0")

print(close10(9,12))