---
title: "AIFB OWL tools"
date: 2005-03-22
language: "en"
slug: "aifb-owl-tools"
aliases:
  - "/wiki/AIFB_OWL_tools"
tags:
  []
---

Working with ontologies isn't yet as easy as it could be - especially
because the number of little helpers is still far too small. After
having written [dlpconvert](dlpconvert "wikilink") and
[owlrdf2owlxml](owlrdf2owlxml "wikilink") (the tool with the maybe most
clumsy name in the history of the Semantic Web) I noticed how easy it
would be to write some more tools based on
[Boris'](Boris_Motik "wikilink") [KAON2](KAON2 "wikilink") OWL ontology
infrastructure.

And so I went ahead. First I integrated dlpconvert and owlrdf2owlxml (or
short, r2x) in it, then I added a simple ontology dumper and axiom and
entity counter. Want to know how many individuals are in your ontology?
Simply type *owl count myontology.owl -individual*, and there you go.
Want a list of all Classes? Try *owl print myontology.owl -owlclass*.
It's as easy as that.

I'm totally aware that this functionality maybe isn't worth the effort
of building a tool for. But this is just a beginning: I want to add more
functionality to filter, merge, compare and much more to it. The point
is, at the end having a handy little set of OWL tools you can work with.
I miss that really with OWL, and now here it is. At least, a beginning.

Grab your copy now of the [AIFB OWL Tools](owl_tools "wikilink").
