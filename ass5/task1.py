dict1={'alice':90,'ben':99,'meeth':1,'elonmusk':0}
name=input("enter student name")
if name in dict1:
    print(dict1[name])
else :
    print('student not found.')