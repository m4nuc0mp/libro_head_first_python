"""This module is an example for the first chapter of
Head First Python."""

def print_lol(the_list):
    """This function prints the elements of a list. If nested lists
    are present, it will print their element, and so on for further
    nested lists inside."""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)