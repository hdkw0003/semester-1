# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

albums = {

"Tom Vance": {
    "Sank on the River": "Country Genre",
    "Whispering Sink": "Country Genre",
    "I'm Done With This": "Country Genre",
    },
"Neil Brahn": {"Extra Tog": "Rock",
               "Six Bottles on the Thames": "Rock",
               "I Drank Four Ginger Beers": "Rock",
               },
"Roma Liheg": {"Bamke ta Baro": "Folk",
               "Talog mi Mubarya": "Folk",
               "Ego He Hata O Kalo Palu": "Folk"
                  },
"Lonnie Nathanson": {"Don Juan": "Country Genre",
                     "I Sank in Cheyenne": "Country Genre",
                     "A Mature Horse": "Country Genre"
                          }

}

# Pretty-print the data structure

[pprint(albums)]

# Display details of one album recorded by a specific artist
