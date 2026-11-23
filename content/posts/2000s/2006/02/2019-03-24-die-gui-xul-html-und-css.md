---
title: "Die GUI - XUL, HTML und CSS"
date: 2006-02-27
language: "de"
slug: "die-gui-xul-html-und-css"
aliases:
  - "/wiki/Die_GUI_-_XUL,_HTML_und_CSS"
tags:
  []
---

Das Herzstück von Mozilla ist die Renderingengine Gecko. Sie liest zum
Beispiel (X)HTML ein und stellt dieses dann auf dem Monitor dar. Damit
lassen sich bereits sehr interaktive und sich äußerst dynamisch
anfühlende Webseiten erstellen, insbesondere wenn man JavaScript mit
verwendet. An Beispielen wie GMail oder start.com kann man erkennen,
wieviel heute schon mit HTML möglich ist. Dennoch: viele GUI-Elemente
wie Listen, Menüs oder Knöpfe sind in HTML eher umständlich umgesetzt.
Darum wurde XUL, die XML User Interface Language, eingeführt, eine
XML-Sprache zur Beschreibung von graphischen Benutzerschnittstellen.

Mit XUL ist es dann möglich zu beschreiben, wo bestimmte Elemente
auftauchen, welche wo auftauchen, etc. Dadurch wird es zum Beispiel
leicht fallen, verschiedene Versionen der GUI zu erstellen, eine für
Experten und eine für Anfänger. Insbesondere könnte man sich einen
Schritt-für-Schritt-Wizard für die Heldenerschaffung vorstellen, wie sie
in den meisten anderen Editoren wie Helden praktiziert wird. Meine
persönliche Vorliebe bleibt dennoch beim "Immer alles
veränderbar"-Modus. Aber die Codebasis wird sehr einfach beides
hergeben.

Ein weiterer Vorteil von XUL ist, dass damit das User Interface
interpretiert, nicht compiliert wird. Das hat den Vorteil, dass, wenn
man das Aussehen des Programms verändern will, man nicht eine ganze
Programmierumgebung mit Compiler etc. braucht, sondern einfach nur einen
Texteditor und etwas XML- oder HTML-Kenntnisse. Hoffnung dabei: schöne
neue Skins und bessere Bedienbarkeit können von wesentlich mehr Leuten
beigesteuert werden als bisher.

Apropos Skins: ja, auch das wird möglich sein. Wie von Thunderbird und
Firefox gewohnt, sind XUL-basierte Anwendung vollkommen mit CSS und
ähnlichem skinbar. Das heißt Farben, Hintergründe, Aussehen der
Elemente sind steuerbar. Ich stelle mir jetzt schon ein Horasreich-Skin,
ein Myranor-Skin und ein G7-Skin vor. Mal sehen. Es wird letztlich von
Eurer Kreativität abhängen.

Auch hier ist das wichtige: man muss dafür keine Programmierumgebung
besitzen und keine Programmierkenntnisse haben (auch wenn sie natürlich
nicht schaden). Der wichtigste Teil des neuen Designs ist es, die
einzelnen Teile der Architektur orthogonal zu gestalten, so dass man an
einem bestimmten Teil arbeiten kann, ohne das man ein Experte in allen
sein muss. Etwas, was bei der ersten Version sträflichst vernachlässigt
wurde.

Nächstes Mal: zum Datenmodell und der Datenhaltung.


