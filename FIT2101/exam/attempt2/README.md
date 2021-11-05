# Exam


## Project inception

1.a. Who should be invited to a story-writing workshop for this project, and
why? Write about half a page.

Project Stakeholders such as product owner, potential end-users, executives, managers, also organisations representatives. User stories are inclusive modelling tools that are easy to learn and for all project stakeholders to understand and also story-writing workshops are necessary for facilitating Just in Time analysis because you need to have conversations with the customers to know what features to implement. Also the team needs to be their so they can negotiate the scope of the product and they are responsible as well for coming up with example user stories for the stakeholder and customers so they have an idea on how to use the tool. 

Project stakerholders are requirements because they have different knowledge domain so they can give the team some advice on features and requirements. You could have law professional in the workshop who can identify some necessary features for the product before it gets deployment on app store.

Acceptance criteria are often required for user stories. The team is necessary here because not only product owners but also the team can write acceptance critiria to help the team members nail down the requirement of each user stories. Another reason why the team is necessary is because they can come up with personas for potential end users with varying needs, wants and skill levels. Inside the user-story writing workshops, the team members can let the project stakeholders refer to the personas to everyone can identify features for different users.



1. b. 3 personas

Bob is a pet owner who owns 2 laboradors and 1 poodle. He is very busy with work so he often looks online for groomers and also nannies who can look after hispets when he is off to work. He needs the app able to filter different services for his pet's needs.

Sabrina is a pet owner but she is visually impaired. She needs to access the services without looking at the pictures and often uses voice over. She finds the captions and alt texts of the images very useful online to help her navigate for different services.

Kevin is a service provider that offer grooming services for both dogs and cats. He also can look after all pets while the owner is away at his shop. He needs to be able put multiple services online on the same page, so different filters should lead to the same result.

1.c. The identify information (passports) is used to verify the user's identity. Also contact details are stored in association with the information of the website. The phone numbers of users could be used by exploiters to phish the target. It is important to protect these information being leaked to prevent identify theft, scams or even potential hacks of the user's account information.


Also the passwords could be stored within the server of the Rovr's office. In this case, a poorly protected system could be penetrated by black hat hackers.

1.c.ii. 

Mitigation strategies:
These are by definition, involves paying for infrasctures and a plan to mitigate certain risks. The plan must include installation and maintainence in place as well. The budget and time to implement the mitigation strategies comes from the risk reserve


Risk transfer:
This is also risk mitigation because it requires costs and compensations to the externation organsiation to carry out the contintengy plan. One possible mitigation strategy is to rely on external databases and servers from big companies to store the sensitive data. Google's Two-factor authorisation could be used to prevent potential access from unauthorised users. Also instead of login in with solely password, users can be prompted to login user another service like google.

Risk Acceptanace:
Risk acceptance involves having a contingency plan if there is a suspected penetration or hack into the server. The extra budget can be restrevied from risk reserve if the risk fails to materialise. Ethical hackers can be hired as ops to maintain the servers and respond to hacks.

## Quesiton 2


Missing identification id for every risk involved. This is not ideal because the risks are harder to trace without id (traceability)

Risk breakdown structure: The risks are not categorised.

No severity or risk priority: the likelihood and impact should be combined into one metric to justify how severe the risk poses to the project.

No responsible monitoring members for the risks (no risk ownership): Each risk should be monitored by a responsible member of the team like scrum master or product owner or developers. The risk owner is responsible for deploying the appropriate response and supervising it.

No categories: The risk should be categorised in a broader sense for example based on schedule, budget, technical and external risks.

Poor risk analysis: The risk analysis is not consistent (sometimes qualitative and sometimes quantitative). It should be consistent with one. Also there is no justification for 0 and 0.0001 as risks analysis as these numbers are vague. Also already happened is not a likelihood.

Finger point: "New develpoper" this is not good practice in a documentation and it certainly isn't agile because it adds pressure to the team member and destroys colloborative teams (defensive management) 

Esoteric symbols: A lot of esoteric symbols were utilised to represent the impact which meaningless and doesn't convey any info. A scale should be used instead.

Meaningless mitigation strategies: "avoid writing buggy code" is often a meaningless risk management strategy because often in code it is hard to avoid buggy code without a proper plan or process. That's why certain process model and testing stragies exist to combat this issue. Certainly, you can utilise risk reduction by performance more and better testing (unit and integration).

Narrow and impossible events: Zombie apocalypse is way to far fetched. It can come under a more broad external risk like natural disasters (incl. example flood)

## Requirements

### Invest independent

The user stories should not impact the implementation of other stories. There should be no conflicts and implementing one user stories should not also finish another. No conflict of acceptance criteria of different user stories.

### Non-indenpent user stories

Could lead to user stories that are impossible to implement or meeting the acceptance criteria of after completing another user story. For example, you could have a user stories that the user should be able to see more cards by scrolling to the left, and another user story specify that user can scroll to the bottom to see more cards. These user stories are not independent, if you meet the acceptance criteria and able to allow the user to see more cards by scrolling to the left, how about scrolling to the bottom?

#### As a customer, I want the system to be secure so that my personal information can’t be accessed by a third party.

The first problem with this NFR is that it is not fine-grained enough for the developers to get started on this immediately especially if it is is a high priority user story. In the sprint meeting, the developers should offer some advice from their knowledge domain on how to make this possible even some dev stories could be used or spike stories can be used to experiment with beforehand.

Another problem is that the product owner or the project stakeholder may think this feature is useless and may not be required for the project due to limited budget and time. This can be tackled by staged rolled or give the stakeholder an example case to let them try and see what happens. Also stakeholder mapping and identifying stakeholders who can articulate this can advocate the implementation of this user story. Or seek the advice of the developer themself can be useful or consult a penetration tester's opinion.

## Question 6

No longer agile:
- top-down managment: the product owner monitors the devleopers while the scrum master investigates 
- No definition of done: The Q/A are informally conducted even though there is an acceptnce test. App could be prone to more bugs as one task can be tested more than once or not tested at all. It is very adhoc.
- No longer collaborative-team: Everyone works individually for estimations and they cannot learn from each other and previous sprints to do inspect and aptive. This is supposed to be a team adaptive process not a predictative process where different individual can follow and interprete other people's estimations
- Emergent princple from deep violated: The backlog should be regularly refined, user stories added, broken down, removed or moved. Without a backlog refinement meeting, the tasks will be harder to understand in future sprints and future sprints are less planned and and more haphazard
- Scope creep, more features are shippable out with potentially poorer quality due to less QA


### Metrics
This could lead to the cobra effect and instead reduce the quality. The goal should not be based on the metric because they are variable and the team can bend the estimations to help them achieve a higher velocity. This could lead to perverse incentives as well because team members might do something underhanded to their team mates in order for themself to achieve higher velocity

