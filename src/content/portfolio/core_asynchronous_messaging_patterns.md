+++
showonlyimage = false
draft = false
image = "img/portfolio/workqueue.jpeg"
date = "2018-12-26T19:34:33+01:00"
title = "Core Asynchronous Messaging Patterns"
weight = 1
+++

Messages define the core of a distributed microservice system, thus all of the business transactions are exposed as messages between microservices. In this section we will discuss some core consepts of messaging patterns.

In general, an asynchronous message ends up in a queue handled by the message broker, and the consumer service pulls messages from the queue to handle the business related to the message. As an example, the widely used [RabbitMq](https://www.rabbitmq.com/) message broker which implements the AMQP protocol mainly consist of two modules, exchanges and queues. Exchanges handles all incoming messages tagged with a topic and routes them to queues matching the topic. [^amqp_footnote] 

![alt text](../../img/portfolio/async_rabbitmq.png)

In general, the two main concepts of emitting a message is done as an event or by command.

#### Event
Asynchronous messages should be event driven, and the event driven approach follows the fire-and-forget principle with many possible consumers to the message. The consumers subscribe on a desirable topic, and a producer publish a message on the topic which is received by all subscribing consumers.

#### Command
A message sent by command is directed to a single queue, meaning it is delivered to at most one listening service. A common use of this approach is during an asynchronous request/response transaction. A producer emits an asynchronous message as an event, consumed by one or more consuming services. All of the consuming services responds with a command approach, thus sending the response directly back to the original producer's queue. [^enterprise_int_patterns_footnote]

[^amqp_footnote]: 
    A deeper understanding of the [AMQP](https://www.amqp.org/) protocol is found at https://www.rabbitmq.com/tutorials/amqp-concepts.html.
[^enterprise_int_patterns_footnote]:
    It is highly recommended to visit [Enterprise Integrations Patterns](https://www.enterpriseintegrationpatterns.com/patterns/messaging/) for a thorough introduction to different message patterns.