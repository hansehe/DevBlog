+++
showonlyimage = true
draft = false
image = "img/portfolio/asynchronous-communication-email.png"
date = "2018-12-15T19:34:33+01:00"
title = "Why Services Should Prefer Asynchronous Communication"
weight = 0
+++

In a typical monolitical architecture, all business transaction are usually handled in a synchronous fashion. The business transaction must handle the full aspect of the business logic to succeed, and this design pattern tends to become increasingle time consuming when the business logic grows. 

In a distributed microservice architecture, the services communicate with contracts defining the domain businesses, and communication may be done over [REST](https://www.codecademy.com/articles/what-is-rest). The pitfall to this design is the synchronous fashion of REST calls. If a business transaction relies on a number of other services, and one of these calls fails, then the whole business transaction fails. This architectural flaw, is usually recognized as a monolitich distributed architecture. A single fail at one of the endpoints during the business transaction leads to a full error, although the rest of the business finished with success. In worst case, the whole system may go down if only one of the servies fails hard leading to a cascade error to the rest of the system.

Designing the business logic as triggering other business logics with asynchronous events will prevent services from becoming tightly coupled over synchronous calls. The previously synchronous calls are emitted as events, and picked up by observing services. This design pattern makes the system higly decoupled and more responsive, thus becoming both available and parition tolerant (AP, following the [CAP theorem](https://towardsdatascience.com/cap-theorem-and-distributed-database-management-systems-5c2be977950e)).

At the next section we will discuss the core messaging patterns:

- [Core Messaging Patterns](/portfolio/core_messaging_patterns)