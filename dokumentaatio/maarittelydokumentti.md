# Määrittelydokumentti

Tietorakenteet ja algoritmit-laboratiokurssi <br>

Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti <br>
Ohjelmointikieli: Python <br>
Dokumentaation kieli: Suomi <br>

## Aihe: 
Kurssityöksi aion toteuttaa tekstigeneraattorin, joka luo suomenkielisiä horoskooppiennustuksia. 
Aion toteuttaa ohjelman Markovin ketjun ja Trie-tietorakenteen avulla. Valitsin nämä siksi, että ne ovat yleisesti käytettyjä tapoja toteuttaa tekstigeneraattori. 

## Syöte: 
Ohjelma saa syötteeksi oikeita horoskooppitekstejä. Ohjelma tutkii mitkä sanat esiintyvät useimmin peräkkäin ja sen perusteella muodostaa uusia horoskooppitekstejä. Tarkemmin ohjelma sijoittaa alkuperäisessä tekstissä ilmaantuvat sanat trie-rakenteeseen ja sitten Markovin ketjun avulla valitsee  aina seuraavan sanan lauseeseen. 

## Aika- ja tilavaativuus:

Ohjelman aikavaativuus olisi O(m), missä m on lauseiden pituus ts. käytettävien sanojen määrä. 

## Lähteet:
Opetusaineisto koostettu [Ilta-Sanomat, Me Naiset, 21.6. - 27.7.2021](https://www.is.fi/menaiset/horoskooppi/) 

