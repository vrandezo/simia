---
title: "Gnowsis and further"
date: 2004-11-30
language: "en"
slug: "gnowsis-and-further"
aliases:
  - "/wiki/Gnowsis_and_further"
tags:
  []
---

Today, [Leo Sauermann](http://www.dfki.uni-kl.de/~sauermann/) of the
[DFKI](http://www.dfki.de/web/) was here, presenting his work on
[Gnowsis](http://www.gnowsis.org/). It was really interesting, and
though I don't agree with everything he said, I am totally impressed by
the working system he presented. It's close to some ideas I had, about a
Semantic Operating System Kernel, doing nothing but administrate your
RDF data and offering it to any application around via a http-protocol.
Well, I guess this idea was just a tat too obvious...

So I installed Gnowsis on my own desktop and play around with it now. I
guess the problem is we don't really have roundtrip information yet -
i.e., Information I change in one place shall magically be changed
everywhere. What Gnowsis does is integrate the data from various sources
into one view, that makes a lot of applications easily accessible. Great
idea. But roundtripping data integration is definitively what we need:
if I change the phone number of a person, I want this change to get
propagated to all applications.

So again, differing to Gnowsis I would prefer a RDF store, that actually
offers the whole data householding for all applications sitting atop.
Applications are nought but a view on your data. Integrating from
existing applications is done the Gnowsis way, but after that we leave
the common trail. Oh well, as said, really interesting talk.
