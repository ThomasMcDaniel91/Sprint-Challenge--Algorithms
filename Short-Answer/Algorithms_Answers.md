#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This algorithm is linear because with n being 10 it runs 10 times before the loop stops and with 15, it runs 15 times before the condition is no longer true


b) This algorithm is quadratic. When ran with n(5), it ran 15 times, when the input of n was doubled to (10), it ran 40 times.


c) This algorithm is linear. It runs and adds 2 to the function and then recalls itself
while reducing the number of bunnies input by 1 until it reaches 0.

## Exercise II

Create the function with stories of building(n) and max drop height(f)

For this we would use a binary search to find the optimal floor as quickly as possible

we would start at the middle floor of the building and drop an egg, see if it breaks.

If the egg does not break, we go to the floor that would be the mid point between the egg we dropped and the top floor of the building and the floor would be marked as highest current dropped floor without breaking. If it did break, we would go to the floor mid way between the one we just dropped the egg that broke from, and the ground floor.

Once we either have only 1 floor left to check or we know the above floor breaks and the current one doesn't, we know we have the right floor.

# The runtime for this function would be (log n) because the amount of iterations of the function doesn't increase as quickly as the amount of floors.
# i.e 50 more floors doesn't mean we have to search 50 more times.