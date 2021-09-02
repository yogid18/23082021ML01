Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6 == 6
True
>>> a = 20;
>>> a+=3-;
SyntaxError: invalid syntax
>>> a +=3;
>>> a%=3;
>>> print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3)and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ###########3###########
>>> s1 = "Nice to have it"
>>> s2 = " here"
>>> print(s1+s2)
Nice to have it here
>>> ######4########
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2]
['hello']
>>> #######5#####
>>> a.insert(0,s1)
>>> a.append(s2)
>>> print (a)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, ' here']
>>> #############6##############
>>> color_list_1 = set(["White", "Black", "Red"])
>>> color_list_2 = set(["Red", "Green"])
>>> color_list_1.differnce(color_list_2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    color_list_1.differnce(color_list_2)
AttributeError: 'set' object has no attribute 'differnce'
>>> color_list_1.difference(color_list_2)
{'White', 'Black'}
>>> a = int(input("Input an integer : "))
Input an integer : 5
>>> n1 = int( "%s" % a )
>>> n2 = int( "%s%s" % (a,a) )
>>> n3 = int( "%s%s%s" % (a,a,a) )
>>> print (n1+n2+n3)
615
>>> 