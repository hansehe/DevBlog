+++
showonlyimage = false
draft = false
image = "img/portfolio/microservices.jpg"
date = "2019-01-08T19:34:33+01:00"
title = "Fundamentals Of Microservices"
weight = 0
+++

Microservices offer many great advantages all the way from development to production. It offers autonomy, flexibility and scale for software systems, and it has become a popular solution to the monolith. However, there are some fundamentals to keep in mind before diving into the world of microservices.

### Business Domain
Microservices are well designed when they are modelled by the bounded context of a business domain, and serves the single purpose of the context well. Designing a service based on technical abilitites defies the single purpose of a microservice, instead commonly used tooling should be published as artifacts available to all services. Modelling services by business domain instead of technical abilities naturally leads to more loosely coupled services with high cohesion, and technical tools are shared as artifacts not owned by any of the services. 

Additionally, a typical business domain relies on data being stored in a database, and the owner of the data is the service handling the business domain. It would be unwise to let anyone else read your data without your approval, and the same rule apply to services. This design makes vital services replacable, instead of a growing debt of code. 

### Loose Coupling & Stateless Services
A microservice should have a single purpose, and serve that purpose well. It should be loosely coupled with high cohesion, meaning it is highly dependent on other services to stay alive, while it serves a clearly defined context of a business domain. As an example, if all services relies on a single service to expose metrics, that service becomes a single point of failure and a potential bottleneck [^spf_footnote], thus all services are tightly coupled to that service. 

Immutability is key to a microservice, thus it should be possible to quickly replace or recreate the service from scratch at any time. Combining immutability with stateless design is a core design pattern of microservices. The stateless design is naturally more suitable to scalability and automated deployment since it makes the running services non-vital and replacable, and it offers the possibility to run multiple redundant services through a load balancer.

### Contracts & Messages
Message patterns are the language in a distributed microservice system, and the contracts defines the rules all services have to follow for being able to communicate [^contracts_footnote]. The messages should be considered as first class citizens, irreplacable and valuable. As an example, an interruption to the message flow is the first vital sign of an error to the system, and the weak link is easily located by following the messages.

### Failure Acceptance & Network Limitations
First of all, a software system with no possibility of error simply does not exist, and it would be unwise to follow such a goal. A more suitable approach to system development is to consider failure as inevitable, but manageable. Services should be designed to be fault tolerant, meaning failure is expected and handled accordingly. The failure acceptance copes well with network limitations since networks are well known to be unreliable.

At the next section we will discuss the benefits of asynchronous communication:

- [The Benefits Of Asynchronous Communication](/portfolio/benefits_async_com)

[^spf_footnote]:
    [Prometheus](https://prometheus.io/docs/practices/pushing/) have a clear opinion on when to use the push gateway to expose metrics.

[^contracts_footnote]:
    Contracts defines the rules on how to communicate with a service, without defining implementation details on which programming language to use. Therefore, it is common to define contracts as schemas, with tools to deserialize the contract to the preferred programming language. [Avro](http://avro.apache.org/docs/current/) is a recommended open-source deserializing tool with schemas defined with [Json](http://www.json.org/).