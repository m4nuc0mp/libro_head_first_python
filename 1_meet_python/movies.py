# Primer ejemplo - Lista de Películas
fav_movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese",
                "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

# for each_item in fav_movies:
#     if isinstance(each_item, list):
#         for nested_item in each_item:
#             print(nested_item)
#     else:
#         print(each_item)

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(fav_movies)