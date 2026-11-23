---
title: "What's in a name - Part 6"
date: 2005-01-11
language: "en"
slug: "what-s-in-a-name-part-6"
aliases:
  - "/wiki/What's_in_a_name_-_Part_6"
tags:
  []
---

In this series we learned how to make URIs for entities. I know there's
a big discussion flaring up every few weeks or so, if we should use
fragment identifier or not. For me, this question is pretty much
settled. Using a fragment identifier has the advantage of giving you the
ability of providing a human readable page for those few lost souls who
look up the URI, so maybe it's a tad nicer than using no fragment
identifier and returning 404s. Not using fragids has the advantage of
probably reducing bandwidth - but this discussion should be more or less
academic, because looking up URIs, as we have seen, should not happen.

There is some talking about different representations, negotiating
media-types, returning RDF in one, XHTML in the other case, but to be
honest, I think that's far too complicated. And you would need to use
another web server and extensions to HTTP to make this real, which
doesn't really help the advent of the Semantic Web. Look at [Nokias
URIQA](http://sw.nokia.com/uriqa/URIQA.html) project for more
information.

Keep this rules in mind, and everything should be fine:

  - be careful to use unused URIs if you reference a new entity. Take
    one from an URI space you have control of, so that URI collision
    won't appear
  - don't put a website under the URI you used to to name an entity.
    That would lead to URI collision
  - try to make nice looking URIs, but don't try to hard. They are
    supposed to be hidden by the application anyway
  - provide *rdfs:label* and *rdfs:seeAlso* instead. This solves
    everything you would want to try to solve with URI naming, but in a
    standard compliant way
  - give your resources URIs. Please. So that other can reference them
    more easily.

I should emphasise the last one more. Especially using RDF/XML-Syntax
easily leads to anonymous nodes, which are a pain in the ass because
they are hard or impossible to address. Especially, don't use
rdf:nodeID. They don't give your node an ID that's visible to the outer
world. This is just a local name. Don't use it, please.

The second is using them like this:

    <foaf:person about="me">
      <foaf:knows>
        <foaf:Person>
          <foaf:name>J. Random User</foaf:name>
        </foaf:Person>
      </foaf:knows>
    </foaf:Person>

Actually, the Person known to *"me"* is an anonymous one. You can't
refer to her. Again, try to avoid that. If you can, look up the URI the
person gave to herself in her own FOAF-file. Or give her a name in your
own URI-space. Don't be afraid, you won't run out of it.

Another very interesting approach is to use published subjects. I will
return to this in another blog, promised, but so long: never forget,
there is *owl:sameAs* to make two URIs point to the same thing, so don't
mind too much if you doublename something.

Well, that's it. I hope you enjoyed the series, and that you learned a
bit from it. Looking forward to your comments, and your questions.

**Comments**

*Ash Maurya (11 February 2005 04:02)*

A great series of posts. I've always used URIs for all my resources but was begning to question my judgement after seeing widespread use of rdf:nodeID in foaf.

One of the potential applications for foaf, in my opinion, is aggregation and linking across multiple models. I've been scratching my head on how they plan on avoiding nodeID collisions?

Also, have you looked at the Joseki project? What are your thoughts on the RDFWeb API (especially data objects) described there?

*Denny (11 February 2005 16:06)*

Thanks.

I think HP is doing a great job with Joseki - I mean, I didn't try it myself yet, but the idea behind is the right one. Providing an RDF-WebServer will become essential for the Semantic Web. For me it's much cleaner than the URIQA/MGET-Idea, but according to the mass of discussion ond RDF-IG and now SWIG, I guess, this isn't yet decied... :)
