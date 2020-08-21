# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n): # this is comparing a to n^3
      a = a + n * n        # this is saying that a equals a + n^2
```
# a(0) < 10 * 10 * 10 = 1000
# 0 + 10 * 10 = 100
# a(100) + 100 = 200
# a(200) + 100 = 300
# a(300) + 100 = 400
# 10 iterations with n == 10

# a(0) < 15 * 15 * 15 = 3375
# a(0) + 15 * 15 = 225
# a(225) + 225 = 450
# a(450) + 225 = 675
```
b)  sum = 0
    for i in range(n): # this is linear
      j = 1            # this is constant
      while j < n:     
        j *= 2         # j gets multiplied by 2
        sum += 1       # sum gets 1 added to it
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
