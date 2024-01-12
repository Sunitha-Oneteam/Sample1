# Counting the frequencies in a list using dictionary in Python
	
#     Input: [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
#                   4, 4, 4, 2, 2, 2, 2]
	
    
#     Output:    1 : 5
#        	     2 : 4
#         	    3 : 3
#         	    4 : 3
#      		    5 : 2


list1=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
list1.sort()
dict1={}
for i in list1:
    c=list1.count(i)
    dict1[i]=c

print(dict1)










































# list1=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
# resdict={}
# list1.sort()
# for i in list1:
#     resdict[i]=list1.count(i)
# print(resdict)
