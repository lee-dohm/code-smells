# Practice exam


## Question 1 (4 + 3 + 2 + 3 = 12 Marks)
Here is an idea for a product:
Rovr is a service that helps dog owners find people to provide services for their pets. You can think
of it as “Uber for pets”.
Service providers register themselves via a special app, verify their identity and contact details, and
select which services they provide bathing, clipping, dog walking, pet-sitting, etc. Pet owners can
use the Rovr website or app to request a service. Rovr will offer the job to appropriate service
providers in the local area. After the service has been provided, the owner gets to rate the
provider’s service on a scale of 1-5, and the provider can rate both the owner and the dog – the
system charges an extra fee for handling dogs that are known to bite.
All transactions are logged and audited once a month to verify that service providers are being paid
on a timely basis. A small team of technical staff at head office will manage these logs as well as
maintaining the servers and responding to tech support request

### Who should be invited to a story-writing workshop for this project, and why? Write about half a page. (4 marks)
* Product owner because the product owners should be the person responsible for coming up with ideas for the app. The product owner is the individual responsible for maximising profits and the value out of the team.

* The team (programmers and scrum master). These people knows the domain of the programming language, they are able to suggest functional as well as non-function requirements for user stories. Some user-stories may be not related to the functionality such as robustness, security, usability so the team can point these out.

* Stakeholders or executives, managers. Through stakeholder mapping, you can locate stakeholders who are responsible

* Potential users like a pet owner or service providers. Services and pets are of their domain of knowledge so they can point interesting feature related user stories.

### Suggest three personas that could be used in this workshop

* As a user. This is for regular users of the app. This is often for cases of using or accessing parts of the app so all users should be accomplish these
* As a pet owner. In the pet owner portal, the user should be able to do things only pet owners can do such as selecting a specific service for their pets.
* As a service provider, user stories that are limited to only service providers
* As a programmer for coding stories (?)


###  Consider the information that Rovr’s system will need to store. 

#### i. List two security-related risks related to the storage of this information. (2 marks)

Identity details may include the user's id info like driver's licence. Accidentally leaking it by means of hackers or security leaks is detrimental. Risk transfer can be put into place by let's another organisation or service handle this part. Instead of relying on the head off of a small team of potentially inexperienced technical stuff (operations team), move the sensitive information to a more establish organisation to manage the data.

To avoid accidentally leaking contact details of users risk mitigation can be used by training operation team (a small team of technical staff at head office) how to handle the server properly. Also hiring penetration testers is a good choice because they have better domain of knowledge in this regard.


#### ii. Suggest a mitigation strategy for at least one of these risks. (3 mark)
**Risk Monitoring**
- For identified risks, consistently monitor the risks and take steps to ensure to follow certain policies.

**Risk avoidance**
- Instead of storing the contact details or id of the user. Try to it through another means such as only verifying user through phone number sms or log in through email provider e.g. Gmail

**Risk reserve**
Employed more experienced technical staff and operation team. Hire people who know security as their domain of knowledge (perform expert run penetration testing

**Risk reduction**
Use better design to prevent data leaks. Spend time on improving architecture.

**Risk Transfer**
Instead of relying on a small technical team in the head office. Rely on an external organisation to handle the sensitive data that is more professional.


## Question 2 (8 Marks)

> Data centre flooded, all data is lost <br />
> Data centre burns down <br />

is way to specific. The risks should cover a broader range of issues that could happen to data centres for example, server hosting app is down.

> Team member gets sick, leaves project<br />
> Team member wins lottery, leaves project<br />

Combine these two risks into one and make them more generalised. E.g. Team member(s) leave due to personal reasons

> New developer on project doesn't know java<br />

* This risk description is directly finger pointing a team member and it's a bit specific.
* Instead make it more generalised and broader. E.g. Team not cross-functional (lacking certain technological stacks**

**Inconsistent ranking system**

> 0.0001<br />

0.0001 is not only inconsistent with the rest but also very vague. 0.0001 could represent anything

> 0<br />

0 is inconsistent with the rest of the likelihoods and also it is not useful information.

> Already happened<br />

This is not a type of likelihood. The format of the risk register should be consistent

**Esoteric shapes for impacts**
> crosses and triangles<br />

Instead should grade them alphabetically or numerically in a certain range. Or even with words (minor, medium, catastrophic**

**Vague mitigation strategies**
> Program doesn't work<br />
> Avoid writing buggy code. Fix program if it stops working.<br />

Instead propose a detailed fix. Avoiding writing buggy code is something that is universally accepted by every person so it is often not a strategy.
Strategies can be following a certain coding standard, doing regular regression or progression tests. Incorporate unitesting to CI/CD pipeline etc

> Supply new developer with Java books and revaluate performance periodically<br />

Again, this seems like fingerpointing and may put the indicative developer on the spot.

**not useful far-fetched risks**
> Zombie apocalypse, civilisation breaks down<br />

This is a nearly impossible scenario and since there are many different scenarios that are near impossible. It is best to not list them in the risk register

## Question 3 (2 + 3 + 4 = 9 marks) This question is about requirements. 
User stories can be evaluated using the INVEST criteria. These criteria say that user stories should be “Independent, Negotiable, Valuable, Estimable, Small, and Testable”. 

### Independent TODO improve
Different user stories should not have overlapping or conflicting requirements or features. For example, you should not have a user stories that requires the user to scroll down the page and also another that allows user to get to the middle of the page.

Also they must be able to be moved around in backlog or on a kaban. Also they must be able to be moved around between releases during release planning.

### What are the potential negative consequences of having user stories that are not independent? (3 marks)
You will end up with convoluted user stories and often a lot more user stories than required. This makes it hard to create product back log items because it involves splitting and combining PBIs. 

Also once you complete a user stories, you might ended up moving multiple user stories for one completed user stories. You might also encounter problem where after you complete a user story. You can't move the other user stories due to conflict in requirements.

### Here is an example of a non-functional requirement that has been expressed as a user story:

> As a customer, I want the system to be secure so that my personal information can’t be accessed by a third party. <br/>

#### What problems might this requirement cause if it is selected into the sprint backlog? Suggest an alternative way (or ways) to ensure that the complex requirement is met. Write about half a page. (4 marks)

The product owner may refuse or cannot articulate this NFR since it is not within their knowledge domain. Also the requirement might not be visible (yet or might not even happen at all. 

****Ways to counter this include:****

**Requirement elicitation**

- Staged rollouts

Try and see as the system evolves through iterations, once the problem is visible tell the product owner and stakeholders to include the new NFR. This is best for usability related issues. Since the said issue relates to security, it is not best practice.

- Stakeholder mapping

Through stakeholder mapping, find stakeholders who might be related by this non-functional requirement in which case could be users or clients and ask them to voice their concerns.

- Knowledge domain

If you sense any potential non functional requirement in the sphere of knowledge you can use this knowledge to include the NFRs.

Or, hire people are privy in the knowledge of this particular non-functional requirement and ask them for expert advice. Examples include white hat or ethical hacks to perform a penetration test to test if the system is secure enough. Or hire legal experts to see if the system follow regulations relating to its securities.

## Question 4 (1 + 2 + 2 = 5 marks) This question is about stakeholder identification
> The Golden Days nursing home is a residential care home for people who are unable to look after themselves because they are elderly, disabled, or sick. They provide medical care as well as cleaning, laundry, and housekeeping services, with nursing staff present 24 hours a day and doctors on call. <br />

> Golden Days wishes to computerize its meal planning. They hope to minimize the amount of food wasted while making sure that all residents are eating fresh, nutritious food. The system will need to consider the residents’ preferred types of foods, medical and dietary needs, allergies, and any religious restrictions (e.g., for kosher or halal food) as well as the price and storage requirements of the ingredients. Each day, it will present the kitchen staff with instructions on what to cook for each resident. At the end of each week, the administrative staff will be able to print a list of the ingredients that need to be purchased to create next week’s meals. <br />

a) What is a stakeholder? (1 mark)
Anyone or organisation that could be affected by the app or product which includes end users, product managers, program team, competitors.

b) Identify the stakeholders for this system. (2 mark)
* disabled, sick or elderly people
* Golden Days residents
* doctors
* Other nursing homes
* Product owners
* Golden Days executives
* Legislators of disability, food regulators, nursing home.
* Doctors

c) Draw a stakeholder map showing the relative influence and interest of each stakeholder (alternatively, list stakeholders under each correctly named quadrant of the map.) (2 marks)

TODO


## Question 5 (3 + 4 + 2 + 4 = 13 marks)
This question is about team structure and teamwork.
a) According to the Scrum model, an Agile team may have as many developers as you like but should only ever have one Product Owner. What risks are likely to arise if a team decides to appoint more than one Product Owner?
Write a couple of paragraphs (3 marks)


TODO improve
The product owner is the sole individual responsible for maximising return on investment (ROI). To do so they organise sprint planning and deadline. If there were multiple product owners, there would be conflicts in requirements for backlog items because different product owners often have their own views. Their different approaches in organising meetings, PBIs, user stories, interating with stakeholders may make things complicated and harder


b) One of the practices that DeMarco and Lister identified as “teamicidal” (i.e., bad for teamwork) is having team members spread out through the building instead of sitting together. What are some of the challenges that Agile teams face if their members are not located close by? Suggest some ways that teams might overcome these problems, particularly in modern working environments. Write about half a page. (4 marks)

> TEAMS work best when members have spontaneous, casual interactions as well as planned and guided interactions <br />
> -- Lecture slides

This violates **Physical Separation** teamicide point

When teams are spread out they in a building they are physically separated. They cannot form spontaneous discussion which could be deemed creative. Also this is detrimental to a cross-functional team in sharing their domain of knowledge and multi-learning.

Ways to facilitate spontaneous discussions in workplaces or in a work environment is by having tables where people can commune and discuss things closely. Another aspect is **pair programming** where two people can program together simultaneously on the same table or chat to discuss spontaneous ideas.

Big tech companies have facilities such as sport as well as discussion rooms and tables for this aspect as well. This allows teams to develop as welBig tech companies have facilities such as sport as well as discussion rooms and tables for this aspect as well. This allows teams to develop as well.

During lockdowns, it is useful to establish virtual meeting rooms where people can chat and perform pair programming. Alternatively, a virtual voice chat can also be useful to combat this problem.

c) What is siloing, and why is it considered a bad thing? Write a couple of sentences. (2 marks)

Siloing occurs when a particular group or individual that have access to unique set of skills and access to data only they can access.
> e.g. only QA team know about QA, only DBAs know about databases, etc.

Problems can occur for example for sprints that doesn't touch anything related to part related to the particular skillset.Or when a part of the app require more app in a sprint but only a select group of people know how to perform the tasks.

So team might waste developer time, or struggle to complete sprint backlog

d) Explain how DevOps approaches help overcome siloing, and how this improves outcomes for teams. Write about half a page. (4 marks)

DevOps means breaking down silos so that developers, operators, and QA staff all collaborate. Often the development team and operation team have conflicts and blame each other's mistakes especially when error occur during deployment. Developers tend to blame operators for incorrect deployment while operators blame devs for producing fragile system.


## Question 6 (4 + 4 + 4 = 12 marks) This question is about Agile practices.

> A team is developing web services and web applications. Five years ago, the team used Scrum as documented in the Scrum Primer. Since then, their methodology has changed. The team **no longer uses user stories**. Instead, requirements are managed by tasks. The Product Owner sits where she can see the master task list and notifies the Scrum Master if she sees anything that doesn't seem to be adding value from her perspective, and the Scrum Master investigates.

> A master task list is kept in an online system. The task list is always displayed on a screen in the office that is visible from all team members’ workstations and is also accessible to team members when they are working offsite or from home. Here is an image to show you the structure of this task list (note that this image is too small to let you read task details, but they would be easily readable on the screen.) Whenever a team member is looking for something to do, they can either develop or QA. If they want to develop, they assign themselves a task from the “unassigned” column by putting their name on it and moving it to the Assigned column. When they feel it’s finished, and it passes all unit tests, they move it to the Completed column. Team members who want to do some QA take a task from the Completed column, informally review the code, verify that it passes all automated tests and the **acceptance tests as documented on the card**, then move it to the Done column. The team no longer conducts sprint planning or backlog grooming. Instead, team members do their own estimation at the time that they assign tasks to themselves. The Scrum Master and Product Owner check on an informal basis that the task list looks okay. 

> Instead of running a daily scrum, the Scrum Master makes sure to communicate one-on-one with each team member every day or two to informally check that everything is running smoothly.

> Sprint reviews are no longer conducted because the team no longer feels that they are necessary. Instead, software is deployed to a staging server as soon as it passes unit tests and is manually pushed to production once it has passed user acceptance tests. This means that they are shipping new features much more often than they used to. The team does make sure to conduct a retrospective every two or three weeks to consider how their process can be made more efficient and effective.

### a) Is this still Scrum? Why/why not? Write up to half a page. (4 marks)

This is no longer Scrum. Although there are still aspects of scrum left such as having a sole product owner and a scrum master. However the product owner and scrum master are not performing their tasks appropriately.

The product owner should be trying to maximum the return on investment by identifying features. 

Once the features are identified as user stories and in sprint planning meeting high priority items should be added as PBIs and no changes should be made until the next sprint. One of the pillars of Scrum is that once the Team sets its target for the Sprint, any additions or changes must be deferred until the next Sprint.

Also there seems to be a lot of cross-overs of the scrum master and product owner do. They both seem like managers as they both check on the informal basics. The scrum master and product owner cannot be the same individual as their focus is different. When you have micro-managing product owners it contradicts self-managing teams. If the scrum master was previously a product owner, they need to substantially change their attitude and mindset which can be difficult.

Another pillar of scrum is PBI and they need to adhere to DEEP principles. Tasks is a very vague term and it is not SCRUM. The tasks or items needs to be detailed appropriately, estimated, emergent (regularly refined and continuously updated by the product owner to reflect the changes of the needs to the customer) and prioritised.

Also there seems to be no definition of done as completed tasks can be tested multiple times. Once definition of done is met, they should be treated as completed and potentially shippable code should not require any additional testing. The shipped new features are also not guaranteed to be done.

Sprint review is a pillar of scrum as well. It is to see and learn what is going on and then evolve based on feedback, in repeating cycles. It employs inspect and adapt activity to find and identify flaws in the product or potential requirements (functional and non-functional).

The retrospective should be conducted after every sprint and identify areas the team did well and areas that need improvement. Strategies should be put forward to mitigate these issues. It is another inspect and adapt process instead regarding the process and environment. It is not only a meeting to help with improving efficiency and effectiveness but rectifying things that are not working and need to be addressed.

### b) Is this still Agile? Why/why not? Write up to half a page. (4 marks)

No because this the methodology employed no longer is flexibility to changes. 

No longer aims to satisfy the customer through early and continuous delivery of valuable software. Spring reviews are not held to receive feedback. No user stories to include the needs to users and personas.

No longer business people and developers work together daily throughout the project. Product owner is doing things he/she is not supposed to do. No involvement from business people and stakeholders.

No longer there is continuous attention to technical excellence and good design enhances agility. No definition of done

No longer self-organising. No daily scrum meeting to say what each team member did yesterday going to do today and barriers.

### c) Have the changes to this process increased or decreased the risks involved? What are the trade-offs (i.e., costs and benefits)? Write about half a page. (4 marks)

There are definitely more risk involved. Quality assurance could be not met since some completed "tasks" could be not sufficiently tested. Also, end users or business people may not be satsified since there is no involvement from them. Since the scrum master seems to do minimal amount of teaching, coaching and supporting role. This could lead the team astray and and team mates may leave the team or cause the sprint velocity or quality to decrease.

[silo]: "https://www.agiledrop.com/blog/3-key-considerations-successful-agile-transformation
