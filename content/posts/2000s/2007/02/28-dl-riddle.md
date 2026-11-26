---
title: "DL Riddle"
date: 2007-02-28
language: "en"
slug: "dl-riddle"
aliases:
  - "/wiki/DL_Riddle"
tags:
  []
---

Yesterday we stumbled upon quite a hard description logics problem. At
least I think it is hard. The question was, why is this ontology
unsatisfiable? Just six axioms. The ontology is availbe in [OWL
RDF/XML](http://nodix.de/download/unsatisfiable.owl), in
[PDF](http://nodix.de/download/unsatisfiable.pdf) (created with the [owl
tools](owl_tools "wikilink")), and here in Abstract Syntax.

    Class(Rigid complete restriction(subclassof allValuesFrom(complementOf(AntiRigid))))
    Class(NonRigid partial)
    DisjointClasses(NonRigid Rigid)
    ObjectProperty(subclassof Transitive)
    Individual(publishedMaterial type(NonRigid))
    Individual(issue type(Rigid) value(subclassof publishedMaterial))

So, the question is, why is this ontology unsatisfiable? It is even a
minimally unsatisfiable subset, actually, that means, remove any of the
axioms and you get a satisfiable ontology. Maybe you like to use it to
test your students. Or yourself. The debugger in
[SWOOP](http://www.mindswap.org/2004/SWOOP/) actually gave me the right
hint, but it didn't offer the full explanation. I figured it out, after
a few minutes of hard thinking (so, now you know how bad I am at DL).

Do you know? (I'll post the answer in the comments if no one else does
in a few days)

(Just in case you wonder, this ontology is based on a the
[OntOWLClean](http://www.ontoclean.org/ontoclean-dl-v1.owl) ontology
from [Chris
Welty](http://domino.research.ibm.com/comm/research_people.nsf/pages/welty.index.html),
see his paper at
[FOIS2006](http://www.formalontology.org/fois-2006/fois-2006.htm/) if
you like more info)


