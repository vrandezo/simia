---
title: "Ten years of Wikidata"
date: 2022-10-29
language: "en"
slug: "ten-years-of-wikidata"
aliases:
  - "/wiki/Ten_years_of_Wikidata"
tags:
  - Wikidata
  - jubilee
  - history
  - Simia
  - english

---

Today it's ten years since [Wikidata](https://wikidata.org) had
launched. A few memories.

It's been an amazing time. In the summer of 2011, people still didn't
believe Wikidata would happen. In the fall of 2012, it was there.

[Markus Krötzsch](https://www.korrekt.org/page/Markus_Kr%C3%B6tzsch) and
I were pushing for the idea of a [Semantic
Wikipedia](https://meta.wikimedia.org/wiki/Wikimania05/Paper-MK2) since
2005. [Semantic
MediaWiki](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki)
was born from that idea,
[Freebase](https://en.wikipedia.org/wiki/Freebase_\(database\)) and
[DBpedia](https://www.dbpedia.org/) launched in 2007, [microformats in
Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Microformats)
became a grassroots thing, but no one was working on the real thing at
the [Wikimedia Foundation](https://wikimediafoundation.org/).

With [Elena Simperl](https://www.kcl.ac.uk/people/elena-simperl) at
[KIT](https://www.kit.edu/) we started the EU research project
[RENDER](http://render-project.eu/) in 2010, involving [Mathias
Schindler](http://www.mathias-schindler.de/) at [Wikimedia
Deutschland](https://www.wikimedia.de/). It was about knowledge
diversity on the Web, still an incredibly important topic. In RENDER, we
developed ideas for the flexible representation of knowledge, and how to
deal with contradicting and incomplete information. We analysed
Wikipedia to understand the necessity of these ideas.

In 2010, I was finishing my PhD at KIT, and got an invitation by
[Yolanda Gil](https://www.isi.edu/~gil/) to work at the
[ISI](https://www.isi.edu/) at University of Southern California for a
half year sabbatical. There, Yolanda, Varun Ratnakar, Markus and I
developed a prototype for Wikidata which received the third place in the
ISWC Semantic Web Challenge that year.

In 2011, the Wikimedia Data summit happened, invited by [Tim
O'Reilly](https://www.oreilly.com/tim/) and organised by [Danese
Cooper](https://www.facesofopensource.com/danese-cooper/), to the
headquarters of O'Reilly in Sebastopol, CA. There were folks from the
Wikimedia Foundation, Freebase, DBpedia, Semantic MediaWiki, O'Reilly,
there was Guha, Mark Greaves, I think, and others. I think that's where
it became clear that Wikidata would be feasible.

It's also where I first met [Guha](http://www.guha.com/cv.html) and
where I admitted to him that I was kinda a fan boy. He invented MFC,
RDF, had worked with [Douglas Lenat](https://cyc.com/leadership-team/)
on CYC, and later that year introduced
[Schema.org](https://schema.org/). He's now working on [Data
Commons](https://blog.google/outreach-initiatives/sustainability/data-commons-sustainability/).
Check it out, it's awesome.

[Mark Greaves](https://aim.pnnl.gov/staff/dr-mark-greaves), a former
DARPA program officer, who then was working for Paul Allen at Vulcan,
had been supporting Semantic MediaWiki for several years, and he really
wanted to make Wikidata happen. He knew my PhD was done, and that I was
thinking about my next step. I thought it would be academia, but he
suggested I should write up a project proposal for Wikidata.

After six years advocating for it, I understood that someone would need
to step up to make it happen. With the support and confidence of so many
people - Markus Krötzsch, Elena Simperl, Mark Greaves, Guha, Jamie
Taylor, Rudi Studer, John Giannandrea, and others - I drafted the
proposal.

The Board of the Wikimedia Foundation approved the proposal as a new
Wikimedia project, but neither allocated the funding, nor directed the
Foundation to do it. In fact, the Foundation was reluctant to take it
on, unsure whether they would be able to host such a project development
at that time. Back then, that was a wise decision.

[Erik Möller](https://social.coop/@eloquence), then CTO of the
Foundation, was the driving force behind a major change: instead of
turning the individual Wikipedias semantic, we would have a single
Wikidata for all languages. Erik was also the one who had secured the
domain for Wikidata. Many years prior.

Over the next half year and with the help of the Wikimedia Foundation,
we secured funding from AI2 (Paul Allen), Google (who had acquired
Freebase in the meantime), and the Gordon and Betty Moore Foundation,
1.3 million.

Other funders backed out because I insisted on the Wikidata ontology to
be entirely under the control of the community. They argued to have
professional ontologists, or reuse ontologies, or to use DBpedia to seed
Wikidata. I said no. I firmly believed, and still believe, that the
ontology has to be owned, created and maintained by the community. I
invited the ontologists to join the project as community members, but to
the best of my knowledge, they never made significant contributions. We
did miss out on quite a bit of funding, though.

There we were. We had the funding and the project proposal, but no one
to host us. We were even thinking of founding a new organisation, or
hosting it at KIT, but due to the RENDER collaboration, Mathias
Schindler had us talk with Pavel Richter, ED of Wikimedia Deutschland,
and Pavel offered to host the development of Wikidata.

For Pavel and Wikimedia Deutschland this was a big step: the development
team would significantly increase WMDE (I think, almost double it in
size, if I remember correctly), which would necessitate a sudden
transformation and increased professionalisation of WMDE. But Pavel was
ready for it, and managed this growth admirably.

On April 1st 2012, we started the development of Wikidata. On October 29
2012 we launched the site.

The original launch was utterly useless. All you could do was creating
new pages with Q IDs (the Q being a homage to Kamara, my wife),
associated those Q IDs with labels in many languages, and connect to
articles in Wikipedia, so called sitelinks. You could not add any
statements yet. You could not connect items with each other. The
sitelinks were not used anywhere. The labels were not used anywhere. As
I said, the site was completely useless. And great fun, at least to me.

QIDs for entities are still being often disparaged. Why QIDs? Why not
just the English name? Isn't `dbp:Tokyo` much easier to understand than
`Q1490`? It was an uphill battle ten years ago to overcome the
anglocentricity of many people. Unfortunately, this has not changed
much. I am thankful to the Wikimedia movement to be one of the places
that encourages, values, and supports the multilingual approach of
Wikidata.

Over the next few months, the first few Wikipedias were able to access
the sitelinks from Wikidata, and started deleting the sitelinks from
their Wikipedias. This lead to a removal of more than 240 million lines
of wikitext across the Wikipedias. 240 million lines that didn't need to
be maintained anymore. In some languages, these lines constituted more
than half of the content of the Wikipedia. In many languages, editing
activity dropped dramatically at first, sometimes by 80%.

But then something happened. Those edits were mostly bots. And with
those bots gone, humans were suddenly better able to see each other and
build a more meaningful community. In many languages, this eventually
lead to an increased community activity.

One of my biggest miscalculations when launching Wikidata was to
entirely dismiss the possibility of a SPARQL endpoint. I thought that
none of the existing open source triple stores would be performant
enough. Peter Haase was instrumental in showing that I was wrong. Today,
the SPARQL endpoint is an absolutely crucial piece of the Wikidata
infrastructure, and is widely used to explore the dataset. And with its
beautiful visualisations, I find it almost criminally underused.
Unfortunately, the SPARQL endpoint is also the piece of infrastructure
that worries us the most. The Wikimedia Foundation is working hard on
figuring out the future for this service, and if you can offer
substantial help, please reach out.

Today, Wikidata has more than 1.4 billion statements about approximately
100 million topics. It is by far the most edited Wikimedia project, with
more edits than the English, German, and French Wikipedia together -
even though they are each a decade older than Wikidata.

Wikidata is widely used. Almost every time Wikipedia serves one of its
24 billion monthly page views. Or during the pandemic in order to
centralise the data about COVID cases in India to make them available
across the languages of India. By large companies answering questions
and fulfilling tasks with their intelligent assistants, be it Google or
Apple or Microsoft. By academia, where you will find thousands of
research papers using Wikidata. By numerous Open Source projects, by
one-off analyses by data scientists, by small enterprises using the
dataset, by student programmers exploring and playing with it on the
weekend, by spreadsheet enthusiasts enriching their data, by scientists,
librarians and curators linking their datasets to Wikidata, and thus to
each other. Already, more than 7,000 catalogs are linked to Wikidata,
and thus to each other, really and substantially establishing a Web of
linked data.

I will always remember the Amazon developer who approached me after a
talk. He had used Wikidata to gather data about movies. I was surprised:
Amazon owns imdb, why would they ever use anything else for movies? He
said that imdb was great for what it had, but Wikidata complemented it
in unexpected ways, offering many interesting connections between the
movies and other topics which would be out of scope for imdb.

Not to be misunderstood: knowledge bases such as imdb are amazing, and
Wikidata does not aim to replace them. They often have a clear scope,
have a higher quality, and almost always a better coverage in their
field than Wikidata ever can hope to have, or aims to have. And that's
OK. Wikidata's goal is not to replace these knowledge bases. But to
provide the connecting tissue between the many knowledge bases out
there. To connect them. To provide a common set of entities to work
with. To turn the individual knowledge bases into a large interconnected
Web of knowledge.

I am still surprised that Wikidata is not known more widely among
developers. It always makes me smile with joy when I see yet another
developer who just discovered Wikidata and writes an excited post about
it and how much it helped them. In the last two weeks, I stumbled upon
two projects who used Wikidata identifiers where I didn't expect them at
all, just used them as if it was the most normal thing in the world.
This is something I hope we will see even more in the future. I hope
that Wikidata will become the common knowledge base that is ubiquitously
used by a large swarm of intelligent applications. Not only to make
these applications be smarter, by knowing more about the world - but
also by allowing these applications to exchange data with each other
more effectively because they are using the same language.

And most importantly: Wikidata has a healthy, large, and comparatively
friendly and diverse community. It is one of the most active Wikimedia
projects, only trailing the English Wikipedia, and usually similarly
active as Commons.

Last time I checked, more than 400,000 people have contributed to
Wikidata. For me, that is easily the most surprising number about the
project. If you had asked me in 2012 how many people would contribute to
Wikidata, I would have sheepishly hoped for a few hundred, maybe a few
thousand. And I would have defensively explained why that's OK. I am
humbled and awestruck by the fact that several hundred thousand people
have contributed to an open knowledge base that is available to
everyone, and that everyone can contribute to.

And that I think is the most important role that Wikidata plays. That it
is a place that everyone can contribute to. That the knowledge base that
everyone uses is not owned and gateguarded by any one company or
government, but that it is a common good, that everyone can contribute
to. That everyone with an internet connection can lend their voice to
the sum of all knowledge.

We all own Wikidata. We are responsible for Wikidata. And we all benefit
from Wikidata.

It has been an amazing ten years. I am looking forward to many more
years of Wikidata, and to the many new roles that it will play in the
years to come, and to the many people who will contribute to it.

Shoutout to the brilliant team that started the work on Wikidata: Lydia
Pintscher, Abraham Taherivand, Daniel Kinzler, Jeroen De Dauw, Katie
Filbert, Tobias Gritschacher, Jens Ohlig, John Blad, Daniel Werner,
Henning Snater, and Silke Meyer.

And thank you for all these amazing pictures of cakes for Wikidata's
birthday. (And if you're curious what is coming next: we are working on
Wikifunctions and Abstract Wikipedia, in order to allow more people to
contribute more knowledge to even more people\!)
