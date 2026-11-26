---
title: "What's in a name - Part 3"
date: 2005-01-05
language: "en"
slug: "what-s-in-a-name-part-3"
aliases:
  - "/wiki/What's_in_a_name_-_Part_3"
tags:
  []
---

Last time we merrily published our first statement for the Semantic Web:

    http://www.imdb.com/title/tt0088247/ http://purl.org/dc/elements/1.1/creator "James Cameron".

A fellow Semantic Web author didn't like the number-encoded IMdb-URI,
but found a much more compelling one and then published the following
statement:

    http://en.wikipedia.org/wiki/The_Terminator http://purl.org/dc/elements/1.1/date "1984-10-26".

A third one sees those and, in order to foster integration of data
offers helpfully the following statement:

    http://www.imdb.com/title/tt0088247/ owl:sameAs http://en.wikipedia.org/wiki/The_Terminator.

And now they live merrily ever after. Or do you hear the thunder of doom
rolling?

The problem is that the URIs above actually already denote something,
namely the IMdb website about the Terminator and the Wikipedia-article
on the Terminator. They did not denote the movie itself, but that's how
they're used in our examples. Statement \#3 above actually says the two
websites are the same. The first one says, that *"James Cameron"*
created the IMdb website on the Terminator (they'd wish), and the second
one says that the Wikipedia article was created in 1984, which is wrong
(July 23, 2001 would be the correct date). We have a classic case of URI
collision.

This happens all the time. People working professionally on this do this
too:

    _person foaf:interest http://dmoz.org/Computers/Security/.

I'd bet, *\_person* (remaining anonymously here) does not have such a
heavy interest in the website *<http://dmoz.org/Computers/Security/>*,
but rather in the Topic the website is about.

    _person foaf:interest _security.
    http://dmoz.org/Computers/Security/ dc:subject _security.

Instead of letting *\_security* be anonymous, we'd rather give it a real
URI. This way we can reference it later.

    _person foaf:interest http://semantic.nodix.net/topic/security.
    http://dmoz.org/Computers/Security/ dc:subject http://semantic.nodix.net/topics/security.

But, oh pain - now we're exactly at the same spot we've been in the last
part. We have an URI that does not dereference to a website (by the way,
I do know that the definition of *foaf:interest* actually says the
semantics of *foaf:interest* is, that the Subject is interested in the
Topic of the Object, and not the Object itself, but that's not my point
here)  
Thinking for a moment about it, we must conclude that it is actually
impossible to achieve both goals: either the URIs will identify a
resource retrievable over the web and are thus unsuitable as URIs for
entities outside the web (like persons, chairs and such) because of URI
collision, or they don't - and will then lead to 404-land.

Isn't there any solution? (Drums) Stay tuned for the next exciting
installment of this series, introducing not one, not two, not three, but
four solutions to this problem\!

**Comments**

*Richard Cyganiak (7 January 2005 15:58)*

You have a good point here, but your examples fail to make it clear.

As you say yourself, foaf:interest is defined to point to a web page about the interest, not to the interest iteself. This means the problem you're trying to show doesn't exist in the case of foaf:interest, and it makes your last two examples bogus. You should have used foaf:topic_interest instead.

The problem, though, is real for many cases.


*Denny (10 January 2005 16:25)*

Hi Richard,

you are totally right - the example fails. But I took it on purpose, nevertheless: because humans, when they read the predicate "foaf:interest" will think that it means that Subject is interested in the Object.

You are right - and I point it out in the Blog - it actually means the Subject is interested in the Topic of the Object. But I think this is an (intentional) bug in the FOAF-specification. Intentional in order to make writing FOAF-files easier, a bug nevertheless because it creates a cognitive difference between the expected naive and intented specified use of "foaf:interest".

I wanted to stress this cognitive difference with this example. The second reason for selecting this example is to make the reader wary of such subtle differences and mistakes that can happen everywhere. Anything claimed about the Semantic Web should be taken with care, no matter who claims it!

Thanks for your comments, denny

*Richard Cyganiak (15 January 2005 17:41)*

I agree, foaf:topic is a poorly defined term. foaf:topic should be named foaf:pageAboutTopic or so. And foaf:topic_interest should be foaf:topic. But that's not what your post talks about, and I'm not sure that mixing this issue into your post is helping to get your point across.

Just a thought.

*Pascal Grouselle (14 April 2005 13:29)*

*(Text lost)*
