# Design Processes

[Design Processes][agilemodeling] Design processes are creative processes and there are often more than 1 solution to a problem. However applying techniques well doesn’t guarantee that our designs will always be good.

Design processes require a lot of practice..

[Where to start?][agilemodeling] Start by understanding the problem domain. Draw models of the problem domain, e.g.
      – Conceptual or Domain Class Diagrams (to understand the
      concepts within the domain, and how they are related)
      – activity diagrams (to model business processes)

These can be evolved towards a design. Understanding the problem better will often make a solution obvious.


[Model storming is just in time (JIT)][agilemodeling] You identify an issue which you need to resolve, you quickly grab a few team mates who can help you, the group explores the issue, and then everyone continues on as before. 

It"s common on agile projects, Extreme Programmers (XPers) call it a stand-up design session or a customer Q&A session, and it"s clearly common on traditional projects as well. Everyone model storms at some point and I think that it"s about time we started talking about it so we can find ways to get even better at it.


## Analysis Model Storming

You and the stakeholder analyse the requirements and draw out several examples of the screen sketches until you come to a common understanding of what needs to be built. Sketches such as this are [inclusive models][inclusivetools] because you"re using simple tools and modeling techniques, this enabling the Agile Modeling (AM) practice of Active Stakeholder Participation. Note that you may also have created a model such as this as part of your iteration modeling efforts, the "rules" aren't carved in stone.

Stakeholder friendly model storming

### Screen sketeches (inclusive tool)
![screen sketch](/design-process/uiSketchStudentEdit.jpeg "Example of screen sketches")

## Design Model Storming

Agile developers (including Xpers), don't always go straight to code once they've chosen to work on a requirement (contrary to what detractors of agile development will tell you). This is because model storming is also very common for architecture and design. 

Java programmers will often work through complex code by sketching a quick UML sequence diagram, XPers will create Class Responsibility Collaborator (CRC) cards on standard index cards to explore detailed structural design problems

Visual Basic programmers may choose to draw flow charts to model a complex business rule. Regardless of the model(s) that you need to create, you're still model storming.


### CRC cards

![CRC cards](/design-process/crcCardExample.jpg "Example of CRC card")


## Scenario base design

Visualise you as the customer or user and try to come up with possible scenarios and actions.

* storyboard, use case, activity diagram, plain text, etc.
* this may come out of requirements or analysis (depending on whether thing is “the system” or some small part of it) Work through your scenario(s)
* trace through your design as it stands Modify/rework design to support scenario effectively
* keep <kbd>quality properties</kbd> in mind Repeat with additional scenarios


![buying jeans](/design-process/process1 "Buying jeans")

![taking diabetes meds](/design-process/process2 "taking diabetes medication")



[agilemodeling]: http://agilemodeling.com/essays/modelStorming.htm
[inclusivetools]: http://agilemodeling.com/essays/inclusiveModels.htm
