"""Utilities for manipulating lists."""


def head(input_list):
    """Return the first item of the input list.

    For example:

      >>> head(['Jan', 'Feb', 'Mar'])
      'Jan'
    """
    #Return index [0] item

    return input_list[0]


def tail(input_list):
    """Return a new list of all items, excluding the first item.

    For example:

    >>> tail(['Jan', 'Feb', 'Mar'])
    ['Feb', 'Mar']

    """
    #Create a new list
    tail_list = input_list[1:]
    #Assign slice to new list
    #return new list
    return tail_list


def last(input_list):
    """Return the last item of the input list.

    For example:

    >>> last(['Jan', 'Feb', 'Mar'])
    'Mar'

    """
    #Return index [-1]
    return input_list[-1]


def top(input_list):
    """Return all elements of the input list except the last.

    For example:

    >>> top(['Jan', 'Feb', 'Mar'])
    ['Jan', 'Feb']

    """
    #Return slice 0 to -1
    return input_list[0:-1]


def first_three(input_list):
    """Return the first three elements of the input list.

    For example:

    >>> first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    ['Jan', 'Feb', 'Mar']

    """
   
    #Return slice 0 to 3
    return input_list[0:3]


def last_five(input_list):
    """Return the last five elements of the input list.

    For example:

    >>> last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [15, 18, 21, 24, 27]

    """
    #slice [-5: ]
    return input_list[-5:]


def middle(input_list):
    """Return all elements of input_list except the first two and the last two.

    For example:

    >>> middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15, 18, 21]

    """
    #slice [2:-2]
    return input_list[2:-2]


def inner_four(input_list):
    """Return the third, fourth, fifth, and sixth elements of input_list.

    For example:

    >>> inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15]

    """
    #slice [2:6]
    return input_list[2:6]


def inner_four_end(input_list):
    """Return the elements that are 6th, 5th, 4th, and 3rd from the end of input_list.

    This function should return those elements in a list, in the exact order
    described above.

    For example:

    >>> inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [12, 15, 18, 21]

    """
    #slice [-3:2:-1]
    #Original idea was to reverse list with -1 step, but reread the docstring
    #and realized that it was 6th from the END of list not 6th IN list.
    return input_list[-6:-2]


def replace_head(input_list):
    """Replace the head of input_list with the value 42 and return nothing.

    Input list must be modified in-place, not merely reassigned to a new value.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_head(multiples)
    >>> multiples
    [42, 3, 6, 9, 12, 15, 18, 21, 24, 27]

    """
    input_list[0] = 42



def replace_third_and_last(input_list):
    """Replace third and last elements of input_list with 37 and return nothing.

    Input list must be modified in-place, not merely reassigned to a new value.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_third_and_last(multiples)
    >>> multiples
    [0, 3, 37, 9, 12, 15, 18, 21, 24, 37]

    """
    #Original idea was to list indices and set to value of 37, but not possible
    #without a loop. So split into 2 lines of code.
    input_list[2] = 37
    input_list[-1] = 37
   


def replace_middle(input_list):
    """Replace all elements of a list but the first two and last two with 42 and 37.

    After the replacement, 42 and 37 should appear in that order in input_list.
    Input list must be modified in-place, not merely reassigned to a new value.

    Return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_middle(multiples)
    >>> multiples
    [0, 3, 42, 37, 24, 27]

    """
    #Slice [1:-2] = [42, 37]
    input_list[2:-2] = [42, 37]



def delete_third_and_seventh(input_list):
    """Remove third and seventh elements of input_list and return nothing.

    Input list must be modified in-place, not merely reassigned to a new value.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_third_and_seventh(notes)
    >>> notes
    ['Do', 'Re', 'Fa', 'So', 'La', 'Do']

    """
    input_list.pop(2)
    #Original idea was to pop index[6], but after 2 is removed, 6 no longer exists
    input_list.pop(5)


def delete_middle(input_list):
    """Remove all elements from input_list except the first two and last two.

    Input list must be modified in-place, not merely reassigned to a new value.

    Return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_middle(notes)
    >>> notes
    ['Do', 'Re', 'Ti', 'Do']

    """
    #Slice [2:-2]
    input_list[2:-2] = []
