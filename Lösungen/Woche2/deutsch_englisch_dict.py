#!/usr/bin/python
#encoding=utf-8

englisch_deutsch_dict = {"hello": "hallo", "world": "welt", "good bye": "auf wiedersehen"}
deutsch_englisch_dict = dict()

for key, value in englisch_deutsch_dict.items():
    deutsch_englisch_dict[value] = key
    
print deutsch_englisch_dict
