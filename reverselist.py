"""reverse list/string :- """


ls = [1,2,3,4]
print(ls)

def rev(ls):
    new=ls[::-1]
    return new

print(rev(ls))

def rev1(ls):
    ls.reverse()
    return ls

print(rev(ls))