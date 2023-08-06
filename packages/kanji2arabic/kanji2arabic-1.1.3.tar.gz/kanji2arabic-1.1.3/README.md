# kanji2arabic_number

Convert Kanji numerals to Arabic numerals.

powerd by [Interman co., ltd](https://interman.jp/)

[GitHub](https://github.com/interman-corp/kanji2arabic)

## Demo

```python
from kanji2arabic import Kanji2Arabic

print(Kanji2Arabic.kanji2arabic("一二三"))
  # "123"

print(Kanji2Arabic.kanji2arabic("百二十三"))
  # "123"

print(Kanji2Arabic.kanji2arabic("二〇二〇"))
  # "2020"

print(Kanji2Arabic.arabic2kanji("1230456"))
  # "一二三〇四五六"

```

## Requirements

kanjize 1.3.0
