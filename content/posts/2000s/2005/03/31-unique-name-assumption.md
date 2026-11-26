---
title: "Unique Name Assumption"
date: 2005-03-31
language: "en"
slug: "unique-name-assumption"
aliases:
  - "/wiki/Unique_Name_Assumption"
tags:
  []
---

I just read [Andrew Newman's](http://morenews.blogspot.com/) entry on
the [Unique Name Assumption
(UNA)](http://morenews.blogspot.com/2005/03/why-different-things-are-same.html).
He thinks that not having an UNA is "weird, completely backwards and
very non-intuitive". Furher he continues, that "It does seem perverse
that the basis for this, the URI, is unique." He cites an [OWL
Flight](http://www.deri.at/teaching/seminars/internal/slides/OWL_DLvsFlight.pdf)
paper that caused me quite some headache a few weeks ago (cause there
was so little in it that I found to like).

Andrew, whose blog I really like to read, makes one very valid point:
"It doesn't really say, though, why you need non-unique names."

There was an [OWL
requirement](http://www.w3.org/TR/2004/REC-webont-req-20040210/#req-id-equivalence)
that gives a short rationale for the UNA, but it seems it is not yet
stated obvious enough.  
Let's make a short jump to the close future: the Semantic Web is
thriving, private homepages offer rich information sources about
anything, and even the companies see the value of offering
machine-processable information, thus, ontologies and knowledge bases
everywhere\!

People want to say how they liked the movie they just saw. They enrich
their movie review with an RDF-statement that says

    http://semantic.nodix.net/movie#Ring_2 http://semantic.nodix.net/rating#rated http://semantic.nodix.net/rating#4_of_5.

Or rather, their editor creates this statement automatically and
publishes it along the review.

I'd be highly surprised if [imdb](http://www.imdb.com/) would use the
same URI for denoting the movie. They would probably use an imdb-URI.
And so could I, using the imdb-specified URI for the movie. But I
didn't, and I don't have to. If I want to state that this is the same
movie, I can assert that explicitly. If I had UNA, I couldn't do that.
The two knowledge bases could not work together.

With UNA, many knowledge bases relying on inverse functional properties
would break as well. [FOAF](http://www.foaf-project.org/), for examples,
uses this, identifiying persons with an IFP of their eMail-Hash. With
UNA, this wouldn't work anymore.

Let's take another example. On my mothers webpage there could be a
statement saying she has three kids, Jurica, Rozana and Zdenko. I would
state on my page that I am my moms kid. My sister, being the social
kind, tells the world about her mom and her two brothers, Jurica and
Denny.  
Now, if we have UNA, a reasoner would infer that one of us is lying. But
all of us are very honest, trustworthy people. The problem here is, that
my name is Zdenko, but most people refer to me as Denny. UNA says that
Denny and Zdenko are the same person. If we have no UNA, we wouldn't
believe that. But still we can state it explicitly: my mom could have
said that she has three kids, Jurica, Rozana and Zdenko, and those are
mutually distinct. Problem solved.

You could say, wait, if we had UNA we still could just claim that Zdenko
owl:sameAs Denny, and the problem wouldn't arise. That is true. But then
I would have to consider my moms statements. That maybe OK on a scale
like this, but imagine this in the wilds of the web - you would have to
consider every statement made about something, before you may state
something as well. Impossible\! And you would introduce non-monotonic
inferences, and you probably wouldn't really want that.

What does this mean? Let's take the following row of statements, and
consider the answer to the question "Is Kain on of Adams two sons?". So
we know that Adam has two sons, and that there is an entity named Kain.

    Adam fatherOf Abel.

UNA and non-UNA both answer: don't know.

    Adam fatherOf Cain.

UNA says "No, Kain is no son of Adam". non-UNA says: "Sorry, I still
don't know".

    Cain sameAs Kain.

UNA says "Yes, Kain is a son of Adam (hope you didn't notice my little
lie seconds before)". non-UNA says: "Yes, Kain is a son of Adam".

Assuming that, instead of the last statement, we claimed that

    Adam fatherOf Kain.

UNA would say: "I'm messed up, I don't know anything, my database is
inconsistent, sorry." , whereas non-UNA would answer: "Yes, Kain is a
son of Adam (and by the way, maybe Kain and Abel are the same, or Kain
and Cain, or Abel and Cain)."

The problem is, that in the setting of the Semantic Web you have a World
Wide Web with thousands of facts, always changing, and you must assume
that you didn't fetch all the information about a subject. You really
can't know if you know everything there is about Adam. But you still
want to be able to ask questions. And you want to get answers, and these
answers to be monotonic. You don't want the Semantic Web to answer one
day "No", the other "Yes" and sometimes "I don't know", but you could be
fine with having it either provide the correct answer or non at all.

OWL-Flight and proponents of UNA actually forgot that it's a Semantic
Web, not just a Semantic Knowledge Base. If you want UNA, take your
Prolog-engine. The Semantic Web is more. And therefore it has to meet
some requirements, and UNA is an astonishingly basic requirement of the
Semantic Web. Don't forget, you can create local unique names if needed.
But the other way would be much harder.

Still, Andrews arguments lead to a very important question: taking for
granted that Andrew is an intelligent guy with quite some experience
with this kind of stuff, how probable is it, that Joe Random User will
have really big problems with grasping such concepts as non-UNA? How
should the primers be written? How should the tools work in order to
help users deal with this stuff - without requiring the user to study
these ideas in advance?

Still a long way to go.

**Comments**

*Benedikt Linse (5 November 2007 09:21)*

Hi Denny! Nice little essay. I aggree that the unique name assumption would not be a good choice for the semantic web, since we would all have to agree on a common vocabulary for everything before we could even start putting semantic information on the web.

However, I do not understand why inverse functional properties would break with the unique name assumption. In foaf persons are identified with the hash value of their email addresses. With the unique name assumption, we would not be allowed to use two different URIs for the same person. Hence we would not need inverse functional properties and the problem would not occur in the first place.

Greetings,

Ben
