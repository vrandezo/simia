---
title: "Architektur"
date: 2006-01-27
language: "de"
slug: "architektur"
aliases:
  - "/wiki/Architektur"
tags:
  []
---

Die bisherige Version des DSA4 Werkzeugs ist in C++ programmiert. Für
die Daten entschied ich mich damals für ein XML-Datenformat, was zu der
Anbindung von Xerces führte. Die GUI wurde mit wxWindows gemacht (die
ersten Versionen, falls sich noch jemand erinnert, beruhten auf MSXML
und native Windows GUI Elementen). Der Wechsel auf Xerces und wxWindows
wurde durchgeführt, um Plattformunabhängig zu sein. Und tatsächlich: der
Code compilierte auch unter Linux (dank hier an die Portierer). Aber
richtig laufen tat er nie, es waren immer irgendwelche Bugs in der
Linuxversion, die ich nicht in der Windowsversion nachvollziehen konnte.

Außerdem war das verwendete C++ viel zu kompliziert. Ich benutzte massig
Templates (vor allem für die Rassen, Kulturen und Professionen), was den
Code sehr schwer lesbar und bearbeitbar machte. Auch ein schlichtes
compilen war eine recht anspruchsvolle Prozedur. Ich gehe davon aus,
dass deswegen nie im größeren Maße Entwicklungsarbeit von anderen als
von mir geleistet wurde: mein Code war schlicht zu kompliziert. Aus de
selben Grund habe ich selber ja in den letzten Monaten den Code nicht
angefasst.

Dies ist die wichtigste Lektion für die neue Version: deutlich
einfacherer Code. Änderungen müssen auch ohne sich extrem reinzuarbeiten
möglich sein. Idealerweise sollte das ganze Werkzeug interpretiert sein.
Kein compilen mehr. Ändern. Neustart. Fertig.

Wie ich das erreichen will verrate ich in den nächsten Blogeinträgen
genauer (deswegen habe ich auch nicht so viel geschrieben die letzten
Tage -- und weil ich auf Dienstreisen in Kaiserslautern und Düsseldorf
war -- ich wollte zunächst ein halbwegs tragbares Konzept haben. Das
kommt jetzt die nächsten paar Tage. Hier schonmal eine grobe Übersicht
-- ich werde im Folgenden genauer auf die Begriffe und den Aufbau
eingehen.

Mozilla, die Open Source Gruppe die uns nicht nur Firefox und
Thunderbird beschert hat, hat, was die Basis ihrer Tools ist, ein
umfangreiches, sogenanntes Mozilla Application Framework erstellt. Im
Großen und Ganzen ist es ein supermächtiges Biest -- ich will es soweit
zähmen, damit das DSA4 Werkzeug darauf läuft. Hierbei gibt es eine
Hauptengine, die XULRunner heißt. XUL ist so etwas wie HTML, bloß für
GUIs von Anwendungen (und man kann tatsächlich auch HTML und JavaScript
in XUL mit benutzen). Das bedeutet, das User Interface des neuen DSA4
Werkzeugs zu ändern wird so leicht sein wie HTML-Seiten schreiben, ja,
sogar mit CSS arbeitet das ganze zusammen. Interessant ist hierbei vor
allem das Verwenden von JavaScript, das eine dynamische GUI erlaubt. Die
Applikationslogik hingegen kann entweder in JavaScript implementiert
werden, oder auch in C++ oder Java (oder Python), um dann über XPCOM
(oder PyXPCOM) darauf zuzugreifen. Potenziell also kann man auch Teile
des bisherigen Codes wiederverwenden\! Schließlich, die Daten werden in
RDF gespeichert, einer XML-basierten Sprache, die aber deutlich Vorteile
zu XML (und ein paar Nachteile) aufweist.

All dies unterstützt das Mozilla Application Framework von Haus aus.
Anhand von Thunderbird und Firefox sieht man ja, dass das durchaus zu
brauchbaren Applikationen führen kann. Ich hoffe, dass es auch hier
aufgeht.


