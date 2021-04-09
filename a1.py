import math
import re

def is_multiple_of_11(n):
    """Return True if n is a multiple of 11; False otherwise."""
    return n % 11 == 0

def last_prime(x):
    """Return the largest prime number p that is less than or equal to m.
    You might wish to define a helper function for this.
    You may assume m is a positive integer."""
    if x < 0:
        return False
    if x < 3:
        return 2
    if x % 2 == 0:
        x -= 1
    for i in range(x, 2, -2):
        if isPrime(i):
            return i

def isPrime(x):
    if x % 2 == 0:
        return False
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True


def quadratic_roots(a, b, c):
    # -b +/- sqrt(b**2 - 4*a*c)
    # /2a
    bb = b**2
    ac = 4*a*c
    if bb < ac:
        return "complex"
    rad = math.sqrt(bb - ac)
    return ((-b + rad)/(2*a), (-b - rad)/(2*a))
    """Return the roots of a quadratic equation (real cases only).
    Return results in tuple-of-floats form, e.g., (-7.0, 3.0)
    Return "complex" if real roots do not exist."""



def perfect_shuffle(even_list):
    l = len(even_list)
    if l % 2 != 0:
        return "list has an odd number of elements!"
    listA = even_list[0:l//2]
    listB = even_list[l//2:]
    listA.reverse()
    listB.reverse()
    newList = []
    for i in range(l//2):
        newList.append(listA.pop())
        newList.append(listB.pop())
    return newList
    """Assume even_list is a list of an even number of elements.
    Return a new list that is the perfect-shuffle of the input.
    Perfect shuffle means splitting a list into two halves and then interleaving
    them. For example, the perfect shuffle of [0, 1, 2, 3, 4, 5, 6, 7] is
    [0, 4, 1, 5, 2, 6, 3, 7]."""


def five_times_list(input_list):
    return [x*5 for x in input_list]
    """Assume a list of numbers is input. Using a list comprehension,
    return a new list in which each input element has been multiplied
    by 5."""


def triple_vowels(text):
    vowels = ["A","E","I","O","U","a","e","i","o","u"]
    for v in vowels:
        text = text.replace(v, v*3)
    return text

    """Return a new version of text, with all the vowels tripled.
    For example:  "The *BIG BAD* wolf!" => "Theee "BIIIG BAAAD* wooolf!".
    For this exercise assume the vowels are
    the characters A,E,I,O, and U (and a,e,i,o, and u).
    Maintain the case of the characters."""


def count_words(text):
    count = {}
    for word in re.findall(r"([A-Za-z0-9-+*/@#%'/]+)", text.lower()):
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1
    return count
    """Return a dictionary having the words in the text as keys,
    and the numbers of occurrences of the words as values.
    Assume a word is a substring of letters and digits and the characters
    '-', '+', *', '/', '@', '#', '%', and "'" separated by whitespace,
    newlines, and/or punctuation (characters like . , ; ! ? & ( ) [ ] { } | : ).
    Convert all the letters to lower-case before the counting."""


def make_quartic_evaluator(a, b, c, d, e):
    return lambda x: a*x**4 + b*x**3 + c*x**2 + d*x + e
    """When called with 5 numbers, returns a function of one variable (x)
    that evaluates the quartic polynomial
    a x^4 + b x^3 + c x^2 + d x + e.
    For this exercise Your function definition for make_quartic_evaluator
    should contain a lambda expression."""


class Polygon:
    """Polygon class."""
    def __init__(self, n_sides, lengths=None, angles=None):
        self.n_sides = n_sides
        self.lengths = lengths
        self.angles = angles

    def is_rectangle(self):
    #returns True if the polygon is a rectangle,
    #False if it is definitely not a rectangle, and None
    #if the angle list is unknown (None).
        if self.angles is None:
            return None
        if self.n_sides == 4 and \
           self.angles = [90, 90, 90, 90]:
            sides = self.lengths
            for i in range(2):
                w = self.lengths[1]
                sides.remove(w)
                if w not in sides:
                    return False
                else:
                    remove(w)
            return True
        if self.n_sides != 4 or \
           sum(self.angles) != 360
            [i for i,a in enumerate(self.angles) if a == 90] != [90, 90, 90, 90]:
            return False
        pass

    def is_rhombus(self):
        pass

    def is_square(self):
        pass

    def is_regular_hexagon(self):
        pass

    def is_isosceles_triangle(self):
        pass

    def is_equilateral_triangle(self):
        pass

    def is_scalene_triangle(self):
        pass