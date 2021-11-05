# Black box testing

## Boundary value testing

### Identifying boundaries

```python
def total_points(current_points, remaining_lives):

    if current_points < 50:

        return current_points + 50
    elseif remaining_lives < 3: 
        return current_points + 30
    else:
        return current_points *3

```

* Score < 50
* Score >= 50 and remaining life < 3
* Score >= 50 and remaining life >= 3

![Alt Text](pic1.png) 

### Boundary 1:

Score < 50

Off-point: 49
On-point: 50

#### Example inputs

B1.1 = input = {score=49, remaining lives=5}, output={99}
B1.2 = input = {score=50, remaining lives=5}, output={150}

### Boundary 2:

Score >=50, Remaining_lives < 3

Off-point (remaining life < 3): 2
On-point: 3

#### Example inputs
500 is arbitrarily chosen from an outpoint

B2.1 = input= {score=500, remaining lives=3}, output={1500}
B2.2 = input= {score=500, remaining lives=2}, output={530**

### Boundary definition
**On-point:** the value that is on the boundary
**Off-point**: the value closest to the boundary that flips the conditions. Note: when dealing with equalities or non-equalities (e.g. x = 6 or x ≠ 6, there are two off-points; one in each direction.
**In-points** are all the values that make the condition true.
**Out-points** are all the values that make the condition false.

![Alt Text](pic2.png) 
![Alt Text](pic3.png) 

## Implicitly boundaries

Explore the boundaries between your partitions

## Combinatorial Testing

Nearly all software failures are caused by interactions between relatively few parameters.

## Pairwise testing
**Pairwise testing** requires that for a given numbers of input parameters to the system each possible combination of values for any pair of parameters be covered by at least one test case

Category partitioning, discussed earlier, works well when intuitive constraints reduce the number of combinations to a small amount of test cases


### Example: car ordering application

a. Order Types
i. Buy
ii. Sell
b. Locations
i. Melbourne
ii. Sydney
c. Car Models
i. BMW
ii. Audi
iii. Mercedes
d. Registration Numbers
i. Valid (let us say ABC1500)
ii. Invalid
e. Order Types
i. E-Booking (I call it online for time being)
ii. In-Store
f. Order Times
i. Working hours (we can also call it trading hours)
ii. Non-working hours

![Alt Text](pic4.png) 
![Alt Text](pic5.png) 

## Jenny.c
```
jenny:
  Given a set of feature dimensions and withouts, produce tests
  covering all n-tuples of features where all features come from
  different dimensions.  For example (=, <, >, <=, >=, !=) is a
  dimension with 6 features.  The type of the left-hand argument is
  another dimension.  Dimensions are numbered 1..65535, in the order
  they are listed.  Features are implicitly named a..z, A..Z.
   3 Dimensions are given by the number of features in that dimension.
  -h prints out these instructions.
  -n specifies the n in n-tuple.  The default is 2 (meaning pairs).
  -w gives withouts.  -w1b4ab says that combining the second feature
     of the first dimension with the first or second feature of the
     fourth dimension is disallowed.
  -ofoo.txt reads old jenny testcases from file foo.txt and extends them.

  The output is a testcase per line, one feature per dimension per
  testcase, followed by the list of all allowed tuples that jenny could
  not reach.

  Example: jenny -n3 3 2 2 -w2b3b 5 3 -w1c3b4ace5ac 8 2 2 3 2
  This gives ten dimensions, asks that for any three dimensions all
  combinations of features (one feature per dimension) be covered,
  plus it asks that certain combinations of features
  (like (1c,3b,4c,5c)) not be covered.
```
