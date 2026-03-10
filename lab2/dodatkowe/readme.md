# Jak używać

main.py [-h] --input INPUT --output OUTPUT

options:
-h, --help show this help message and exit
--input INPUT input_file
--output OUTPUT output_file

# Wymagania

- venv
- python 3.10
- pip install xmltodict

# plik config.json

Plik konfiguracyjny pozwala wybierać jakie elementy obiektu będą w pliku wyjściowym

```json
{
  "obiekt": {
    "tablca": [
      {
        "primitive1": true,
        "primitive2": true,
        "primitive3": true,
        "primitive4": true
      }
    ],
    "primitive5": true
  },
  "primitive6": true
}
```
