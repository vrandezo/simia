---
title: "What's in a name - Part 1"
date: 2004-12-28
language: "en"
slug: "what-s-in-a-name-part-1"
aliases:
  - "/wiki/What's_in_a_name_-_Part_1"
tags:
  []
---

There are tons of mistakes that may occur when writing down
[RDF](RDF "wikilink") statements. I will post a six part series of blog
entries, starting with this one, about what can go wrong in the course
of naming resources, why it is wrong, and why you should care - if at
all. I'll try to mix experience with pragmatics, usability with
philosophy. And I surely hope that, if you disagree, you'll do so in the
comments or in your own blog.

The first one is the easiest to spot. Here we go:

    "Politeia" dc:creator "Plato".

If you don't know about the differences between Literals, QNames and
URIs, please take a look at the [RDF
Primer](http://www.w3.org/TR/rdf-primer/). It's easy to read and
absolutely essential. If you know about the differences, you already
know that the above said actually isn't a valid RDF statement: you can't
have a literal as the subject of a statement. So, let's change this:

    philo:Politeia dc:creator "Plato".

What's the difference between these two? In the first one you say that
*"Plato"* is the creator of *"Politeia"* (we take the semantics of
*dc:creator* for granted for now). But in the second you say that
*"Plato"* is the creator of *philo:Politeia*. That's like in
*[Dragonheart](Dragonheart "wikilink")*, where Bowen tries to find a
name for the dragon because he can't just call him *"dragon"*, and he
decides on *"draco"*. The dragon comments: *"So, instead of calling me
dragon in your own language, you decide to call me dragon in another
language."*

Yep, we decide to talk about Politeia in another language. Because RDF
*is* another language. It tries to look like ours, it even has subjects,
objects, predicates, but it is not the language of humans. It is
(mostly) much easier, so easy in fact even computers can cope with it
(and that's about the whole point of the Semantic Web in the first
place, so you shouldn't be too surprised here).

*"Politeia"* has a well defined meaning: it is a literal (the quotation
marks tell you that) and thus it is interpreted as a value. *"Politeia"*
actually is just a word, a symbol, a sign pointing to the meant string
Politeia (a better example would be: *"42"* means the number 42.
*"101010b"*, *"Fourty-Two"* or *"2Ah"* would have been perfectly valid
other signs denoting the number 42).

And what about *philo:Politeia*? How is it different from *"Politeia"*,
what does this point to?

*philo:Politeia* is a Qualified Name (QName), and thus ultimatively a
short-hand notation for an URI, an Unified Resource Identifier. In RDF,
everything has to be a resource (well, remember, RDF stands for Resource
Description Framework), but that's not really a constraint, as you may
simply consider everything a resource. Even you and me. And URIs are
names for resources. Universally (well, at least globally) unique names.
Like *philo:Politeia*.

You may wonder about what your URI is, the one URI denoting you. Or what
the URI of Plato is, or of the Politeia? How to choose good URIs, and
what may go wrong? And what do URIs actually denote, and how? We'll
discuss this all in the next five parts of this series, don't worry,
just stay tuned.
