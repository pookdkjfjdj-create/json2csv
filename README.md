<p align="center">
  <strong><code>json2csv</code></strong><br>
  <em>Convert JSON to CSV with smart column flattening -- zero dependencies.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge&logo=opensourceinitiative" alt="License">
  <img src="https://img.shields.io/badge/Dependencies-None-ff69b4?style=for-the-badge" alt="Zero deps">
</p>

---

## What It Does

Takes JSON, flattens nested objects into dot-notation columns, and writes clean CSV.

## Quick Start

### Convert JSON to CSV

```bash
python -m json2csv convert data.json
# Output: data.csv
```

Input:
```json
[
  {"name": "Alice", "address": {"city": "NYC", "zip": "10001"}},
  {"name": "Bob", "address": {"city": "LA", "zip": "90001"}}
]
```

Output:
```csv
name,address.city,address.zip
Alice,NYC,10001
Bob,LA,90001
```

### Inspect before converting

```bash
python -m json2csv inspect data.json
```

```
File: data.json
Records: 2451
Columns: name, email, age, address.city, address.zip, tags
```

### Custom delimiter

```bash
python -m json2csv convert data.json --delimiter "|"
```

## How It Works

1. Parse JSON (array or single object)
2. Flatten nested dicts with dot notation
3. Serialize arrays as JSON strings
4. Write CSV with full column union across records

## License

MIT

<p align="center">
  <a href="https://github.com/pookdkjfjdj-create">@pookdkjfjdj-create</a>
</p>
