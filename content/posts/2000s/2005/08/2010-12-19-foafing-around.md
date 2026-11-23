---
title: "FOAFing around"
date: 2005-08-23
language: "en"
slug: "foafing-around"
aliases:
  - "/wiki/FOAFing_around"
tags:
  []
---

I tried to create FOAF-files out of the ontology we created during the
[Summer School for the Semantic Web](SSSW_Last_Day "wikilink"). It
wasn't that hard, really: with our ontology I have enough data to create
some FOAF-skeletons, so I looked into the FOAF-specification and started
working on it.

    <foaf:person about="#gosia">
      <foaf:knows resource="#anne" />
      <foaf:name datatype="http://www.w3.org/2001/XMLSchema#string">Gosia Mochol</foaf:name>
    </foaf:person>
    <rdf:description about="#anne">
      <rdfs:isdefinedby resource="http://semantic.nodix.net/sssw05/anne.rdf" />
    ...

Well, every one of us gets his own FOAF-file, where one can find more
data about the person. Some foaf:knows-relations have been created
automatically for the people who worked together in a miniproject. I
didn't want to assume too much else.

The code up there is valid FOAF as much as I can tell. But all the
(surprisingly sparse) tools could not cope with it, due to different
reasons. One complained about the datatype-declaration in the foaf:name
and then ignored the name at all. Most tools didn't know that
rdfs:isDefinedBy is a subproperty of rdfs:seeAlso, and thus were not
able to link the FOAF-files. And most tools were obviously surprised
that I gave the persons URIs instead of using the IFP over the sha1-sum
of their e-Mails. The advantage of having URIs is that we can use those
URIs to tag pictures or to keep track of each other publications, after
the basic stuff has been settled.

Pitily, the basic stuff is not settled. To me it seems, that the whole
FOAF stuff, although being called the most widespread use of the
Semantic Web, is still in its infancy. The tools hardly collaborate,
they don't care too hard about the specs, and there seems no easy way to
browse around ([Mortens
explorer](http://xml.mfd-consult.dk/foaf/explorer/) was down at the time
when I created the FOAFs, which was frustrating, but now it works: take
a look at the created FOAF files, entering with [my generated FOAF
file](http://xml.mfd-consult.dk/foaf/explorer/?foaf=http://semantic.nodix.net/sssw05/denny.rdf)
or the one for [Enrico
Motta](http://xml.mfd-consult.dk/foaf/explorer/?foaf=http://semantic.nodix.net/sssw05/enricoM.rdf)).
Maybe I just screwed it all up when generating the FOAF-files in the
first run, but I don't think so really...

Guess someone needs to create some basic working toolset for FOAF. Does
anyone need requirements?
