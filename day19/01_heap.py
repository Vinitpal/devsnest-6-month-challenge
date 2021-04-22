# Heap data structure is mainly used to represent 
# a priority queue. In python, we use "heapq" module.
# Advantage of this is that whenever we elements are
# pushed or popped, our heap structure is maintained

#---------------------------------------------#

# Various operations on heap:

# -> heapify(arr):
# convert arr into a heap structure

# -> heappush(heap, ele):
# push element in heap and also maintain heap structure

# -> heappop(heap):
# remove and return the smallest element from heap

# -> heappushpop(heap, ele):
# (push the element) and (pop the smallest ele) simultaneously

# -> heapreplace(heap, ele):
# (pop the smallest ele) and (push the element) simultaneously
# looks similar to heappushpop() but this one, 
# pop the smallest ele first and then push the new ele

# -> nlargest(k, arr, key = (condition)):
# returns the k largest elements from arr
# by satisfying the key if mentioned

# -> nsmallest(k, arr, key =(condition)):
# returns the k smallest elements from arr
# by statisfying the key if mentioned

#---------------------------------------------#

# Implementation of heapq operations

# Importing heapq
import heapq

# taking an example arr
arr = [5,7,9,1,3]

# using "heapify" to convert arr into heap
heapq.heapify(arr)

# printing created heap
print("The created heap is :")
print(list(arr))

#---------------------------------------------#

# using "heappush" to push elements into heap
heapq.heappush(arr, 4)

# printing heap after pushing 4
print("The heap after pushing 4 is :")
print(list(arr))

#---------------------------------------------#

# using "heappop()" to pop smallest element
print("The popped element is: ")
print(heapq.heappop(arr))

#---------------------------------------------#

# using "heappushpop()" to push and pop the min element simultaneously
print ("The popped item using heappushpop() is : ")
print(heapq.heappushpop(arr, 8))
print(list(arr))


# using "heapreplace()" to pop the min element and push the new element simultaneously
print ("The popped item using heapreplace() is : ")
print(heapq.heapreplace(arr, 18))
print(list(arr))

#---------------------------------------------#

# using "nlargest()" to print k large elements
print("The 3 largest nums in heap are:")
print(heapq.nlargest(3, arr))

# using "nsmallest()" to print k small elements
print("The 3 smallest nums in heap are:")
print(heapq.nsmallest(3, arr))

#---------------------------------------------#

