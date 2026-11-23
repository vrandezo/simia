---
title: "Semantic MediaWiki 0.6: Timeline support, ask pages, et al."
date: 2006-11-18
language: "en"
slug: "semantic-mediawiki-0-6-timeline-support-ask-pages-et-al"
aliases:
  - "/wiki/Semantic_MediaWiki_0.6:_Timeline_support,_ask_pages,_et_al."
tags:
  []
---

It has been quite a while since the last release of [Semantic
MediaWiki](Semantic_MediaWiki "wikilink"), but there was enormous work
going into it. Huge thanks to all contributors, especially
[Markus](Markus_Krötzsch "wikilink"), who has written the bulk of the
new code, reworked much of the existing, and pulled together the
contributions from the other coders, and the [Simile
team](http://simile.mit.edu/) for their great
[Timeline](http://simile.mit.edu/timeline/) code that we reused. (I lost
overview, because the last few weeks have seen some travels and a lot of
work, especially ISWC2006 and the final review of the
[SEKT](SEKT "wikilink") project I am working on. I will blog on SEKT
more as soon as some further steps are done).

So, what's new in the second Beta-release of the Semantic MediaWiki?
Besides about 2.7 tons of code fixes, usability and performance
improvements, we also have a number of neat new features. I will outline
just four of them:

  - **Timeline support**: you know [SIMILE's
    Timeline](http://simile.mit.edu/timeline/) tool? No? You should. It
    is like Google Maps for the fourth dimension. Take a look at the
    [Timeline webpage](http://simile.mit.edu/timeline/) to see some
    examples. Or at [ontoworld](ontoworld "wikilink")'s [list of
    upcoming events](http://ontoworld.org/wiki/Upcoming_events). Yes,
    created dynamically out of the wiki data.
  - **Ask pages**: the simple semantic search was too simple, you think?
    Now we finally have a semantic search we dare not to call simple.
    Based on the existing Ask Inline Queries, and actually making them
    also fully functional, the [ask
    pages](http://ontoworld.org/index.php?title=Special:ask&query=%0A++%5B%5Bend+date%3A%3D%3E%7B%7BCURRENTYEAR%7D%7D-%7B%7BCURRENTMONTH%7D%7D-%7B%7BCURRENTDAY%7D%7D%5D%5D%0A++%5B%5Btitle%3A%3D%2A%7CName%5D%5D%0A++%5B%5Bhas+location+city%3A%3A%2A%7CCity%5D%5D%0A++%5B%5Bhas+location+country%3A%3A%2A%7CCountry%5D%5D%0A++%5B%5BStart+date%3A%3D%2A%5D%5D%0A++%5B%5BEnd+date%3A%3D%2A%5D%5D%0A&sort=end+date&order=ASC)
    allow to dynamically query the wiki knowledge base. No more sandbox
    article editing to get your questions answered. Go for the semantic
    search, and build your ask queries there. And all retrievable via
    GET. Yes, you can link to custom made queries from everywhere\!
  - **Service links**: now all attributes can automatically link to
    further resources via the [service
    links](http://ontoworld.org/wiki/Help:Service_links) displayed in
    the fact box. Sounds abstract? It's not, it's rather a very powerful
    tool to weave the web tighter together: service links specify how to
    connect the attributes data to external services that use that data,
    for example, how to connect geographic coordinates with [Yahoo
    maps](http://maps.yahoo.com/), or ontologies with
    [Swoogle](http://swoogle.umbc.edu/), or movies with
    [IMdb](http://www.imdb.com/), or books with
    [Amazon](http://www.amazon.com/), or ... well, you can configure it
    yourself, so your imagination is the limit.
  - **Full RDF export**: some people don't like pulling the RDF together
    from many different pages. Well, go and get [the whole RDF export
    here](http://ontoworld.org/RDF/). There is now a maintenance script
    included which can be used via a cron job (or manually) to [create
    an RDF
    dump](http://ontoworld.org/wiki/Help:RDF_export#Exporting_all_data)
    of the whole data inside the wiki. This is really useful for smaller
    wikis, and external tools can just take that data and try to use it.
    By the way, if you have an external tool and reuse the data, we
    would be happy if you tell us. We are really looking forward to more
    examples of reuse of data from a Semantic MediaWiki installation\!

I am looking much forward to December, when I can finally join Markus
again with the coding and testing. Thank you so very much for your
support, interest, critical and encouraging remarks with regards to
Semantic MediaWiki. [Grab the
code](http://ontoworld.org/wiki/Help:Installation), update your
installation, or take the chance and switch your wiki to Semantic
MediaWiki.

Just a remark: my preferred way to install both MediaWiki and Semantic
MediaWiki is to pull it directly from the SVN instead of taking the
releases. It's actually less work and helps you tremendously in keeping
up to date.


