# Sprint Planning
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Sprint Planning](#sprint-planning)
    - [Objectives](#objectives)
    - [Sprint goals (must be short and succinct)](#sprint-goals-must-be-short-and-succinct)
    - [Pre-requisites](#pre-requisites)
    - [Start of sprint](#start-of-sprint)
    - [After each sprint](#after-each-sprint)
    - [Sprint planning meeting](#sprint-planning-meeting)
        - [Required members](#required-members)
    - [what should sprint backlogs contain?](#what-should-sprint-backlogs-contain)
    - [Preparing the stories](#preparing-the-stories)
    - [Definition of ready](#definition-of-ready)
    - [Selecting user stories](#selecting-user-stories)

<!-- markdown-toc end -->

The process of preparing the sprint backlog.

## Objectives

* Create sprint backlog

**Do not think about*** future sprints!

This is done at the end of the sprint in backlog maintenance.

Backlog grooming sessions don’t need to involve the whole team, so they’re less likely to end up going off-topic, and you’re losing less productivity if they do.

If you end up doing your sprint planning at epic level and therefore considering multiple iterations, that’s likely to take a lot longer than planning a single iteration.

## Sprint goals (must be short and succinct)
Optionally, team can decide on a sprint theme, or sprint goal.  

One or two sentence description of what the team will focus on for this sprint.  

Doing this can help team members set **priorities**, and makes the customer value easier for developers to understand.

It facilitates **communicating progress to stakeholders** without going into much detail.

## Pre-requisites
  * [ ] user stories (from story-writing activities during project inception)
  * [ ] user stories seeded into product backlog read for next sprint. 

**selecting a story during sprint planning should not automatically remove it from the product backlog.**

**Stories should not be removed from the product backlog until they are done according to your team’s Definition of Done.**

**Deciding that you want to implement a story doesn’t guarantee that you will be able to complete it during the sprint.**

## Start of sprint

  * [ ] [Sprint planning meeting](#sprint-planning-meeting)
  * [ ] Team decide on the aim to achieve during the sprint.
  * [ ] Select stories from the **product backlog**, break them down into tasks, and putting them into the **sprint backlog**.


## After each sprint
  * [ ] Backlog maintenance at the end of every sprint.


## Sprint planning meeting

Inside a SPM, meeting members create the [sprint backlog](#what-should-sprint-backlogs-contain).

The team also needs to plan how it will organize itself to get the sprint backlog Done.  That usually means planning at a more finely-grained level than user stories.

The meeting should be **timeboxed** (one hour per week of development is a good rule of thumb). If the time isn’t strictly limited, sprint planning can easily get out of hand. 


The team also needs to plan how it will organize itself to get the sprint backlog Done.  That usually means planning at a more finely-grained level than user stories.

**Main tasks:** <br />
1. high-priority stories need to be well understood, and choose which items from the product backlog should be selected into the sprint backlog.  

2. the team needs to figure out how to go about how to organise development so that those stories can be completed.

### Required members
The **Product Owner** needs to be there to explain the client's value priorities.

**Team members** need to be there to learn about what the client values, and to explain any relevant technical constraints.

The **Scrum Master** needs to be there to facilitate the meeting

## what should sprint backlogs contain?
Anything that your team plans to do:

* user stories
* dev stories TODO
* refactors
* spikes
* maintenance tasks

## Preparing the stories
No matter what the client’s priorities are, you shouldn’t select stories into the sprint backlog until:

* they meet the **INVEST criteria** well
* the team understands what the client wants (TODO inclusion modelling tools)
* they have been **estimated**, e.g. using planning poker, fibonacci numbering
* the Product Owner is sure of their **priority**

In the **first half of the sprint planning meeting**, the team makes sure that enough stories (or product backlog items) are ready to be selected.  This usually means:

* reviewing any **high-priority stories** that weren't reviewed during backlog management
* running estimation sessions (e.g. planning poker)
* confirming with the **Product Owner** what the stories will require and how important they are

You should try to get about **twice as many stories ready for sprint planning as you think you'll need**.  This gives your team and Product Owner more **flexibility**.

## Definition of ready
A list that defines steps have been taken before sprint planning.

Here, **Done** means that the story is completed and can be removed from the backlog, and **Ready** means that the story has been **refined, prioritized, and estimated** and is ready to be put into a sprint backlog.

You can put a note on each product backlog item (or use a kanban column) to indicate their state of Readiness. It’s handy to be able to see what needs to happen before a particular story will be Ready.


## Selecting user stories
Once enough stories are ready to be implemented, the team works with the Product Owner to select which ones should be put into the sprint backlog.

To figure out how many stories should be selected, consider the concept of velocity. That's the number of story points your team gets Done in a sprint.

* It's not what you’d planned to do
* It's not what you "need" to get through to meet a deadline
* not what you NEARLY had finished 

If it’s not Done, it’s not done, and anything else is wishful thinking.

If your team has been working together long enough, you'll usually find your velocity is pretty consistent from sprint to sprint.

## Velocity
Velocity is **unique for each team** because each team estimates differently and has different detailed work practices. So you can never assume that Team A and Team B will have identical velocities.

Velocity can also be **affected by external factors**.  If half the team comes down with the flu, for example, velocity will probably go down.  If the Scrum Master goes off to a conference, velocity will probably go down. 

When a new team member joins, velocity might go down initially. Remember **Brooks’ Law**: Adding manpower to a late software project makes it later.  The new **starter will need to be mentored**, and that will take at least one of your team members away from their regular duties.  But once the team member is up to speed, velocity should go up, higher than it originally was.

### Stable and unstable velocity (inspect and adapt)
If velocity in your team is **stable**, you can simply use last iteration’s velocity to estimate how many story points your team will be able to complete. 

At the start, your initial estimate of velocity will be very rough and likely to be inaccurate, but as you gain experience you'll get better at this.  Then, you will be able to use your past velocity to predict how many story points your team is likely to get through in the sprint.  As a rule of thumb, you can expect your tasks to take about twice as long as you think they will.

## Don't forget your technical stories

If you have accrued significant technical debt, you may also need to select some tech stories so that you can refactor it away.

If the Product Owner asks you to implement stories that you can only implement by incurring technical debt, have them promise to select some tech stories in future sprints -- and get that promise in writing!


## Detailed planning

After the team and Product Owner have agreed on which stories should be implemented during the sprint, the team needs to figure out how that will happen.  The Product Owner doesn't need to be present for this part, especially if they are a **non-technical client representative**.

The team needs to:

* break each story down into its component tasks
* decide who should perform each task
* ensure that team members aren’t overloaded or underloaded for the sprint

## Stories and Tasks

### Stories
A **user story** describes a feature from the client’s or user’s point of view.  **Stories are vertical** – that is, they involve front-end work, back-end work, and everything in between.

So far, we have assumed that stories will be the basic unit of work for the team, but this will not usually be the case.  

**Some stories will require several team members to work together**, e.g. one person might implement the user interface while another gets the functionality working in the back end, so that each team member works on a horizontal slice of the functionality.  Doing this means that we can make our development more efficient by parallelising it, but it means that we need to distinguish between stories and tasks.

### Task

#### A thing a team member does
**A task is simply a thing that a team member does**.  Unlike a story, it may or **may not deliver customer-visible value by itself**.  

#### Always part of a story
It will always form part of a story. but the story might involve other tasks too.

#### Involve a lot of tech stacks
Typically, a task will only involve one or two technologies (e.g. languages, services, packages, protocols).

