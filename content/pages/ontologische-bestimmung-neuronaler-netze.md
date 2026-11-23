---
title: "Ontologische Bestimmung Neuronaler Netze"
language: "de"
slug: "Ontologische_Bestimmung_Neuronaler_Netze"
aliases:
  - "/wiki/Ontologische_Bestimmung_Neuronaler_Netze"
topics:
  - Studium
  - AI
  - philosophy
  
---

-   
    *„Für Trubel und hitzige Diskussionen sorgte in der letzten Runde
    des Turniers auch die Partie von Shredder: In klar gewonnener
    Stellung ließ der spätere Champion eine dreifache
    Stellungswiederholung zu. Sein Gegner hätte nach den Schachregeln
    daraufhin die Partie für Unentschieden erklären lassen können. Dies
    empfand er aber in verlorener Stellung als unfair, spielte weiter
    und verlor schließlich. Gut für Shredder, schlecht für Fritz, das im
    Falle eines Unentschiedens Weltmeister gewesen wäre, so aber in den
    Stichkampf mußte und diesen auch noch verlor.“*
      -   
        *(heise newsticker, 30. November 2003)*

*Shredder* und *Fritz*, von denen in der oben genannten Meldung die Rede
ist, sind nicht etwa menschliche Gegner – sondern Computerprogramme. Das
erwähnte Turnier war die Weltmeisterschaft im Computerschach, und
interessanter als die tatsächlichen Ereignisse – wenn man diesen
nachgeht, wird man feststellen, dass die Meldung irreführend geschrieben
ist – sind Art und Weise ihrer Darstellung: Computerprogrammen werden
hier ganz selbstverständlich ein Sinn für Fairness unterstellt, ihre
Handlungen werden wie die Handlungen menschlicher Akteure beschrieben
und behandelt: Shredders Gegner *hätte können*, *empfand als unfair*,
Fritz hingegen *musste*.

Wenn jemand *hätte können*, bedeutet das schlicht: wir unterstellen ihm,
dass er, dank seiner Freiheit, in der Situation in der er war, sich auch
hätte anders entscheiden können, anders handeln können. Der Begriff der
„Handlung“ scheint hier angebracht, trotz und gerade wegen seiner
zahlreichen Implikationen. Wie gesagt: wenn man die tatsächlichen
Ereignisse recherchiert, die zu der oberen Meldung geführt haben,
entpuppt sich das ganze als bei weitem nicht so dramatisch wie zunächst
angenommen: bei Shredders Gegner entschloss letztlich dessen
Programmierer, das Spiel fortzusetzen, weil er es für unfair empfunden
hätte, diesen offensichtlichen Fehler auszunutzen und so Shredder um
die Siegchancen zu bringen. Fritz musste in den Stichkampf, weil nun mal
die Regeln des Turniers so lauteten.

Dennoch: wie selbstverständlich erscheint eine solche Meldung auf einer
angesehen Nachrichtenseite über die Informationstechnik. Im Allgemeinen
werden Entscheidungen heute immer häufiger auf Grundlage
computergestützter Analysen getroffen. In der Mathematik ist ein
heftiger Streit über die Gültigkeit von Computerbeweisen entfacht.

Das bekannteste Beispiel dürfte das **Vierfarbenproblem** sein: lässt
sich eine beliebige Landkarte mit nur vier Farben so einfärben, dass
keine zwei Länder mit einer gemeinsamen Grenze mit der selben Farbe
eingefärbt werden? Schon lange nahm man an, dass dem so sei, doch es
fehlte der Beweis, bis schließlich die beiden Mathematiker **Kenneth
Appel** und **Wolfgang Haken** ihn 1977 vorlegen konnten. Dieser Beweis
beruht auf einer Fallunterscheidung mit knapp 2000 Fällen, und um diese
durchzurechnen, wurde ein Computer zu Hilfe gezogen.

Mit der Begründung, dass kein Mensch diesen Beweis nachvollziehen könne,
wurde er von zahlreichen Mathematikern jener Zeit abgelehnt. Wenn wir
Computerberechnungen bei einem formalen Beweis gelten lassen wollen,
schlossen sie, müsse zuerst die Hard- und Software, mit deren Hilfe die
Berechnungen durchgeführt wurden, formal als korrekt bewiesen werden –
eine Forderung, die bei Hardware unmöglich zu erfüllen ist. Aufgrund
unserer beschränkten Lebenszeit hingegen ist jedoch auch das formelle
Nachvollziehen der Computerergebnisse durch Menschen keine effizient
machbare Lösung – und selbst wenn es ein einzelner Mensch durchrechnen
sollte, verleiht es dann den Ergebnissen auf magische Weise Gültigkeit?

Hier kann man in die andere Richtung fragen: würde denn die Hard- und
Software des Menschen irgendeiner formellen Überprüfung standhalten?
Natürlich nicht. Was ist es also, was der Nachvollziehbarkeit durch den
Menschen in den Augen mancher Mathematiker ihre Magie verleiht? Was
müsste ein Computer erfüllen, um ebenfalls einen solchen Status zu
erreichen? Ist das überhaupt möglich?

Dieser Beitrag behandelt diese und verwandte Fragen nicht im Ganzen,
sondern versucht einen Teil der Frage genauer zu beleuchten. Sie
konzentriert sich auf Neuronale Netze und versucht, diese ontologisch zu
bestimmen. Dabei werden zunächst ein paar grundlegende Begriffe wie das
Mooresche Gesetz oder die Turingberechenbarkeit für den Rahmen dieser
Hausarbeit bestimmt. Beruhend auf diesen Begriffen und einigen
Ergebnissen jüngerer Forschung werden wir schließlich auf eine
überraschend einfache Antwort gelangen.

### Rechner und Rechengeschwindigkeit

**Computer** ist das englische Wort für Rechner – und nichts anderes
machen Computer: Rechnen. Ihre Besonderheit ist, dass sie dabei für
Menschen unvorstellbare Geschwindigkeiten erreichen, und durch den
technischen Fortschritt in diesem Bereich nimmt die mögliche
Geschwindigkeit dauernd zu.

Dieser Anstieg der Rechengeschwindigkeit wird in **Moore's Law**
(Mooresche Gesetz) formuliert: alle 18 Monate verdoppelt sich die
Rechengeschwindigkeit, die man für einen bestimmten Betrag erwerben
kann.

Das Mooresche Gesetz ist natürlich eine rein empirische Beobachtung der
bisherigen Entwicklung, doch seit seiner Formulierung 1965 durch Gordon
Moore, einem der Begründer der Firma Intel, ist seine Gültigkeit
festzustellen – wobei es natürlich sein kann, dass das Mooresche Gesetz
zu einer selbsterfüllenden Prophezeiung wurde, und dass die Entwicklung
ohne dem Gesetz anders abgelaufen wäre. Ray Kurzweil versucht in *„Homo
s@piens“* leidenschaftlich das Gesetz, das natürlich nur eine Projektion
bisheriger Daten über die verfügbare Rechenkraft in die Zukunft ist, mit
Beispielen und Statistiken zu belegen und führt aus, dass es gar seit
dem Jahr 1900 (mit Charles Babbages Analytischer Maschine), und damit
schon lange vor der Erfindung integrierter Schaltkreise (auf welche
Moore seine Beobachtung eigentlich bezog) Gültigkeit besaß. Einen Beweis
für das Gesetz kann es natürlich nicht geben, und zahlreiche Artikel in
diesem Bereich prophezeien ein Ende des Mooreschen Gesetzes in zehn
Jahren voraus (wobei das Erscheinungsjahr dieser Artikel unwichtig ist,
es wird mit einer beeindruckenden Konstanz von „in zehn Jahren“
gesprochen, weil dann eine physikalische Grenze erreicht sein würde.
Diese Propheten irrten bislang, was aber auch keine Aussage über die
Zukunft sein kann).

Seit über hundert Jahren also kann die Gültigkeit des Mooreschen
Gesetzes beobachtet werden, und insbesondere Kurzweil baut darauf seine
Zukunftsprojektionen auf: *„Laut Kurzweil überflügeln den Menschen schon
2019 handelsübliche PCs in allen Bereichen, 2029 lässt sich das
menschliche Hirn scannen und per Computer duplizieren. In einem neuen
Evolutionssprung werden Mensch und Maschine verschmelzen“* (Klappentext
Homo s@piens, Ray Kurzweil, 1999). Natürlich kann man Kurzweil
antworten, dass er mit der selben Begeisterung und Überzeugungskraft
1978 vorraussagen hätte können, dass der neue Papst Italiener sein werde
– eine damals seit über 450 Jahren erfolgreich zu beobachtende
empirische Aussage.

Heißt das, Kurzweil hat Unrecht? Sind wir von dem *Aufstand der
Maschinen* und einer echten K.I. außerhalb der Kinoleinwand weiter
entfernt, als uns Kurzweil weismachen will?

Ohne sich selber unter die Propheten zu mischen, ist eine Beantwortung
dieser Frage nicht möglich. Doch ist sie in diesem Rahmen auch gänzlich
irrelevant: ist es wirklich wichtig, ob 2019 oder 2029 oder 2049 die
Maschinen den Menschen an Intelligenz übertreffen werden? Nein, die
Frage ist doch vielmehr: ist das prinzipiell überhaupt möglich, oder
basieren Kurzweils Thesen auf einem Irrtum? Und wenn es doch möglich
ist, was bedeutet das?

Was wir aber im Hinterkopf behalten sollten ist der exponentielle
Wachstum der Rechengeschwindigkeit: zahlreiche Argumente der Form *„Das
ist für einen Computer viel zu komplex“* oder *„Die schiere Datenmenge
macht das unberechenbar“* haben plötzlich nur mehr eine aufschiebende
Funktion. Eine Verdopplung alle 18 Monate bedeutet schließlich, dass
alle 15 Jahre von einer Vertausendfachung der Rechengeschwindigkeit
auszugehen ist, und in 30 Jahren eine Vermillionfachung

### Neuronale Netze

Was sind diese Neuronalen Netze nun eigentlich?

Neuronale Netze beschreiben die Strukturen, welche von den
**Nervenzellen** (Neuronen) im Gehirn gebildet werden. Diese Strukturen
werden durch den Zustand der Nervenzellen sowie durch die Verbindungen
zwischen ihnen beschrieben. Nervenzellen haben üblicherweise mehrere
Ein- und einen Ausgang, der bei durch den Zellzustand bestimmten
Eingangskonfigurationen feuert. Dadurch ist die Bearbeitung elektrischer
Signale möglich.

Sowohl der innere Zustand wie auch die Verbindungen zwischen den Zellen
können durch die bearbeitenden Signale geändert werden. Diese
Veränderung wird **Lernen** genannt: die verarbeiteten Signale
verändern die zukünftige Bearbeitung weiterer Signale.

Auf dieser Idee beruhend, versuchte man mit mathematischen Modellen
diese Arbeitssweise abzubilden, um so Neuronen wie auch Neuronale Netze
berechnen zu können. 1969 jedoch wiesen **Marvin Minsky** und **Seymour
Papert** in ihrer Arbeit *Perceptrons* nach, dass die von ihnen
untersuchten Neuronalen Netze nicht mal in der Lage sind, die
*XOR*-Funktion (eine logische Entweder-Oder-Verknüpfung) zu berechnen.
Dies sorgte dafür, dass die Forschung in den folgenden Jahren Neuronale
Netze vernachlässigte.

Erst in den 1980ern stellte man fest, dass Neuronale Netzwerke mit mehr
Ebenen als die von Minsky und Papert untersuchten durchaus in der Lage
sind, nicht nur die XOR-Funktion zu berechnen, sondern sogar
**turingvollständig** sind. Dies führte zu einer Wiederbelebung der
Forschung auf diesem Gebiet, und seit dem konnten zahlreiche
Fortschritte gemacht werden.

### Turingvollständigkeit & die Church-Turing-These

Das Konzept der Turingvollständigkeit ist in der Informatik und
Mathematik grundlegend. Die Church-Turing-These, 1936 gebildet,
behauptet, dass die Menge der durch eine **Universelle Turingmaschine**
berechenbaren Algorithmen der Menge der berechenbaren Algorithmen
überhaupt entspricht. Das bedeutet, dass wir definieren können, was
überhaupt berechenbar ist.

Eine Turingmaschine kann hier aus Platzgründen nicht erklärt werden, es
sei hier auf ein beliebiges Buch zur theoretischen Informatik verwiesen.

Neben der Turingmaschine sind noch zahlreiche weitere Systeme zur Lösung
von Algorithmen entwickelt worden – etwa generative Grammatiken,
partiell rekursive Funktionen, Lambdakalküle, zelluläre Automaten und
manch andere. **Turingvollständigkeit** eines Systems bedeutet, dass das
System in der Lage ist, alles zu berechnen, dass auch eine universelle
Turingmaschine berechnen könnte – oder eben, wenn man die
Church-Turing-These akzeptiert, alle überhaupt berechenbaren Funktionen.

Die mathematischen Modelle von Neuronalen Netzen sind turingvollständige
Lösungssysteme.

### Substrat einer Berechnung

Die Frage nach der ontologischen Natur Neuronaler Netze muss aufgeteilt
werden auf die zwei verschiedenen Arten Neuronaler Netze: biologische
Neuronale Netze, wie sie etwa im Gehirn eines jeden Menschen zu finden
sind, und den simulierten Neuronalen Netzen, die auf Computern laufen.
Diese beiden Bereiche müssen selbstverständlich einzeln betrachtet
werden.

Simulierte Neuronale Netze unterscheiden sich in einigen Punkten von
biologischen Neuronalen Netzen: insbesondere werden sie aufgrund der
heutigen Computer sequentiell berechnet. Dies bedeutet, dass die
Neuronen eines simulierten Netzes eins nach dem anderen berechnet werden
müssen, ein sehr rechenintensiver Vorgang. Biologische Netze sind hier
klar im Vorteil: die chemischen und physikalischen Vorgänge in den
Neuronen geschehen unabhängig voneinander und insbesondere auch
unabhängig von einer zentralen Recheneinheit, so dass man hier massiv
parallel vorgehen und in wesentlich kürzerer Zeit zu einem Ergebnis
kommen kann. Dadurch sind biologische Neuronale Netze den simulierten um
Größenordnungen im Vorteil.

Ein weiteres Unterscheidungskriterium ist der gesamte Aufbau des
Menschen im Vergleich zu einem Computer. Hier haben wir ein lebendes
System aus Fleisch und Blut, dort ein industriell gefertigtes Gerät aus
Silizium und Aluminium.

Berechnungen laufen immer auf irgendeinem Träger, einem **Substrat** ab.
Dies kann der menschliche Geist sein, der, vielleicht mit der Hilfe von
Papier und Stift, eine Berechnung durchführt, dies können die
Leiterbahnen eines hochintegrierten Schaltkreises sein, oder die Kugeln
in einem Abakus. Neben diesem materiellen Substrat können wir noch ein
**Berechnungsystem** definieren. Dieses beschreibt das Gedankenmodell,
durch welches die Funktion abgewickelt, berechnet, wird.

Hierzu ein Beispiel: wenn wir die hochkomplexe Aufgabe *2+3* mit Hilfe
eines Abakus' rechnen wollen, schieben wir zunächst zwei Kugeln auf die
eine Seite (dies stellt die *2* dar), und dann nochmal drei weitere (für
die *3*) und zählen nun die Anzahl von Kugeln auf dieser Seite ab
(fünf). Das materielle Substrat mag in dem Fall aus Holzkugeln und
einer metallenen Stange gebildet sein, das Berechnungssystem ist unser
Wissen zur Verwendung eines Abakus'. Theoretisch könnten wir aber auch
die Simulation eines Abakus' auf einem Computer verwenden. Das
materielle Substrat ändert sich plötzlich zu Elektronen, Silizium und
Aluminium, aber das Berechnungssystem bleibt dennoch das Selbe wie
zuvor. Wir haben hier einen simulierten Abakus zur Verfügung.

Natürlich wurde der Abakus mit Hilfe einer modernen Programmiersprache
entwickelt, doch für den Endbenutzer spielen diese Zwischenstufen keine
Rolle. Auch interessiert ihn nicht, wie die Befehle der
Programmiersprache in Maschinensprache und diese in elektrische Impulse
im integrierten Schaltkreis abgebildet werden. Alles, was der Benutzer
möchte, ist, dass sich der Abakus so verhält, wie er es von ihm
erwartet, und dass er sein gewohntes Berechnungssystem verwenden kann.

Wenn wir also eine Berechnung durchführen, ist uns für die Ontologie
dieser Berechnung egal, ob sie in einem Taschenrechner, einem Abakus
oder im Kopf stattfand. Die Berechnung fand offensichtlich statt, und
ein Ergebnis liegt vor.

Kann man eine Berechnung simulieren? Der Gedanke ist unsinnig. Eine
Berechnung kann nicht simuliert werden – lediglich das Substrat und das
Berechnungssystem, der materielle Träger und die Art und Weise seiner
Verwendung, können sich unterscheiden, offensichtlich kann auch der
materielle Träger simuliert werden. Wir können mit einem virtuellen
Abakus oder Taschenrechner ebenso rechnen wie mit einem realen Abakus
oder Taschenrechner. Doch obwohl das materielle Substrat, in welchem die
Berechnung stattfindet, sich ändern kann, durch eine virtuelles Substrat
ersetzt werden kann, eben simuliert werden kann – die Berechnung selber,
der Weg von einem Problem zu einem Ergebnis, ist stets durchgeführt
worden, und nicht etwa nur simuliert.

Ein weniger abstraktes Beispiel: auch wenn *virtuelle Chatrooms* keine
realen sondern simulierte Räume sind, sind die dort durchgeführten
*Chats*, Gespräche, durchaus real und nicht simuliert.

Berechnungssysteme können andere Berechnungssysteme simulieren.

Turingmaschinen wurden nie wirklich gebaut, aber es existieren für viele
Computer Programme, die Turingmaschinen simulieren. Auch gibt es
sogenannte Emulatoren, welche auf einem Computersystem einen kompletten
Computer eines anderen Systems simuliert (dies kann zum Beispiel für das
Verwenden von älterer Software von Nutzen sein, die nicht auf aktuelle
Systeme portiert wurde).

Eine Turingmaschine korrekt zu simulieren ist ein pragmatischer Beweis
für die Turingvollständigkeit des simulierenden Berechnungssystems (da
ja die Turingmaschine turingvollständig ist, und somit zur Not ja alles
auf dieser simulierten Turingmaschine berechnet werden könnte, womit
auch das simulierende System turingvollständig sein muss).

Neuronale Netze werden natürlich auf Computern simuliert. Eine solche
Simulation erschließt uns die Möglichkeit, Neuronale Netze zu verwenden.
Für unsere Fragestellung ist das materielle Substrat und das
Berechnungssystem des Neuronalen Netzes irrelevant (für die tatsächliche
Anwendung hingegen ist es durchaus von Belang, da dadurch die
Geschwindigkeit bestimmt wird. Auch wenn ein Mensch, bewaffnet mit
Rechenschieber, Stift und (sehr, sehr viel) Papier durchaus prinzipiell
in der Lage ist, ein Neuronales Netz realistischer Größe durchzurechnen,
ist diese Berechnung bei einem Computer allein ob dessen Geschwindigkeit
besser aufgehoben).

Daraus ergibt sich, dass die eingangs aufgestellte Unterscheidung
zwischen tatsächlichen und simulierten Neuronalen Netzen hinfällig ist,
sondern lediglich eine, für den ontologischen Status irrelevante
Unterscheidung bezüglich des materiellen Substrats der Berechnung
vorliegt. Sprich: ob das Neuronale Netz sich in einem menschlichen Hirn,
einer Computersimulation oder in der Rechnung eines Menschen mit Stift
und Papier abspielt, ist für die Rechnung unwichtig.

### Überberechenbarkeit

Turing selber behandelte ab 1939 die Möglichkeit von **überberechenbaren
Funktionen** (*hypercomputability*, *super-Turing computation*), das
heißt, eine Klasse von Funktionen außerhalb der berechenbaren
Funktionen, die möglicherweise in der Physik vorkommen (insbesondere in
der Quantentheorie). Ein physikalisches System, in dem ein Quanteneffekt
stattfindet, wäre effektiv gesehen ein **Hypercomputer**.
Turingmaschinen und alle von ihr simulierbaren Berechnungssysteme
müssten vor solchen überberechenbaren Funktionen kapitulieren.

Vielleicht stellen Quantencomputer Überberechenbarkeit zur Verfügung
(die Forschung ist hier erst am Anfang). Auch Quantencomputer sind
turingvollständig – es stellt sich bloß die Frage, ob sie *mehr* sind.
Können sie neben den berechenbaren auch die überberechenbaren
Funktionen lösen? Bisher sind weder Quantencomputer noch sonstige
Hypercomputer in brauchbaren Maßstab realisiert worden, weswegen die
Frage vorerst offen bleibt.

Finden wir hier möglicherweise den Schlüssel zur Unterscheidung
Neuronaler Netze von einfachen Computern? Werden wir hier erkennen, dass
Neuronale Netze prinzipiell mehr können als ein Taschenrechner? Nein –
die mathematischen Modelle Neuronalen Netze, auf denen die
Computersimulationen beruhen, können mit überberechenbaren Funktionen
nicht umgehen: dies lässt sich dadurch beweisen, dass sie ja letzten
Endes auch auf einer Turingmaschine simuliert werden könnten, und somit
auch prinzipiell die Beschränkungen nicht aufbrechen können, denen das
zugrundeliegende System unterliegt.

Kurz zusammengefasst: mathematische Modelle Neuronaler Netze sind ein
turingvollständiges Lösungssystem – und auch nicht mehr.

-----

**John Lucas** und **Roger Penrose** schlugen vor, dass der menschliche
Geist womöglich ein Ergebnis der Überberechenbarkeit von
Quantenprozessen im menschlichen Körper ist. Doch selbst die
mikroskopisch kleinen Zellen des Menschen, oder die Teile des Gehirnes
wie Dendriten und Axonen, sind riesig im Vergleich zu den Maßstäben, die
in der Quantenphysik üblicherweise vorkommen. Dadurch wird diese
Hypothese unwahrscheinlich, wenn sie auch nicht ausgeschlossen werden
kann.

Allerdings darf man hier keine Rettung für den gebeutelten menschlichen
Geist durch Quanteneffekte erhoffen: wie **Peter Bieri** in *Das
Handwerk der Freiheit* zeigt, konstituiert Zufälligkeit keine Freiheit –
und um mehr als ein zufälliges, statistisches Element vermag die
Quantenphysik das klassischen mechanisch-deterministischen Weltbild
nicht zu ergänzen.

### Computer sind auch nur Menschen

Wie wir also gesehen haben, ist für den ontologischen Status Neuronaler
Netze das materielle Substrat nicht relevant. Eine Computersimulation
der Neuronalen Netze eines menschlichen Hirnes leistet, insofern sie
korrekt ist, dasselbe wie die Neuronalen Netze im menschlichen Hirn
selbst leisten. Folgt daraus also, dass eine Computersimulation einen
Menschen ersetzen kann, und das gar ohne an ontologischem Status
einzubüßen? Diese Computersimulation wäre also nicht einmal die
Simulation eines Menschen, nein, sie wäre all das, was den Menschen
ausmacht – sein Denken, sein Fühlen, seine Erinnerung, sein Charakter?

Die Schlüsse im letzten Absatz sind ebenso reißerisch wie nicht
zwingend. Sie beruhen auf einer handvoll Annahmen, die schlicht nicht
gegeben sind. Auf der Seite der Neuronalen Netze werden dabei die
Möglichkeiten, die ein Neuronales Netz angeblich besitzt, so weit
ausgedehnt, dass sie sich mit den gesamten Aufgaben des menschlichen
Hirnes decken. Auf der anderen Seite, der Seite auf welcher der Mensch
steht, wird der Mensch reduziert auf Denken, Fühlen, Erinnern und
Charakter, und das wiederum wird vollständig in dem biologischen Organ
Gehirn lokalisiert. Somit erscheint es, als ob Neuronale Netze die
Essenz dessen sind, was wir als Mensch bezeichnen. Hier wird urplötzlich
eine Antwort auf eine der grundlegenden Fragen der Philosophie gegeben:
Was ist der Mensch? – Ein Neuronales Netz.

Das ist natürlich falsch. Bei beiden scheinbar so naheliegenden
Bewegungen haben wir Fehler gemacht. Im folgenden werde beide Seiten
betrachtet. Zunächst zu der Aussage, ein Neuronales Netz könne
vollständig die Funktionsweise des Gehirns nachvollziehen. Allein aus
biologischer Notwendigkeit ist das natürlich nicht der Fall: neben den
Neuronenzellen besteht das Hirn auch aus Gliazellen, welche die
Neuronenzellen unterstützen und ernähren. Der Sauerstoffzufuhr durch
Blut muss gewährleistet werden. Dieser biologisch notwendige Mechanismus
wird in den mathematischen Modellen Neuronaler Netze nicht
berücksichtigt.

Der Hypothalamus oder die von Descartes so geschätzte Zirbeldrüse
erzeugen Hormone, welche widerum für die Zustandsänderung des Körpers
zuständig sind. Natürlich können wir diese Teile des Gehirns als nicht
zum Gehirn zugehörig definieren, um so unsere These zu retten, dass das
Gehirn nur ein Neuronales Netz ist – doch damit verwandeln wir diese
These zur Nullaussage, weil wir das Neuronale Netz des Gehirns als
Gehirn definieren.

Schließlich ist natürlich noch anzumerken, dass das Gehirn sich in
seiner Entwicklung sehr von einem Neuronalen Netz unterscheidet. Große
Teile des Gehirnes sind bereits genetisch mit bestimmten Aufgaben
versehen. Bei einem „reinen“ Neuronalen Netz gehen wir davon aus, dass
seine gesamte Organisation autonom entstanden ist. Ein guter Teil des
Aufbaus eines menschlichen Gehirnes ist jedoch bereits vorherbestimmt.
Föten entwickeln Seh- und Sprachzentren, obwohl sie natürlich weder
allzuviel gesehen, geschweige denn einen angenehmen Plausch gehabt haben
können. Die Abbildung genetischer Informationen auf die Grobstruktur des
Gehirnes, sowie dessen danach noch beobachtbare, verblüffend große
Dynamik sind Gegenstand der Forschung und werden sicher noch viele
erstaunliche Ergebnisse hervorbringen. Für unsere Diskussion relevant
ist, dass der Mensch offensichtlich nicht als unbeschriebenes Blatt auf
die Welt kommt, sondern dass ein unbekannt großer Anteil seines Gehirnes
bereits genetisch prädestiniert ist (vergleiche hierzu auch **Steven
Pinker**, *Das unbeschriebene Blatt*).

Die Aufteilung des Gehirnes spricht ebenfalls gegen eine einfache
Beschreibung des Gehirnes als Neuronales Netz: die Neuronen des
Sehzentrums sind auf die Verarbeitung visueller Reize spezialisiert; der
Kortex kann hervorragend Informationen speichern, abrufen, den Zustand
anderer Neuronen abbilden und darüber reflektieren; motorische Neuronen
unterscheiden sich von den körperbeobachtenden Neuronen des limbischen
Systems.

Das alles sollte hinreichend gezeigt haben, dass die derzeitigen, allzu
vereinfachenden mathematischen Modelle Neuronaler Netze keineswegs
alleine die Funktion des Gehirnes abbilden können. Allein um das zu
erreichen, muss noch sehr viel in die Erforschung der Arbeitsweise und
der Entwicklung des Gehirnes investiert werden, es ist, im Gegensatz zu
Kurzweils Annahme, nicht einfach eine Frage der Rechengeschwindigkeit.

Auf der anderen Seite stand die Behauptung, der Mensch sei auf die
Funktionen des Organs Gehirn reduzierbar. Auch dies ist falsch.
Natürlich ist zum Menschsein der Körper relevant, und das nicht nur als
lebenserhaltende und mobile Hülle für das Gehirn.

Das vielleicht einsichtigste Beispiel bietet die Welt der Gefühle.
Gefühle gehören zum Menschsein dazu – Liebe, Hass, Angst. Antonio
Damasio beschreibt aber das Entstehen von Gefühlen dadurch, dass das
limbische System die Körperfunktionen überwacht. Er unterscheidet dabei
strikt Gefühle von Emotionen: Emotionen sind messbare Zustände unseres
Körpers, etwa erhöhte Herzfrequenz, erweiterte Pupillen, aufgerichtete
Haare. Das limbische System misst diese Körperfunktionen, und das
widerum wird vom Gehirn als ein Gefühl interpretiert. Kurz gesagt:
Gefühle entstehen aus dem Zusammenspiel des gesamten Körpers. Und da
Menschen Gefühle als Teil ihres Menschsseins betrachten, kann die
Reduktion auf das Gehirn offensichtlich nicht sinnvoll sein.

Ein geläufiges Beispiel für den Einfluss des Körpers auf den Menschen
mag das Kastrieren von Männern sein. Durch die stark gesenkte
Testosteronproduktion sinken Libido und Aggresivität. Selbst wenn wir
also das Gehirn eines Menschen durch ein Neuronales Netz nachbilden
würden, würde sich das Ergebnis von dem nachgebildeten Menschen stark
unterscheiden, da der Einfluss des Körpers hierbei nicht mit
nachgebildet wird.

Der Mensch ist nicht nur durch die Funktionalität seines Gehirnes
definiert. Wie gezeigt wurde, spielt auch der restliche Körper für den
Menschen eine relevante Rolle. Und, wie wir zuvor schon gezeigt haben,
sind Neuronale Netze nicht einmal in der Lage, das Gehirn alleine
nachzubilden. Menschen sind somit nicht auf Neuronale Netze reduzierbar,
unabhängig davon, wie viele Ängste (vor gefühllosen Superintelligenzen,
welche die Menschheit überflüssig machen) oder Hoffnungen (auf
Unsterblichkeit, wie bei Ray Kurzweil) mit dieser These verbunden
werden.

### Einschränkung

Aus der bereits dargelegten Turingvollständigkeit Neuronaler Netze
erwachsen mehrere Konsequenzen, insbesondere: weiter oben wurde
ausgeführt, dass das Gehirn in seiner Funktionalität nicht durch ein
Neuronales Netz dargestellt werden kann. Dies ist so nicht korrekt: die
Turingvollständigkeit erlaubt es, auch in einem Neuronalen Netz ein
System zu programmieren, dass die restlichen Funktionen des Gehirns,
oder auch des gesamten menschlichen Körpers simuliert, insofern diese
nicht überberechnbar sind. Dies ist hier lediglich der Vollständigkeit
halber erwähnt, denn pragmatisch sinnvoll wäre eine solche
Vorgehensweise nicht. Einfachere Systeme, wie etwa die
Melatoninregulierende Zirbeldrüse können mit deutlich einfacheren
Subsystemen dargestellt werden.

### Modell und Vorbild

Hierbei wird jedoch stillschweigend von einer nicht trivialen
Voraussetzung ausgegangen: die mathematischen Modelle von Neuronalen
Netzen geben die biologischen Neuronale Netze korrekt wieder. Betrachtet
man aber die mathematischen Modelle, wie sie in etwa bei Klaus Mainzer
dargestellt werden, und stellt sie der Beschreibung gegenüber, die etwa
Eric Kandel über die Funktionsweise des Gedächtnisses auf molekularer
Ebene angefertigt hat, und für diese er den Nobelpreis erhielt, so
erkennen wir, dass viele Elemente, die in biologischen Neuronalen Netzen
enthalten sind, überhaupt nicht abgebildet werden. Natürlich,
mathematische Neuronale Netze sind offensichtlich von den biologischen
inspiriert, doch um der Einfachheit Willen wird von zahlreichen Teilen
abstrahiert – und bei jeder solcher Abstraktion muss man die Frage
untersuchen, ob damit ein essenzieller oder doch nur ein akzidentieller
Bestandteil aus dem Modell entfernt wurde.

Diese letzte Frage ist nicht trivial: verschiedene Modelle können für
verschiedene Zwecke sinnvoll sein. In diesem Zusammenhang bedeutet dies:
ob ein abstrahiertes Element Neuronaler Netze für eine bestimmte
Fragestellung essenziell ist, hängt nicht von den Neuronalen Netzen ab
sondern allein von der Fragestellung. Möchte ein Hirnforscher
herausfinden, wie die Synapsenneubildung und das Langzeitgedächtnis
funktionieren, wird er ein anderes Neuronenmodell hernehmen müssen als
ein Informatiker, der die Aufgabe hat, ein Neuronales Netzes für das
Erkennen von Gesichtern zu trainieren.

Wir müssen also unsere Fragestellung kennen, um die Frage nach dem
passendem Modell beantworten zu können. Wie aber lautet unsere Frage?
Der ontologische Status Neuronaler Netze. Was aber ist hierfür relevant?
Nun, genau davon handelt die Frage. Kurz: uns bleibt nichts anderes
übrig, als bei der Abstrahierung extrem vorsichtig zu sein.

Sind wir das? Betrachten wir Eric Kandels Arbeit über die Arbeitsweise
des Gedächtnisses: stark vereinfacht gesagt, wirkt das
Kurzzeitgedächtnis durch das Nachklingen abgefeuerter Synapsen, der
Zustand der Synapsen wird also kurzfristig verändert. Das
Langzeitgedächtnis hingegen basiert allein auf dem Entstehen neuer
Verbindungen zwischen den Neuronen.

Diese beiden Mechanismen funktionieren also sehr unterschiedlich.
Dennoch gehen mathematische Modelle nicht einmal auf diesen sehr groben
Unterschied ein, sondern verwenden ein Lösung, die sich irgendwie
zwischen den beiden Mechansimen finden lässt. Natürlich, socherart
gestalteten Neuronalen Netze erfüllen ihre Aufgabe in der
Mustererkennung, als Assoziationsmaschine oder bei der Suche nach dem
besten Schachzug – doch das ist hier gar nicht die Frage. Die Frage ist
vielmehr: inwiefern können wir eben diese mathematischen Modelle als
Abbildungen der biologischen Neuronalen Aktivitäten betrachten?

Mathematische Modelle Neuronaler Netze, wie wir sie heute verwenden,
wurden nicht mit diesem Ziel entworfen. Deswegen darf es nicht
überraschen, wenn sie sich dafür als nicht geeignet erweisen. Kurzweils
Berechnungen aber basieren auf eben dieser Prämisse. Ein weiterer Beleg
gegen Kurzweil? Wenn, dann nur was die Jahreszahlen anbelangt. Der
rasante Wissenszuwachs gerade der 1990er Jahre, des Jahrzehnt des
Gehirns, lässt vermuten, dass innerhalb der nächsten Jahrzehnte die
grundlegende Funktionsweise biologischer Neuronen entschlüsselt sein
wird. Selbst wenn es sich dabei ergeben sollte, dass die Biologie in
diesem Bereich um das zehn- oder hundertfache komplexer sein sollte als
bislang angenommen, bedeutet dies ob des durch Moores Gesetz
postulierten exponentiellen Wachstums verfügbarer Rechenkraft nur
Probleme mit aufschiebender Wirkung, nicht aber prinzipielle
Unlösbarkeit.

### Einschub: ein kleiner Wurm

Neuronale Netze haben sich als ein turingvollständiges Berechnungssystem
erwiesen, und es scheint hierbei irrelevant zu sein, ob es sich dabei um
tatsächliche, biologische Neuronale Netze handelt, oder um mathematische
Modelle. Trotz der vorgebrachten Argumente könnte dies ein schwer zu
akzeptierender Punkt sein. Biologische Neuronale Netze, die müssen doch
was besonderes sein\! Schließlich basiert unser Denken darauf. All die
Begriffe wie Erleben, Erinnerung, Denken, Entscheiden, Glauben,
Reflektieren – all das basiert doch auf diesen biologischen Neuronalen
Netzen.

Ein Argument gegen die Besonderheit biologischer Neuronaler Netze trägt
den unaussprechlichen Namen *Caenorhabditis elegans* und ist ein Wurm.
Dieser Wurm hat etwa 18000 Gene, und jedes Exemplar dieses Wurmes hat
exakt 959 Zellen. Und selbst dieses so einfache Lebewesen besitzt ein
Neuronales Netz, bestehend aus exakt 302 Neuronen, deren Schaltplan
starr im Genom festgehalten ist. Diese wenigen Fakten führen zu einer
überraschen großen Zahl von Konsequenzen, von denen einige hier kurz
dargestellt werden.

Erstens. Das Genom kann Informationen darüber enthalten, wie Neuronale
Netze verdrahtet sind. Das bedeutet, das Gehirn auch des Menschen kann
in Teilen schon genetisch bedingt fest verdrahtet sein. Die Prämisse
einer *Tabula Rasa*, von der Informatiker bei den mathematischen
Modellen Neuronaler Netze ausgehen, ist nicht notwendig gegeben – und
das nicht nur in der Grobstruktur Neuronaler Netze, sondern bis hinab in
die einzelnen Synapsen\!

Zweitens. Es gibt biologische Neuronale Netze, die in ihrer
Lösungsfähigkeit allgemeiner Probleme mathematischen Modellen stark
unterliegen. Das Neuronale Netz des C. elegans ist bei weitem nicht so
lernfähig und trainierbar wie einfache simulierte Neuronale Netze.
Offensichtlich ist die biologische Grundlage kein Zeichen von Qualität.

Drittens. Nervensysteme sind Organe wie alle anderen auch. Trotz der
Anwesenheit eines Neuronalen Netzes wird niemand dem C. elegans
Intelligenz oder Selbstbewusstsein im klassischen Sinne unterstellen. Um
Konstrukte wie 'Ich' oder 'Schmerz' überhaupt darstellen zu können, ist
das Neuronale Netz des C. elegans nicht komplex genug und zudem zu sehr
mit der ihm eigentlich von der Evolution angedachten Aufgabe der
Sinnesdatenverarbeitung beschäftigt.

Viertens. Es ist wahrscheinlich, dass die Evolution die Grundlagen für
diverse Neuronale Aufgaben in unseren Genen bereits festgehalten hat.
Das dürfte von so einfachen Aufgaben wie der Überspielung des Blinden
Flecks in unserem Sichtfeld reichen bis hin zu hochkomplexen Aufgaben
wie der Ich-Konstruktion und den Grundregeln von Sprache. Dies wäre eine
Erklärung für den außerordentlich schnellen Spracherwerb von Kindern und
ihr verblüffendes Verständnis des Konzepts 'Ich'.

### Der ontologische Status einer Zahnfüllung

Ändert sich am ontologischen Status eines Menschen irgendetwas, wenn er
eine Zahnfüllung erhält? Ändert sich etwas am ontologischen Status der
Zahnfüllung?

Die erste Frage können wir bedenkenlos verneinen. Die zweite Frage
hingegen ist komplizierter: der Mensch, der die Zahnfüllung betrachtet,
wird diese als ein Teil von sich selber vereinnahmen, zumindest solange
sie nicht auffällig wird. Sie wird zu einem Teil von ihm und verliert
den Status eines außenstehenden Objekts.

Sollte die Zahnfüllung jedoch Schwierigkeiten bereiten, etwa Schmerzen
verursachen, wird sie jedoch vom Menschen wieder externalisiert. Dies
ist jedoch auch bei biologischen Organen des Menschen zu beobachten: nur
bei Schwierigkeiten spricht man davon, dass *„die Hand schmerzt“* oder
*„das Herz will nicht mehr“*. Dies gilt auch für das Gehirn. Da das
Gehirn selber jedoch aufgrund mangelnder Sensoren keine Schmerzen
empfinden kann, sind hier alle Störungen psychisch, zum Beispiel *„das
Gehirn gaukelt vor“*. Wem schmerzt die Hand, wem gaukelt das Gehirn
etwas vor? Der jeweiligen Person. Im Fall von Problemen trennt sich
sonst vereintes plötzlich.

Wir hatten das Beispiel der Zahnfüllung. Wie sieht es mit komplexeren
Prothesen aus? Künstlichen Haaren? Beinen? Händen? Ein künstliches Herz?
Oder gar transplantierte Organe? Auch hier gilt: solange es keine
Schwierigkeiten gibt, sind sie Teil der Person. „Er hat mich berührt“
ist eine vollkommen als adäquat akzeptierte Aussage, selbst wenn
eigentlich die Beinprothese berührt wurde.

Theodore Berger von der University of Southern California gelang es,
Nervenzellen mit Chips zu verbinden und miteinander kommunizieren zu
lassen. Sein Fernziel ist es, etwa Alzheimererkrankten Prothesen zu
implantieren, die das restliche Gehirn als Gedächtnis verwenden kann.
Natürlich sei dem Forscher bewusst, dass die Chips keine echten Neuronen
ersetzen kann, aber *„so grob das Implantat auch sein mag, für das Hirn
ist das gewiss besser als nichts.“* Insofern das kühne Unterfangen
Bergers gelingen sollte, wird es spannend zu beobachten sein, inwiefern
sich die Personen durch das Implantat künstlicher Neuronaler Netze
verändern, aber ich wage die Voraussage, dass es sich strukturell wie
bei allen oben aufgeführten Prothesen verhalten wird: sofern alles
funktioniert, wird das Implantat als Teil der Person betrachtet. Der
ontologische Status des Implantatsträgers hingegen bleibt von dem
Implantat unberührt. Dem Menschen wird egal sein, wie die Funktion der
Neuronalen Netze erfüllt wird.

### Ergebnis

Betrachten wir zusammenfassend die Schlüsse, zu denen wir gekommen sind:

Die Neuronalen Netze, die wir von Natur aus haben, erfüllen innerhalb
des menschlichen Organismus ihre Aufgaben: Daten von unseren Sinnen und
von den eigenen Organen entgegenzunehmen und zu verarbeiten und daraus
unsere Realität zu konstruieren. Diese Funktion ist eine notwendige
Bedingung für das Mensch-sein. Die genaue Art und Weise der Erfüllung
dieser Funktion ist jedoch, und dies sollte dieser Beitrag klar gemacht
haben, irrelevant.

Antonio Damasio stellt klar, dass das Feuern von Synapsen nicht
neuronales Korrelat von Gedanken ist, auch nicht die Repräsentation
eines Gedankens – es ist der Gedanke. Dies ist notwendig und
einleuchtend, wenn wir das Denken nicht außerphysikalischen Geistern und
Seelen überlassen wollen, die dann in irgendeiner Weise mit unseren
physikalischen, körperlichen Hüllen interagieren.

Dadurch werden biologische Neuronale Netze zum Substrat des Denkens.

Der Dualismus von Körper und Geist ist dadurch hinfällig und höchstens
noch als Modell sinnvoll. Das Verschwinden dieses Dualismus bedeutet
aber, dass wir die Neuronalen Netze unseres Gehirns nur als ein
turingvollständiges Berechnungssystem betrachten dürfen. Davon
ausgehend, dass die biologischen Neuronalen Netze des Menschen nicht
überberechnend sind, sind sie prinzipiell durch andere
turingvollständige Berechnungssysteme und andere Substrate ersetzbar.

Der Schluss, dass der Mensch durch den Computer ersetzt werden kann,
wurde jedoch widerlegt. Der Mensch ist mehr als seine Neuronalen Netze.
Zwar werden auch in Zukunft immer mehr Arbeitsplätze, die bisher von
Menschen wahrgenommen wurden, Computern übergeben, doch hier von einer
Ersetzung des Menschen durch den Computer zu sprechen, würde bedeuten,
den Menschen über seine Arbeit zu definieren.

Intelligenz oder Vernunft, soweit auf Berechenbarkeit reduzierbar, ist
nicht dem Menschen vorbehalten, und kann somit auch nicht mehr als
alleiniges Merkmal der Spezies *Sapiens* hergenommen werden. Wieder wird
eine der Grundfragen der Philosophie aufgeworfen.

*Was ist der Mensch?*

### Quellen

  - **Brooks, Rodney** (2002), *Menschmaschinen – Wie uns die
    Zukunftstechnologien neu erschaffen* (*Flesh and Machines*), Campus
    Verlag, Frankfurt, New York
  - **Church, Alonzo** (1936), *A Note on the Entscheidungsproblem*.
    Journal of Symbolic Logic, 1, S. 40-41.
  - **Cruse, Holk**; **Dean, Jeffrey** und **Ritter, Helge** (1998),
    *Die Entdeckung der Intelligenz oder Können Ameisen denken?*, C.H.
    Beck, München
  - **Damasio, Antonio** (2001), *Wie das Gehirn Geist erzeugt*, in
    Spektrum der Wissenschaft – Digest: Rätsel Gehirn, S. 6-11
  - **Dworschak, Manfred** (2003), *Denken auf Krücken*, in Spiegel
    Spezial 4/2003, S. 138-140
  - **Kandel, Eric**; **Grolle, Johann** und **Traufetter, Gerald**
    (2003), *„Hirne verändern sich“* - *Interview mit Eric Kandel*, in
    Spiegel Special 4/2003, S. 72-75
  - **Kurzweil, Ray** (1999), *Homo s@piens, Leben im 21. Jahrhundert –
    Was bleibt vom Menschen?* (*The Age of Spiritual Machines*), Viking
    Press, London
  - **Mainzer, Klaus** (1995), *Computer – Neue Flügel des Geistes? Die
    Evolution computergestützter Technik*, Wissenschaft, Kultur und
    Philosophie, de Gruyter, Berlin, New York
  - **Mainzer, Klaus** (2004), *Im Zeitalter der denkenden Maschinen*,
    in Technology Review 2/2004, S. 100-104
  - **Minsky, Marvin** und **Papert, Seymour** (1969), *Perceptrons*,
    Cambridge, MA: MIT Press
  - **Pinker, Steven** (2002), *Das unbeschriebene Blatt – Die moderne
    Leugnung der menschlichen Natur* (*The Blank Slate. The Modern
    Denial of Human Nature*), Berlin Verlag, Berlin/Viking Penguin, New
    York
  - **Rosenblatt, Frank** (1958), *The Perceptron: A Probabilistic Model
    for Information Storage and Organization in the Brain*, Cornell
    Aeronautical Laboratory, Psychological Review, v65, No. 6, pp.
    386-408.
  - **Turing, Alan** (1936), *On Computable Numbers, with an Application
    to the Entscheidungsproblem.* Proceedings of the London Mathematical
    Society, Series 2, 42 (1936-37), S. 230-265
  - **Zimmerli, Walter** und **Wolf, Peter** (Hg.) (1994), *Künstliche
    Intelligenz – Philosophische Probleme*, Reclam, Stuttgart

-----

*Dies ist eine Hausarbeit die ich in meinem Philosophie-Studium schrieb.
Das wird Anfang 2004 gewesen sein. Die älteste Archivierung durch das
Internet Archive ist vom 19. März 2004.*

Spätere Anmerkungen (2026) (was nicht heißt, dass der Rest keine
Anmerkungen braucht, aber nur ein paar hier):

  - Die Aussage *"Die mathematischen Modelle von Neuronalen Netzen sind
    turingvollständige Lösungssysteme."* ist etwas zu stark: nur
    bestimmte Architekturen von Neuronal Netzen sind turingvollständig
    (z.B. wenn sie rekurrierend sind und sie Zugriff auf einen Speicher
    haben). Das macht aber für die Argumentation hier keinen
    Unterschied. Wieviel das Argument selbst trägt, ist jedoch eine
    andere Frage.
  - Die Aussage *"um mehr als ein zufälliges, statistisches Element
    vermag die Quantenphysik das klassischen
    mechanisch-deterministischen Weltbild nicht zu ergänzen."* würde ich
    heute nicht mehr unterschreiben. Quantenphysik scheint viel schräger
    als einfach nur Zufall zu sein, und dementsprechend ist es unklar,
    was Quantenphysik beitragen kann. Vielleicht hatten Lucas und
    Penrose doch Recht, was ich davor ablehnte. Ich halte es immer noch
    für unwahrscheinlich, aber für möglich. Dies kann die Argumentation
    gefährden, beruht aber auf der Natur der Quantenphysik.
  - *...die chemischen und physikalischen Vorgänge in den Neuronen
    geschehen unabhängig voneinander und insbesondere auch unabhängig
    von einer zentralen Recheneinheit, so dass man hier massiv parallel
    vorgehen und in wesentlich kürzerer Zeit zu einem Ergebnis kommen
    kann. Dadurch sind biologische Neuronale Netze den simulierten um
    Größenordnungen im Vorteil.*. Das hat sich natürlich inzwischen
    durch massiv-parallele Rechner- und Chiparchitekturen erübrigt.
  - *Im Fall von Problemen trennt sich sonst vereintes plötzlich.*
    Autsch.
