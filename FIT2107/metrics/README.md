# Metrics

## Testing metric


### Coverage metrics

* Can compute statement and branch coverage

* MC/DC coverage are available for the kinds of languages in which safety-critical automotive and aerospace code is written


* Code coverage is easy to compute and useful indicator of test suit quality.

* There is *no reliable industry model* that can tell you "x% coverage is sufficient to give you reliability".

* **specification coverage** should somewhere around 100%


## Mutation analysis

* Involves automatically seeding a change in your code.
* Mutation score varies between 0 to 1.
* Better indication whether your test suite is any good than just code coverage.


* Can be problematic if **generating thousands of mutants and running the test suite on each of them**

## Design and code metrics

Statically analysing source code and in some cases uml diagrams

* Good indicator of **functional correctness** and potentially useful proxies for the maintainability and **portability of software**.

### Code size

* Determine how big it is.

* lines of code (LOC). This very easy to measure

#### Comment lines
Are useful and often when there are a lot of comment lines it indicates that the code itself is harder to understand

Are quicker to write compared to code itself

**LOC counters** provide more detailed counts, tabulating comments and blank lines separately.

Larger methods are much more error-prone than small methods.

## Halsteads software science metrics

    HSCM can predict the difficulty, effort required and likely correctness of code.


## OO design metrics

The more interactions and complex the interactions are between modules and classes, the harder code is to write and debug More interactions between classes means more mocking for unit testing, more tracing faults down through many different classes.


### Weighted methods per class (WMC)

For class with methods M_1, M_2 up to M_n.


Complexities of each method: c_1, c_2, c_n.

![Alt Text](pic1.png) 


#### Complexities for a method

There are a number of ways  already discussed and Chdiamber and Kemerer deliberately did not refine this.

The complexity of a method is likely to be application specific due to different programming languages and different definitions of operands and operators.

The complexity metric **requires code to measure**. 

## Depth of inheritance -DIT

The depth or inheritance it takes to reach to the class of the inheritance tree.

![Alt Text](pic2.png)

DIT for <kbd>VerticalLayout</kbd> is 3 and DIT for object is 0.



A higher DIT number was thought to make designs more complex. This is because the class at the bottom of the hierarchy inherits more and more properties, but a higher DIT also implies more reuse (which is considered good.)


## Number of children - NOC

![Alt Text](pic2.png)

Widget has three children
Object has 1 children
Leaf nodes like VerticalLayout have zero children
