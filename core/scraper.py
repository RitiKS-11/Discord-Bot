import requests, random, json
from bs4 import BeautifulSoup

def scrape(url):
    response = requests.get(url, timeout=10)  
    return response  
    

def parse_content(response):
    meme_list = []
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find_all('a', attrs={'class':'absolute inset-0'})
    post_link = soup.find_all('a', attrs={'class': 'block font-semibold text-neutral-content-strong m-0 visited:text-neutral-content-weak text-16 xs:text-18 mb-2xs xs:mb-xs'})
    image_link = soup.find_all('a', attrs={'rel':'noopener noreferrer ugc'})

    print(len(title), len(post_link), len(image_link))
    for index in range(len(title)):
        meme_list.append({
            'title': title[index].text.replace('\n', ''),
            'post': 'https://www.reddit.com/r/ProgrammerHumor'+ post_link[index]['href'],
            'image': image_link[index]['href']
        })

    return meme_list

def parse_json(response):
    meme_list = []

    if response.status_code == 200:
        res = json.loads(response.text)
        posts = res['data']['children']

        for post in posts:
            image = post['data']['thumbnail']
            url = post['data']['permalink']
            title = post['data']['title']

            meme_list.append({
                'title': title,
                'post': 'https://www.reddit.com/r/ProgrammerHumor'+ url,
                'image': image
            })
    
    else:
        print(f"{res.message}\n {res.status_code}")

    return meme_list


def store_meme(meme_list):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
        print(json_data)

    with open('data.json', 'w') as file:
        if json_data != meme_list:
            meme_list = meme_list + json_data
        json.dump(meme_list, file, indent=4)


def preiodict_task(url='https://www.reddit.com/r/ProgrammerHumor.json'):
    response = scrape(url)
    print(response.text)
    memes = parse_json(response)
    store_meme(memes)


def meme():
    with open('data.json') as file:
        memes = json.load(file)

    meme = random.choice(memes)
    return meme

if __name__ == "__main__":
    preiodict_task()