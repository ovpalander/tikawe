# Talonaattori - taloyhtiön hallintasovellus

## Sovelluksen ominaisuudet

## 1. Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen
* Käyttäjätilejä on kahdenlaisia:
    * Asukas / osakas (normaalikäyttäjä).
    * Ylläpitäjä (esim. hallituksen jäsen tai isännöitsijä).

## 2. Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan tietokohteita
* Pääasialliset tietokohteet:
    * Taloyhtiö (hallinnollinen kokonaisuus).
    * Asunnot (taloyhtiön sisällä olevat yksiköt).
    * Osakkaat (taloyhtiön asukkaat eli sovelluksen käyttäjät)
* Käyttäjä voi lisätä oman asuntonsa tietoihin lisäyksiä (esim. remontti-ilmoitus).
* Ylläpitäjä voi luoda ja muokata taloyhtiön tietoja (osoite, yhteystiedot, yhtiöjärjestys, taloyhtiön dokumentit).

## 3. Käyttäjä näkee sovellukseen lisätyt tietokohteet
* Jokainen käyttäjä voi selata:
    * Taloyhtiön tiedot (yleiset dokumentit [yhtiöjärjestys, rakennusvuosi, y-tunnus, tilinpäätökset, pöytäkirjat], hallituksen tiedotteet).
    * Omat asuntonsa tiedot (esim. huoneiston numero, pinta-ala, osakenumerot).
* Lisäksi voidaan näyttää muiden käyttäjien julkiset lisäykset (esim. tiedotteet, ilmoitukset)

## 4. Käyttäjä pystyy etsimään tietokohteita hakusanalla tai muulla perusteella
* Hakutoiminto:
    * Haku taloyhtiön nimellä (jos käyttäjä kuuluu useampaan).
    * Haku asuntojen perusteella (asunnon numero, osoite, osakenumerot).
* Haku dokumenteista tai ilmoituksista.

## 5. Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät tietokohteet
* Käyttäjäprofiilissa näkyy:
    * Mihin taloyhtiöön käyttäjä kuuluu.
    * Mitä asuntoja käyttäjä hallinnoi.
* Käyttäjän tekemät ilmoitukset / lisäykset.
* Tilastot (esim. montako ilmoitusta tehty, viimeisin aktiivisuus).

## 6. Käyttäjä pystyy valitsemaan tietokohteelle luokittelun
* Tietokohteilla (käyttäjä, taloyhtiö, asunto, ilmoitus) voi olla luokkia, esim.:
    * Käyttäjien luokat: asukas/osakas, hallituksen jäsen tai isännöitsijä.
    * Asuntojen luokat: huoneistotyyppi (1h, 2h, 3h…).
    * Ilmoitusten luokat: huolto, remontti, yleinen tiedote.
* Luokat tallennetaan tietokantaan ja niitä voi suodattaa haussa.

## 7. Toissijaiset tietokohteet täydentävät pääasiallisia tietokohteita
* Pääkohteena asunto.
    * Toissijainen kohde voi olla esim. autopaikka
* Pääkohteena on taloyhtiö.
    * Toissijainen kohde voi olla esim. asunto, yhtiökokouspöytäkirja, taloyhtiön sääntö, yhteiset tilat.
* Käyttäjä voi lisätä toissijaisia kohteita myös muiden kohteisiin (esim. hallitus lisää taloyhtiön dokumentteja tai isännöitsijä lisää asunnon huoltokirjaan tietoja).

