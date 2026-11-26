---
title: "Need help with SQL"
date: 2006-05-11
language: "en"
slug: "need-help-with-sql"
aliases:
  - "/wiki/Need_help_with_SQL"
tags:
  []
---

But I have no time to write it down... I will sketch my problem, and
hopefully get an answer (I've started this blog in the morning, and now
I need to close it, cause I have to leave).

Imagine I have following table (a triple store):

<table border="1">

<tr>

<th>

Subject

</th>

<th>

Predicate

</th>

<th>

Object

</th>

</tr>

<tr>

<td>

Adam

</td>

<td>

yahoo im

</td>

<td>

adam@net

</td>

</tr>

<tr>

<td>

Adam

</td>

<td>

skye

</td>

<td>

adam

</td>

</tr>

<tr>

<td>

Berta

</td>

<td>

skype

</td>

<td>

berta

</td>

</tr>

</table>

How do I make a query that returns me the following table:

<table border="1">

<tr>

<th>

Subject

</th>

<th>

o1

</th>

<th>

o2

</th>

</tr>

<tr>

<td>

Adam

</td>

<td>

adam@net

</td>

<td>

adam

</td>

</tr>

<tr>

<td>

Berta

</td>

<td>

\-

</td>

<td>

berta

</td>

</tr>

</table>

The problems are the default value in the middle lower cell. The rest
works (as maybe seen in the Semantic Mediawiki code, file
includes/SMW\_InlineQueries.php -- note that the CVS is not up to date
for now, because SourceForge's CVS is down for days\!)

It should work in general, with as many columns as I like on the answer
table (based on the predicates in the first one).

Oh, and if you solved this -- or have an idea -- it would be nice if it
worked with MySQL 4.0, i.e. without Subqueries.

Any ideas?


