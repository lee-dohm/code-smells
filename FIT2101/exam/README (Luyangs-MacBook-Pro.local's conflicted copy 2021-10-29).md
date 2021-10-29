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


# Question 2 (8 Marks)

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

#### Question 4 (1 + 2 + 2 = 5 marks) This question is about stakeholder identification
> The Golden Days nursing home is a residential care home for people who are unable to look after themselves because they are elderly, disabled, or sick. They provide medical care as well as cleaning, laundry, and housekeeping services, with nursing staff present 24 hours a day and doctors on call. <br />

> Golden Days wishes to computerize its meal planning. They hope to minimize the amount of food wasted while making sure that all residents are eating fresh, nutritious food. The system will need to consider the residents’ preferred types of foods, medical and dietary needs, allergies, and any religious restrictions (e.g., for kosher or halal food) as well as the price and storage requirements of the ingredients. Each day, it will present the kitchen staff with instructions on what to cook for each resident. At the end of each week, the administrative staff will be able to print a list of the ingredients that need to be purchased to create next week’s meals. <br />

a) What is a stakeholder? (1 mark)
Anyone or organisation that could be affected by the app or product which includes end users, product managers, program team, competitors.

b) Identify the stakeholders for this system. (2 mark)
* disabled, sick or elderly people
* Golden Days residents
* doctors
* Other nursing homes
