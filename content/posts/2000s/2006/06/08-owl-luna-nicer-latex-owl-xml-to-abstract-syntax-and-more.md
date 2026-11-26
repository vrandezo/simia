---
title: "OWL luna, nicer latex, OWL/XML to Abstract Syntax, and more"
date: 2006-06-08
language: "en"
slug: "owl-luna-nicer-latex-owl-xml-to-abstract-syntax-and-more"
aliases:
  - "/wiki/OWL_luna,_nicer_latex,_OWL/XML_to_Abstract_Syntax,_and_more"
tags:
  []
---

After a long hiatus, due to some technical problems, finally I could
create a new version of the owl tools. So, [version 0.27 of the owl
tools](owl_tools "wikilink") is now released. It works with the new
version of [KAON2](KAON2 "wikilink"), and includes six months of bug
fixing, but also a number of new features that have introduced a whole
new world of new, exciting bugs as well.

The owl latex support was improved greatly. Translation of an owl
ontology is done now more careful, and the user can specify much more of
the result than before.

A new tool is owl luna - luna like local unique name assumption. It adds
an axiom to your ontology that states that all individuals are different
from each other. Due to most ontology editors not allowing to do this
automatically, here you find a nice maintenance tool to make your
ontology much less ambiguous.

The translations of OWL/RDF to OWL/XML and back have been joined in one
new tool, called owl syntax, that allows you to translate owl ontologies
also to OWL Abstract Syntax, a much nicer syntax for owl ontologies.

owl dlpconvert has been extended as it now also serialzes it results as
RuleML if you like. So you can just pipe your ontologies to RuleML.

So, the tools have both become sharper and more numerous, making your
toolbelt to work with owl in daily life more usable. Get the new [owl
tools](owl_tools "wikilink") now. And if you peek into the source code,
the code has underwent a major clean up, and you will also see the new
features I am working on, that have to do with ontology evaluation and
more.

Have fun with the tools\! And send me your comments, wishes, critiques\!


