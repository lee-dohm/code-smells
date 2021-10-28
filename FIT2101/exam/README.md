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

> Data centre flooded, all data is lost
> Data centre burns down 
is way to specific. The risks should cover a broader range of issues that could happen to data centres for example, server hosting app is down.

> Team member gets sick, leaves project
> Team member wins lottery, leaves project
Combine these two risks into one and make them more generalised. E.g. Team member(s) leave due to personal reasons

> New developer on project doesn't know java
* This risk description is directly finger pointing a team member and it's a bit specific.
* Instead make it more generalised and broader. E.g. Team not cross-functional (lacking certain technological stacks**

**Inconsistent ranking system**

> 0.0001
0.0001 is not only inconsistent with the rest but also very vague. 0.0001 could represent anything

> 0
0 is inconsistent with the rest of the likelihoods and also it is not useful information.

> Already happened
This is not a type of likelihood. The format of the risk register should be consistent

**Esoteric shapes for impacts**
> crosses and triangles
Instead should grade them alphabetically or numerically in a certain range. Or even with words (minor, medium, catastrophic**

**Vague mitigation strategies**
> Program doesn't work
> Avoid writing buggy code. Fix program if it stops working.
Instead propose a detailed fix. Avoiding writing buggy code is something that is universally accepted by every person so it is often not a strategy.
Strategies can be following a certain coding standard, doing regular regression or progression tests. Incorporate unitesting to CI/CD pipeline etc

> Supply new developer with Java books and revaluate performance periodically
Again, this seems like fingerpointing and may put the indicative developer on the spot.

**not useful far-fetched risks**
> Zombie apocalypse, civilisation breaks down
This is a nearly impossible scenario and since there are many different scenarios that are near impossible. It is best to not list them in the risk register



