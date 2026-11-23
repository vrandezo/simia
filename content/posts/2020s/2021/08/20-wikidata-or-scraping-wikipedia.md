---
title: "Wikidata or scraping Wikipedia"
date: 2021-08-20
language: "en"
slug: "wikidata-or-scraping-wikipedia"
aliases:
  - "/wiki/Wikidata_or_scraping_Wikipedia"
tags:
  - Wikidata
  - Wikipedia
  - Simia
  - english

---

Yesterday I was pointed to a [blog post describing how to answer an
interesting project: how many generations from Alfred the Great to
Elizabeth II](https://billpg.com/data-mining-wikipedia/)? Alfred the
Great was a king in England at the end of the 9th century, and Elizabeth
II is the current Queen of England (and a bit more).

The author of the blog post, Bill P. Godfrey, describes in detail how he
wrote a crawler that started downloading the English Wikipedia article
of Queen Elizabeth II, and then followed the links in the infobox to
download all her ancestors, one after the other. He used a scraper to
get the information from the Wikipedia infoboxes from the HTML page. He
invested quite a bit of work in cleaning the data, particularly doing
entity reconciliation. This was then turned into a graph and the data
analyzed, resulting in a number of paths from Elizabeth II to Alfred,
the shortest being 31 generations.

I honestly love these kinds of projects, and I found Bill’s write-up
interesting and read it with pleasure. It is totally something I would
love to do myself. Congrats to Bill for doing it. Bill provided the
dataset for further analysis on his Website. Thanks for that\!

Everything I say in this post is not meant, in any way, as a criticism
of Bill. As said, I think he did a fun project with interesting results,
and he wrote a good write-up and published his data. All of this is
great. I left a [comment on the blog
post](https://billpg.com/data-mining-wikipedia/#comment-345) sketching
out how Wikidata could be used for similar results.

He submitted his [blog post to Hacker
News](https://news.ycombinator.com/item?id=28234122), where a, to me,
extremely surprising discussion ensued. He was pointed rather naturally
and swiftly to Wikidata and DBpedia. DBpedia is a project that started
and invested heavily in scraping the infoboxes from Wikipedia. Wikidata
is a sibling project of Wikipedia where data can be directly maintained
by contributors and accessed in a number of machine-readable ways. Asked
why he didn’t use Wikidata, he said he didn’t know about it. All fair
and good.

But some of the discussions and comments on Hacker News surprised me
entirely.

Expressing my consternation, I started discussions on
[Twitter](https://twitter.com/vrandezo/status/1428501116401061899) and
on [Facebook](https://www.facebook.com/vrandezo/posts/524817905989). And
there were some very interesting stories about the pain of using
Wikidata, and I very much expect us to learn from them and hopefully
make things easier. The number of API queries one has to make in order
to get data (although, these numbers would be much smaller than with the
scraping approach), the learning curve about SPARQL and RDF (although,
you can ignore both, unless you want to use them explicitly - you can
just use JSON and the Wikidata API), the opaqueness of the identifiers
(wdt:P25 wd:Q9682 instead of “mother” and “Queen Elizabeth II”) were
just a few. The documentation seems hard to find, there seem to be a
lack of libraries and APIs that are easy to use. And yet, comments like
"if you've actually tried getting data from wikidata/wikipedia you very
quickly learn the HTML is much easier to parse than the results wikidata
gives you" surprised me a lot.

Others asked about the data quality of Wikidata, and complained about
the huge amount of bad data, duplicates, and the bad ontology in
Wikidata (as if Wikipedia wouldn’t have these problems. I mean how do
you figure out what a Wikipedia article is about? How do you get a list
of all bridges or events from Wikipedia?)

I am not here to fight. I am here to listen and to learn, in order to
help figuring out what needs to be made better. I did dive into the
question of data quality. Thankfully, Bill provides his dataset on the
Website, and downloading the [query result](https://w.wiki/3vZ8) for the
following query - `select * { wd:Q9682 (wdt:P25|wdt:P22)* ?p . ?p
wdt:P25|wdt:P22 ?q }` - is just one click away. The result of this query
is equivalent to what Bill was trying to achieve - a list of all
ancestors of Elizabeth II. (The [actual query](https://w.wiki/3vrd) is a
little bit more complex, because we also fetch the names of the
ancestors, and their Wikipedia articles, in order to help match the data
to Bill’s data).

I would claim that I invested far less work than Bill in creating my
graph data. No data cleansing, no scraping, no crawling, no entity
reconciliation, no manual checking. How about the quality of the two
datasets?

*Update*: Note, this post is not a tutorial to SPARQL or Wikidata. You
can find an explanation of the query in the [discussion on Hacker News
about this post](https://news.ycombinator.com/item?id=28277749). I
really wanted to see how the quality of the data using the two
approaches compares. Yes, it is an unfamiliar language for many, but I
used to teach SPARQL and the basics of the languages seem not that hard
to learn. Try out this [tutorial](https://wdqs-tutorial.toolforge.org/)
for example. *Update over*

So, let’s look at the datasets. I will refer to the two datasets as the
scrape (that’s Bill’s dataset) and Wikidata (that’s the query result
from Wikidata, as of the morning of August 20 - in particular, none of
the errors in Wikidata mentioned below have been fixed).

In the scrape, we find 2,584 ancestors of Elizabeth II (including
herself). They are connected with 3,528 parenthood relationships.

In Wikidata, we find 20,068 ancestors of Elizabeth II (including
herself). They are connected with 25,414 parenthood relationships.

So the scrape only found a bit less than 13% of the people that Wikidata
knows about, and close to 14% of the relationships. If you ask me,
that’s quite a bad recall - almost seven out of eight ancestors are
missing.

Did the scrape find things that are missing in Wikidata? Yes. 43
ancestors are in the scrape which are missing in Wikidata, and 61
parenthood relationships are in the scrape which are missing from
Wikidata. That’s about 1.8% of the data in the scrape, or 0.24% compared
to the overall parent relationship data of Elizabeth II in Wikidata.

I evaluated the [complete list of those relationships from the scrape
missing from
Wikidata](https://docs.google.com/spreadsheets/d/18RT5c645cvfyzVfFakD_1U90bx46OJGivGvfTf7HyfY/edit#gid=0).
They fall into five categories:

  - Category 1: Errors that come from the scraper. 40 of the 61
    relationships are errors introduced by the scrapers. We have cities
    or countries being parents - which isn’t too terrible, as Bill says
    in the blog post because they won’t have parents themselves and
    won’t participate in the original question of findinging the
    lineage from Alfred to Elizabeth, so no problem. More problematic is
    when grandparents or great-grandparents are identified as the
    parent, because this directly messes up the counting of generations:
    [Ügyek](https://en.wikipedia.org/wiki/%C3%9Cgyek) is thought to be a
    son, not a grandson of [Prince
    Csaba](https://en.wikipedia.org/wiki/Prince_Csaba), [Anna
    Dalassene](https://en.wikipedia.org/wiki/Anna_Dalassene) is skipping
    two generations to [Theophylact
    Dalassenos](https://en.wikipedia.org/wiki/Theophylact_Dalassenos),
    etc. This means we have an error rate of at least 1.1% in the
    scraper dataset, besides having the low recall rate mentioned above.
  - Category 2: Wikipedia has an error. Those are rare, it happened
    twice. [Adelaide of
    Metz](https://en.wikipedia.org/w/index.php?title=Adelaide_of_Metz&oldid=1018764546)
    had the wrong father and [Sophie of
    Mecklenburg](https://en.wikipedia.org/w/index.php?title=Sophie_of_Mecklenburg_\(1481%E2%80%931503\)&oldid=1024458664)
    linked to the wrong mother in the infobox (although the text was
    linking to the right one). The first one has been
    [fixed](https://en.wikipedia.org/w/index.php?title=Adelaide_of_Metz&diff=1038232032&oldid=1018764546)
    since Bill ran his scraper (unlucky timing\!), and I
    [fixed](https://en.wikipedia.org/w/index.php?title=Sophie_of_Mecklenburg_\(1481%E2%80%931503\)&diff=next&oldid=1024458664)
    the second one. Note I am linking to the historic version of the
    article with the error.
  - Category 3: Wikidata was missing data. [Jeanne de Fougères, Countess
    of La Marche and of
    Angoulême](https://www.wikidata.org/wiki/Q6172243) and [Albert Azzo
    II, Margrave of Milan](https://www.wikidata.org/wiki/Q706730) were
    missing one or both of their parents, and Bill’s scraping found
    them. So of the more than 3,500 scraped relationships, only 2 were
    missing\! I added both.
  - In addition, correct data was marked deprecated once. I
    [fixed](https://www.wikidata.org/w/index.php?title=Q380373&diff=1484662887&oldid=1476641523)
    that, too.
  - Category 4: Wikidata has duplicates, and that breaks the chain. That
    happened five times, I think the following pairs are duplicates:
    Q28739301/Q106688884, Q105274433/Q40115489, Q56285134/Q354855,
    Q61578108/Q546165 and Q15730031/Q59578032. Duplicates were mentioned
    explicitly in one of the comments as a problem, and here we can see
    that they happen with quite a bit of frequency, particularly for
    non-central items. I merged all of these.
  - Category 5: the situation is complicated, and different Wikipedia
    versions disagree, because the sources seem to disagree. [Sometimes
    Wikidata models that disagreement quite
    well](https://www.wikidata.org/wiki/Q7796194#P22) - but often not.
    After all, we are talking about people who sometimes lived more than
    a millennium ago. Here are these cases: [Albert II, Margrave of
    Brandenburg](https://en.wikipedia.org/wiki/Albert_II,_Margrave_of_Brandenburg)
    to [Ada of Holland](https://en.wikipedia.org/wiki/Ada_of_Holland);
    [Prince Álmos](https://en.wikipedia.org/wiki/Prince_%C3%81lmos) to
    [Sophia](https://en.wikipedia.org/wiki/Sophia_\(wife_of_G%C3%A9za_I_of_Hungary\))
    to [Emmo of Loon](https://en.wikipedia.org/wiki/Emmo_of_Loon)
    (complicated by a duplicate as well); [Oldřich, Duke of
    Bohemia](https://en.wikipedia.org/wiki/Old%C5%99ich,_Duke_of_Bohemia)
    to [Adiva](https://en.wikipedia.org/wiki/Adiva); [William
    III](https://en.wikipedia.org/wiki/William_III,_Count_of_Toulouse)
    to [Raymond
    III](https://en.wikipedia.org/wiki/Raymond_III,_Count_of_Toulouse),
    both Counts of Toulouse;
    [Thored](https://en.wikipedia.org/wiki/Thored) to [Oslac of
    York](https://en.wikipedia.org/wiki/Oslac_of_York); [Bermudo II of
    León](https://en.wikipedia.org/wiki/Bermudo_II_of_Le%C3%B3n) to
    [Ordoño III of
    León](https://en.wikipedia.org/wiki/Ordo%C3%B1o_III_of_Le%C3%B3n)
    (Galician says IV); and [Robert
    Fitzhamon](https://en.wikipedia.org/wiki/Robert_Fitzhamon) to [Hamo
    Dapifer](https://en.wikipedia.org/wiki/Hamo_Dapifer). In total,
    eight cases. I didn't edit those as these require quite a bit of
    thought.

Note that there was not a single case of “Wikidata got it wrong”, which
surprised me a lot - I totally expected errors to happen. Unless you
count the cases in Category 5. I mean, even English Wikipedia had
errors\! This was a pleasant surprise. Also, the genuine complicated
cases are roughly as frequent as missing data, duplicates, and errors
together. To be honest, that sounds like a pretty good result to me.

Also, the scraped data? Recall might be low, but the precision is pretty
good: more than 98% of it is corroborated by Wikidata. Not all scraping
jobs have such a high correctness.

In general, these results are comparable to a [comparison of Wikidata
with DBpedia and Freebase I did two years
ago](https://colab.research.google.com/github/vrandezo/colabs/blob/master/Comparing_coverage_and_accuracy_of_DBpedia%2C_Freebase%2C_and_Wikidata_for_the_parent_predicate.ipynb).

Oh, and what about Bill’s original question?

Turns out that Wikidata knows of a path between Alfred and Elizabeth II
that is even shorter than the shortest 31 generations Bill found, as it
takes only 30 generations.

This is Bill’s path:

  - Alfred the Great
  - Ælfthryth, Countess of Flanders
  - Arnulf I, Count of Flanders
  - Baldwin III, Count of Flanders
  - Arnulf II, Count of Flanders
  - Baldwin IV, Count of Flanders
  - Judith of Flanders
  - Henry IX, Duke of Bavaria
  - Henry X, Duke of Bavaria
  - Henry the Lion
  - Henry V, Count Palatine of the Rhine
  - Agnes of the Palatinate
  - Louis II, Duke of Bavaria
  - Louis IV, Holy Roman Emperor
  - Albert I, Duke of Bavaria
  - Joanna Sophia of Bavaria
  - Albert II o \_Germany
  - Elizabeth of Austria
  - Barbara Jagiellon
  - Christine of Saxony
  - Christine of Hesse
  - Sophia of Holstein-Gottorp
  - Adolphus Frederick I, Duke of Mecklenburg-Schwerin
  - Adolphus Frederick II, Duke of Mecklenburg-Strelitz
  - Duke Charles Louis Frederick of Mecklenburg
  - Charlotte of Mecklenburg-Strelitz
  - Prince Adolphus, Duke of Cambridge
  - Princess Mary Adelaide of Cambridge
  - Mary of Teck
  - George VI
  - Elizabeth II

And this is the path that I found using the Wikidata data:

  - Alfred the Great
  - Edward the Elder *(surprisingly, it deviates right at the
    beginning)*
  - Eadgifu of Wessex
  - Louis IV of France
  - Matilda of France
  - Gerberga of Burgundy
  - Matilda of Swabia *(this is a weak link in the chain, though, as
    there might possibly be two Matildas having been merged together.
    Ask your resident historian)*
  - Adalbert II, Count of Ballenstedt
  - Otto, Count of Ballenstedt
  - Albert the Bear
  - Bernhard, Count of Anhalt
  - Albert I, Duke of Saxony
  - Albert II, Duke of Saxony
  - Rudolf I, Duke of Saxe-Wittenberg
  - Wenceslaus I, Duke of Saxe-Wittenberg
  - Rudolf III, Duke of Saxe-Wittenberg
  - Barbara of Saxe-Wittenberg (Barbara has no article in the English
    Wikipedia, but in German, Bulgarian, and Italian. Since the scraper
    only looks at English, they would have never found this path)
  - Dorothea of Brandenburg
  - Frederick I of Denmark
  - Adolf, Duke of Holstein-Gottorp *(husband to Christine of Hesse in
    Bill’s path)*
  - Sophia of Holstein-Gottorp *(and here the two lineages merge again)*
  - Adolphus Frederick I, Duke of Mecklenburg-Schwerin
  - Adolphus Frederick II, Duke of Mecklenburg-Strelitz
  - Duke Charles Louis Frederick of Mecklenburg
  - Charlotte of Mecklenburg-Strelitz
  - Prince Adolphus, Duke of Cambridge
  - Princess Mary Adelaide of Cambridge
  - Mary of Teck
  - George VI
  - Elizabeth II

I hope that this is an interesting result for Bill coming out of this
exercise.

I am super thankful to Bill for doing this work and describing it. It
led to very interesting discussions and triggered insights into some
shortcomings of Wikidata. I hope the above write-up is also helpful,
particularly in providing some data regarding the quality of Wikidata,
and I hope that it will lead to work in making Wikidata more and easier
accessible to explorers like Bill.

Update: there has been a discussion of this post on [Hacker
News](https://news.ycombinator.com/item?id=28277749).
