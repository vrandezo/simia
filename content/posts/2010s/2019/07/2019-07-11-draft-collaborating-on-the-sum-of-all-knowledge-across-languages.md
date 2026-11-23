---
title: "Draft: Collaborating on the sum of all knowledge across languages"
date: 2019-07-10
language: "en"
slug: "draft-collaborating-on-the-sum-of-all-knowledge-across-languages"
aliases:
  - "/wiki/Draft:_Collaborating_on_the_sum_of_all_knowledge_across_languages"
tags:
  []
---

For the upcoming [Wikipedia@20
book](https://meta.wikimedia.org/wiki/Wikipedia@20), I published my
chapter draft. [Comments are welcome on the pubpub Website until
July 19](https://wikipedia20.pubpub.org/pub/vyf7ksah).

Every language edition of Wikipedia is written independently of every
other language edition. A contributor may consult an existing article in
another language edition when writing a new article, or they might even
use the Content Translation tool to help with translating one article to
another language, but there is nothing that ensures that articles in
different language editions are aligned or kept consistent with each
other. This is often regarded as a contribution to knowledge diversity,
since it allows every language edition to grow independently of all
other language editions. So would creating a system that aligns the
contents more closely with each other sacrifice that diversity?

## Differences between Wikipedia language editions

Wikipedia is often described as a wonder of the modern age. There are
more than 50 million articles in almost 300 languages. The goal of
allowing everyone to share in the sum of all knowledge is achieved,
right?

Not yet.

The knowledge in Wikipedia is unevenly distributed. Let’s take a look at
where the first twenty years of editing Wikipedia have taken us.

The number of articles varies between the different language editions of
Wikipedia: English, the largest edition, has more than 5.8 million
articles, Cebuano — a language spoken in the Philippines — has 5.3
million articles, Swedish has 3.7 million articles, and German has 2.3
million articles. (Cebuano and Swedish have a large number of machine
generated articles.) In fact, the top nine languages alone hold more
than half of all articles across the Wikipedia language editions — and
if you take the bottom half of all Wikipedias ranked by size, they
together wouldn’t have 10% of the number of articles in the English
Wikipedia.

It is not just the sheer number of articles that differ between
editions, but their comprehensiveness does as well: the English
Wikipedia article on Frankfurt has a length of 184,686 characters, a
table of contents spanning 87 sections and subsections, 95 images,
tables and graphs, and 92 references — whereas the Hausa Wikipedia
article states that it is a city in the German state of Hesse, and lists
its population and mayor. Hausa is a language spoken natively by 40
million people and as a second language by another 20 million.

It is not always the case that the large Wikipedia language editions
have more content on a topic. Although readers often consider large
Wikipedias to be more comprehensive, local Wikipedias may frequently
have more content on topics of local interest: the English Wikipedia
knows about the Port of Călărași that it is one of the largest Romanian
river ports, located at the Danube near the town of Călărași — and
that’s it. The Romanian Wikipedia on the other hand offers several
paragraphs of content about the port.

The topics covered by the different Wikipedias also overlap less than
one would initially assume. English Wikipedias has 5.8 million articles,
German has 2.2 million articles — but only 1.1 million topics are
covered by both Wikipedias. A full 1.1 million topics have an article in
German — but not in English. The top ten Wikipedias by activity — each
of them with more than a million articles — have articles on only
hundred thousand topics in common. 18 million topics are covered by
articles in the different language Wikipedias — and English only covers
31% of these.

Besides coverage, there is also the question of how up to date the
different language editions are: in June 2018, San Francisco elected
London Breed as its new mayor. Nine months later, in March 2019, I
conducted an analysis of who the mayor of San Francisco was, according
to the different language versions of Wikipedia. Of the 292 language
editions, a full 165 had a Wikipedia article on San Francisco. Of these,
86 named the mayor. The good news is that not a single Wikipedia lists a
wrong mayor — but the vast majority are out of date. English switched
the minute London Breed was sworn in. But 62 Wikipedia language editions
list an out-of-date mayor — and not just the previous mayor Ed Lee, who
became mayor in 2011, but also often Gavin Newsom (2004-2011), and his
predecessor, Willie Brown (1996-2004). The most out-of-date entry is to
be found in the Cebuano Wikipedia, who names Dianne Feinstein as the
mayor of San Francisco. She had that role after the assassination of
Harvey Milk and George Moscone in 1978, and remained in that position
for a decade in 1988 — Cebuano was more than thirty years out of date.
Only 24 language editions had listed the current mayor, London Breed,
out of the 86 who listed the name at all.

An even more important metric for the success of a Wikipedia are the
number of contributors: English has more than 31,000 active contributors
— three out of seven active Wikimedians are active on the English
Wikipedia. German, the second most active Wikipedia community, already
only has 5,500 active contributors. Only eleven language editions have
more than a thousand active contributors — and more than half of all
Wikipedias have fewer than ten active contributors. To assume that fewer
than ten active contributors can write and maintain a comprehensive
encyclopedia in their spare time is optimistic at best. These numbers
basically doom the mission of the Wikimedia movement to realize a world
where everyone can contribute to the sum of all knowledge.

## Enter Wikidata

Wikidata was launched in 2012 and offers a free, collaborative,
multilingual, secondary database, collecting structured data to provide
support for Wikipedia, Wikimedia Commons, the other wikis of the
Wikimedia movement, and to anyone in the world. Wikidata contains
structured information in the form of simple claims, such as “San
Francisco — Mayor — London Breed”, qualifiers, such as “since — July 11,
2018”, and references for these claims, e.g. a link to the official
election results as published by the city.

One of these structured claims would be on the Wikidata page about San
Francisco and state the mayor, as discussed earlier. The individual
Wikipedias can then query Wikidata for the current mayor. Of the 24
Wikipedias that named the current mayor, eight were current because they
were querying Wikidata. I hope to see that number go up. Using Wikidata
more extensively can, in the long run, allow for more comprehensive,
current, and accessible content while decreasing the maintenance load
for contributors.

Wikidata was developed in the spirit of the Wikipedia’s increasing drive
to add structure to Wikipedia’s articles. Examples of this include the
introduction of infoboxes as early as 2002, a quick tabular overview of
facts about the topic of the article, and categories in 2004. Over the
year, the structured features became increasingly intricate: infoboxes
moved to templates, templates started using more sophisticated MediaWiki
functions, and then later demanded the development of even more powerful
MediaWiki features. In order to maintain the structured data, bots were
created, software agents that could read content from Wikipedia or other
sources and then perform automatic updates to other parts of Wikipedia.
Before the introduction of Wikidata, bots keeping the language links
between the different Wikipedias in sync, easily contributed 50% and
more of all edits.

Wikidata allowed for an outlet to many of these activities, and relieved
the Wikipedias of having to run bots to keep language links in sync or
of massive infobox maintenance tasks. But one lesson I learned from
these activities is that I can trust the communities with mastering
complex workflows spread out between community members with different
capabilities: in fact, a small number of contributors working on
intricate template code and developing bots can provide invaluable
support to contributors who more focus on maintaining articles and
contributors who write large swaths of prose. The community is very
heterogeneous, and the different capabilities and backgrounds complement
each other in order to create Wikipedia.

However, Wikidata’s structured claims are of a limited expressivity:
their subject always must be the topic of the page, every object of a
statement must exist as its own item and thus page in Wikidata. If it
doesn’t fit in the rigid data model of Wikidata, it simply cannot be
captured in Wikidata — and if it cannot be captured in Wikidata, it
cannot be made accessible to the Wikipedias.

For example, let’s take a look at the following two sentences from the
English Wikipedia article on Ontario, California:

“To impress visitors and potential settlers with the abundance of water
in Ontario, a fountain was placed at the Southern Pacific railway
station. It was turned on when passenger trains were approaching and
frugally turned off again after their departure.”

There is no feasible way to express the content of these two sentences
in Wikidata - the simple claim and qualifier structure that Wikidata
supports can not capture the subtle situation that is described here.

## An Abstract Wikipedia

I suggest that the Wikimedia movement develop an Abstract Wikipedia, a
Wikipedia in which the actual textual content is being represented in a
language-independent manner. This is an ambitious goal — it requires us
to push the current limits of knowledge representation, natural language
generation, and collaborative knowledge construction by a significant
amount: an Abstract Wikipedia must allow for:

1.  relations that connect more than just two participants with
    heterogeneous roles.
2.  composition of items on the fly from values and other items.
3.  expressing knowledge about arbitrary subjects, not just the topic of
    the page.
4.  ordering content, to be able to represent a narrative structure.
5.  expressing redundant information.

Let us explore one of these requirements, the last one: unlike the
sentences of a declarative formal knowledge base, human language is
usually highly redundant. Formal knowledge bases usually try to avoid
redundancy, for good reasons. But in a natural language text, redundancy
happens frequently. One example is the following sentence:

“Marie Curie is the only person who received two Nobel Prizes in two
different sciences.”

The sentence is redundant given a list of Nobel Prize award winners and
their respective disciplines they have been awarded to — a list that
basically every large Wikipedia will contain. But the content of the
given sentence nevertheless appears in many of the different language
articles on Marie Curie, and usually right in the first paragraph. So
there is obviously something very interesting in this sentence, even
though the knowledge expressed in this sentence is already fully
contained in most of the Wikipedias it appears in. This form of
redundancy is common place in natural language — but is usually avoided
in formal knowledge bases.

The technical details of the Abstract Wikipedia proposal are presented
in (Vrandečić, 2018). But the technical architecture is only half of the
story. Much more important is the question whether the communities can
meet the challenges of this project?

Wikipedia and Wikidata have shown that the communities are capable to
meet difficult challenges: be it templates in Wikipedia, or constraints
in Wikidata, the communities have shown that they can drive
comprehensive policy and workflow changes as well as the necessary
technological feature development. Not everyone needs to understand the
whole stack in order to make a feature such as templates a crucial part
of Wikipedia.

The Abstract Wikipedia is an ambitious future project. I believe that
this is the only way for the Wikimedia movement to achieve its goal,
short of developing an AI that will make the writing of a comprehensive
encyclopedia obsolete anyway.

## A plea for knowledge diversity?

When presenting the idea of the Abstract Wikipedia, the first question
is usually: will this not massively reduce the knowledge diversity of
Wikipedia? By unifying the content between the different language
editions, does this not force a single point of view on all languages?
Is the Abstract Wikipedia taking away the ability of minority language
speakers to maintain their own encyclopedias, to have a space where, for
example, indigenous speakers can foster and grow their own point of
view, without being forced to unify under the western US-dominated
perspective?

I am sympathetic with the intent of this question. The goal of this
question is to ensure that a rich diversity in knowledge is retained,
and to make sure that minority groups have spaces in which they can
express themselves and keep their knowledge alive. These are, in my
opinion, valuable goals.

The assumption that an Abstract Wikipedia, from which any of the
individual language Wikipedias can draw content from, will necessarily
reduce this diversity, is false. In fact, I believe that access to more
knowledge and to more perspectives is crucial to achieve an effective
knowledge diversity, and that the currently perceived knowledge
diversity in different language projects is ineffective at best, and
harmful at worst. In the rest of this essay I will argue why this is the
case.

## Language does not align with culture

First, it is wrong to use language as the dimension along which to draw
the demarcation line between different content if the Wikimedia movement
truly believes that different groups should be able to grow and maintain
their own encyclopedias.

In case the Wikimedia movement truly believes that different groups or
cultures should have their own Wikipedias, why is there only a single
Wikipedia language edition for the English speakers from India, England,
Scotland, Australia, the United States, and South Africa? Why is there
only one Wikipedia for Brazil and Portugal, leading to much strife? Why
are there no two Wikipedias for US Democrats and Republicans?

The conclusion is that the Wikimedia movement does not believe that
language is the right dimension to split knowledge — it is a historical
decision, driven by convenience. The core Wikipedia policies, vision,
and mission are all geared towards enabling access to the sum of all
knowledge to every single reader, no matter what their language, and not
toward capturing all knowledge and then subdividing it for consumption
based on the languages the reader is comfortable in.

The split along languages leads to the problem that it is much easier
for a small language community to go “off the rails” — to either, as a
whole, become heavily biased, or to adopt rules and processes which are
problematic. The fact that the larger communities have different rules,
processes, and outcomes can be beneficial for Wikipedia as a whole,
since they can experiment with different rules and approaches. But this
does not seem to hold true when the communities drop under a certain
size and activity level, when there are not enough eyeballs to avoid the
development of bad outcomes and traditions. For one example, the article
about skirts in the Bavarian Wikipedia features three upskirt pictures,
one porn actress, an anime screenshot, and a video showing a drawing of
a woman with a skirt getting continuously shorter. The article became
like this within a day or two of its creation, and, even though it has
been edited by a dozen different accounts, has remained like this over
the last seven years. (This describes the state of the article in April
2019 — I hope that with the publication of this essay, the article will
finally be cleaned up).

## A look on some south Slavic language Wikipedias

Second, a natural experiment is going on, where contributors that are
more separated by politics than language differences have separate
Wikipedias: there exist individual Wikipedia language editions for
Croatian, Serbian, Bosnian, and Serbocroatian. Linguistically, the
differences between the dialects of Croatian are often larger than the
differences between standard Croatian and standard Serbian. Particularly
the existence of the Serbocroatian Wikipedia poses interesting questions
about these delineations.

Particularly the Croatian Wikipedia has turned to a point of view that
has been described as problematic. Certain events and Croat actors
during the 1990s independence wars or the 1940s fascist puppet state
might be represented more favorably than in most other Wikipedias.

Here are two observations based on my work on south Slavic language
Wikipedias:

First, claiming that a more fascist-friendly point of view within a
Wikipedia increases the knowledge diversity across all Wikipedias might
be technically true, but is practically insufficient. Being able to
benefit from this diversity requires the reader to not only be
comfortable reading several different languages, but also to engage
deeply enough and spend the time and interest to actually read the
article in different languages, which is mostly a profoundly boring
exercise, since a lot of the content will be overlapping. Finding the
juicy differences is anything but easy, especially considering that most
readers are reading Wikipedia from mobile devices, and are just looking
to satisfy a quick information need from a source whose curation they
trust.

Most readers will only read a single language version of an article, and
thus any diversity that exists across different language editions is
practically lost. The sheer existence of this diversity might even be
counterproductive, as one may argue that the communities should not
spend resources on reflecting the true diversity of a topic within each
individual language. This would cement the practical uselessness of the
knowledge diversity across languages.

Second, many of the same contributors that write the articles with a
certain point of view in the Croatian Wikipedia, also contribute on the
English Wikipedia on the articles about the same topics — but there they
suddenly are forced and able to compromise and incorporate a much wider
variety of points of view. One might hope the contributors would take
the more diverse points of view and migrate them back to their home
Wikipedias — but that is often not the case. If contributors harbor a
certain point of view (and who doesn’t?) it often leads to a situation
where they push that point of view as much as they can get away with in
each of the projects.

It has to be noted that the most blatant digressions from a neutral
point of view in Wikipedias like the Croatian Wikipedia will not be
found in the most central articles, but in the large periphery of
articles surrounding these central articles which are much harder to
keep an eye on.

## Abstract Wikipedia and Knowledge diversity

The Abstract Wikipedia proposal does not require any of the individual
language editions to use it. Each language community can decide for each
article whether to fall back on the Abstract Wikipedia or whether to
create their own article in their language. And even that decision can
be more fine grained: a contributor can decide for an individual article
to incorporate sections or paragraphs from the Abstract Wikipedia.

This allows the individual Wikipedia communities the luxury to entirely
concentrate on the differences that are relevant to them. I distinctly
remember that when I started the Croatian Wikipedia: it felt like I had
the burden to first write an article about every country in the world
before I could write the articles I cared about, such as my mother’s
home village — because how could anyone defend a general purpose
encyclopedia that might not even have an article on Nigeria, a country
with a population of a hundred million, but one on Donji Humac, a
village with a population of 157? Wouldn’t you first need an article on
all of the chemical elements that make up the world before you can write
about a local food?

The Abstract Wikipedia frees a language edition from this burden, and
allows each community to entirely focus on the parts they care about
most — and to simply import the articles from the common source for the
topics that are less in their focus. It allows the community to make
these decisions. As the communities grow and shift, they can revisit
these decisions at any time and adapt them.

At the same time, the Abstract Wikipedia makes these differences more
visible since they become explicit. Right now there is no easy way to
say whether the fact that Dianne Feinstein is listed as the Mayor of San
Francisco in the Cebuano Wikipedia is due to cultural particularities of
the Cebuano language communities or not. Are the different population
numbers of Frankfurt in the different language editions intentional
expressions of knowledge diversity? With an Abstract Wikipedia, the
individual communities could explicitly choose which articles to create
and maintain on their own, and at the same time remove a lot of
unintentional differences.

By making these decisions more explicit, it becomes possible to imagine
an effective workflow that observes these intentional differences, and
sets up a path to integrate them into the common article in the Abstract
Wikipedia. Right now, there are 166 different language versions of the
article on the chemical element Helium — it is basically impossible for
a single person to go through all of them and find the content that is
intentionally different between them. With an Abstract Wikipedia, which
contains the common shared knowledge, contributors, researchers, and
readers can actually take a look at those articles that intentionally
have content that replaces or adds to the commonly shared one, assess
these differences, and see if contributors should integrate the
differences in the shared article.

The differences in content may be reflecting difference in policies,
particularly in policies of notability and reliability. Whereas on first
glance it might seem that the Abstract Wikipedia might require unified
notability and reliability requirements across all Wikipedias, this is
not the case: due to the fact that local Wikipedias can overlay and
suppress content from the Abstract Wikipedias, they can adjust their
Wikipedias based on their own rules. And the increased visibility of
such decisions will lead to easier identify biases, and hopefully also
to updated rules to reduce said bias.

## A new incentive infrastructure

The Abstract Wikipedia will evolve the incentive infrastructure of
Wikipedia.

Presently, many underrepresented languages are spoken in areas that are
multilingual. Often another language spoken in this area is regarded as
a high-prestige language, and is thus the language of education and
literature, whereas the underrepresented language is a low-prestige
language. So even though the low-prestige language might have more
speakers, the most likely recruits for the Wikipedia communities, people
with education who can afford internet access and have enough free time,
will be able to contribute in both languages.

In which language should I contribute? If I write the article about my
mother’s home town in Croatian, I make it accessible to a few million
people. If I write the article about my mother’s home town in English,
it becomes accessible to more than a hundred times as many people\! The
work might be the same, but the perceived benefit is orders of magnitude
higher: the question becomes, do I teach the world about a local
tradition, or do I tell my own people about their tradition? The world
is bigger, and thus more likely to react, creating a positive feedback
loop.

This cannibalizes the communities for local languages by diverting them
to the English Wikipedia, which is perceived as the global knowledge
community (or to other high-prestige languages, such as Russian or
French). This is also reflected in a lot of articles in the press and in
academic works about Wikipedia, where the English Wikipedia is being
understood as the Wikipedia. Whereas it is known that Wikipedia exists
in many other languages, journalists and researchers are, often
unintentionally, regarding the English Wikipedia as the One True
Wikipedia.

Another strong impediment to recruiting contributors to smaller
Wikipedia communities is rarely explicitly called out: it is pretty
clear that, given the current architecture, these Wikipedias are doomed
in achieving their mission. As discussed above, more than half of all
Wikipedia language editions have fewer than ten active contributors —
and writing a comprehensive, up-to-date Wikipedia is not an achievable
goal with so few people writing in their free time. The translation
tools offered by the Wikimedia Foundation can considerably help within
certain circumstances — but for most of the Wikipedia languages,
automatic translation models don’t exist and thus cannot help the
languages which would need it the most.

With the Abstract Wikipedia though, the goal of providing a
comprehensive and current encyclopedia in almost any language becomes
much more tangible: instead of taking on the task of creating and
maintaining the entire content, only the grammatical and lexical
knowledge of a given language needs to be created. This is a far smaller
task. Furthermore, this grammatical and lexical knowledge is comparably
static — it does not change as much as the encyclopedic content of
Wikipedia, thus turning a task that is huge and ongoing into one where
the content will grow and be maintained without the need of too much
maintenance by the individual language communities.

Yes, the Abstract Wikipedia will require more and different capabilities
from a community that has yet to be found, and the challenges will be
both novel and big. But the communities of the many Wikimedia projects
have repeatedly shown that they can meet complex challenges with
ingenious combinations of processes and technological advancements.
Wikipedia and Wikidata have both demonstrated the ability to draw on
technologically rather simple canvasses, and create extraordinary rich
and complex masterpieces, which stand the test of time. The Abstract
Wikipedia aims to challenge the communities once again, and the promise
this time is nothing else but to finally be able to reap the ultimate
goal: to allow every one, no matter what their native language is, to
share in the sum of all knowledge.

## Acknowledgements

Thanks to the valuable suggestions on improving the article to Jamie
Taylor, Daniel Russell, Joseph Reagle, Stephen LaPorte, and Jake
Orlowitz.

## Bibliography

  - Bao, Patti, Brent J. Hecht, Samuel Carton, Mahmood Quaderi, Michael
    S. Horn and Darren Gergle. “Omnipedia: bridging the wikipedia
    language gap.” in Proceedings of the Conference on Human Factors in
    Computing Systems (CHI 2012), edited by Joseph A. Konstan, Ed H.
    Chi, and Kristina Höök. Austin: Association for Computing Machinery,
    2012: 1075-1084.
  - Eco, Umberto. The Search for the Perfect Language (the Making of
    Europe). La ricerca della lingua perfetta nella cultura europea.
    Translated by James Fentress. Oxford: Blackwell, 1995 (1993).
  - Graham, Mark. “The Problem With Wikidata.” The Atlantic, April 6,
    2012.
    <https://www.theatlantic.com/technology/archive/2012/04/the-problem-with-wikidata/255564/>
  - Hoffmann, Thomas and Graeme Trousdale, “Construction Grammar:
    Introduction”. In The Oxford Handbook of Construction Grammar,
    edited by Thomas Hoffmann and Graeme Trousdale, 1-14. Oxford: Oxford
    University Press, 2013.
  - Kaffee, Lucie-Aimée, Hady ElSahar, Pavlos Vougiouklis, Christophe
    Gravier, Frédérique Laforest, Jonathon S. Hare and Elena Simperl.
    “Mind the (Language) Gap: Generation of Multilingual Wikipedia
    Summaries from Wikidata for Article Placeholders.” in Proceedings of
    the 15th European Semantic Web Conference (ESWC 2018), edited by
    Aldo Gangemi, Roberto Navigli, Marie-Esther Vidal, Pascal Hitzler,
    Raphaël Troncy, Laura Hollink, Anna Tordai, and Mehwish Alam.
    Heraklion: Springer, 2018: 319-334.
  - Kaffee, Lucie-Aimée, Hady ElSahar, Pavlos Vougiouklis, Christophe
    Gravier, Frédérique Laforest, Jonathon S. Hare and Elena Simperl.
    “Learning to Generate Wikipedia Summaries for Underserved
    Languages from Wikidata.” in Proceedings of the 2018 Conference of
    the North American Chapter of the Association for Computational
    Linguistics: Human Language Technologies, Volume 2, edited by
    Marilyn Walker, Heng Ji, and Amanda Stent. New Orleans: ACL
    Anthology, 2018: 640-645.
  - Schindler, Mathias and Denny Vrandečić. “Introducing new features to
    Wikipedia: Case studies for Web Science.” IEEE Intelligent Systems
    26, no. 1 (January-February 2011): 56-61.
  - Vrandečić, Denny. “Restricting the World.” Wikimedia Deutschland
    Blog. February 22, 2013.
    <https://blog.wikimedia.de/2013/02/22/restricting-the-world/>
  - Vrandečić, Denny and Markus Krötzsch. “Wikidata: A Free
    Collaborative Knowledgebase.” Communications of the ACM 57, no. 10
    (October 2014): 78-85. DOI 10.1145/2629489.
  - Kaljurand, Kaarel and Tobias Kuhn. “A Multilingual Semantic Wiki
    Based on Attempto Controlled English and Grammatical Framework.” in
    Proceedings of the 10th European Semantic Web Conference (ESWC
    2013), edited by Philipp Cimiano, Oscar Corcho, Valentina Presutti,
    Laura Hollink, and Sebastian Rudolph. Montpellier: Springer, 2013:
    427-441.
  - Milekić, Sven. “Croatian-language Wikipedia: when the extreme right
    rewrites history.” Osservatorio Balcani e Caucaso, September 27,
    2018.
    <https://www.balcanicaucaso.org/eng/Areas/Croatia/Croatian-language-Wikipedia-when-the-extreme-right-rewrites-history-190081>
  - Ranta, Aarne. Grammatical Framework: Programming with Multilingual
    Grammars. Stanford: CSLI Publications, 2011.
  - Vrandečić, Denny. “Towards a multilingual Wikipedia,” in Proceedings
    of the 31st International Workshop on Description Logics (DL 2018),
    edited by Magdalena Ortiz and Thomas Schneider. Phoenix: Ceur-WS,
    2018.
  - Wierzbicka, Anna. Semantics: Primes and Universals. Oxford: Oxford
    University Press, 1996.
  - Wikidata Community: “Lexicographical data.” Accessed June 1, 2019.
    <https://www.wikidata.org/wiki/Wikidata:Lexicographical_data>
  - Wulczyn, Ellery, Robert West, Leila Zia and Jure Leskovec. “Growing
    Wikipedia Across Languages via Recommendation.” in Proceedings of
    the 25th International World-Wide Web Conference (WWW 2016), edited
    by Jaqueline Bourdeau, Jim Hendler, Roger Nkambou, Ian Horrocks, and
    Ben Y. Zhao. Montréal: IW3C2, 2016: 975-985.


