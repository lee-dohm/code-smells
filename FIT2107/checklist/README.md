# Checklists

## Equivalence (class) partitioning ##
  * [ ] Identify input domain of the program (both valid and invalid inputs)
  * [ ] Identify parts of that input domain that you believe that the program will treat similar (homogeneous behaviour)
  * [ ] Each equivalence partition should be disjointed (i.e. there should be no overlap)
  * [ ] For each equivalence partition, pick a small number of tests. (can pick randomly from each equiv. partition for now)
  * [ ] For each test input, make sure you know what the expected outputs are.
  * [ ] Perform test

### Category partitioning testing ###
  * [ ] Identify the parameters, or the input of the program. (e.g. parameters the classes or methods receive)
  * [ ] Derive characteristics for each parameter. (Can be found direct from specs of the program and some cannot like input cannot be null)
  * [ ] Add constraints (remove **invalid combinations** and **single out corner cases**) to minimise the test suite
  * [ ] Generate combinations of the input values. These form test cases

#### Mocking practices ####
Guidelines by ​Gil Zilberfeld and Dror Helper translated into python-English:
  * [ ] Know what to isolate. 
  * [ ] Fake as little as needed. More fakes causes more chances of having a hard-to-find bug in your faking, and the more "brittle" the tests become.
  * [ ] Fake the immediate neighbours (several method calls down the tree). because any change in any one of the intermediate classes might cause the mocking to not work right.
  * [ ] Don't misuse assertions on the arguments to mocked method. Verify correctness when there's no other way to
do so, or it forms part of the external definition of the module's correct behaviour.

Others:
  * [ ] Try to avoid mocking other people's code where possible​. Other people's interfaces are subject to change beyond your control, and are often quite difficult to mock well. An abstraction layer often can be used easily mocked.
  * [ ] If your code is hard to mock, that's a code smell.
  * [ ] If your code is hard to mock, that's a code smell. ​If your interfaces are simple, share minimal information.

