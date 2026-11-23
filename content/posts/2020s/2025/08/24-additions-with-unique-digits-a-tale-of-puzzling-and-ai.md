---
title: "Additions with unique digits: a tale of puzzling and AI"
date: 2025-08-24
language: "en"
slug: "additions-with-unique-digits-a-tale-of-puzzling-and-ai"
aliases:
  - "/wiki/Additions_with_unique_digits:_a_tale_of_puzzling_and_AI"
tags:
  - math
  - Simia
  - english
  - AI

---

The other day, [Markus
Krötzsch](https://www.korrekt.org/page/Markus_Kr%C3%B6tzsch) and I were
catching up when one of his kids came in. She told us about a puzzle her
math teacher gave her:

*How many integer sums are there where the equation uses each digit at
most once?*

The simplest example is 1+2=3, but 12+47=59 also works. On the other
hand, 1+9=10 isn’t a solution because the digit ‘1’ appears twice (in
the first number and the sum). Markus’s wife Anja was the first of us to
find a solution using three-digit numbers.

I recommend trying to solve it yourself at this point, and then come
back to this post. It is much more fun like that.

Thinking for a moment, we realized there seemed to be quite a few
solutions. But how many? As computer scientists, our immediate thought
was to write a program. First, though, we estimated the complexity of a
brute force approach: if we tried all possible permutations of the
digits 0 to 9, that’s 10\! permutations, or about 3.6 million. A
computer should work through that pretty quickly.

I started writing code, and did so even more inefficiently. I included
‘+’ and ‘=’ with the 10 digits, then iterated through all permutations
(and shorter versions) to check for solutions. This ballooned the
candidate pool to an upper bound of 12\!x10, or about 5 billion. I knew
there was plenty of room for improvement – the code wasn’t smart – but
it should find all the results. I started running it. At this point, I
was pretty sure this was the kind of problem that with raw computational
power can be solved faster than taking the time to come up with 'smart'
code and better heuristics. [My full code is
here](/pages/unique-digits-addition/denny).

As my code ran, Markus took it as a fun challenge and set out to create
a smarter solution — which, admittedly, shouldn’t be too hard. Instead
of iterating through all possible (and many impossible) equation
strings, he only permuted the numbers, applied a maximum length, and
checked those. [Markus’
code](/pages/unique-digits-addition/markus) was impressively fast
– just **4 seconds**\! It seemed like we had found the 'right' way to
solve it, using better heuristics. Or had we?

Soon after, my code finished, taking **20 minutes**. We both had the
same answer\! (You can find the answer in the linked material, but I am
keeping it out here in case you want to try it out yourself). Having two
different approaches with the same result gave us high confidence in the
answer.

Now, that’s where it could have ended. But the kids were teasing us: it
took us forever to write the code (less than half an hour, but still),
why didn’t we just ask ChatGPT for the answer?

We were pretty convinced there’s no chance ChatGPT would be able to
answer that. So we asked. Markus formulated the prompt (in German, due
to my prodding, so it’s more fun for his kid watching), and ChatGPT
started thinking.

I have never seen it thinking for so long. Almost seven minutes.

We used that time to laugh and joke about it. No way it would figure it
out\! We were looking at the steps it was describing. They didn’t seem
too bad. What is a
[cryptarithm](https://en.wikipedia.org/wiki/Verbal_arithmetic)? Never
heard of that. We were getting ready to amuse ourselves by watching and
dissecting ChatGPT’s answer.

Boy, we were wrong\!

It returned the same number we had found. The answer was great\! Not
only that, we looked into the thinking process and found [the code that
ChatGPT wrote](/pages/unique-digits-addition/chatgpt). That code
ran in fractions of a second. It wasn’t just faster; the way it built
the equations, digit by digit, felt like a fundamentally different
strategy than our permutations. Here is [a link to the full
conversation](https://chatgpt.com/share/68a8d196-bab8-8007-9a27-192391ce5b07)
([local
archive](/pages/unique-digits-addition/chatgpt-conversation)).
Where my code ran in 20 minutes and Markus’s in 4 seconds, ChatGPT’s
code ran in 60 milliseconds.

We were completely baffled. I searched the Web for this riddle and
solutions, hoping to find indications it had been solved before, that it
was part of the corpus. It might be the case, but we didn’t find it
anywhere. ChatGPT came up with more efficient code, and was faster to
write it. We were deeply impressed, and were left with two questions,
without immediate answers:

1.  Given that this is a language model, how did it actually manage to
    reach this solution? Why did this work?
2.  Given that ChatGPT can do this, what does this mean? What are the
    consequences of having such an ability available? How does this
    change things?

I kicked off my local [Ollama](https://ollama.com/) with [OpenAI’s
recent Open Weight model](https://openai.com/index/introducing-gpt-oss/)
(120 billion parameters), using Markus’s prompt. I let it run in the
background while Markus and I kept chatting. It took a long time – tens
of minutes? I didn’t keep track – and we were again confident it
wouldn’t be able to answer the question. This was mostly because my
local Ollama doesn’t have access to a Python interpreter. And indeed, it
answered that there were 45 solutions, very much off from the 1991
solutions we were looking for.

We were a bit relieved. It was getting late, so we called it a night.
Seeing Ollama struggle initially, giving me numbers far off the mark,
actually reinforced my earlier skepticism. It felt like my intuition
about what these models *couldn't* do was being confirmed – at least for
a moment. I asked the system to list all 45 solutions, and it did. I
noticed that 1+2=3 was missing. I asked if that would be a correct
answer and if it wanted to reconsider its number of solutions, then left
it to run while I went to sleep.

The next day I checked the answer. The model had increased its answer to
124 solutions and wrote new code. It told me I should run that Python
code myself, as a next step. So, again, the wrong answer.

And then I did run the code. From both [the first
answer](/pages/unique-digits-addition/gpt-oss), and [the second,
improved answer](/pages/unique-digits-addition/gpt-oss-v2). If you
actually run the code, both of them result in the correct answer\! The
first version took about 20 seconds. The second version then took almost
half an hour to run, but I think that’s only because at this point the
LLM was becoming a bit extra cautious; it even checked for five-digit
numbers, although four-digit numbers were sufficient. I took the LLM’s
last code, made some [minor clean-up to the
code](/pages/unique-digits-addition/gpt-oss-cleaned), and reduced
it to four digits again, and the code gives the correct answer in 20
seconds again. [My complete conversation with gpt-oss is available
here](/pages/unique-digits-addition/gpt-oss-conversation).

Not only that: I would even claim that this cleaned-up code provides the
easiest to read and understand of all the solutions we discussed so far.
It iterates over all possible numbers up to four digits, making sure the
second number is always bigger than the first, gets their sum, checks
the result for digit uniqueness (quite elegantly using a set\!), and
counts the solutions. The code is short and, I’d say, elegant.

Markus has also written [a second
version](/pages/unique-digits-addition/markus-v2), which beats the
one by ChatGPT in efficiency, running in only *20 milliseconds*, and
probably being so fast that the Unix time command doesn't measure it
reliably.

I am impressed by the answers by the models (and by Markus as well). I
think this is a great example of my biggest problem with all of these
models, something I’ve been saying for years: **I cannot explain to
someone else what these models are good at, and what they are not good
at**.

But I thought I had a good intuition myself. That I roughly knew what
kind of questions they would answer well, and which ones I shouldn’t
trust them with. What my experience from this experiment showed me is
that I do not. **I don’t know what the capabilities of these models
are**.

Given the [recent news around the math
olympiad](https://www.heise.de/en/news/OpenAI-and-Google-win-gold-at-the-Math-Olympics-10496839.html),
should I have expected such a result? Was this just a toss-up? Do these
systems now reliably solve problems like these? Would we have trusted
ChatGPt’s result, or would we have been skeptical, if Markus and I
hadn't calculated the result for the riddle ourselves?

I am tempted to rationalize it away, to think that the problem was
simpler than we made it, that my complex code involving permutations was
a red herring, and that’s why the systems could solve it. Maybe that’s
just me dealing with the [AI
effect](https://en.wikipedia.org/wiki/AI_effect), where we downplay AI
achievements once they happen.

Thanks for reading so far. And big thanks to Markus’s kids for bringing
up this riddle, and their math teacher for asking it.
