# Teams and Team-work

## Teams ### Teams vs group
* A group is a collection of people
* A team is a group that is (or is expected to be)
  * cohesive
  * focused on a common purpose or goal
* All teams are groups, but not all groups are teams!

### Why teams inside software?
* Important life skill
    * almost all non-trivial **research** and **software development** are done in a team.
    * important inter-personal skill in potential employers of IT graduates. 
    
* You’ll need it for later study: senior projects in IT disciplines often
involve teamwork

### When is teamwork required?
• Software engineering is about delivering systems that are large or
complicated or mission-critical (or all of these things!)
• To make these systems work, we will need
– lots of people
– working together effectively
• And these teams need to be structured carefully, because the
structure of the organization can affect the success of the project


### Conway's Law
> Organizations which design systems [...] are constrained to produce designs which are copies of the communication structures of these organizations. <br/>
> -- **Melvin Conway, How do committees invent? 1967**

* To create a software module, developers need to communicate and collaborate
closely
* It’s harder to collaborate outside your team, and easier to collaborate with
teammates

> “If you have four groups working on a compiler, you’ll get a four-pass compiler.” <br/>
> -- Eric S. Raymond

* So the software’s internal architecture ends up mirroring the organization’s
structure
  * which might not lead to the best architectural design…
  * if there’s a reorganization of team structure, the existing architecture might become hard to
  work with

## Why team work can be terrible?

### Autocracy

![autocracy](autocracy.png)

* Sometimes students think this is
what teams should be like
* The boss hands out orders, team
members carry them out
* This is a bad team structure!
  * little opportunity for teammates to collaborate
  * morale tends to suffer
  * boss is a single point of failure 
  * if they get sick or are transferred, team cannot function

### Anarchy
* This can arise if teams fear
autocracy but don’t know what
else they can do
  * Good news: no boss!
  * Bad news: nobody knows what to do!
  
### Democracy
* Sounds like a simple idea: make all decisions collaboratively
* One problem is that “all decisions” might
turn out to be a lot
  * team gets bogged down in decision-making
  * little gets achieved
* Another problem: dilution of individual responsibility
  * if anything goes wrong, it’s nobody’s fault
  * so less incentive to make good decisions
  
## IDEAL: Collaborative teams
***Effective teams tend to have a fairly flat structure***
  * team members may have different responsibilities
* Members make decisions within their area of expertise
  * so all teammates participate in decision making to some extent
    * avoids the problems of autocracy
    * avoids the problems of democracy
    * don’t have to consult the whole team for
      * every decision
      * only those with relevant expertise

# How to form teams
***All teams are groups, but not all groups are teams***
* Suppose we want to create a team

* We start out with a group of people who may have no affiliation or shared
experiences at all

* how do these people develop into a team?

  * Two things to bear in mind:

    * <span style="color: #1e90ff">Interpersonal/group dynamics</span>: how do teammates behave towards one
    another?

    * <span style="color: #1e90ff"> task focus </span>: how do teammates behave towards the work they are doing?

## Tuckman model
* Tuckman proposed a model for group development in 1965
* Teams go through these stages:
  * Forming
  * Storming
  * Norming
  * Performing
* In 1977, Tuckman and Jensen added a fifth stage:
  * Adjourning
* Let’s see how group dynamics and task focus change as teams progress through these stages.

## Peopleware: Teamicide
* Defensive management
    * if management makes it clear to the team that they’re not trusted, the team loses motivation

* Bureaucracy
    * hard to maintain your enthusiasm when you’re doing lots of mindless paperwork

* Physical separation
    * teams work best when members have spontaneous, casual interactions as well as planned and guided interactions

    * spontaneous interactions enable creativity but are impossible if team members aren't co-located
        * Pair programming

* Fragmentation of time
    * because you can’t concentrate if you keep switching back and forth between projects
    * Links back to agile principle of focusing only on one task at a time

* Quality-reduced product
    * idea might be to lower costs or to ship earlier but it’s still demotivating to ship a poor product

* Phony deadlines
  * i.e. trying to make team members work faster by imposing artificially-close deadlines
  * Really a form of defensive management: management doesn't trust the team to work hard unless they are nagged
  * So trust team members that they can finish task on time without imposing artificially-close deadlines?

* Clique control
  * i.e. management may have policies that actively interfere with the health of teams (e.g. regularly rotating people through different roles)
  * Links back to agile principle to be *focused*.
  > A basic productivity theme in Scrum is for the Team to be focused on one product or application for one Sprint. <br />
  > -- [scrum primer][scrumprimer]
  * the authors see this as a consequence of management’s failure to understand teams, since teams seldom exist at management level

[scrumprimer]: https://scrumprimer.org/
