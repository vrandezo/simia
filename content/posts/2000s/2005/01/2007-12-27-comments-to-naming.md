---
title: "Comments to naming"
date: 2005-01-13
language: "en"
slug: "comments-to-naming"
aliases:
  - "/wiki/Comments_to_naming"
tags:
  []
---

[Richard Newman](http://holygoat.co.uk/) sent me some thoughtful
comments via eMail on the [What's in a
name](What's_in_a_name "wikilink") series (there were also some great
comments on the individual entries, feel free to browse them). He sent
them via eMail, cause he thought he couldn't comment - that should be
wrong, everyone should be able to comment anonymously. Or did anyone
else encounter problems? I should switch to some dedicated software
soon, anyway, but right now I don't have the time to dig deeper into it.
I especially miss trackback, sigh.

Here's what Richard wrote:

*"Your first point, about ISBNs and "what's being referenced" --- I
think you'd be interested in
[FRBR](http://www.oclc.org/research/projects/frbr/default.htm), which is
a modelling of the bibliographical domain. It splits things up into*

*Work -\> Expression -\> Manifestation -\> Item*

*A work is an abstract concept, like "Politeia". An expression is a
realisation of a work, so a particular translation is an expression. A
manifestation is physical embodiment of an expression: this is what's
given an ISBN. All copies of a certain book are Items; the edition of
the book is their Manifestation.*

*So, you see, when you're discussing Plato's Politeia, you have to be
conceptually clear about whether you're talking about works,
expressions, manifestations, or items.*

*E.g.*

    :PolWork dc:creator "Plato" ;
      rdfs:label "Plato's Politeia, the abstract concept." .
    :PolExp1 ex:translator "Mr Smith" ;
      frbr:work :PolWork ;
      rdfs:label "Mr. Smith's translation of Plato's Politeia." .
    :PolMan1 ex:publisher "Penguin" ;
      frbr:expression :PolExp1 ;
      rdfs:label "Penguin's edition of Smith's translation." .
    :MyCopy ex:owner hg:RichardNewman ;
      frbr:manifestation :PolMan1 ;
      rdfs:label "Richard's copy of the Penguin edition." .

*Do you see? Each level has its own properties (and some may be
duplicated; e.g. each has a title: the title of the abstract work, the
name given to the translation, the name Penguin prints on each book, and
the name printed on my copy).*

*I've done a bit of work on modelling FRBR in RDFS/OWL, but haven't yet
finished. "*

I think that's really interesting, and taking a look at FRBR it was
pretty well done. I sure am looking forward to see Richards
interpretation in OWL, and will probably use it.

*"Your second issue is the difference between a resource and its
representation. A URI should only refer to one thing; it is entirely
wrong to use <http://www.holygoat.co.uk> to refer both to my homepage
(as in using RDF to describe its language, or size, or last-modified)
and to me (my name, my email address, etc.) which I have seen done.*

*Your web server should return RDF for <http://semantic.nodx.net/#Plato>
if your browser says that it accepts RDF+XML. A normal browser should
have an HTML representation returned. Indeed, it's possible to do the
following:*

  - the abstract resource. Hit this with a browser, get an HTML page;
    with an RDF agent, get some RDF.

<!-- end list -->

    http://example.com/Plato a rdf:resource .

  - the HTML representation.

<!-- end list -->

    http://example.com/Plato/html a ex:representation ;
      ex:representationOf http://example.com/Plato .

\*\# the RDF.

    http://example.com/Plato/rdf a ex:representation ;
      ex:representationOf http://example.com/Plato .

*i.e. you can unambiguously refer to each representation, and the
resource. When your client arrives, asking for Plato, you can redirect
them to the appropriate place. Clever, huh?*

*URIs should never give a 404. They should return the appropriate
headers or content for whatever the client is requesting; this may be
the RDF file in which the resource is defined, if the client understands
RDF, or an HTML page.*

*If you're interested in this sort of thing, it pops up on the W3C's RDF
Interest Group list occasionally.*

*Patrick Stickler and others have come up with an additional HTTP verb,
MGET, which will return the RDF description of a resource. Combined with
their URIQA architecture, it will give you a Concise Bounded Description
for a URI. This stops you having to somehow put descriptions into
particular files, and better deals with the distributed nature of the
Semantic Web. Check it out; it presents several convincing arguments for
not using fragment identifiers to refer to resources, and solves your
bandwidth problem. You should never have to dump a whole file to get a
description of a URI."*

I have to note that Richard wrote me this just after [part 4 of the
series](What's_in_a_name_-_Part_4 "wikilink") was published, so I could
answer some of the questions already in the last two parts. Just to
summarise it: I don't like content negotiation. Although it is
technically totally feasible, I disagree that it should be done or is a
good solution. If my browser asks for
*<http://semantic.nodix.net/#Plato>* I don't think I should get
different things depending on the content negotiation. This feels like
cheating.

I wrote that to Richard already, and he answered:

*"I think we agree on the main point, which is that*

    foaf:name "Richard" ; ex:format "HTML" .

*which is a travesty :) "*

He is totally right here.

*"You still see it happen, though, with people referring to Wikipedia
pages as if they were the abstract resource.*

*The content negotiation (getting different things depending on what you
accept) is exactly what the Web is supposed to do. If I'm using a mobile
browser, I want a simplified version of a page; if I'm an RDF agent, I
want RDF, if it exists, because HTML is of no use to me. A common usage
of this is to serve up strict XHTML to Mozilla, and less-strict HTML to
Internet Explorer. It is also done all the time to serve PNG where the
client accepts it, and GIF if it doesn't, and there is an intentional
disconnect on the Web between a resource and its representations.*

*The lack of such a disconnect would lead to exactly the problem you
describe; if I can't return a representation of a resource, because it's
abstract, then how do I find out anything about it? I could use MGET,
but you can't MGET a person... so, if you want to talk about the real
world thing "Plato", he has to 404, or you get the "what am I talking
about?" problem. Better, in my view, to redirect a browser to plato.html
and a SW agent to a chunk of RDF. "*

I would rather like to ask for *<http://semantic.nodix.net/Plato.rdf>*
to get the RDF/XML representation,
*<http://semantic.nodix.net/Plato.owl>* to get the OWL/XML
representation, *<http://semantic.nodix.net/Plato.html>* to get a HTML
page for the user to read and *<http://semantic.nodix.net/Plato.jpg>*
for a picture of Plato. This shouldn't be hidden behind content
negotiation. I know, I know, Patrick would strongly disagree here, but I
think it feels wrong and actually defies the idea of an URI.

*"You can do exactly that (and I agree that the representations should
have separate URIs --- conneg is only for when you're trying to get some
description of an abstract resource), but then how do you refer to the
abstract concept of "Plato"? <http://>.../Plato is a resource, and I
want to make statements about him. But there's no point in it being 404
when dereferenced, because then how would I find out that Plato.html
exists? HTTP doesn't return URIs, it returns representations of them.*

*A URI is simply something that is dereferenced to get a representation,
and that representation should be decided on by conneg. In this case,
/Plato is an abstract resource, so one of the representations should be
returned. We can then make statements about Plato (e.g. foaf:name
"Plato"), and about the JPEG and HTML representations, because they have
different URIs, but still get something useful back when we want to
access /Plato."*

I also dislike MGET right now. Maybe I am wrong, but to me, the whole
URIQA architecture feels somewhat wrong - but maybe I should just dwell
deeper into it, I have to admit, I didn't study it yet enough to really
be in a position to bash on it. The problem is, that MGET seems
unnecessary to me - and it works on a different conceptual level than
the rest of the Semantic Web proposals. I think everything MGET solves
can be solved with tools that already exist: Richards example above,
where he gives triples telling us which representations are used to
describe a resource, shows perfectly well that you actually don't need
content negotiation and MGET.

*"There are things to question about
[URIQA](http://sw.nokia.com/uriqa/URIQA.html), but it does have some
good going for it. MGET is actually an implicit query. In the standard
Web model, you request URIs and get back document representations. Doing
an MGET on a Web server is asking it to return a description, regardless
of where on the site descriptions of that resource exist, and you're
explicitly asking for meta-data. As Patrick points out, it's similar
doing a GET and specifying that you accept RDF, but is likely to be more
concise (the difference between a "representation" and a "description").
In fact, this is exactly what the Nokia URIQA server does.*

*MGET overlaps with query servers a bit, and with GET a bit, but it's a
little bit special, too. The whole idea is that from a single URI you
can get a useful description of a resource, just by issuing a single
MGET. Every other approach needs more work."*

This URIQA / MGET stuff sounds more and more interesting. I really
should dwell deeper into it.

Also, the idea of Concise Bounded Descriptions may be very neat, I have
to study that more as well. Funny thing, the very same day Richard
pointed me to it, a colleague told me about it too - this is usually a
sign, that this idea is worth considering more.

Richard also wrote "URIs should never give a 404", and as you know, I
disagreed with it mildly. He tried to summarise his position:

*"I consider that each returned resource should have its own URI ---
e.g. Plato.jpg --- and that the original URI should be used to make
statements about the abstract resource. This allows you to say*

    ...Plato foaf:name "Plato" .
    ...Plato.jpg ex:resolution "150dpi" .
    ...Plato.html dc:creator "Denny" .

*Dereferencing the abstract resource, rather than throwing a 404, should
do something useful --- e.g. redirecting with a 303 to one of the
representations. Have you ever tried viewing a Blogger Atom feed in your
browser? If you hit it with an RSS reader, you get the XML, but in a
browser Blogger shows you an XHTML transformation of the XML. That's
useful, and I think that's how the Semantic Web should work. Imagine if
your agent hit /Plato, and got RDF out of it, but when you looked at it
with your browser you saw a dynamically-generated HTML page? Handy\!*

*I can understand your objection, though; it does seem wrong that you
get different things out of the same URI. However, you should almost
always get HTML out of plato.html, and RDF out of plato.rdf. All the
conneg is doing is making sure you can see an abstract thing in the best
way possible, according to what you've told the server you can
understand. "*

Richard is pretty good in convincing me, cause he uses the right
arguments: it's for the people, dummy, and the machines can work it out
anyway.

I still stick to the [recommendations I gave
yesterday](What's_in_a_name_-_Part_6 "wikilink"). But just as I am
writing, and rereading it all, I am starting to change my mind on
content negotiation. Maybe it is a good thing. I will have to think
about it some more, and as soon as I come to a solution, I will bother
you with it again. I still have a gut feeling about it that tells me
'no', but the reasons given sound very convincing and I agree with most
of them, so heck, let's meditate on this as soon as I find a few hours
to spare.

Big thanks to Richard and his thoughts, anyway. I hope this discussion
helps you to make up your own mind as well.
