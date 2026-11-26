---
title: "Annotating axioms in OWL - Reloaded"
date: 2005-11-25
language: "en"
slug: "annotating-axioms-in-owl-reloaded"
aliases:
  - "/wiki/Annotating_axioms_in_OWL_-_Reloaded"
tags:
  []
---

*Yesterday I sent a [lengthy
mail](http://lists.mindswap.org/pipermail/owl/2005-November/000034.html)
to the [OWL-ED
Mailinglist](http://lists.mindswap.org/mailman/listinfo/owl)\] about
[how to annotate axioms](Annotating_axioms_in_OWL "wikilink"). [Peter
Patel-Schneider](http://www-db.research.bell-labs.com/user/pfps/)
himself, first author of the [OWL Semantics
specification](http://www.w3.org/TR/owl-semantics/), told me in [nice
words](http://lists.mindswap.org/pipermail/owl/2005-November/000035.html)
that my solution sucked heavily, by pointing out that [the semantics of
annotations in OWL](http://www.w3.org/TR/owl-semantics/direct.html) are
a tiny bit different than I thought. Actually, they are not at all as I
thought. So, in the evening hours, instead of packing my stuff for a
trip, I tried to solve the problem anew. Let's see where the problem
will be this time.*

Peter, you were right, I was wrong. I took a thorough look at the
Semantics, and I had to learn that my understanding of annotations was
totally screwed. I thought they would be like comments in C++ or Prolog,
but instead they are rather like a second ABox over (almost) the whole
universe. This surprised me a lot.

But still, I am not that good at giving up, and I think my solution
pretty much works syntactically. Now we need only a proper Semantics to
get a few things right.

What would be the problem? Let's make an example. I need some kind of
Syntax to give axioms name. I will just take *Name":" Axiom.* This is no
proposal for the Abstract Syntax extension, this is just for now.

    Axiom1: SubClassOf(Human Mortal)
    Axiom2: Individual(Socrates type(Human))

Do they entail the following?

    Axiom3: Individual(Scorates type(Mortal))

Well, pitily they don't. Because the Axiom3 has a name, Axiom3, that is
not entailed by Axiom1 and Axiom2. Their contents would be entailed, but
the name of the axiom would not.

I guess, this is the problem Peter saw. So, can we solve it?

Well, yes, we can. But it's a bit tricky.

First, we need the notion of Combined Inverse Functional Properties,
CIFP. A CIFP has several dimensions. A CIFP with dimension 1 ist a
normal Inverse Functional Property. A CIFP with dimension 2 over the
properties R, S can be represented with the following rule: a R c, a S
d, b R c, b S d -\> a = b. This means, in a two dimensional space I can
identify an individual with the help of two roles. More on this here:
<http://lists.w3.org/Archives/Public/semantic-web/2005Feb/0095.html>

Second, we extend the semantics of OWL. Every axiom entails reifying
annotations. This means:

    SubClassOf(Human Mortal)

entails

    Individual(Statement1 type(rdf:statement)
    annotation(rdf:subject Human)
    annotation(rdf:property owl:SubClassOf)
    annotation(rdf:object Mortal))

or, in N3:

    Human owl:subClassOf Mortal.

entails

    Statement1 rdf:type rdf:statement.
    Statement1 rdf:subject Human.
    Statement1 rdf:property owl:subClassOf.
    Statement1 rdf:object Mortal.
    rdf:subject rdf:type owl:AnnotationProperty.
    rdf:predicate rdf:type owl:AnnotationProperty.
    rdf:object rdf:type owl:AnnotationProperty.

Third, we have to state that we have a 3D-CIFP for statements over
rdf:subject, rdf:property and rdf:object\*. This is to ensure that
Statement1 always maps to the same element in the universe, even though
an OWL API could give it a blank node, or a different URI everytime
(mind you, I am not suggesting to extend the OWL language with CIFPs, I
just say that it is used here in order to state that all triples with
the same subject, object and predicate actually is the same triple).

Fourth, the above statement also entails

    Individual(Axiom1 type(owl11:axiom)
    annotation(owl11:consistsOf Statement1))

or, in N3:

    Axiom1 rdf:type owl11:axiom.
    Axiom1 owl11:consistsOf Statement1.
    owl11:consistsOf rdf:type owl:AnnotationProperty.

Fifth, owl11:consistsOf needs to be an n-dimensional CIFP with n being
the number of triples the original axiom got translated to (in this
case, happy us\!, n=1).

This assures that an axiom is always the same, whatever it's name is, as
long as it expresses the same thing. Thus, in our example, Axiom3 would
indeed be entailed by Axiom1 and Axiom2. So, even if two editors load an
ontology an annotate an axiom, they could later interchange and find
each others annotation attached to the correct axiom.

This is only a rough sketch of the way, and yes, I see that the
Interpretation gets filled up with a lot of annotations, but I still
think that this is quite easy to implement, actually. Both the OWL API
by Bechhofer and Volz and the KAON2 API by Motik offer access to axioms
on an ontology level, and also offer the possibility to check if they
are the same anyway, if I remember correctly (which is basically a
shortcut for the whole semantic entailment and CIFP-stuff proposed
earlier). All they need is a further field containing the URI of the
axiom.

As said, this looks far more nasty than it actually is, and for most
practical reasons it won't do much harm. Now we finally can annotate
axioms, yeeeha\!

Merrily awaiting Peter to acknowledge that this is a brilliant solution
:) Or else tell me I did it all wrong again, so that I have to think
over the weekend how to solve this problem again.

Cheers, denny

 \*What I mean with that is the following rule: a=b :- a rdf:subject s,
a rdf:property p, a rdf:object o, b rdf:subject s, b rdf:property p, b
rdf:object o
