---
title: "Semantic Mediawiki 0.4 - Knowledge Inside!"
date: 2006-05-15
language: "en"
slug: "semantic-mediawiki-0-4-knowledge-inside"
aliases:
  - "/wiki/Semantic_Mediawiki_0.4_-_Knowledge_Inside!"
tags:
  []
---

Until now, [Semantic MediaWiki](Semantic_MediaWiki "wikilink") was kind
of a nerds project. Yes, you could get a lot of information out in RDF,
and actually, I used it as an RDF editor more than once -- but heck,
what normal person needs that?

Now, with the freshly implemented feature, the advantages of a Semantic
MediaWiki over a normal MediaWiki should become obvious: you can simply
ask the wiki for stuff\! Wiki, what are the 10 biggest city in the US?
Put a list here. Or, wiki, what is the height of the current German
chancellor? Put the info here. I have made a writeup on those [inline
queries](http://wiki.ontoworld.org/index.php/Help:Inline_queries) on our
demo wiki. Go there, read it.

But a lot of other things made it into the 0.4 release. Here's Markus'
list:

  - Improved output for Special:Relations and Special:Attributes: usage
    of
  - relations and attributes is now counted
  - Improved ontology import feature, allowing to import ontologies and
    to update existing pages with new ontological information
  - Experimental suport for date/time datatype
  - More datypes with units: mass and time duration
  - Support for EXP-notation with numbers, as e.g. 2.345e13. Improved
    number formating in infobox.
  - Configurable infobox: infobox can be hidden if empty, or switched
    off completely. This also works around a bug with MediaWiki
    galeries.
  - Prototype version of Special:Types, showing all available datatypes
    with their names in the current language setting.
  - "\[\[:located in::Paris\]\]" will now be rendered as "located in
    \[\[Paris\]\]"
  - More efficient storage: changed database layout, indexes for fast
    search
  - Code cleaned up, new style guidelines
  - Bugfixes, a lot of Bugixes

Thanks to everyone who contributed and still contributes to the
project\! And, connected to this, thanks to the answers to my last blog
entry -- I will write more on this tomorrow.


