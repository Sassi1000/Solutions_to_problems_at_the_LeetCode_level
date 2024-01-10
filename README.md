#is_ordered

A list of integers is called an "ordered list" if all even values ​​(if any) are at the beginning
The list and all the odd values ​​(if any) are after them, at the end of the list.
for example:
The following lists are "ordered" lists:
lst1 = [6, 24, 12, 8, 44, 3, 7]
lst2 = [6, 24, 12, 8, 16, 22]
The first function receives a list of integers arr.
 The operation will return a True value, if the list is "ordered" and not, the operation will return a False value.
 
The second function receives three parameters of integer type: size, x, y.
 The operation should create an ordered list of integers of size filled with random numbers
 Between x and y (inclusive).
 
 It can be assumed that 0<size and y<x as well.






Distance Finder

The first function in this exercise checks the distance of a certain number from the two borders of the array.
For example: the array [4,8,6,3,5,9,2,3,2,1]
If we choose the number 3 for testing, we will find that its distance is 5.  3 from the left side and 2 from the right side.
The second function checks what is the smallest distance among all the members of the array.





 BinarySearch

When we come to look for a certain object in an array,
The simple way is to go through the entire array. Of course this is inefficient, so there is the binary search method, which asks whether the object is below the midpoint of the array or above it, and accordingly updates the boundaries of the array.
This way cuts the array in half each round, and thus can find an object (if it exists), within 40 tests, assuming there are a billion elements in the array.
The Zen method is also called the "logarithmic method"
Attached are the two types of solutions + a random array for testing.
