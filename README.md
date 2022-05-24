# adventofcode-21

![](https://img.shields.io/badge/python-3.9+-blue.svg)

**Advent of Code 2021**
Create file with the name `Day0.py`

```python3
import requests, os


if not os.path.exists(f'data_folder'):
    os.mkdir('data_folder')


def day_data(day):
    
    fname = f'data_folder/Day{day}.txt'
    
    if os.path.exists(fname):
        with open(fname, 'r') as f:
            txt = f.read()
        return txt
    
    else:
        headers = {
            'cookie': YOUR_COOKIES_HERE,
        }
        
        response = requests.get(f'https://adventofcode.com/2021/day/{day}/input', headers=headers)
        
        with open(fname, 'w') as f:
            f.write(response.text)
        
        return response.text
```