---
title: "Playing around with Aliquot"
date: 2024-01-28
language: "en"
slug: "playing-around-with-aliquot"
aliases:
  - "/wiki/Playing_around_with_Aliquot"
tags:
  - Simia
  - english
  - math
  - programming

---

-   
    *Warning\! Very technical, not particularly insightful, and overly
    long post about hacking, discrete mathematics, and rabbit holes. I
    don't think that anything here is novel, others have done more
    comprehensive work, and found out more interesting stuff. This is
    not research, I am just playing around.*

[Ernest Davis](https://cs.nyu.edu/~davise/) is a NYU professor, author
of many publications (including “[Rebooting AI](http://rebooting.ai/)”
with [Gary Marcus](http://garymarcus.com/index.html)) and a friend on
Facebook. Two days ago he posted about [Aliquot
sequences](https://en.wikipedia.org/wiki/Aliquot_sequence), and that it
is yet unknown how they behave.

What is an Aliquot sequence? Given a number, take all its proper
divisors, and add them up. That’s the next number in the sequence.

It seems that most of these either lead to 0 or end in a repeating
pattern. But it may also be that they just keep on going indefinitely.
We don’t know if there is any starting number for which that is the
case. But the smallest candidate for that is 276.

So far, we know the first 2,145 steps for the Aliquot sequence starting
at 276. That results in a number with 214 digits. We don’t know the
successor of that number.

I was curious. I know that I wouldn’t be able to figure this out
quickly, or, probably ever, because I simply don’t have enough skills in
discrete mathematics (it’s not my field), but I wanted to figure out how
much progress I can make with *little* effort. So I coded something up.

Anyone who really wanted to make a crack on this problem would probably
choose C. Or, on the other side of the spectrum, Mathematica, but I
don’t have a license and I am lazy. So I chose JavaScript. There were
two hunches for going with JavaScript instead of my usual first
language, Python, which would pay off later, but I will reveal them
later in this post.

So, my first implementation was very naïve ([source
code](https://github.com/vrandezo/aliquot/blob/main/aliquot1.js)). The
function that calculates the next step in the Aliquot sequence is
usually called s in the literature, so I kept that name:

` const divisors = (integer) => {`  
`   const result = []`  
`   for(let i = BigInt(1); i < integer; i++) {`  
`     if(integer % i == 0) result.push(i)`  
`   }`  
`   return result`  
` }`

` const sum = x => x.reduce(`  
`   (partialSum, i) => partialSum + i, BigInt(0)`  
` )`

` const s = (integer) => sum(divisors(integer))`

I went for BigInt, not integer, because Ernest said that the 2,145th
step had 214 digits, and the standard integer numbers in JavaScript stop
being exact before we reach 16 digits (at 9,007,199,254,740,991, to be
exact), so I chose BigInt, which supports arbitrary long integer
numbers.

The first 30 steps ran each under a second on my one decade old 4 core
Mac occupying one of the cores, reaching 8 digits, but then already the
36th step took longer than a minute - and we only had 10 digits so far.
Worrying about the limits of integers turned out to be a bit
preliminary: With this approach I would probably not reach that limit in
a lifetime.

I dropped BigInt and just used the normal integers ([source
code](https://github.com/vrandezo/aliquot/blob/main/aliquot2.js)). That
gave me 10x-40x speedup\! Now the first 33 steps were faster than a
second, reaching 9 digits, and it took until the 45th step with 10
digits to be the first one to take longer than a minute. Unsurprisingly,
a constant factor speedup wouldn’t do the trick here, we’re fighting
against an exponential problem after all.

It was time to make the code less naïve ([source
code](https://github.com/vrandezo/aliquot/blob/main/aliquot3.js)), and
the first idea was to not check every number smaller than the target
integer whether it divides (line 3 above), but only up to half of the
target integer.

` const divisors = (integer) => {`  
`   const result = []`  
`   const half = integer / 2`  
`   for(let i = 1; i <= half; i++) {`  
`     if(integer % i == 0) result.push(i)`  
`   }`  
`   return result`  
` }`

Tiny change. And exactly the expected impact: it ran double as fast. Now
the first 34 steps ran under one second each (9 digits), and the first
one to take longer than a minute was the 48th step (11 digits).

Checking until half of the target seemed still excessive. After all, for
factorization we only need to check until the square root. That should
be a more than constant speedup. And once we have all the factors, we
should be able to quickly reconstruct all the divisors. Now this is the
point where I have to admit that I have a cold or something, and the
code for creating the divisors from the factors is probably overly
convoluted and slow, but you know what? It doesn’t matter. The only
thing that matters will be the speed of the factorization.

So my next step ([source
code](https://github.com/vrandezo/aliquot/blob/main/aliquot4.js)) was a
combination of a still quite naïve approach to factorization, with
another function that recreates all the divisors.

` const factorize = (integer) => {`  
`   const result = [ 1 ]`  
`   let i = 2`  
`   let product = 1`  
`   let rest = integer`  
`   let limit = Math.ceil(Math.sqrt(integer))`  
`   while (i <= limit) {`  
`     if (rest % i == 0) {`  
`       result.push(i)`  
`       product *= i`  
`       rest = integer / product`  
`       limit = Math.ceil(Math.sqrt(rest))`  
`     } else {`  
`       i++`  
`     }`  
`   }`  
`   result.push(rest)`  
`   return result`  
` }`

` const divisors = (integer) => {`  
`   const result = [ 1 ]`  
`   const inner = (integer, list) => {`  
`     result.push(integer)`  
`     if (list.length === 0) {`  
`       return [ integer ]`  
`     }`  
`     const in_results = [ integer ]`  
`     const in_factors = inner(list[0], list.slice(1))`  
`     for (const f of in_factors) {`  
`       result.push(integer*f)`  
`       result.push(f)`  
`       in_results.push(integer*f)`  
`       in_results.push(f)`  
`     }`  
`     return in_results`  
`   }`  
`   const list = factorize(integer)`  
`   inner(list[0], list.slice(1))`  
`   const im = [...new Set(result)].sort((a, b) => a - b)`  
`   return im.slice(0, im.length-1)`  
` }`

That made a big difference\! The first 102 steps all were faster than a
second, reaching 20 digits\! That’s more than 100x speedup\! And then,
after step 116, the thing crashed.

Remember, integer only does well until 16 digits. The numbers were just
too big for the standard integer type. So, back to BigInt. The
availability of BigInt in JavaScript was my first hunch for choosing
JavaScript (although that would have worked just fine in Python 3 as
well). And that led to two surprises.

First, sorting arrays with BigInts is different from sorting arrays with
integers. Well, I find already sorting arrays of integers a bit weird in
JavaScript. If you don’t specify otherwise it sorts numbers
lexicographically, instead of by value:

` [ 10, 2, 1 ].sort() == [ 1, 10, 2 ]`

You need to provide a custom sorting function in order to sort the
numbers by value, e.g.

` [ 10, 2, 1 ].sort((a, b) => a-b) == [ 1, 2, 10 ]`

The same custom sorting functions won’t work for BigInt, though. The
custom function for sorting requires an integer result, not a BigInt. We
can write something like this:

` .sort((a, b) => (a < b)?-1:((a > b)?1:0))`

The second surprise was that BigInt doesn’t have a square root function
in the standard library. So I need to write one. Well, Newton is quickly
implemented, or copy and pasted ([source
code](https://github.com/vrandezo/aliquot/blob/main/aliquot5.js)).

Now, with switching to BigInt, we get the expected slowdown. The first
92 steps run faster than a second, reaching 19 digits, and then the
first step to take longer than a minute is step 119, with 22 digits.

Also, the actual sequences started indeed diverging, due to the
inaccuracy of large JavaScript integer: step 83 resulted in
23,762,659,088,671,304 using integers, but 23,762,659,088,671,300 using
BigInt. And whereas that looks like a tiny difference on only the last
digit, the number for the 84th step showed already what a big difference
that makes: 20,792,326,702,587,410 with integers, and
35,168,735,451,235,260 with BigInt. The two sequences went entirely off.

What was also very evident is that at this point some numbers took a
long time, and others were very quick. This is what you would expect
from a more sophisticated approach to factorization, that it depends on
the number and size of the factors. For example, calculating step 126
required to factorize the number 169,306,878,754,562,576,009,556,
leading to 282,178,131,257,604,293,349,484, and that took more than 2
hours with that script on my machine. But then in Step 128 the result
552,686,316,482,422,494,409,324 was calculated from
346,582,424,991,772,739,637,140 in less than a second.

At that point I also started taking some of the numbers, and googled
them, surfacing [a Japanese blog
post](https://hyperion64.hatenadiary.org/entry/20130728/p1) from ten
years ago that posted the first 492 numbers, and also confirming that
the 450th of these numbers corresponds to a published source. I compared
the list with my numbers and was happy to see they corresponded so far.
But I guesstimated I would not in a lifetime reach 492 steps, never mind
the actual 2,145.

But that’s OK. Some things just need to be let rest.

That’s also when I realized that I was overly optimistic because I
simply misread the number of steps that have been already calculated
when reading the original post: I thought it was about 200-something
steps, not 2,000-something steps. Or else I would have never started
this. But now, thanks to the sunk cost fallacy, I wanted to push it just
a bit further.

I took the biggest number that was posted on that blog post,
111,953,269,160,850,453,359,599,437,882,515,033,017,844,320,410,912, and
let the algorithm work on that. No point in calculating steps 129, which
is how far I have come, through step 492, if someone else already did
that work.

While the computer was computing, I leisurely looked for libraries for
fast factorization, but I told myself that no way am I going to install
some scientific C library for this. And indeed, I found a few, such as
the [msieve project](https://sourceforge.net/projects/msieve/).
Unsurprising, it was in C. But I also found a Website, [CrypTool-Online
with msieve](https://www.cryptool.org/en/cto/msieve) on the Web (that’s
pretty much one of the use cases I hope
[Wikifunctions](https://www.wikifunctions.org/) will also support rather
soonish). And there, I could not only run the numbers I already
calculated locally, getting results in subsecond speed which took
minutes and hours on my machine, but also the largest number from the
Japanese website was factorized in seconds.

That just shows how much better a good library is than my naïve
approach. I was slightly annoyed and challenged by the fact how much
faster it is. Probably also runs on some fast machine in the cloud.
Pretty brave to put a site like that up, and potentially have other
people profit from the factorization of large numbers for, e.g. Bitcoin
mining on your hardware.

The site is fortunately Open Source, and when I [checked the source
code](https://github.com/cryptool-org/cto) I was surprised, delighted,
and I understood why they would make it available through a Website:
they **don’t** factorize the number in the cloud, but on the edge, in
your browser\! If someone uses a lot of resources, they don’t mind: it’s
their own resources\!

They took the msieve C library and compiled it to WebAssembly. And now I
was intrigued. That’s something that’s useful for my work too, to better
understand WebAssembly, as we use that in Wikifunctions too, although
for now server side. So I rationalized, why not see if I can get that
run on Node.

It was a bit of guessing and hacking. The JavaScript binding was written
to be used in the browser, and the binary was supposed to be loaded
through fetch. I guessed a few modifications, replacing fetch with
Node’s FS, and managed to run it in Node. The hacks are terrible, but
again, it doesn’t really matter as long as the factorization would speed
up.

And after a bit of trying and experimenting, I got it running ([source
code](https://github.com/vrandezo/aliquot/blob/main/aliquot6.js)). And
that was my second hunch for choosing JavaScript: it had a great
integration for using WebAssembly, and I figured it might come in handy
to replace the JavaScript based solution. And now indeed, the
factorization was happening in WebAssembly. I didn’t need to install any
C libraries, no special environments, no nothing. I just could run Node,
and it worked. I am absolutely positive there are is cleaner code out
there, and I am sure I mismanaged that code terribly, but I got it to
run. At the first run I found that it added an overhead of 4-5
milliseconds on each step, making the first few steps much slower than
with pure JavaScript. That was a moment of disappointment.

But then: the first 129 steps, which I was waiting hours and hours to
run, zoomed by before I could even look. Less than a minute, and all the
492 steps published on the Japanese blog post were done, allowing me to
use them for reference and compare for correctness so far. The overhead
was irrelevant, even across the 2,000 steps the overhead wouldn’t amount
to more than 10 seconds.

The first step that took longer than a second was step 596, working on a
58 digit number. All the first 595 steps took less than a second each.
The first step that took more than a minute, was step 751, a 76 digit
number, taking 62 seconds, factorizing
3,846,326,269,123,604,249,534,537,245,589,642,779,527,836,356,985,238,147,044,691,944,551,978,095,188.
The next step was done in 33 milliseconds.

The first 822 steps took an hour. Step 856 was reached after two hours,
so that’s another 34 steps in the second hour. Unexpectedly, things
slowed down again. Using faster machines, modern architectures, GPUs,
TPUs, potentially better algorithms, such as
[CADO-NFS](https://cado-nfs.gitlabpages.inria.fr/) or
[GGNFS](https://www.math.ttu.edu/~cmonico/software/ggnfs/), all of that
could speed that up by a lot, but I am happy how far I’ve gotten with,
uhm, *little* effort. After 10 hours, we had 943 steps and a 92 digit
number, 20 hours to get to step 978 and 95 digits. My goal was to reach
step 1,000, and then publish this post and call it a day. By then, a
number of steps already took more than an hour to compute. I hit step
1000 after about 28 and a half hours, a 96 digit number:
162,153,732,827,197,136,033,622,501,266,547,937,307,383,348,339,794,415,105,550,785,151,682,352,044,744,095,241,669,373,141,578.

I rationalize this all through “I had fun” and “I learned something
about JavaScript, Node, and WebAssembly that will be useful for my job
too”. But really, it was just one of these rabbit holes that I love to
dive in. And if you read this post so far, you seem to be similarly
inclined. Thanks for reading, and I hope I didn’t steal too much of your
time.

I also [posted a list of all the
numbers](https://github.com/vrandezo/aliquot/blob/main/results.txt) I
calculated so far, because I couldn’t find that list on the Web, and I
found the list I found helpful. Maybe it will be useful for something. I
doubt it. *(P.S.: the list was already on the Web, I just wasn't looking
careful enough. Both, [OEIS](https://oeis.org/A008892) and
[FactorDB](http://factordb.com/sequences.php?se=1&aq=276&action=all&fr=0&to=100)
have the full list.)*

I don’t think any of the lessons here are surprising:

  - for many problems a naïve algorithm will take you to a good start,
    and might be sufficient
  - but never fight against an exponential algorithm that gets big
    enough, with constant speedups such as faster hardware. It’s a
    losing proposition
  - But hey, first wait if it gets big enough\! Many problems with
    exponential complexity are perfectly solvable with naïve approaches
    if the problem stays small enough
  - better algorithms really make a difference
  - use existing libraries\!
  - advancing research is hard
  - WebAssembly is really cool and you should learn more about it
  - the state of WebAssembly out there can still be wacky, and sometimes
    you need to hack around to get things to work

In the meantime I played a bit with other numbers (thanks to having a 4
core computer\!), and I will wager one ambitious hypothesis: **if 276
diverges, so does 276,276, 276,276,276, 276,276,276,276, etc., all the
way to 276,276,276,276,276,276,276,276,276, i.e. 9 times "276".**

I know that 10 times "276" converges after 300 steps, but I have tested
all the other "lexical multiples" of 276, and reached 70 digit numbers
after hundreds of steps. For 276,276 I pushed it further, reaching 96
digits at step 640. (And for at least 276,276 we should already know the
current best answer, because the Wikipedia article states that all the
numbers under one million have been calculated, and only about 9,000
have an unclear fate. We should be able to check if 276,276 is one of
those, which I didn't come around to yet).

Again, this is not research, but just fooling around. If you want actual
systematic research, the [Wikipedia
article](https://en.wikipedia.org/wiki/Aliquot_sequence) has a number of
great links.

Thank you for reading so far\!

P.S.: Now that I played around, I started following some of the links,
and wow, there's a whole community with great tools and infrastructure
having fun about Aliquot sequences and prime numbers doing this for
decades. This is extremely fascinating.
