import math
import re

def is_multiple_of_11(n):
    """Return True if n is a multiple of 11; False otherwise."""
    return n % 11 == 0

def last_prime(x):
    """Return the largest prime number p that is less than or equal to m.
    You might wish to define a helper function for this.
    You may assume m is a positive integer."""
    if x < 2:
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
        if self.is_square():
            return True
        if self.n_sides != 4:
            return False
        if self.angles is None:
            return None
        for i in range(4):
            if self.angles[i] != 90:
                return False
        return True

    def is_rhombus(self):
        if self.n_sides != 4:
            return False

        if self.angles is None and self.lengths is None:
            return None

        if self.lengths is not None:
            l = self.lengths
            if not (l[0] == l[1] == l[2] == l[3]):
                return False

        if self.angles is not None:
            angles = self.angles
            a = angles.pop()
            if a in angles:
                angles.remove(a)
                if angles[0] != angles[1] or angles[0] + a != 180:
                    return False
            else:
                return False
            if self.lengths is None:
                return None
        
        return True
        #rhombus:
        #4 equal sides, 4 vertices
        #2 unique angles, opposite angles match
        #total angle sum 360
        #non unique angle pair sum 180

    def is_square(self):
        if self.n_sides != 4:
            return False
        
        if self.angles is None and self.lengths is None:
            return None

        if self.angles is not None:
            for i in range(4):
                if self.angles[i] != 90:
                    return False

        if self.lengths is not None:
            for i in range(4):
                if self.lengths[i] != self.lengths[0]:
                    return False

        return True
        #square:
        #4 equal sides
        #4 90 degree angles
        #satisfies is_rectangle

    def is_regular_hexagon(self):
        if self.n_sides != 6:
            return False

        if self.angles is None and self.lengths is None:
            return None

        if self.angles is not None:
            angs = self.angles
            a = angs.pop()
            for i in range(5):
                if a != 120:
                    return False
                a = angs.pop()
            if self.lengths is None:
                return None

        if self.lengths is not None:
            if len(self.lengths) != 6:
                return False
            for i in range(6):
                l = self.lengths[i]
                if l != self.lengths[0]:
                    return False
            if self.angles is None:
                return None

        return True
        #reg hex:
        #6 equal sides
        #6 equal 120 angles
        #angle sum 720

    def is_isosceles_triangle(self):
        if self.is_scalene_triangle():
            return False
        if self.is_equilateral_triangle():
            return True
        if self.n_sides != 3:
            return False
        if self.lengths is None and self.angles is None:
            return None

        if self.lengths is not None:
            if self.lengths[0] != self.lengths[1] and self.lengths[0] != self.lengths[2]:
                return False

        if self.angles is not None:
            if sum(self.angles) != 180:
                return False
            if self.angles[0] == self.angles[1] == self.angles[2]:
                return False
            if self.angles[0] != self.angles[1] and self.angles[0] != self.angles[2]:
                return False

        return True
        #iso tri
        #3 sides
        #2 equal sides
        #180 deg total
        #2 equal angles

    def is_equilateral_triangle(self):
        if self.lengths is None and self.angles is None:
            return None
        if self.angles == [60, 60, 60] and self.n_sides == 3:
            return True
        if self.angles is not None:
            if self.angles[0] == [self.angles[0]]*3:
                return True
        if self.lengths is not None:
            if self.lengths[0] == [self.lengths[0]]*3:
                return True
        return False
        #eq tri
        #3 equal sides
        #3 60 angles

    def is_scalene_triangle(self):
        if self.n_sides != 3:
            return False
        if self.lengths is not None:
            if self.lengths[0] == self.lengths[1] or \
            self.lengths[1] == self.lengths[2] or \
            self.lengths[0] == self.lengths[2]:
                return False
        if self.angles is not None:
            if sum(self.angles) != 180 or \
            self.angles[0] == self.angles[1] or \
            self.angles[1] == self.angles[2] or \
            self.angles[0] == self.angles[2]:
                return False
        if self.angles is None and self.lengths is None:
            return None
        return True
        #scal tri
        #no equal sides
        #no equal angles
        #3 sides
        #3 angles