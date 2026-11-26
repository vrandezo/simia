---
title: "First look at Freebase"
date: 2007-03-16
language: "en"
slug: "first-look-at-freebase"
aliases:
  - "/wiki/First_look_at_Freebase"
tags:
  []
---

I got the chance to get a close look at
[Freebase](http://www.freebase.com/) (thanks,
[Robert](http://www.freebase.com/view/user?id=/user/robert)\!). And I
must say -- I'm impressed. Sure, the system is still not ready, and you
notice small glitches happening here and there, but that's not what I
was looking for. What I really wanted to understand is the idea behind
the system, how it works -- and, since it was mentioned together with
Semantic MediaWiki one or twice, I wanted to see how the systems
compare.

So, now here are my first impressions. I will sure play more around with
the system\!

Freebase is a databse with a flexible schema and a very user friendly
web front end. The data in the database is offered via an API, so that
information from Freebase can be included in external applications. The
web front end looks nice, is intuitive for simple things, and works for
the not so simple things. In the background you basically have a huge
graph, and the user surfs from node to node. Everything can be
interconnected with named links, called properties. Individuals are
called topics. Every topic can have a multitude of types: Arnold
Schwarzenegger is of type politician, person, actor, and more. Every
such type has a number of associated properties, that can either point
to a value, another topic, or a compound value (that's their solution
for n-ary relations, it's basically an intermediate node). So the type
politician adds the party, the office, etc. to Arnold, actor adds
movies, person adds the family relationships and dates of birth and
death (I felt existentially challenged after I created my user page, the
system created a page of me inside freebase, and there I had to deal
with the system asking me for my date of death).

It is easy to see that types are crucial for the system to work. Are
they the right types to be used? Do they cover the right things? Are
they interconnected well? How do the types play together? A set of types
and their properties form a domain, like actor, movie, director, etc.
forming the domain "film", or album, track, musician, band forming the
domain "music". A domain is being administrated by a group of users who
care about that domain, and they decide on the properties and types. You
can easily see ontology engineering par excellence going on here, done
in a collaborative fashion.

Everyone can create new types, but in the beginning they belong to your
personal domain. You may still use them as you like, and others as well.
If your types, or your domain, turns out to be of interest, it may
become promoted as being a common domain. Obviously, since they are
still alpha, there is not yet too much experience with how this works
out with the community, but time will tell.

Unsurprising I am also very happy that Metaweb's Jamie Taylor will give
an invited talk at the
[CKC2007](http://km.aifb.uni-karlsruhe.de/ws/ckc2007/) workshop in Banff
in May.

The API is based on JSON, and offers a powerful query language to get
the knowledge you need out of Freebase. The description is so good that
I bet it will find almost immediate uptake. That's one of the things the
Semantic Web community, including myself, did not yet manage to do too
well: selling it to the hackers. Look at this API description for how it
is done\! Reading it I wanted to start hacking right away. They also
provide a few nice "featured" applications, like the [Freebase movie
game](http://www.akuma.us/metaweb/moviegame.html). I guess you can play
it even without a freebase account. It's fun, and it shows how to reuse
the knowledge from Freebase. And they did some good tutorial movies.

So, what are the differences to [Semantic
MediaWiki](Semantic_MediaWiki "wikilink")? Well, there are quite a lot.
First, Semantic MediaWiki is totally open source, Metaweb, the system
Freebase runs on, seems not to be. Well, if you ask me, Metaweb (also
the name of the company) will probably want to sell MetaWeb to
companies. And if you ask me again, these companies will make a great
deal, because this may replace many current databases and many problems
people have with them due to their rigid structure. So it may be a good
idea to keep the source closed. On the web, since Freebase is free, only
a tiny amount of users will care that the source of Metaweb is not free,
anyway.

But now, on the content side: Semantic MediaWiki is a wiki that has some
features to structure the wiki content with a flexible, collaboratively
editable vocabulary. Metaweb is a database with a flexible,
collaboratively editable schema. Semantic MediaWiki allows to extend the
vocabulary easier than Metaweb (just type a new relation), Metaweb on
the other hand enables a much easier instantiation of the schema because
of its form based user interface and autocompletion. Metaweb is about
structured data, even though the structure is flexible and changing.
Semantic MediaWiki is about unstructured data, that can be enhanced with
some structure between blobs of unstructured data, basically, text.
Metaweb is actually much closer to a wiki like
[OntoWiki](http://3ba.se/). Notice the name similarity of the domains:
freebase.com (Metaweb) and 3ba.se (OntoWiki).

The query language that Metaweb brings along, MQL, seems to be almost
exactly as powerful as the query language in Semantic MediaWiki. Our
design has been driven by usability and scalability, and it seems that
both arrived at basically the same conclusions. Just a funny
coincidence? The query languages are both quite weaker than SPARQL.

One last difference is that Semantic MediaWiki is fully standards based.
We export all data in RDF and OWL. Standard-compliant tools can simply
load our data, and there are tons of tools who can work with it, and
numerous libraries in dozens of programming languages. Metaweb? No
standard. A completely new vocabulary, a completely new API, but
beautifully described. But due to the many similarities to Semantic Web
standards, I would be surprised if there wasn't a mapping to RDF/OWL
even before Freebase goes fully public. For all who know Semantic Web or
Semantic MediaWiki, I tried to create a [little dictionary of Semantic
Web terms](http://ontoworld.org/wiki/Semantic_Web_Vocabulary).

All in all, I am looking forward to see Freebase fully deployed\! This
is the most exciting Web thingy 2007 until now, and after [Yahoo\!
pipes](http://pipes.yahoo.com/), and that was a tough one to beat.


