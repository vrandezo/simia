---
title: "How much information is in a language?"
date: 2019-04-16
language: "en"
slug: "how-much-information-is-in-a-language"
aliases:
  - "/wiki/How_much_information_is_in_a_language?"
tags:
  []
---

About the paper "Humans store about 1.5 megabytes of information during
language acquisition“, by Francis Mollica and Steven T. Piantadosi.

This is one of those papers that I both love - I find the idea is really
worthy of investigation, having an answer to this question would be
useful, and the paper is very readable - and can't stand, because the
assumptions in the papers are so unconvincing.

The claim is that a natural language can be encoded in \~1.5MB - a
little bit more than a floppy disk. And the largest part of this is the
lexical semantics (in fact, without the lexical semantics, the rest is
less than 62kb, far less than a short novel or book).

They introduce two methods about estimating how many bytes we need to
encode the lexical semantics:

Method 1: let's assume 40,000 words in a language (languages have more
words, but the assumptions in the paper is about how many words one
learns before turning 18, and for that 40,000 is probably an Ok
estimation although likely on the lower end). If there are 40,000 words,
there must be 40,000 meanings in our heads, and lexical semantics is the
mapping of words to meanings, and there are only so many possible
mappings, and choosing one of those mappings requires 553,809 bits.
That's their lower estimate.

Wow. I don't even know where to begin in commenting on this. The
assumption that all the meanings of words just float in our head until
they are anchored by actual word forms is so naiv, it's almost cute.
Yes, that is likely true for some words. Mother, Father, in the naive
sense of a child. Red. Blue. Water. Hot. Sweet. But for a large number
of word meanings I think it is safe to assume that without a language
those word meanings wouldn't exist. We need language to construct these
meanings in the first place, and then to fill them with life. You can't
simply attach a word form to that meaning, as the meaning doesn't exist
yet, breaking down the assumptions of this first method.

Method 2: let's assume all possible meanings occupy a vector space. Now
the question becomes: how big is that vector space, how do we address a
single point in that vector space? And then the number of addresses
multiplied with how many bits you need for a single address results in
how many bits you need to understand the semantics of a whole language.
There lower bound is that there are 300 dimensions, the upper bound is
500 dimensions. Their lower bound is that you either have a dimension or
not, i.e. that only a single bit per dimension is needed, their upper
bound is that you need 2 bits per dimension, so you can grade each
dimension a little. I have read quite a few papers with this approach to
lexical semantics. For example it defines "girl" as +female, -adult,
"boy" as -female,-adult, "bachelor" as +adult,-married, etc.

So they get to 40,000 words x 300 dimensions x 1 bit = 12,000,000 bits,
or 1.5MB, as the lower bound of Method 2 (which they then take as the
best estimate because it is between the estimate of Method 1 and the
upper bound of Method 2), or 40,0000 words x 500 dimensions x 2 bits =
40,000,000 bits, or 8MB.

Again, wow. Never mind that there is no place to store the dimensions -
what are they, what do they mean? - probably the assumption is that they
are, like the meanings in Method 1, stored prelinguistically in our
brains and just need to be linked in as dimensions. But also the idea
that all meanings expressible in language can fit in this simple vector
space. I find that theory surprising.

Again, this reads like a rant, but really, I thoroughly enjoyed this
paper, even if I entirely disagree with it. I hope it will inspire other
papers with alternative approaches towards estimating these numbers, and
I'm very much looking forward to reading them.

  - [Humans store about 1.5MB of information during language
    acquisition](https://royalsocietypublishing.org/doi/10.1098/rsos.181393),
    Royal Society Open Science


