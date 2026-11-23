---
title: "Experiment to understand LLMs better"
date: 2024-06-12
language: "en"
slug: "experiment-to-understand-llms-better"
aliases:
  - "/wiki/Experiment_to_understand_LLMs_better"
tags:
  - Simia
  - english
  - AI

---

Here’s an experiment I would love to do if I had the resources. Just to
start gaining some more understanding of how LLMs work.

1.  Train an LLM Z on a lot of English text.
2.  Ensure that the LLM in its response uses correctly the past tense of
    “go”, “went”, in its responses.
3.  Ask the LLM directly what the past tense of “to go” is, and expect
    “went”.
4.  Remove all sentences / texts from the corpus that contain the word
    “went”. Add more text to the corpus to make it roughly the same
    size again.
5.  Train an LLM A on that corpus.
6.  Use the same prompts to see what the LLM uses instead of “went”.
7.  Ask the LLM directly what the past tense of “to go” is. I expect
    “goed”?
8.  How many example sentences / texts containing the text “went” does
    one need to add to the corpus of LLM A and retrain in order for the
    resulting LLM to get it right. Is one enough? Ten? A thousand?
9.  Add an explicit sentence ‘The past tense of “to go” is “went”’. to
    the corpus of LLM A and retrain instead of the implicit training
    data. Did the trained LLM now get it right? Does it use it right?
    Does it answer the explicit question correctly?
10. Add an explicit sentence to the prompt of LLM A, instead of
    retraining it. Does it use the word right? Does it answer the
    explicit question correctly?

If there is some similar work to this out there, or if anyone has some
work like this, I’d be very curious for pointers.

P.S.: Also, I would love to see whether people who do research on LLMs
could correctly predict the result of this experiment ;)
