---
title: "What's in a name - Part 4"
date: 2005-01-07
language: "en"
slug: "what-s-in-a-name-part-4"
aliases:
  - "/wiki/What's_in_a_name_-_Part_4"
tags:
  []
---

I promised you four solutions to the problem of dubbing with appropriate
URIs. So, without further ado, let's go.

The first one you've seen already. It's using anonymous nodes.

    _person foaf:interest _security.
    http://dmoz.org/Computers/Security/ dc:subject _security.

But here we get the problem, that we can't reference *\_security* from
outside, thus loosing a lot of the possibilities inherent in the
Semantic Web, because this way you can not say that someone else is
interested in the same topic as \_person above. Even if you say, in
another RDF file,

    _person2 foaf:interest _security.
    http://dmoz.org/Computers/Security/ dc:subject _security.

*\_security* actually does not have to be the same as above. Who says,
websites only have one subject? The coincidental equality of the
variable name *\_security* bears as much semantics as the equality of
two variables x in a C and a Python-Program.  
So this solution, although possible, bears too much short-comings. Let's
move on.

The second solution is hardly available to the majority of us puny
mortals. It's introducing a new URI schema. Let's return to our very
first example, where we wanted to say that the Politeia was written by
Plato.

    urn:isbn:0192833707 dc:creator "Plato".

Great\! No problems here. Sure, your web-browser can't (yet) resolve
*<urn:isbn:0192833707>*, but no ambiguity here: we know exactly of what
we speak.

Do we? Incidentally, *<urn:isbn:0465069347>* also denotes the Politeia.
No, not in another language (those would be another handful of ISBN
numbers), just a different version (the text is public domain). Now,
does the following statement hold?

    urn:isbn:0192833707 owl:sameAs urn:isbn:0465069347.

Most definitively not. They have different translators. They have
different publishers. These are different books. But it's the same -
what? What is the same? It's not the same text. It's not the same book.
They may have the same source text they are translated from. But how to
express this correctly and still useful?

The *<urn:isbn>:* scheme is very useful for a very special kind of
entities - published books, even the different versions of published
books.  
The problem with this solution that you would need tons of schemes.
Imagine the number of committees\! This would, no, this should never
happen. We definitively need an easier solution, although this one
certainly does work for very special domains.

Let's move on to the third solution: the magic word is fragment
identifier. \#. Instead of saying:

    http://semantic.nodix.net/Politeia dc:creator http://semantic.nodix.net/Plato.

and thus getting 404s en masse, I just say:

    http://semantic.nodix.net/#Politeia dc:creator http://semantic.nodx.net/#Plato.

See? No 404. You get to the homepage of this blog by clicking there. And
it's valid RDF as well. So, isn't it just perfect? Everything we wished
for?

Not totally, I fear. If I click on *<http://semantic.nodx.net/#Plato>*,
I actually expect to read something about Plato, and not to see a blog
about the Semantic Web. So this somehow would disappoint me. Better than
a 404, still...  
The other point is my bandwidth. There can be RDF files with thousands
of references. Following every single one will lead to considerable
bandwidth abuse. For naught, as there is no further information about
the subject on the other side. Maybe using
*<http://semantic.nodix.net/person#Plato>* would solve both problems,
with *<http://semantic.nodix.net/person>* being a website saying
something like *"This page is used to reserve conceptual space for
persons. To understand this, you must understand the magic of URIs and
the Semantic Web. Now, go back whereever you came from and have a nice
day."* Not too much webspace and bandwith will be used for this tiny
HTML-page.

You should be careful though to not have a real fragment identifier
*"Plato"* in the page, or you would actually dereference to this
element. URI collision again. You don't want Plato to become
half-philosopher / half-XML-element, do you?

We will return to fragment identifiers in the last part of this six part
series again. And now let's take a quick look at the fourth solution -
we will discuss it more thoroughly next time.

Use a fresh URI whenever you need an URI and don't care about it giving
a 404.

**Comments**

*Richard Cyganiak (7 January 2005 16:26)*

Good writeup! A couple of points:

The "overloaded fragment identifier" problem is not really much of a problem. The URI http://semantic.nodix.net/person#Plato can very well be both "a section about Plato in a web page" and "an RDF resource representing Plato in an RDF document". When a web browser asks for the URL, it can be served the web page; when a semantic web agent asks, it can be served the RDF document (through HTTP content negotiation), thus pretty much avoiding the problem.

I'd argue that the anonymous node approach is the right one in many cases. Often, there's no requirement for your stuff being referencable from the outside. In these cases, using anonymous nodes is fine and may save some headaches.

In the long run, maybe there will be sites publishing directories with RDF information about movies or philosophers. Maybe there will be a search engine that lets you search for URIs representing those concepts. Then you can simply use that URI, and don't have to make up your own.

You're mixing up foaf:interest and foaf:topic_interest. The former simply doesn't have the meaning you assume in your examples. Arguably, the FOAF people should have defined them differently, but there's nothing we can do about this now.

I'm looking forward to the last two parts of your series.

What's in a name - Part 4 Comment 1

*Denny (10 January 2005 16:39)*

Hi Richard,

Thank you a lot for making the first comment to Semantic Nodix! :)

About your thoughtful points:

I don't like to use content negotiation in order to get the right resource (or rather, representation of a resource, which itself is a resource again). I prefer getting explicitly the resource I asked for, and I feel like that's why URLs are there for: to locate one specific resource. That's why I try to avoid that way.

Anonymous nodes. My only reason against them is that they are not referenceable. You say, most of the time that's ok - I'd claim, well, most of the time you can't know if maybe someone will want to reference it in the future. Why making it impossible? Actually making URIs is very cheap (well, making good URIs isn't, but that's the point of this blogging series), so why not give a reference to every node? The web grew the way it did because we did not claim beforehand to know which resources need to be adressible and which not. It would be a totally different web today if the majority of resource out there were not adressable.

Your last point was answered in the blog and comments of the previous part.

Thanks on your comments, denny
