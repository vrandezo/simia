---
title: "Annotating axioms in OWL"
date: 2005-11-24
language: "en"
slug: "annotating-axioms-in-owl"
aliases:
  - "/wiki/Annotating_axioms_in_OWL"
tags:
  []
---

*This was sent to the
[OWLED-List](http://lists.mindswap.org/mailman/listinfo/owl) by me, that
prepares to come up with an OWL 1.1 recommendation. The week before,
[Alan Rector
suggested](http://lists.mindswap.org/pipermail/owl/2005-November/000002.html)
to add the possibility to annotate axioms in OWL, which is currently not
possible. There is many a good use for that, like provenance, trust, and
son on. But the discussion wasn't too fruitful, so I suggested the
following solution.*

After it came up in discussion last week, I hoped an elegant solution
for annotating axioms would arise. Pitily, no one had a brilliant idea,
so I went ahead and tackled the problem in my mediocre way.

First, what do I want to achieve with my solution:

1.  Don't crack the Semantic Web stack. The solution has to be
    compatible to XML, RDF and OWL. I don't want to separate OWL from
    RDF, but to offer a solution that is able to be handled by both.
2.  We want to annotate not just entities, but also axioms. Thus an
    axiom needs to be able to be a subject in a statement. Thus an axiom
    needs to have an URI.
3.  The solution must be easy to implement, or either people will get my
    FOAF-file and see whom I care about and hurt them.

Did I miss something? I found two solutions for this problem.

A) Define the relationship between an ontology (which does have an URI)
and the axioms stated inside. Then we can talk about the ontologies,
annotate those, add provenance information, etc. Problem: after
importing axioms from one ontology into another, those information is
lost. We would need a whole infrastructre for Networked Ontologies to
achieve that, which is a major and worthy task. With this solution, you
can annotate a single axiom by putting it alone into an ontology, and
claim that when annotating the ontology you actually annotate the axiom
as well. Not my favourite solution, because of several drawbacks which I
won't dwell in deeper if not asked.

B) The other solution is using Reification (stop yelling and moaning
right now\!). I'm serious. And it's not that hard, really. First, the
OWL specification offers a standard of how to translate the Axioms into
triples. Second, thte RDF specification offers a standard way to reify a
triple. With the RDF reification we can give a triple a name. Then we
can introduce a new resource type owl11:axiom, where its instances
contains the triples that were translated from a certain DL Axiom. This
rdf resource of type owl11:axiom is then the name/URI of the original DL
Axiom.

RDF-triples that have a subject of type rdf:statement or owl11:axiom
don't have semantics with regards to OWL DLs Model Theoretic Semantics,
they are just syntactic parts of the ontology in order to allow the
naming of axioms in order to annotate them.

For example, we say that all Humans are Mortal. In Abstract Syntax this
is

    SubClassOf(Human Mortal)

In RDF triples (N3) this is:

    :Human rdfs:subClassOf :Mortal.

Now reifiying this we add the triples:

    :statement1 rdf:type rdf:statement.
    :statement1 rdf:hasSubject :Human.
    :statement1 rdf:hasPredicate owl:subClassOf.
    :statement1 rdf:hasObject :Mortal.
    :axiom1 owl11:consistsOf :statement1.

Now we can make annotations:

    :axiom1 :bestBefore "24/12/2011"^xsd:date.
    :axiom1 :utteredBy :Aristotle.

Naturally, :bestBefore and :utteredBy have to be Annotation Properties.
When an axiom is broken up in more than one triple, the reasone of
having an extra owl11:axiom instead of simply using rdf:statement should
become clear.

Does this solution fulfill the given conditions?

1.  The Semantic Web stack is safe and whole. RDF Semantics is adhered
    to, and OWL semantics is fine, and all syntax regulations imposed by
    XML and RDF/XML are regarded. Everything is fine.
2.  Yep, we can annotate single axioms. Axioms have URIs. We can
    annotate our metadata\! Yeah\!
3.  Is it easy to implement? I think it is: for reading OWL ontologies,
    a tool may just ignore all those extra triples (it can easily filter
    them out), and still remain faithful to the standard semantics.
    Tools that allow to name axioms (or annotate them) and want to deal
    with those, have to simply check for the correct reification (RDF
    toolkits should provide these anyway), and get the axiom's URI.

Problems that I see: I identified two problems. First, what happens, if
those triples get separated from the other actual axiom triples? What if
they get ripped apart and mushed into another ontology? Well, that
problem is somewhat open for OWL DL and Lite anyway, since not all
axioms map to single triples. The answer probably is, that reification
would fail in that case. Strict reading could be that the ontology
leaves OWL DL then and moves to OWL full, but I wouldn't require that.

Second problem, and this is by far more serious, is that people can't
stand reification in RDF, that they simply hate it and that alone for
that they will ignore this solution. I can only answer that reification
in practise is probably much easier than expected when done properly,
due to some short-hand notations available in RDF/XML-serialization, and
other syntaxes. No one holds us back from changing the Abstract Syntax
and the OWL XML Presentation Syntax appropriately in order to name
axioms far more easy than in the proposed RDF/XML-Syntax. Serializations
in RDF/XML-Syntax may get yucky, and the RDF graph of an OWL ontology
could become cluttered, but then, so what? RDF/XML isn't read by anyone
anyway, is it? And one can remove all those extra triples (and then the
annotations) automatically if wished, without changing the Semantics of
the ontology.

So, any comments on why this is bad? (Actually, I honestly think this is
a practicable solution, though not elegant. I already see the 2007 ISWC
best paper award, "On the Properties of Higher Order Logics in OWL"...)

I hope you won't kill me too hard for this solution :) And I need to
change my FOAF-file now, in order to protect my friends...
