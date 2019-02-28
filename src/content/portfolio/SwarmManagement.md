+++
showonlyimage = false
draft = false
image = "img/portfolio/docker_swarm.png"
date = "2019-02-28T19:34:33+01:00"
title = "SwarmManagement - Container Deployment Tool"
weight = 4
+++

[![PyPI version](https://badge.fury.io/py/SwarmManagement.svg)](https://badge.fury.io/py/SwarmManagement)

[SwarmManagement](https://github.com/DIPSAS/SwarmManagement) is a simple to use tool for deploying docker containers on [Docker Swarm](https://docs.docker.com/engine/swarm/). 
The tool is implemented as a [python](https://www.python.org/) executable package installed with pip:

- `pip install --upgrade SwarmManagement`

When SwarmManagement is installed it is available in the command line with the short-key command `swm`. The application makes it easy to create networks, config files, secret files, volumes, and finally to deploy stacks with services on the Swarm. The full deployment configuration is defined by a single `swarm-management.yml` file.