vocals = ["a","e","i","o","u"]

def is_vocal(x):
    if x.lower() in vocals:
        return True
    else:
        return False
    
print(is_vocal("J"))