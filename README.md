# MatrixWebCam
## Preview
![Demo](assets/output.gif)

Webcam ASCII Renderer — applicazione Python che cattura il video dalla webcam e lo converte in output ASCII in tempo reale.

## Requisiti Minimi
Python 3.10+
WebCam funzionante
Terminale font monospaziato

## Teconologie utilizzate
python3
opencv-python

## Funzionalita'
Cattura video in tempo reale Converte i Frame in ASCII con rendering fluido da terminale supporto a diverse risoluzioni

## Come Funziona
Legge il frame con OpenCV, converte i pixel in scala di grigi Mappa i valori a una lista di caratteri ASCII Stampa il risultato sul terminale

## Installazione
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements
```


## Utilizzo

```bash
python3 livecapture.py
```
per uscire dal programma premere Ctrl + C
