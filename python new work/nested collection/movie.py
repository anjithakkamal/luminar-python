movies=[

    {
        "title": "Bad Asses on the Bayou",
        "year": 2011,
        "cast": [
            "Danny Trejo",
            "Danny Glover",
            "John Amos",
            "Loni Love"
        ],
        "genres": [
            "Action"
        ]
    },
    {
        "title": "Chappie",
        "year": 2015,
        "cast": [
            "Sharlto Copley",
            "Dev Patel",
            "Watkin Tudor Jones",
            "Yolandi Visser"
        ],
        "genres": [
            "Science Fiction"
        ]
    },
    {
        "title": "Road Hard",
        "year": 2015,
        "cast": [
            "Adam Carolla",
            "David Koechner",
            "Diane Farr",
            "Jay Mohr",
            "David Alan Grier"
        ],
        "genres": [
            "Comedy"
        ]
    },
    {
        "title": "The Second Best Exotic Marigold Hotel",
        "year": 2015,
        "cast": [
            "Judi Dench",
            "Maggie Smith",
            "Bill Nighy"
        ],
        "genres": [
            "Comedy",
            "Drama"
        ]
    },
    {
        "title": "Unfinished Business",
        "year": 2015,
        "cast": [
            "Vince Vaughn",
            "Dave Franco",
            "Sienna Miller",
            "Nick Frost"
        ],
        "genres": [
            "Comedy"
        ]
    },
    {
        "title": "Cinderella",
        "year": 2015,
        "cast": [
            "Lily James",
            "Richard Madden",
            "Cate Blanchett",
            "Helena Bonham Carter",
            "Holliday Grainger"
        ],
        "genres": [
            "Romance"
        ]
    },
    {
        "title": "The Cobbler",
        "year": 2015,
        "cast": [
            "Adam Sandler",
            "Dustin Hoffman",
            "Dan Stevens",
            "Steve Buscemi"
        ],
        "genres": [
            "Comedy",
            "Drama"
        ]
    },
    {
        "title": "Cymbeline",
        "year": 2015,
        "cast": [
            "Ed Harris",
            "Milla Jovovich",
            "Ethan Hawke",
            "John Leguizamo"
        ],
        "genres": [
            "Crime"
        ]
        
    },
    {
        "title": "Home Sweet Hell",
        "year": 2015,
        "cast": [
            "Patrick Wilson",
            "Katherine Heigl",
            "Jordana Brewster",
            "Jim Belushi"
        ],
        "genres": [
            "Comedy"
        ]
    },
    {
        "title": "It Follows",
        "year": 2015,
        "cast": [
            "Maika Monroe",
            "Keir Gilchrist",
            "Jake Weary",
            "Daniel Zovatto"
        ],
        "genres": [
            "Horror"
        ]
    }
]
#1) total number of movies*****************************
print("total number of movies :- ",len(movies))

#2) print movie names*********************************
movie_names=[m.get("title") for m in movies]
print("movies names :- ",movie_names)

#3) 2015 movies title*****************************
movies_2015=[m.get("title") for m in movies if m.get("year")==2015]
print("2015 movies names :- ",movies_2015)

#4) genres comedy movie*************************

comedy_movies=[m.get("title") for m in movies if "Comedy" in m.get("genres")]
print("comedy movies :- ",comedy_movies)
# print(count(comedy_movie))

#5)print it follow movie cast********************
cast=[m.get("cast") for m in movies if m.get("title")=="It Follows"]
print("it follow movie cast :- ",cast)

#6)both comedy and drama
comedy_drama=[m.get("title") for m in movies if "Comedy" in m.get ("genres") and "Drama" in m.get("genres")]
print("both comedy and drama :- ",comedy_drama)

#7)comedy or drama
comedy_drama=[m.get("title") for m in movies if "Comedy" in m.get ("genres") or "Drama" in m.get("genres")]
print("both comedy or drama :- ",comedy_drama)

#8)maggie smith cast title
cast_title=[m.get("title") for m in movies if "Maggie Smith" in m.get("cast")]
print("cast title of maggie smith :- ",cast_title)

#9)actors count
actors=[]
for m in movies:
    for a in m.get("cast"):
        actors.append(a)
print(actors)
wc={a:actors.count(a) for a in set(actors)}
print(" actors count :-",wc)