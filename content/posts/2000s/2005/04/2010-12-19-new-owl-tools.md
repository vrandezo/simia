---
title: "New OWL tools"
date: 2005-04-06
language: "en"
slug: "new-owl-tools"
aliases:
  - "/wiki/New_OWL_tools"
tags:
  []
---

The [KAON2 OWL Tools](owl_tools "wikilink") get more diverse and
interesting. Besides the simple axiom and entity **counter** and
**dumper**, the not so simple **dlpconverter**, and the **syntactic
transformer** from XML/RDF to OWL/XML and back, you now also have a
**filter** (want to extract only the subClassOf-Relations out of your
ontology? Take filter), **diff** and **merge** (for some basic syntactic
work with ontologies), **satisfiable** (which checks if the ontology can
have a satisfying model), **deo** (turning SHOIN-ontologies in
SHIN-ontologies by weakening, should be sound, but naturally not
complete) and **ded** (removes some domain-related axioms, but it seems
this one is still buggy).

I certainly hope this toolbox will still grow a bit. If you have any
suggestions or ideas, feel free to mail me or comment here.
