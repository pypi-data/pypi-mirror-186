<h1 style="text-align: center"> langSrc </h1>

## Install

```shell
pip3 install langSrc
```

## Demo

```python
from langSrc import LanguageDetector

lang = LanguageDetector("zh", "lang.json")
lang.register(
    "language",
    {
        "zh": "语言",
        "en": "Language",
        "jp": "言語",
        "kor": "언어",
        "fra": "Langue",
        "spa": "Idioma",
        "th": "ภาษา",
    },
)

print(lang.language) # or print(lang["language"])

# 语言
```

This will generate a file named [`lang.json`](./lang.json):

```json title="lang.json"
{
  "language": {
    "zh": "语言",
    "en": "Language",
    "jp": "言語",
    "kor": "언어",
    "fra": "Langue",
    "spa": "Idioma",
    "th": "ภาษา"
  }
}
```
