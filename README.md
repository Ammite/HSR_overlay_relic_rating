# HSR_overlay_relic_rating

## Info

### Project idea

    Project should use overlay interface in game to rate relics based on Set, Slot, Main stat and Sub stats. Project uses <a href="https://pypi.org/project/pytesseract/">pytesseract</a> (python lib to analyze text on image) and <a href="https://pypi.org/project/mss/">mss</a> (python lib to get screenshot)

### Points
- Хочется рейтинг прописывать, что-то около S, A, B, M, где М - это "Мусор". 
- Возможно стоит указывать для какого архетипа этот релик хорош
- Может указывать каким персонажам он подходит в виде развернутого ответа по кнопке. 

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