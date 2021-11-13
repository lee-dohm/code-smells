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


