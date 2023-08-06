import youtube_search
import youtubesearchpython
import bs4
import requests
import random
import datetime


def get_random_number():
    number = random.randrange(10000)
    if number >= 1000:
        return str(number)
    if number >= 100:
        return "0" + str(number)
    if number >= 10:
        return "00" + str(number)
    if number >= 0:
        return "000" + str(number)


def get_random_p_search(p=random.choice(["img", "mvi", "mov", "dsc"])):
    case = random.randrange(3)
    p = p.upper()
    if not case:
        return "{} {}".format(p, get_random_number())
    if case == 1:
        return "{}_{}".format(p, get_random_number())
    if case == 2:
        return "{}{}".format(p, get_random_number())


def get_random_wiki_search():
    if random.choice([True, False]):
        r = requests.get(
            "https://en.wikipedia.org/wiki/Special:Random#/random")
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        if random.choice([True, False]):
            words = []
            for i in soup.find_all("p"):
                for j in i.text.split():
                    if j in words:
                        continue
                    words.append(j)
            return random.choice(words)
        else:
            return soup.title.text.split("-")[0]
    else:
        r = requests.get("https://en.wikipedia.org/wiki/Main_Page")
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        return random.choice(soup.text.split())


def get_random_vid_search():
    year = random.randint(2009, datetime.datetime.now().year)
    month = random.randint(1, 12)
    day = random.randint(1, 30)
    if year == datetime.datetime.now().year:
        month = random.randint(1, datetime.datetime.now().month)
    if month > datetime.datetime.now().month:
        day = random.randint(1, datetime.datetime.now().day)
    year = str(year)
    if month < 10:
        month = "0" + str(month)
    month = str(month)
    if day < 10:
        day = "0" + str(day)
    day = str(day)
    return "vid {}{}{}".format(year, month, day)


def get_new_video():
    word = random.choice(["img", "vid", "mvi", "mov", "dsc"])
    return random.choice(advanced_search(word, youtubesearchpython.VideoSortOrder.uploadDate))


def normal_search(word):
    results = youtube_search.YoutubeSearch(word, max_results=100).to_dict()
    video_ids = []
    for i in results:
        video_ids.append(i["id"])
    return video_ids


def advanced_search(word, mode=None):
    if not mode:
        a = random.randrange(3)
        if a == 0:
            mode = youtubesearchpython.VideoSortOrder.uploadDate
        if a == 1:
            mode = youtubesearchpython.VideoSortOrder.viewCount
        if a == 2:
            mode = youtubesearchpython.VideoSortOrder.rating
    results = youtubesearchpython.CustomSearch(word, mode, limit=100)
    video_ids = []
    for i in results.result().get("result"):
        video_ids.append(i.get("id"))
    return video_ids


def get_word():
    case = random.randrange(6)
    if case == 0:
        word = get_random_p_search("img")
    if case == 1:
        word = get_random_wiki_search()
    if case == 2:
        word = get_random_vid_search()
    if case == 3:
        word = get_random_p_search("mvi")
    if case == 4:
        word = get_random_p_search("mov")
    if case == 5:
        word = get_random_p_search("dsc")

    return word


def get_random_video_id():
    if not random.randrange(7):
        return get_new_video()

    while True:
        word = get_word()

        if not random.randrange(4):
            video_ids = normal_search(word)
        else:
            video_ids = advanced_search(word)

        try:
            id = random.choice(video_ids)
            break
        except IndexError:
            continue

    return id


if __name__ == "__main__":
    print(get_random_video_id())