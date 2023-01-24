#  It' s important that it will form the dictionary...
a={}
print(type(a))
print(a)
b=set()
print(type(b))
print(b)
# The set is well define collection of object.. .
# set does not contain repetative elements...
b.add(3)
b.add(3)
b.add(4)
print(b)
# b.add([1,2,3,4,5,6,7,8,9,10,11])
# print(b)// We can not add the list in the set because in unhashable mean it can be changed...
# on the otherhand hash able object are those which can not be modified in ...mean they have some identity , because of immutablity.

# so we cann't add the list or dictionary in set but we can tuple...
b.add((1,2,3,4,5,6,7,8,9,10,11))
print(b)
