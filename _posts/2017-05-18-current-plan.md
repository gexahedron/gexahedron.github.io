---
layout: post
title: Current plan
ref: plan20170518
category: graphs
tags: [cdc, berge-fulkerson, nz5-flows, petersen-colouring]
lang: en
---

Current question to explore: can we (sometimes) derive 5cdc from o6c4c?<!--more-->

I have experimentally found, that sometimes we can take o6c4c solution, find weights for the cycles and produce some nowhere--zero 5--flow.

Experiments also show that we can always construct some (3,3)--flow parity--pair--cover (which always leads to 5cdc) from any nowhere--zero 5--flow.

We also have another connection between 6c4c and 5cdc --- through Petersen colouring.

And it is also known, that there is no obvious oriented version of Petersen colouring.

But it looks like we could have 2 different connections between 6c4c and 5cdc (more on that later).

So the plan is following:

* take some graph, e. g. 18g1 (more on that notation later);
* generate all of its Petersen colourings, at first in the format of poor and rich edges, and then just any possible normal/Petersen colouring/mapping;
* take also Petersen graph - generate all possible 6c4c solutions (there is just 1) and all possible 5cdc solutions (about 10 for 96555 configuration and about 30 for 86655 configuration);
* now we combine all of 18g1 Petersen colourings with all possible 6c4c--5cdc pairs coming from Petersen graph;
* after that we take some o6c4c solution for 18g1;
* we find all compatible nowhere--zero 5--flows for it;
* we try somehow to find all (3,3)--flow parity--pair--cover, compatible with these nz5--flows;
* we find all 5cdc from these (3,3)--flow parity--pair--covers;
* ...
* PROFIT!
