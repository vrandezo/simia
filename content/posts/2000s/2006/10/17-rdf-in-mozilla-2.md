---
title: "RDF in Mozilla 2"
date: 2006-10-17
language: "en"
slug: "rdf-in-mozilla-2"
aliases:
  - "/wiki/RDF_in_Mozilla_2"
tags:
  []
---

I read last week [Brendan Eich's post on
Mozilla 2](http://weblogs.mozillazine.org/roadmap/archives/2006/10/mozilla_2.html),
where he said that with Moz2 they hope that they can *"get rid of RDF,
which seems to be the main source of "Mozilla ugliness""*. [Danny
Ayers](http://dannyayers.com/2006/10/17/mozilla-2--baby-and) commented
on this, saying that RDF *"should be nurtured not ditched."*

Well, RDF in Mozilla always was crappy, and it was based on a
pre-[1999-standard
RDF](http://www.w3.org/TR/1999/REC-rdf-syntax-19990222/). No one ever
took up the task -- remind you, it's open source -- to dive into the RDF
inside Mozilla and repair and polish it, make it a) compatible to the
[2004 RDF standard](http://www.w3.org/TR/2004/REC-rdf-primer-20040210/),
(why didn't RDF get version numbers, by the way?) and b) clean up the
code and make it faster.

My very first encounter with RDF was through Mozilla. I was diving into
[Mozilla as a platform for application
development](http://www.mozillazine.org/talkback.html?article=4600),
which seemed like a very cool idea back then (maybe it still is, but
Mozilla isn't really moving into this direction). RDF was prominent
there: as an internal data structure for the developed applications.
Let's repeat that: RDF, which was developed to allow the exchange of
data on the web, was used within Mozilla as an internal data structure.

Surprisingly, they had performance issues. And the code was cluttered
with URIs.

I still think it is an interesting idea. In last year's [Scripting for
the Semantic Web workshop](http://www.semanticscripting.org/SFSW2005/) I
presented an idea on [integrating semantic technologies tightly into
your
programming](http://www.aifb.uni-karlsruhe.de/Publikationen/showPublikation?publ_id=937).
[Marian Babik](http://projects.semwebcentral.org/users/bb_/) and
[Ladislav Hluchy](http://ups.savba.sk/parcom/laco/laco.html) picked that
idea up and [expanded and implemented the
work](http://www.semanticscripting.org/SFSW2006/Paper1.pdf) much better
than I ever could.

It would be very interesting how this combination could really be put to
work. An internal knowledge base for your app that is queried via
SPARQL. Doesn't sound like the most performant idea. But then -- imagine
not having one tool accessing that knowledge base. But rather a system
architecture with a number of tools accessing that knowledge base.
Adding data to existing data. Imagine just firing up a newly installed
Adressbook, and -- shazam\! -- all your data is available. You don't
like it anymore? Switch back. No changes lost. Everything is just views.

But then again, didn't the DB guys try to do the same? Yes, maybe. But
with semantic web technology, shouldn't it be easier to do it, because
it is meant to integrate?

Just thinking. Would love to see a set of tools based on a plugabble
knowledge base. I'm afraid, performance would suck. I hope we will see.


