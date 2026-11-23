---
title: "KAON2 and Protégé"
date: 2005-11-01
language: "en"
slug: "kaon2-and-prot-g"
aliases:
  - "/wiki/KAON2_and_Protégé"
tags:
  []
---

[KAON2](KAON2 "wikilink") is the Karlsruhe Ontology infrastructure. It
is an industry strength reasoner for OWL ontologies, pretty fast and
comparable to reasoners like
[Fact](http://www.cs.man.ac.uk/~horrocks/FaCT/) and
[Racer](http://www.racer-systems.com/), who gained from years of
development. Since a few days KAON2 also implements the DIG Interface\!
Yeah, now you can use it with your tools\! Go and grab KAON2 and get a
feeling for how good it fulfills your needs.

Here's a step to step description of how you can use KAON2 with
[Protégé](http://protege.stanford.edu/) (other DIG based tools should
be pretty the same). [Get the KAON2
package](http://kaon2.semanticweb.org/), unpack it and then go to the
folder with the kaon2.jar file in it. This is the Java library that does
all the magic.

Be sure to have [Java 5](http://java.sun.com/j2se/1.5.0/download.jsp)
installed and in your path. No, Java 1.4 won't do it, KAON2 builds
heavily on some of the very nice Java 5 features.

You can start KAON2 now with the following command:

    java -cp kaon2.jar org.semanticweb.kaon2.server.ServerMain -registry -rmi -ontologies server_root -dig -digport 8088

Quite lengthy, I know. You will probably want to stuff this into a
shell-script or batch-file so you can start your KAON2 reasoner with a
simple doubleclick.

The last argument - *8088* in our example - is the port of the DIG
service. Fire up your Protege with the OWL plugin, and check in the OWL
menu the preferences window. The reasoner URL will tell you where
Protege looks for a reasoner - with the above DIG port it should be
*<http://localhost:8088>*. If you chose another port, be sure to enter
the correct address here.

Now you can use the consistency checks and automatic classification and
all this as provided by Protege (or any other Ontology Engineering tool
featuring the DIG interface). Protégé tells you also the time your
reasoner took for its tasks - compare it with Racer and Fact, if you
like. I'd be interested in your findings\!

But don't forget - this is the very first release of the DIG interface.
If you find any bugs, say so\! They must be squeezed\! And don't forget:
KAON2 is quite different than your usual tableaux reasoner, and so some
questions are simply not possible. But the restrictions shouldn't be too
severe. If you want more information, go to the [KAON2 web
site](http://kaon2.semanticweb.org/) and check the references.

**Comments**

*Olivier Rossel (30 November 2005 17:23)*

If I create a basic OWL-DL project in Protege and ask Kaon2 to check consistency, I get a Protege exception.

Something like: edu.stanford.smi.protegex.owl.inference.dig.exception.DIGErrorException: Invalid object property type 'catom'. [ID: ] at edu.stanford.smi.protegex.owl.inference.dig.reasoner.DefaultDIGReasoner.performErrorCheck(Unknown Source)

Any hint?
