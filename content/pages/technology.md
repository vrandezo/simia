---
title: "Simia technology"
language: "en"
slug: "technology"
aliases:
  - "/wiki/Simia_technology"
tags:
  - Simia
  - Nodix
  - technology
  - english
---

In more than a quarter of a century, this Website used a number of technologies.
This page gives a short overview.

## Current setup (since 2026)

The current setup is both very simple and rather complicated.

For the last twenty years, my requirements were that I want to be able to
publish from anywhere.
I shouldn't need to sit in front of my computer, but I should be able to simply
open a Website and write a post there, and get the post published within a
few minutes.
Once Smartphones were around, I also wanted to be able to post from my phone.
Whereas this sounds trivial today, these requirements evolved over the years
for me.

Currently, the blog runs on
[Hugo](https://en.wikipedia.org/wiki/Hugo_(software))
with a slightly modified
[PageMod](https://themes.gohugo.io/themes/hugo-papermod/)
as the them.
Hugo is a software that takes a bunch of
[Markdown](https://en.wikipedia.org/wiki/Markdown)
files with a bit of metadata, and turns the whole thing into a single
directory with static files.
This is awesome because static files are very easy and cheap to serve,
and hopefully that will remain stable in a world where AI bots are
mercilessly hammering all the sites on the Web, even this litte,
unimportant Website.

Now you may ask, where are those Markdown files which are the source of the
static files? Aren't they just on my own computer, so how do I actually write
posts from everywhere?

Well, the whole directory with the content of Simia is version controlled with
[Git](https://en.wikipedia.org/wiki/Git)
and then synced against
[a repo](https://github.com/vrandezo/simia/)
on
[Github](https://en.wikipedia.org/wiki/GitHub).
So you can see the source code there, and even send pull requests directly.

A GitHub action rebuilds the static output directory everyime the repo is being
changed, and then uses
[rsync](https://en.wikipedia.org/wiki/Rsync)
to push that static directory to a
[Google Cloud VM](https://en.wikipedia.org/wiki/Google_Cloud_Platform)
where it is being served to the world.

Finally, with
[PagesCMS](https://pagescms.org/)
I can easily create new and maintain existing posts in my git repository
through the Web.

As said, this is both a very simple method, using a static site generator
from local text sources to create the site, harking back to how this
site was created from about 2002 to 2007, and also a rather complex setup,
involving plenty of Open Source components and two of giant tech companies
(Google for the cloud VM and Microsoft for GitHub), just to host a simple
blog.

This could be simpler, but for now I am happy to see if this works,
and if it will reduce the cost of running the site considerably, as I hope.

## Semantic MediaWiki (2007-2026)

For more on the reasons why I switched from Semantic MediaWiki to the settings
above, see this [post about switching Simia away from Semantic Mediawiki](/posts/switching-simia-way-from-semantic-mediawiki).

From 2007 to 2026, for almost two decades,
[**Simia**](/pages/simia)
was run on
[MediaWiki](https://en.wikipedia.org/wiki/MediaWiki)
with the
[Semantic MediaWiki](https://en.wikipedia.org/wiki/Semantic_MediaWiki)
and *Blog2RSS* extensions enabled.
This allowed for a large number of almost magically feeling features:
  - A timeline view of all posts that have been published on the Nodix blog
  - A timeline view of all comments to the blogs here
  - An alphabetical list of all blog posts
  - RSS feeds of intersections of tags, e.g. only German movie reviews
  - All comments by people with a specific employer

*Blog2RSS* was an extension to MediaWiki, that requires Semantic
MediaWiki. It allows to use Semantic MediaWiki's query mechanism to
create RSS feeds. Blog2RSS was never published.

In good web tradition you were able to view the source of any page (and I don't
mean the HTML source, which your browser allows you to view anyway, I
mean the wiki source of the page): you just could go to the bottom of the
page and click on the *view source* link. That's gone.

I even managed to upload posts directly from
[OpenOffice](https://en.wikipedia.org/wiki/OpenOffice.org),
which didn't really make a difference, but was a fun experiment.

## Blogger (2004-2007)

From 2004 to 2007, the blog (back then named *Nodix*) was run through
[Blogger](https://en.wikipedia.org/wiki/Blogger_(service)).
I had started a new job, and that came with much more traveling than before,
so I really wanted to be able to post from the way.
Blogger allowed for that.

Blogger is a Website, acquired by Google, that allows you to maintain and
create your blog. I just used my own domain to point at Blogger, and ready.

This was also the only time, where comments worked well, because Blogger
supported them.

In this era, I also created a number of blogs with Blogger, such as
*Semantic Nodix*, or a blog for the [nutkidz](https://nutkidz.net),
and an individual blog the *DSA4 Werkzeug*. Most of these have been folded
back in when switching over to Semantic MediaWiki, as SMW was powerful enough
to maintain several different topics in a single space.

## The very beginning (2001-2004)

When I kicked off *Nodix*, what would later become *Simia*, in 2001, it was
not my first Website. I had run two Websites before, one on the servers of a
local Internet club (from about 1994 on or so), and another on
[CompuServe](https://en.wikipedia.org/wiki/CompuServe) (from about 1997).
Of both sites, I cannot find any traces.

Back then I had created the sites manually in HTML.
So when I started *Nodix*, I did the same. But as the page was getting more
and more content, I started to write *NodixGen*, a software in
[Delphi](https://en.wikipedia.org/wiki/Delphi_(software))
with the sole task to create the site from a simple content format.
Today, you would call that a
[static site generator](https://en.wikipedia.org/wiki/Static_site_generator)
and it's almost funny that in 2026 I returned to that approach
(but this time taking an existing Open Source generator).

NodixGen powered the Website from 2001 to 2004.

In 2004, I had started a new job, and that came with much more traveling than
before, so I really wanted to be able to post from the way.
I first started with rewriting NodixGen in
[Python](https://en.wikipedia.org/wiki/Python_(programming_language))
(called *pyNodix*).

pyNodix was a Python script, and the idea was, I can run it anywhere because
almost any computer has Python (well, that wasn't true for many Windows
computers back then). pyNodix would first download the current source version
of the Website from the server, then allow me to make the modifications in a
terrible UI, then generate the static HTML sites locally, and upload the
new source version together with the generated static sites back to the
server hosting the site. It was basically trying to combine a static site
generator with a distributed version control system.

(To my defense, this was before
[git](https://en.wikipedia.org/wiki/Git)
existed.
[Subversion](https://en.wikipedia.org/wiki/Apache_Subversion)
did exist, but running a Subversion server for this task would have been
massive overkill, denying the advantage of running a static website.)

Within less than a month I gave that up and switched to *Blogger*.

At that time I became fascinated by the idea of having your own server on your
phone, as more and more people were starting to use smartphones, and I feel
this idea still reverberates with
[Solid](https://en.wikipedia.org/wiki/Solid_project)
and personal agents, but in both cases with a much larger loss of autonomy,
because all of that runs in the cloud.
It is an idea that is still bouncing in my head.

<!-- ## Mobile wiki

<http://ausweb.scu.edu.au/aw06/papers/refereed/roe/paper.html>

<http://max.limpag.com/2006/11/19/running-a-web-server-wordpress-on-my-phone/>

<http://research.nokia.com/research/projects/mobile-web-server/>
-->
