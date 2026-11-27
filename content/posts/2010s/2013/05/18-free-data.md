---
title: "Free data"
date: 2013-05-18
language: "en"
slug: "free-data"
aliases:
  - "/wiki/Free_data"
tags:
  - Simia
  - english
  - data
  - legal
  - licensing
---

tl;dr - If you publish data, attach the CC0 license to it, but that’s
basically just advertising - don’t think it means anything. If you use
data, you do not have to care much about the data license. If you
republish data, it’s a bit more complicated, but not as horrible as you
might think.

Imagine a student reading a CC-BY-SA published textbook on compilers.
Next thing, based on that knowledge, they write a parser and publish the
binary on the Web. Do they have to acknowledge the textbook? Do they
have to publish their code under the same license?

Imagine a designer creating an image with GIMP, a fantastic open source
image processing tool, published under the GPL. Or a developer writing
his code in Eclipse. Or a website being served from a Linux box. What
legal implications does it have for the license of the image? For the
source code? For the served page?

Imagine a search engine that changes its background color depending on
the type of thing you are searching for. You enter a city - it turns
gray. You enter a person - red for females, blue for males, and purple
for others. You enter a company - yellow. And so on. Let us assume that
the search engine does that by figuring out the thing you are searching
for and then asking DBpedia for its type. Since DBpedia is licensed
under CC-BY-SA, does this mean we have to put a link on the search
result acknowledging DBpedia? Does this mean we have to publish our
search index under CC-BY-SA as well?

Imagine Red Cross publishing pages about the countries they work in, and
adding the population data to each of them from Freebase, the location
from OpenStreetMaps, the local name of the country from GeoNames, and
the capital from DBpedia. What amount of legal disclaimer would need to
be displayed on the page? Maybe some of the data items derive from
another source? What about their licenses? What about this license
stacking effect?

There are some rather vague ideas floating about how the whole
intellectual property law apparatus works for data. I have mulled over
this for a long time, and read more laws and court cases than I care to
admit. I want to try to make a few points in the following.

Let’s start with the basics. What laws do actually apply?

Copyright law protects the expression, not the idea - the form, not the
content. You can watch the newest Iron Man movie, and you are legally
allowed to annoy your friends with retellings of the movie as often as
you want. But you are not allowed to film it with your phone camera in
the theater and display it to your friends. If you learn something from
a textbook, you are free to write your own textbook, adding other
knowledge you have acquired, possibly from other textbooks and
publications. Only if you start copying the original texts too closely,
you will get into legal trouble.

Almost all of the above mentioned licenses - all Creative Commons
licenses currently available, as well as the GFDL or the GPL - are based
on copyright laws. The GPL has started, as Stallmann admits, as a legal
hack of copyright law. This makes a lot of sense, since these licenses
have not meant to cover data, but expressions: texts, music, and the
like. This means, these licenses cannot extend beyond that. They only
cover the expression. They cover the actual RDF/XML file, the string of
characters. Not the content. Not the graph.

(Note that ODBL and the current draft of the upcoming fourth revision of
CC go beyond copyright and include database right where applicable, i.e.
within the legislation of the EU. This extension is irrelevant for the
US.)

This means that such licenses, like GFDL for data, have no restricting
effect if you want to use the data. Only if you want to republish the
data files more or less verbatim (in whole or partially, standalone or
as part of a bigger project), you need to think about the original
license. Merely including the data (not the files\!) has no effect
stemming from copyright.

This also makes intuitively sense: if someone takes Wikipedia and counts
the distribution of words and letters in Wikipedia, the subsequent
publication of the results is not restricted by the original license
Wikipedia was published under. If someone takes the whole Web, and
creates a graph of all links on the Web, and starts to apply some
algorithms on this graph, the subsequent usage of the results of these
algorithms are not subject to any of the licenses of the original texts
published on the Web. Copyright simply does not extend this far. And
that is good.

So much to copyright. Unfortunately, the European Union went a step
further. They recognized that copyright does not apply to databases.
They also recognized that the EU was not doing well in their competition
against the US, with regards to publishing databases. So they decided to
level the field by introducing a completely new right, the database
right. This protects the effort that goes into creating databases -
basically their schema (which columns should I have) and the coverage
(which rows do I have in my database). Ten years later the EU made an
evaluation of the effectiveness of the laws, and came to some
interesting conclusions: first, technically the newly database rights
made things more complicated; second, most publishers obviously do not
understand it, but are happy with what they think it means (which
usually contradicts with what it actually means); and third, it
completely failed in its goal to advance the database publishing sector.
The report offers options to drop the whole database rights thing again,
but so far nothing has happened.

Also, this novel database right got a few major blows by the European
Court of Justice, where it clearly stated that the right does not cover
the creation of the database, merely the effort put into obtaining,
selecting, and cleaning a database. This means, e.g. that the
publication of match dates and fixtures by FIFA can not be protected
under the database right. On the other hand, if an external Website
keeps statistics of all FIFA player, how much their cost, where they
currently are, etc., then their database as a whole could be protected.

But to make it clear: the database right does not apply to single data
items in the database: should I keep a database of all cities in the UK
and their populations, and if someone asks for the population of Oxford
from my database, the database rights do not prevent them from
republishing and using that data item as they like. Eurostat cannot sue
you if you tell someone the population of France.

To summarize on database rights: the EU, and only the EU, have
introduced in 1996 the so called database rights. They are independent
of copyright, and cover a database as a whole in certain circumstances.
If you are in the EU, and want to use the data, database right does not
restrict you. It only restricts you from republishing the database as a
whole or in relevant parts.

Besides the legal foundations of the data licenses, one also has to
consider that copyright law refers dominantly to the right to copy the
data, not to use it: if you want to count how often certain explicit
words are uttered in a movie like Pulp Fiction, you are free to do so.
If you want to count and compare the death count in certain books and
movies (like, Rambo, War and Peace, and the Bible - the results might
surprise you), you are free to do so. You are free to publish the
results, and you are even more free to use them internally in your
organization.

Having said that, I still recommend to add the CC0 license to a dataset
when you publish it. I grudge every time I do it, but it still makes
sense. Not because I believe that it means much: as said, the data in it
is free anyway. But because a lot of other people believe that it means
a lot. They might believe that if they integrate a point of data from a
CC-BY-SA licensed dataset in their own dataset, they have to publish it
under CC-BY-SA as well. They might believe that mixing a CC-BY-SA
dataset with an ODBL dataset and displaying the results is legally
impossible. Maybe they don’t even believe it, but they are required to
ask their lawyers, and their lawyers will prefer to play it safe for
their clients (it is their job\!) and advise them accordingly. And for
all of these people, the CC0 license is an item of assurance. So if you
want your dataset to be usable by them, just add a CC0 license to it.
And grudge about it.

There is a completely independent aspect of why it could make sense to
cite your data sources, which is trust and provenance. Even if a dataset
is not published under a CC-BY-like license, meaning that it requires
attribution, it often makes sense to keep the provenance and attribution
intact - simply because the user of your data might ask for the source
themselves, and might want to check on their credibility. But
attribution for increasing your credibility is something entirely
different than attribution because you think you are legally obliged due
to the used data.

If I were an organization or individual with sufficient financial
backup, I would even offer to pick up your legal battles if a data
publisher ever sues you for using their data (not for republishing it
verbatim, though). I hope that maybe an organization or individual will
step up at some point to do so, but I wouldn’t hold my breath for it.
Both the US Supreme Court and the European Court of Justice have
repeatedly decided in favour of the freedom of data, be it the results
of games, be it telephone numbers, be it horse racing fixtures.

So, as paradoxical as it sounds: Data is free. Free the data\!

There is a battle over minds going on. The one side fights for the
establishment and extension of intellectual property rights. In the last
decades, even years, they have achieved some considerable victories.
Copyright law, as it was introduced in the United States, was meant for
14 years, and had to be explicitly stated. Today it holds not only for
the lifetime of the creator, but also an additional 70 years (to
incentivize the creator to produce more, because an author would be much
less motivated to write if they knew that half a century after their
death their highly beloved publisher wouldn’t make profit out of their
work anymore). Today, copyright applies automatically, without any
registration or statement. There is no need to put the little c in a
circle anywhere. It is there, automatically, everywhere.

The extension from works to content, from expression to ideas, is
another dimension, this time in scope instead of time, in the continuous
struggle to extend and expand intellectual property rights. It is not
just a battle over the laws, but also, and more importantly, over our
believes and minds, to make us more accepting towards the notion that
ideas and knowledge belong to companies and individuals, and are not
part of our commons.

Every time data is published under a restrictive license, “they” have
managed to conquer another strategic piece of territory. Restrictive in
this case includes CC-BY, CC-BY-SA, CC-BY-NC, GFDL, ODBL, and (god
forbid\!) CC-BY-SA-NC-ND, and many other such licenses.

Every time you wonder what license some data has that you want to use,
or whether you need to ask the data publisher if you can use it, “they”
have won another battle.

Every time you integrate two data sources and want to publish the
results, and start to wonder how to fulfill your legal obligation
towards the original dataset publishers, “they” laugh and welcome you as
a member of their fifth column.

Let them win, and some day you will be sued for mentioning a number.

Links: I am not linking to the obvious texts, which are the actual laws.
Read them. They are not as impenetrable as you think. I mean, heck, if
you can make sense of an RDF/XML file, you shouldn’t be scared of some
legal text.

  - [Evaluation of the European Commission on the effect of database
    rights](http://ec.europa.eu/internal_market/copyright/docs/databases/evaluation_report_en.pdf)
  - [US Supreme Court, Baker v. Selden - on the extent of copyright with
    regards to the expression, not the
    content](http://www.justia.us/us/101/99/case.html)

This text was written by me on a Saturday morning, as a completely
personal opinion. It does not represent the official point of view of
any current, former, or future employer, nor of any project I ever was,
am, or will be affiliated with or am thought to be affiliated with.

For a version you can leave comments: [Google Plus
post](https://plus.google.com/104177144420404771615/posts/cvGay9eDSSK)
