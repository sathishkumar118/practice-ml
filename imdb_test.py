import imdb
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from PIL import Image

# creating an instance of the IMDB()
def main():
    ia = imdb.IMDb()
    search_movie(input('Name of the Movie: '),ia)

# Using the Search movie method
def search_movie(name,ia):

    items = ia.search_movie(name)
    for i, item in enumerate(items):
        print(i+1, item)

    while True:
        try:
            search_idx = int(input('Enter the index of the movie you are looking for:'))
            movie_name = items[search_idx-1]
            break
        except:
            print('Enter a number in the range 1 to {}'.format(len(items)))
            continue
    movie_obj = ia.get_movie(movie_name.movieID)
    display_movie_cover(movie_obj,ia)
    print(movie_obj['directors'])

def display_movie_cover(movie_obj,ia):
    poster_url = movie_obj.data['cover url']
    print(poster_url)
    req = Request(
        url=poster_url,
        headers={'User-Agent': 'Chrome'}
        )
    with urlopen(req) as response:
        html = response.read()
        image_loc = 'movie_cover.jpg'
        with open(image_loc, 'wb') as f:
            f.write(html)
    img = Image.open(image_loc)
    img.show()

if __name__ == "__main__":
    main()
