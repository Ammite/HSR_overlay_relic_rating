# HSR_overlay_relic_rating

## Info

### Project idea

Project should use overlay interface in game to rate relics based on **relic set**, **slot**, **main stat** and **sub stats**. 

Project uses [pytesseract](https://pypi.org/project/pytesseract/) (python lib to analyze text on image) and [mss](https://pypi.org/project/mss/) (python lib to get screenshot)

### Points
- Хочется рейтинг прописывать, что-то около S, A, B, M, где М - это "Мусор". 
- Возможно стоит указывать для какого архетипа этот релик хорош
- Может указывать каким персонажам он подходит в виде развернутого ответа по кнопке. 
- Отсюда можно формулу взять https://www.mobilemeta.gg/honkai-starrail/guide/relic-scorer-guide

## Installation

### Requirements
- Python 3.12.3
- requirements.txt for python libs
- Install [tesseract](https://github.com/tesseract-ocr/tesseract)

## Usage
...


## TODO: 
* Написать настройки для тессеракта, чтобы он правильно принимал все данные и обрабатывал их
* Написать оверлей для отображения рейтинга релика