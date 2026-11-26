---
title: "Unexpected problems"
date: 2005-03-11
language: "en"
slug: "unexpected-problems"
aliases:
  - "/wiki/Unexpected_problems"
tags:
  []
---

As you know, I'm a strong believer in the vision of the Semantic Web,
and I actively pursue this goal. I am not too sure what it means, but I
have hundreds of ideas floating through my head, about what will be
possible in this future...

But the road seems longer than expected. For some time I have the
[dlpconvert](dlpconvert "wikilink") and
[rdf2owlxml](rdf2owlxml "wikilink") web services running. It is very
enlightening and interesting to see, what kind of ontologies were used
for testing. And I most certainly don't mean the domain of the
ontologies used, but rather the syntax.

Both services state very clearly what syntaxes you may use. dlpconvert
allows only [OWL XML presentation
syntax](http://www.w3.org/TR/owl-xmlsyntax/), rather obscure, I admit.
That's the main reason, rdf2owlxml was offered. But most people didn't
care, they just keep on using RDF - and not just OWL in
RDF/XML-serialisation, but much more simple, plain RDF.

Yeah, every RDF is in OWL Full. But dlpconvert only deals with OWL DL.
That's stated explicitly. And much less does it work with Abstract
Syntax or N3. All of this was tested.

I most definitively don't want to rant about users here. You never
should rant about users (I mean, in public). Especially, since everyone
who uses a service like dlpconvert is probably quite intelligent and has
some expertise in the field of Semantic Web. It's not his fault. It
isn't mine either, I wrote quite explicitly what is needed. Maybe it's
the W3Cs fault, or maybe it's just to blame on politics.

The fine differences between RDF, RDFS, RDF(S), OWL, OWL Full, OWL DL,
OWL Lite, DLP - yes, I said fine differences between RDF and OWL DL -
it's just too much to cope with. If it is too much for us, what do we
expect of the future user of the Semantic Web? The web as we know it
grew to its todays size because it was easy. It wasn't because of
standards. For the first few years no one really cared about the HTML
standard, I mean, not to the extent we do today in the Semantic Web.
Even with tons of errors, pages would load and show nice results. It was
a very forgiving system. And now, find out why it was so widely adopted?

The problem is: maybe we really need to be as strict as we are. But I
hope we don't. I strongly believe into the virtue of "View source" - but
this means understandable views on the source. Not
RDF/XML-Serialisation. And still easy to copy. Only this way the
Semantic Web can lift off from the roots, from the users. The users were
creating the Web in the first years, not the companies. I don't know why
everybody is turning to the companies today.

Oh, I should stop, it sounds like ranting again.
