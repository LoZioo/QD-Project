# QD-Project
Repository progetto per materia Quality Developement.

## Table of Contents
- [Introduzione](#introduzione)
- [Cenni di teoria](#cenni-di-teoria)
  * [Definizione di ASFD](#definizione-di-asfd)
  * [Linguaggio formale](#linguaggio-formale)
  * [Linguaggio denotato da un ASFD](#linguaggio-denotato-da-un-asfd)
  * [Stringa accettata da un ASFD](#stringa-accettata-da-un-asfd)
  * [Computazione di una stringa da parte di un ASFD](#computazione-di-una-stringa-da-parte-di-un-asfd)
  * [Osservazioni sulla funzione di transizione](#osservazioni-sulla-funzione-di-transizione)
- [Risorse aggiuntive](#risorse-aggiuntive)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Introduzione
Si vuole realizzare un software in Python che implementi un riconoscitore a stati finiti deterministico (ASFD):
-	Dato un certo file `XML`, si ricavi un ASFD $m$ (Automa a Stati Finiti Deterministico) rappresentato tramite un grafo diretto.
-	Che prenda in input un arbitrario numero di stringhe $x$.
-	Per ognuna delle suddette stringhe, tale script dovrà ritornare il risultato della computazione su $m$ della suddetta stringa $x$, dove con risultato della computazione si intende uno dei due seguenti risultati:
	-	L'ASFD $m$ accetta la stringa $x$.
	-	L'ASFD $m$ non accetta la stringa $x$.

## Cenni di teoria
### Definizione di ASFD
Un ASFD è una quintupla: $$m=(\Sigma,Q,\delta,q_0,F)$$
Dove:
-	$\Sigma= \\{ a_0,a_1,...,a_n \\}$ è l'alfabeto su cui lavora $m$.
-	$Q=\\{q_0,q_1,...,q_k\\}$ è l'insieme degli stati (nodi) di $m$.
-	$\delta:(Q\times\Sigma)\rightarrow Q$ è la funzione di transizione **totale** tra stati o alternativamente, la rappresentazione della matrice di adiacenza relativa al grafo grafo $m$.
-	$q_0\in Q$ è lo stato iniziale di $m$.
-	$F\subseteq Q$ è l'insieme degli stati **finali** di $m$.

### Linguaggio formale
Sia ${L\subseteq\Sigma^* }$ finito, un linguaggio formale.
Tale linguaggio è formato da un sottinsieme finito di tutte le possibili stringhe su $\Sigma$ a loro volta denotate con la notazione $\Sigma^*$.

### Linguaggio denotato da un ASFD
Sia $L(m)$ il linguaggio denotato dall'ASFD $m$.
Tale linguaggio è composto da tutte e sole le stringhe accettate da $m$: $$L(m)=\\{x\in\Sigma^*\ |\ m\ accetta\ x\\}$$

### Stringa accettata da un ASFD
Sia ${x\in\Sigma^*}$ una stringa ed $m$ un ASFD, allora:
$$m\ accetta\ x\leftrightarrow s_{|x|}\in F$$

Alternativamente, $x$ è accettata da $m$ se e solo se la computazione di $m$ sulla stringa $x$ termina in uno stato $s_{|x|}$ appartenente all'insieme degli stati finali $F$.

### Computazione di una stringa da parte di un ASFD
Sia ${x\in\Sigma^*}$ una stringa, $m$ un ASFD e $||$ l'operatore di concatenazione tra stringhe.  
La computazione della stringa $x$ su $m$ è denotata dalla seguente procedura:

$Evaluate_m(x)$:  
&emsp;let $n=|x|$  
&emsp;let $x\leftarrow a_1||a_2||...||a_n$  
&emsp;let $q\leftarrow q_0$  

&emsp;for $i$ = 1 to $n$ do:  
&emsp;&emsp; $q=\delta(q,a_i)$  

&emsp;if $q\in F$ then return $1$  
&emsp;else return $0$  

### Osservazioni sulla funzione di transizione
La funzione di transizione $\delta:(Q\times\Sigma)\rightarrow Q$ di un ASF **Deterministico** è totale, cioè:
$$\delta(q,a)\in Q, \forall q\in Q, \forall a\in \Sigma$$

Alternativamente, per ogni coppia di stato e carattere di transizione, deve sempre esistere sempre un arco per cui transitare.

La funzione $\delta$ è quindi sempre definita su tutto il suo dominio.

## Risorse aggiuntive
-	[TOC generator](http://ecotrust-canada.github.io/markdown-toc/)
-	[Graph Online](https://graphonline.ru/en/)

## Utilizzo e test del codice
Il codice può essere testato in locale tramite lo script [test.sh](test.sh).  
Questo script provvede ad eseguire quasi gli stessi comandi di test previsti nella pipeline di GitHub, eseguilo quindi sempre prima di eseguire il push del tuo codice nella repository (`git push`): in questo modo non romperai la pipeline!
