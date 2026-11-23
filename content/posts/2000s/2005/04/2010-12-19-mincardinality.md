---
title: "MinCardinality"
date: 2005-04-05
language: "en"
slug: "mincardinality"
aliases:
  - "/wiki/MinCardinality"
tags:
  []
---

More on the [Unique Name Assumption](Unique_Name_Assumption "wikilink")
(UNA), because [Andrew answered on
it](http://morenews.blogspot.com/2005/04/uniqueness-and-open-world.html),
with further arguments. He quotes
[Paul](http://gearon.blogspot.com/2005/04/more-cardinality-after-prototypos.html):
" The initial problem was cardinality and OWL Flight attempts to solve
the problem with cardinality. [Paul put it
succinctly](http://gearon.blogspot.com/2005/04/more-cardinality-after-prototypos.html):
"So what is the point of statements with the owl:minCardinality
predicate? They can't ever be false, so they don't tell you anything\!
It's kind of like a belt and braces when your belt is unbreakable." "

Again I disagree, this time to Paul: the minimal cardinality axiom does
make sense. For what, they ask - well, for saying that there is a
minimal cardinality on this relation. Yeah, you are right: this is an
axiom which hardly can lead to an inconsisten ontology. But so what? You
nevertheless can cut down the number of possible models with it and get
more information out of the ontology.

"I would agree - this was my main problem - how do you explain to Joe
(and Andrew) that all his CDs are the same rather than different."

That's turning around the argument. If the reasoner would claim that all
of Joes CDs are the same, he would be doing a grave mistake. But so
would he if he would claim that all are different: the point is, he just
doesn't know. Without having someone to state sameness or difference
explicitly, well, you can't know.

"I did comment that the resolution, local unique names using
AllDifferent, didn't actually seem to solve the problem well enough
(without consideration for scalability for example)."

I am not sure why that should be. It seems that Andrew would be happy if
there was a file-wide switch claiming "If I use different URIs here I
mean different objects. This file makes the UNA." These files would
easily be translated to standard OWL files, but there would be less
clutter inside (actually, everything that would need to be done is
adding an axiom of allDifferent with all the names of the file).

"I have a feeling that context is a better solution to this problem
(that might just be my golden hammer though)."

I don't understand this one, maybe Andrew will elaborate a bit on this.

If you imagine an environment with axioms floating around, from
repository to repository, being crawled, collected, filtered, mapped and
combined, you must not make the Unique Name Assumption. If you remain in
your own personal knowledge base, you can embrace UNA. And everything
you need between is one more axiom.

Is it that bad?

**Comments**

*Andrew Newman (11 April 2005 20:58)*

The idea of using context would be a way of saying "close off the world" or whatever - that everything in a particular model followed different axioms - like unique names or whatever - because I think generally they are more useful - of course I might be wrong but at least there's the opportunity to do so without having to explicitly make the AllDifferent statement for each one.

BTW, after reading [Paul's postings on RDF Logic](http://lists.w3.org/Archives/Public/www-rdf-logic/2005Apr/0005.html) I think I got an understanding a lot quicker than I might have otherwise.
