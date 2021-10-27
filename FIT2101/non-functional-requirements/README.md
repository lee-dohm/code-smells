
# Non-functional requirements (NFRs)

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Non-functional requirements (NFRs)](#non-functional-requirements-nfrs)
    - [Functional vs Nonfunctional requirements](#functional-vs-nonfunctional-requirements)
    - [Why is NFRs hard to deal with?](#why-is-nfrs-hard-to-deal-with)
    - [Requirement elicitation](#requirement-elicitation)
        - [Asking stakeholders (canvass widely)](#asking-stakeholders-canvass-widely)
        - [Staged rollouts](#staged-rollouts)
        - [Stakeholder mapping](#stakeholder-mapping)
        - [Knowledge domain](#knowledge-domain)
        - [Hire an expert](#hire-an-expert)
        - [Non functional requirement in user stories](#non-functional-requirement-in-user-stories)

<!-- markdown-toc end -->

> I prefer to think of non-functional requirements as "constraints" we put on the system. <br />
> -- [Mike John][Mike]

**Hard to get right**

Usually properties associated with the system as a whole rather than a single component.

**Possible Non-functional requirements (based on ISO's taxonomy of requirements):** <br />

**They divide quality into two categories:**

**quality in use:** how well does the system work in its environment? <br />
**product quality:** how good is the system in itself?

We’ll take a look at those product qualities now.  They might not cover every single possible non-functional requirement, but they will give you a good basis to start thinking about them. 

1. Functional suitability is about compliance with functional requirements and is not relevant here.  That said, please note: of eight product quality attributes listed, only one is about functional requirements!

2. Performance efficiency includes

* Time behaviour – how much time does it take to do things?
* Resource utilization – does the system use too much of its resources?  (e.g. electricity, printer paper, manufacturing inputs, etc.)
* Capacity – does the system cope with its peak load?

3. Compatibility includes

* Co-existence – does the system play nicely with other software in its environment, without slowing them down, trashing their files, or otherwise breaking them?
* Interoperability – can the system use data provided from other software, and can it provide data in a format other software can use?

4. Usability includes:

* Recognizability – do users understand what they’re looking at?
* Learnability – is it easy for new users to learn how to do things?
* Operability – is the system easy to operate?
* User error protection is self-explanatory.
* UI aesthetics – is it pretty?
* Accessibility – is it usable by a wide range of people with different characteristics and abilities?

5. Reliability includes:

* Maturity – does it work well under normal operation?
* Availability – how often is the system down?
* Fault tolerance – can it deal with hardware and/or software faults?
* Recoverability – if it breaks, is it easy to recover data and restore the system?

6. Security includes:

* Confidentiality – can it keep a secret?
* Integrity – can it prevent unauthorized people from modifying the code or data?
* Non-repudiation – does it keep an audit trail good enough to prove that actions took place, so that whoever did them can’t later claim they didn’t happen?
* Accountability – can we tell who did things?
* Authenticity – do we know everybody’s identity?

7. Maintainability includes:

* Modularity – is the system broken into mostly-independent chunks, so that a change in one chunk doesn’t affect the rest of the system?
* Reusability – can the system’s components be used in other systems or contexts?
* Analyzability – when it breaks, how easy is it to figure out what happened?
* Modifiability – can we change it without breaking it?
* Testability – can we figure out sensible test criteria and test it?

8. Portability includes

Adaptability – can we change it if the requirements or environment change?
Installability – how easy is it to install or uninstall?
Replaceability – can it replace other software products that do the same thing?


## Functional vs Nonfunctional requirements

| Functional requirements                             | Non-functional requirements                |
| :-:                                                 | :-:                                        |
| Easy to spot                                        | Hard to spot                               |
| Can be visualised often immediately                 | Cannot be immediately visualised           |
| Can be described using actions                      | Can be described as want (in user stories) |
| Given inputs A, B, C, the software should compute D |                                            |

## Why is NFRs hard to deal with?

1. The product may look behave differently to expectations. Usability may be different.
    * e.g. Applications look different on bigger screens or on ultrawide.

2. Competing needs of stakeholders.
    * Some stakeholders may want a more secure database (regulators) and some want faster page load times (executives)_ and may conflict on another.

3. Hard to perform acceptance test for usability and most other NFRs.

4. Customers cannot see it (e.g. security) and are not willing to pay for it.

## Requirement elicitation

### Asking stakeholders (canvass widely)
Find through stakeholder mapping and ask their opinions regard the NFRs using interview protocols and questionnaires to prompt them to think about qualities of the software that will be important.


### Staged rollouts

If the NFR involves visible system behaviour:
You might be able to clarify it using iterative design and focus testing to produce a prototype that people can use and get feedback from authentic users as soon as possible.

For invisible behaviour:
Try and see as the system evolves through iterations, once the problem is visible tell the product owner and stakeholders to include the new NFR. This is best for usability related issues. Since the said issue relates to security, it is not best practice.

### Stakeholder mapping

Through stakeholder mapping, find stakeholders who might be related by this non-functional requirement in which case could be users or clients and ask them to voice their concerns.

### Knowledge domain

If you sense any potential non functional requirement in the sphere of knowledge you can use this knowledge to include the NFRs.


### Hire an expert
Hire people are privy in the knowledge of this particular non-functional requirement and ask them for expert advice. 

Examples include white hat or ethical hacks to perform a penetration test to test if the system is secure enough. 

Or hire legal experts to see if the system follow regulations relating to its securities.



### Non functional requirement in user stories

NRFs can be captured by user stories:

> As a customer, I **want** to be able to run your product on all versions of Windows from Windows 95 on. <br />
> As the CTO, I **want** the system to use our existing orders database rather than create a new one, so that we don't have one more database to maintain. <br />
> As a user, I **want** the site to be available 99.999 percent of the time I try to access it, so that I don't get frustrated > and find another site to use. <br />
> As someone who speaks a Latin-based language, I might **want** to run your software someday. <br />
> As a user, I **want** the driving directions to be the best 90 percent of the time, and reasonable 99 percent of the time. <br />


[Mike]: https://www.mountaingoatsoftware.com/blog/non-functional-requirements-as-user-stories
