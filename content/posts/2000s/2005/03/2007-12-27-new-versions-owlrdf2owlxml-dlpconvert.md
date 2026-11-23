---
title: "New versions: owlrdf2owlxml, dlpconvert"
date: 2005-03-16
language: "en"
slug: "new-versions-owlrdf2owlxml-dlpconvert"
aliases:
  - "/wiki/New_versions:_owlrdf2owlxml,_dlpconvert"
tags:
  []
---

New versions of [owlrdf2owlxml](owlrdf2owlxml "wikilink") and
[dlpconvert](dlpconvert "wikilink") are out.

owlrdf2owlxml got renamed, as it was formerly known as
[rdf2owlxml](rdf2owlxml "wikilink"). But as a colleague pointed out,
this name can easily be misunderstood, meaning to transform arbitrarily
RDF to OWL. It doesn't do that, it only transforms OWL to OWL, from
RDF/XML-serialisation to XML Presentation Syntax. And it seems to work
quite stable, it can even transform the famous wine ontology. Version
0.4 out now.

dlpconvert lost a lot of its bugs. And as most of you were feeding
RDF/XML to it, well, now you can do it officially (listen to the users),
too. It reads both syntaxes, and creates a Prolog program out of your
ontology. Version 0.7 is out.

They are both based on [KAON2](KAON2 "wikilink"), the Karlsruhe Ontology
Infrastructure module, written by [Boris Motik](Boris_Motik "wikilink").
My little tools are just wrapped around KAON2 and using its
functionality. To be honest, I'm thinking of writing quite a number of
little tools like this, who offer different functionality, thus
providing you with a nice toolkit to handle ontologies efficiently. I
don't lack ideas right now, it's just I' m not sure that there's
interest in this.

Well, maybe I should just start and we'll see...

By the way, both tools are not only available as web services, but you
may also download them as command line tools from their respective
websites and play around it on your PC. That's a bit more comfortable
than using a browser as your operating system.
