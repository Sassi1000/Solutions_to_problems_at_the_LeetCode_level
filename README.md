# BinarySearch
When we come to look for a certain object in an array,
The simple way is to go through the entire array. Of course this is inefficient, so there is the binary search method, which asks whether the object is below the midpoint of the array or above it, and accordingly updates the boundaries of the array.
This way cuts the array in half each round, and thus can find an object (if it exists), within 40 tests, assuming there are a billion elements in the array.
The Zen method is also called the "logarithmic method"
