
Radix Sort

Radix sorting is the most efficient sorting for lists.
In fact, it is built on Class Queu, which uses the "first in is first out" method.
Sorting is done using 10 queues which receive the unity digit for the first time and according to their order scatters them in all the queues, and then collects back from all the queues the numbers in order into the original array.
The operation is repeated as many digits in the number.
In a test I conducted on a random array of 1000000 organs, with this sorting method it only takes 13 seconds to sort the array. Of course it depends on what computer you have.
On the other hand, in the stupid sort that goes through each organ in front of all the others, it takes much longer.
Both functions are attached.












A changing number

Definition: An alternating number is a positive whole number in which each pair of adjacent digits has a different parity.
That is, next to every even number there is an odd number. A single digit number is an alternating number.

Examples:
 The number 163458 is an alternating number because each pair of adjacent digits in it has a different parity.
 The number 1634589 is an alternating number because each pair of adjacent digits in it has a different parity.
 The number 163789 is not an alternating number because the digits 3 and 7 are adjacent and both are odd.
 The number 6 and the number 12 are alternating numbers.

The first operation accepts a positive integer and returns true if it is an alternating number,
If not - the operation will return the value false.
The second operation accepts an array of positive integers and returns the position (index) of an alternating number whose sum of digits is the smallest. If there is no alternating number in the array, the operation will return a value of -1.








A large palindrome

A "palindrome" is any sequence of characters whose reading from right to left and from left to right is the same.
Examples of palindromes:
ABCCBA, 12A21, a0X$11$X0a
"Large palindromes", is a palindrome consisting only of the letters Z..A (the other letters do not matter)
for example:
fA%B##rkC1^BAdd
is a large palindrome.
The given operation accepts a string and returns True if the string is a large palindrome, otherwise the operation
will return False.








Is Ordered

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
