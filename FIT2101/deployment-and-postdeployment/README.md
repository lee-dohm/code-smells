# Deployment and postdeployment

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Deployment and postdeployment](#deployment-and-postdeployment)
    - [Packaging](#packaging)
    - [Deployment](#deployment)
    - [Continuous Integration](#continuous-integration)
    - [Continuous Deployment](#continuous-deployment)
        - [Delivery](#delivery)
    - [Delivering mobile apps](#delivering-mobile-apps)
    - [Operations and maintenance are hard](#operations-and-maintenance-are-hard)
    - [Reason why it is hard for op team:](#reason-why-it-is-hard-for-op-team)
    - [Operations considerations](#operations-considerations)

<!-- markdown-toc end -->


## Packaging
After the app is finished in the development environment. It needs to be packages, compiled and a makerfile or executable file needs to be created. Sometimes you will need an installer and a set of (installation) instructions.

## Deployment
Deployment means to make something available for use. It could mean:
* simply installing it onto a computer.
* making something live on a server (network based software):
    * maintaining a server
    * security becomes an issue, especially if the software is accessible from the wider internet

## Continuous Integration
* With **continuous integration**, the software is built and tested every time changes are made
  * Separate unittesting files that is ran every time ci/cd pipeline runs
    * Can get artefacts for testing logs and coverage
  * for teams that use git, this typically happens when changes are pushed to master

## Continuous Deployment
Continuous deployment takes this process one step further
– changes are built and tested and deployed, either to a staging server or to production

## Delivery

### Delivering mobile apps
* Mobile apps are usually delivered by putting them on the relevant app store
    * iOS App Store for iPhones
    * Google Play for general Android apps
    * third party stores such as Samsung App Store or Amazon App

* Usability and non-functional rquirement considerations (e.g. usability) like for larger screens.

* The app must be **packaged for delivery** and is then submitted to the store
  * The store **reviews** the app:
    * compliance with the provider’s UI guidelines
    * compliance with the provider’s Terms of Service, e.g. not showing objectionable content, not spamming, etc.
    * this process is done by humans, so takes days to weeks
  * If accepted, the app becomes available for download on the app store

### Delivery in large organisations
* So far, we have only considered standalone programs
* In large enterprises, such as telcos, financial institutions, airlines, major retailers, things can be much more complicated
  * the software you write sits **alongside many other pieces of software**
  * it’s not just a single program but a **complex software ecosystem**
* Each program or project that developers create is a component in this system
* Problems include accidentally implementing a component that breaks another component.
* More security concerns with databases and datamodels
* Components are connected by scripts and small programs usually called **glue**
* Has business rules and policies

Ops (Operations):

Team who deals with the system as a whole instead of units. Integration level system management.

* For enterprises with complex software ecosystems, operational staff keep systems running.
* They deal with planned events
  * **deploying**, **upgrading**, and **decommissioning components of the system**
  * performing maintenance on hardware and software systems
  * **writing and maintaining glue code** (they code as well)

They also deal with unforeseen events:
  * responding to **errors caused by bugs**
  * responding to **natural disasters**
  * proactively combing **logs and conducting checks** to ensure that everything is working

* Operations and support staff see the system in a way that nobody else does
  * they don’t know the architecture of each individual component, but they **understand how the components work together**
  * they see every software component in the system
  * plus the glue that holds them together
  * they get to see **first-hand how users interact with the system**
  * they are often the first to detect errors
      * and the first to **diagnose** them, come up with workarounds for them, or fix them
  * they know which **defects currently exist in the system**
  * they know which **defects used to exist in the system**

## Operations and maintenance are hard
* Enterprise systems tend to **evolve toward complexity** over time
* Requirement documentations and design by contract (liskov substitution principles) for portability and maintainability.
* Acceptance criteria needs to met
* Can try to improve quality metrics for code (e.g. comment to code ratios)
* Some developers deliberately obfusicate code.

Reason why it is hard for op team:
-------------------------------------------------------------------------------

* It is (almost always) harder and more time consuming to read and understand someone else’s code than it is to write a replacement from scratch
  * This is especially true if the original developers have moved on to new projects, or even to a new company
    * this is very likely if they were consultants

* So companies often handle changing business requirements by starting up a new project
  * which must then be integrated into the existing software ecosystem

* The lifecycle and architecture of each component in the system may be straightforward but the 
* The lifecycle and architecture of the system itself are complex

## Operations considerations
* Operations and support staff need to be considered when developing software that will be **deployed** in a complex enterprise environment
  * software needs to be easy to **deploy** and **update**
  * when the software goes wrong, they need to be able to detect and diagnose
the problem
* logging helps with this!
  * components need to be able to coexist within the system without overrunning or blocking one another’s resources
  * components should **report errors** clearly, unmistakably, and promptly. 
    * FailFast: Exception handling, assertions, and localising defects.
    * Assertions can be switched off
* We will look at some of the ways that operations and development staff work together in the next lecture
