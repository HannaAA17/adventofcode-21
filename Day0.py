import requests, os

YOUR_COOKIES = ''

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
            'cookie': YOUR_COOKIES,
        }
        
        response = requests.get(f'https://adventofcode.com/2021/day/{day}/input', headers=headers)
        
        with open(fname, 'w') as f:
            f.write(response.text)
        
        return response.text
