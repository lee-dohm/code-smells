# Risk and risk management

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Risk and risk management](#risk-and-risk-management)
    - [Risk exposure: The exposure to risks (dabbing into the unknown)](#risk-exposure-the-exposure-to-risks-dabbing-into-the-unknown)
    - [Risk management **cycle**](#risk-management-cycle)
        - [Risk Discovery](#risk-discovery)
        - [Forming strategies for risks](#forming-strategies-for-risks)
        - [When encountering risks](#when-encountering-risks)
    - [The **FiveCoreRisks** of software projects (all may cause delay)](#the-fivecorerisks-of-software-projects-all-may-cause-delay)
    - [Risk Management](#risk-management)

<!-- markdown-toc end -->

**Risk is inevitable in real life:** <br />

> If a project has no risks, don't do it." <br />
> -- WaltzingWithBears by TomDeMarco and TimothyLister


## Risk exposure: The exposure to risks (dabbing into the unknown)

Risk exposure itself actually documented and includes the risk (risk discovery) and risk management.

Once we have our RiskExposure for each risk, we can sort our risks and manage only the TopTenRisks.

**Risk exposure** varies over the length of the project. Risk management must be a continuous

**Risk management** therefore must be a continuous iterative process even if our project life-cycle is not.

## Risk management **cycle**

### Risk Discovery
* (re)discover the risks that might impact the project
* **break** new risks into resolvable components - **RiskTree**
* **estimate** the probability and lifetime of each new risk
* create a **Contingency Plan** for each new problem
  * **cost any mitigation** required by the Contingency Plan

### Forming strategies for risks
* decide on a **strategy** for each risk
* add **Risk Mitigation tasks** and a **Risk Reserve** to the schedule

### When encountering risks
* as risks materialise, start their Contingency Plans
* remove risks once they have materialised or expired
* AT REGULAR INTERVALS RETURN TO THE DISCOVERY PHASE

## The **FiveCoreRisks** of software projects (all may cause delay)

* inherent schedule flaw
* FeatureCreep
* employee turnover
* ambiguous specification
* poor productivity

## Risk Management
* Risk mitigation
    * pay for infrastructure upfront to mitigate risks.
* ContingencyPlan
    * Mitigation strategy and plan to act on when risk materialises
    * e.g. if our plan for a fire includes the use of fire-extinguishers, 
    * Mitigation: the plan must include the installation and maintenance of those fire-extinguishers and training the staff in their use. 
* RiskAcceptance
    * For each accepted risk, there must be a risk contingency plan. The plan has a impact on the budget and scheduled time of the risk.
    * We then use the RiskExposure to add an amount to our RiskReserve which balances the risk we are willing to take on the project.
    * If the risk fails to materialise we can reclaim the budget and schedule time allocated to it from the RiskReserve.
* RiskAvoidance
    * remove the source of the risk.
    * Appears to be free (no risk mitigation or risk reserve involved)
    * By avoiding the risk we also avoid the possible benefit from taking on a more risky task.

* RiskTransfer
    * Someone else (insurance, other tech companies) to take the risk for us.
    * Is also risk mitigation as it requires compensations to carry out contingency plan.
* RiskReserve
    * This is the amount of extra **budget and time** we add to our project plan to match the level of risk we want on our project.
    * We can use RiskMitigation to reduce our overall RiskExposure and therefore the size of our RiskReserve while maintaining the same level of risk.

* RiskReduction
  * This consists of **minimizing the likelihood of the undesirable event**.
  * ExtremeProgramming reduces the likelihood that you will lack some features at each milestone by **reducing the amount of "extra" work to be done**, such as paperwork or documentation, and **improving overall quality** so as to make development faster.


**Good or Bad?** Risk evasion <br />
Hoping things will work out.

* [handwaving](https://wiki.c2.com/?RiskEvasion) is a common riskevasion tactic.

## Feature creep

> Our studies about the usefulness of communication services indicate that a small set of basic features is able to provide a great majority of benefits <br />
> --(Pohjola and Kilkki, 2004). 

* Better service for a set of users does not imply better user experience in general, because better service for someone usually means worse or no service for some other users.
* Better technical performance does not directly imply better business performance, because the relationship between transmitted bytes and operator profit varies vastly from case to case.
* Complex methods to boost performance or service quality are likely to generate complex interactions that may seriously complicate network management, and actually cancel out any positive effects.
