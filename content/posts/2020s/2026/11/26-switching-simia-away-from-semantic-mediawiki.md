---
title: Switching Simia away from Semantic MediaWiki
date: 2026-11-27
slug: switching-simia-away-from-semantic-mediawiki
language: en
tags:
  - Simia
  - english
  - internals
  - technology
  - AI
  - Web
---
For almost 20 years, from about 2007 to 2026, this blog was running on
[Semantic MediaWiki](https://en.wikipedia.org/wiki/Semantic_MediaWiki).
Given that I am one of the people who came up with Semantic MediaWiki,
this was both a natural choice, and a very painful one to give up.
But for the last few years, the site was going down again and again,
and it became increasingly expensive to run. Where, before the AI bots
started, I could run the site for $3 to $5 a month, in the end it was often
hitting more than $25 monthly, and yet the page was regularly down.
I increased the CPU capacity of the VM, added much more aggressive caching,
introduced HTTPS, and all that helped -- but every time I had freed up
capacity, for example enabling MediaWiki's file cache (which should
effectively turn MediaWiki into a fancy static site generator), CPU
utilization first went down to 30-40%, just to crawl back to 100% within a
few months.

[![CPU utilization 2024-2026](/images/cpu-load-2426.png)](/images/cpu-load-2426.png)

So, this week I pulled the plug, and migrated all the content from being
stored in Semantic MediaWiki to just a static Website using Hugo.
You can read more about how this works on the [technology page](/pages/technology).
So far, the results look promising.

[![CPU utilization end of November](/images/cpu-to-static-2026.png)](/images/cpu-to-static-2026.png)

I hope this isn't understood as a challenge to the AI bots to try their worst.
I am getting quite tired of how difficult it is getting to just run a Website.

I also wrote up how [this site used to work](/pages/technology).
Maybe some folks will find it interesting, as I struggled with issues that
are very nicely solved today with tools like
[Hugo](https://en.wikipedia.org/wiki/Hugo_(software))
and even
[Git](https://en.wikipedia.org/wiki/Git).

To make it very clear, this is not meant as a critique of MediaWiki or
Semantic MediaWiki. I am super happy about the capabilities I had with SMW,
and I very sorry to loose all these magical features. *sigh*
