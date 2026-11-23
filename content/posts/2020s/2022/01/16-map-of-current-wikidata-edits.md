---
title: "Map of current Wikidata edits"
date: 2022-01-16
language: "en"
slug: "map-of-current-wikidata-edits"
aliases:
  - "/wiki/Map_of_current_Wikidata_edits"
tags:
  - Simia
  - english
  - Wikidata
  - programming

---

It starts entirely black and then listens to Wikidata edits. Every time
an item with a coordinate is edited, a blue dot in the corresponding
place is made. So slowly, over time, you get a more and more complete
map of Wikidata items.

  - <https://vrandezo.github.io/wikidata-edit-map/>

If you open the developer console, you can get links and names of the
items being displayed.

The whole page is less than a hundred lines of JavaScript and HTML, and
it runs entirely in the browser. It uses the [Wikimedia Stream
API](https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams)
and the [Wikidata
API](https://www.wikidata.org/wiki/Special:ApiSandbox), and has no code
dependencies. Might be fun to take a look if you're so inclined.

<https://github.com/vrandezo/wikidata-edit-map/blob/main/index.html>
