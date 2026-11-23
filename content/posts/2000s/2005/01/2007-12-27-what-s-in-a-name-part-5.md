---
title: "What's in a name - Part 5"
date: 2005-01-10
language: "en"
slug: "what-s-in-a-name-part-5"
aliases:
  - "/wiki/What's_in_a_name_-_Part_5"
tags:
  []
---

After calling Plato an XML-Element, making movies out of websites and
having several accidents with careless URIs, it seems we return to the
very beginning of this series.

    http://semantic.nodix.net/document/Politeia dc:creator "Plato".

Whereby *<http://semantic.nodix.net/document/Politeia>* explicitly does
not resolve but returns a 404, resource not found. Let's remember, why
didn't we like it? Because humans, upon seeing this, have the urge to
click on it in order to get more information about it. A pretty good
argument, but every solution we tried brought us more or less trouble.
We didn't get happy with any of them.

But how can I dismiss such an argument? Don't I risk loosing focus with
saying "don't care about humans going nowhere"? No, I really don't think
so. Due to two reasons, one meant for humans and one for the machines.

First the humans (humans always should go first, remember this, Ms and
Mr PhD-student): humans actually never see this URI (or at least, should
not but when debugging). URIs who will grace the GUI should have a
*rdfs:label* which provides the label human users will see when working
with this resource. Let's be honest: only geeks like us think that
*<http://semantic.nodix.net/document/Politeia>* is a pretty obvious and
easy name for a resource. Normal humans would probably prefer
*"Politeia"*, or even *"The Republic"* (which is the usual name in
English speaking countries). Or be able to define their own name.

As they don't see the URI, they actually never feel the urge to click on
it, or to copy and paste it to the next browser window. Naming it
*<http://semantic.nodix.net/document/Politeia>* instead of
*<http://semantic.nodix.net/concept/1383b_xc>* is just for the sake of
readability of the source RDF files, but actually you should not derive
any information out of the URI (that's what the standard says). The
computer won't either.

The second point is, a RDF application shouldn't look up URIs either.
It's just wrong. URIs are just names, it is important that they remain
unique, but they are not there for looking up in a browser. That's what
URLs are for. It's a shame they look the same. Mozilla realised the
distinction when they gave their XUL language the namespace
*<http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul>*.
Application developers should realise this too. *rdfs:seeAlso* and
*rdfs:isDefinedBy* give explicit links applications may follow to get
more information about a resource, and using *owl:imports* actually
forces this behaviour - but the name does not.

Getting information out of names is like making fun of names. It's mean.
Remember the in-kids in primary school making fun of out-kids because of
their names? You know you're better than that (and, being a geek, you
probably were an out-kid, so mere compassion and fond memories should
hold you back too)..

Just to repeat it explicitly: if an URI gives back a 404 when you put it
in a browser navigation bar - that's OK. It was supposed to identify
resources, not to locate them.

Now you know the difference between URIs and URLs, and you know why
avoiding URI collision is important and how to avoid it. We'll wrap it
all in the final instalment of the series (tomorrow, I sincerely hope)
and give some practical hints, too.

By the way, right after the series I will talk about content
negotiation, which was mentioned in the comments and in e-Mails.

Uh, and just another thing: the wary reader (and every reader should be
wary) may also have noticed that

    Philosophy:Politeia dc:creator "Plato".

is total nonsense: it says, that there is a resource (identified with
QName *Philosophy:Politeia*) that is created by *"Plato"*. Rest assured
that this is wrong - no, not because Socrates should be credited as the
creator of the Politeia (this is another discussion entirely) but
because the statement claims that the string *"Plato"* created it - not
a Person known by this name (who would be a resource that should have an
URI). But this mistake is probably the most frequent one in the world of
the Semantic Web - a mistake nevertheless.

It's OK if you make it. Most applications will cope with it (and some
are actually not able to cope with the correct way). But it would not be
OK if you didn't know that you are making a mistake.
