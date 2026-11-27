---
title: "EMWCon 2019, Day 1"
date: 2019-04-04
language: "en"
slug: "emwcon-2019-day-1"
aliases:
  - "/wiki/EMWCon_2019,_Day_1"
tags:
  - trip report
  - presentation
  - Semantic MediaWiki
  - Simia
  - english
---

Today was the first day of the Enterprise MediaWiki Conference, EMWCon,
in Daly City. Among the attendees were people from NASA (6 or more
people), UIC (International Union of Railways), the UK Ministry of
Defence, the US radioactivity safety agencies, cancer research
institutes, the Bureaus of Labour Statistics, PG\&E, General Electric,
and a number of companies providing services around MediaWiki, such as
WikiTeq, Wikiworks, dokit, etc., with or without semantic extensions.
The conference was located at the Headquarter of Genesys.

I'm not going to comment on all talks, and also I will not faithfully
report on the talks - you can just go to YouTube to watch the talks
themselves. The following is a personal, biased view of the first day.

NASA made an interesting comment early on: the discussion was about
MediaWiki and its lack of fine-grained access control. You can set up a
MediaWiki easily for a controlled group (so that not everyone in the
world can access it), but it is not so easy to say "oh, this set of
pages is available for people in this group, and managers in that org
can access the pages with this markers", etc. So NASA, at first, set up
a lot of wiki installations, each one for such specific groups - but
eventually turned it all around and instead had a small number of
well-defined groups and merged the wikis into them, tearing down
barriers within the org and making knowledge wider available.

Evita Hollis from General Electric had an interesting point in her
presentation on how GE does knowledge sharing: they use SharePoint and
Yammer to connect people to people, and MediaWiki to connect people to
Knowledge. MediaWiki has been not-exactly-great at allowing people to
work together in real-time - it is a different flow, where you capture
and massage knowledge slowly into it. There is a reason why Ops at
Wikimedia do not use a wiki during an incident that much, but rather
IRC. I think there is a lot of insight in her argument - and if we take
that serious, we could actually really lift MediaWiki to a new level,
and take Wikipedia there too.

Another interesting point is that SharePoint at General Electric had
three developers, and MediaWiki had one. The question from the audience
was, whether that reflect how difficult it is to work with SharePoint,
or whether that reflected some bias of the company towards SharePoint.
Hollis was adamant about how much she likes Sharepoint, but the reason
for the imbalance was that MediaWiki, particularly Semantic MediaWiki,
allows actually much more flexibility and power than SharePoint without
having to touch a single line of wiki source code. It is a platform that
allows for rapid experimentation by the end user (I am adding the
Spiderman adage about great power coming with great responsibility).

Daren Welsh from NASA talked about many different forms of biases and
how they can bubble up on your wiki. Very interesting was one effect: if
knowledge from the wiki is becoming too readily availble, people may
start to become dependent on it. They had tests where they took away the
wiki randomly from flight controllers in training, in order to ensure
they are resourceful enough to still figure out what to do - and some
failed miserably.

Ike Hecht had a brilliant presentation on the kind of quick application
development Semantic MediaWiki lends itself to. He presented a task
manager, a news feed, and a file management system, calling them
"Semantic Structures That Do Stuff" - which is basically a few pages for
your wiki, instead of creating extensions for all of these. This also
resonated with GE's statement about needling less developers. I think
that this is wildly underutilized and there is a lot of value in this
idea.

Thanks to Yaron Koren - who also gave an intro to the topic - and Cindy
Cicalese for organizing the conference, and Genesys for hosting us. All
presentations are available on
[YouTube](https://www.youtube.com/channel/UCZavo6makpqtRhlFxJkn6HA).

  - [EMWCon website](https://www.mediawiki.org/wiki/EMWCon_Spring_2019)
