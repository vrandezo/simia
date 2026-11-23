---
title: "What's in a name - Part 2"
date: 2004-12-29
language: "en"
slug: "what-s-in-a-name-part-2"
aliases:
  - "/wiki/What's_in_a_name_-_Part_2"
tags:
  []
---

How to give a resource a name, an URI? Let's look at this statement:

    movie:Terminator dc:creator "James Cameron".

Happy with that? This is a valid RDF statement, and you understand what
I wanted to say, and your RDF machine will be able to read and process
it, too, so everything is fine.

Well, almost. *movie:Terminator* is a QName, and *movie:* is just a
shorthand prefix, a namespace, that actually has to be defined as
something. But as what? [URIs are
well-defined](http://ftp.ics.uci.edu/pub/ietf/uri/rfc2396.txt), so we
shouldn't just define the namespace arbitrarily. The problem is, someone
else could do the same, and suddenly, one URI could denote two different
resources - this is called URI collision, and it is the next worst thing
to immanentizing the Eschaton. That's why you should grab some URI space
for yourself and there you go, you may define as many URIs there as you
like (remember, the U in URI means Universal, that's why they make such
a fuss about the URI space and ownership of it).

I am the webmaster of *<http://semantic.nodix.net>*, and the URI belongs
to me and with it, all the URIs starting with it. Thus I decide, that
movie: shall be *<http://semantic.nodix.net/movie/>*. Our example
statement thus is the same as:

    http://semantic.nodix.net/movie/Terminator http://purl.org/dc/elements/1.1/creator "James Cameron".

So this is actually what the computer sees. The short hand notation
above is just for humans. But if you're like me, and you see the above
Subject, you're already annoyed that it is not a link, that you can't
click on it. So you copy it into your browser address bar, and go to
*<http://semantic.nodix.net/movie/Terminator>*. Ups. A 404, the website
is not found. You start thinking, oh man, stupid\! Why you giving the
resource such a name that looks so much like an web address, and then
point it to 404-Nirvana?

Many think so. That's because they don't grasp the difference between
URIs and URLs, and to be honest, this difference is maybe the worst idea
the W3C ever had (that's a hard-to-achieve compliment, considering the
introduction of XML/RDF-serialisation and XSD). We will return to this
difference, but for now, let's see what usually happens.

Because *<http://semantic.nodix.net/movie/Terminator>* leads to nowhere,
and I'm far too lazy to make a website for the Terminator just for this
example, we will take another URI for the movie. Jumping to
[IMdb](http://www.imdb.com) we quickly find the appropriate one, and
then we can reformulate our statement:

    http://www.imdb.com/title/tt0088247/ http://purl.org/dc/elements/1.1/creator "James Cameron".

Great\! Our subject is a valid URI, clicking on
<http://www.imdb.com/title/tt0088247/> (or pasting it to a browser) will
tell you more about the subject, and we have a valid RDF statement.
Everything is fine again...

...until next time, where we will discuss the minor problems of our
solution.
