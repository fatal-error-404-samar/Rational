"""
it is a rational number module. which is similar to fractions.
"""
import math as m
"""
I'm going to use math module for some things. 
Imagine if I did this:-
import fraction as f
class rational(f.Fraction):
    pass
"""
def convert(*nums):
    """
    the inputs Will be converted to float.
    so, your input being accepted depends on the fact that could it be converted to float.
    """
    a = []
    for num in nums:
        a.append(float(num))
    return tuple(a)

def to_int(num):
    """
    the floats must be converted to a int for the p/q for p, q in integers, q != 0 thing.
    """
    a = 0
    while True:
        b = num * 10 ** a
        if b % 1 == 0:
            return int(b), a
        a += 1    

def ceil(num):
    """
    an alias for math.ceil
    """
    return m.ceil(num)

def floor(num):
    """
    an alias for math.floor
    """
    return m.floor(num)

def LCM(*args):
    """
    an alias for math.lcm
    """
    return m.lcm(*args)

def GCD(*args):
    """
    an alias for math.gcd
    """
    return m.gcd(*args)

def simplify(*args):
    """
    to simplify the numerator and denominator 
    """
    g = GCD(*args)
    return tuple(int(arg / g) for arg in args)

def sign(num):
    """
    returns the sign
    """
    if num == 0:
        return 0
    else:
        return 1 if num > 0 else -1
        
class rational:
    """
    to make a rational number/object 
    """
    def __init__(self, p, q=1):
        """
        you can give the numerator and denominator.
        giving denominator is optional as it's 1 by default 
        denominator could not be 0
        """
        if q == 0:
            raise ZeroDivisionError("the denominator of a rational number couldn't be zero. Unless you invent new mathematics")
        p, q = convert(p, q)
        a, b = to_int(p)
        c, d = to_int(q)
        self.p = a if b > d else a * 10 ** (d - b)
        self.q = c if d > b else c * 10 ** (b - d)
        self.n, self.d = simplify(self.p, self.q)

    def __repr__(self):
        """
        the way it'll look when you print it
        """
        return f"{self.n}/{self.d}"
        
    def __format__(self, spec):
        """
        to use in format string.
        """
        if not spec:
            """
            if you don't pass format specifiers, it'll just return the string format of the object 
            """
            return str(self)
        match spec[0]:
            case "r":
                """
                if the first specificier is r then the __repr__ of the num will get the rest of the specifiers will applied to it
                """
                return format(self.__repr__(), spec[1:] if spec[1:] else None)
            case "s":
                """
                s specifiers does that for a str
                """
                return format(str(self), spec[1:])
            case "i":
                """
                i is for int
                """
                return format(int(self), spec[1:])
            case "f":
                """
                f is for float 
                """
                return format(float(self), spec[1:])
            case "c":
                """
                c is for complex
                """
                return format(complex(self), spec[1:])
            case "b":
                """
                b is for boolean
                """
                return format(bool(self), spec[1:])
            case _:
                """
                else, all the specs are used on the float version of it
                """
                return format(float(self), spec)
    def __str__(self):
        """
        it's str version is same as it's repr
        """
        return self.__repr__()
        
    def __int__(self):
        """
        int is just the floor of it as a float 
        """
        return floor(self.n / self.d)
        
    def __float__(self):
        """
        float is numerator/denominator 
        """
        return self.n / self.d
        
    def __complex__(self):
        """
        complex is the complex version of it's float version 
        """
        return complex(float(self))
        
    def __bool__(self):
        """
        it means True unless numerator is 0
        """
        return self.n != 0 
        
    def __index__(self):
        """
        while using as index, it behaves as if it's the int of itself 
        """
        return int(self)
        
    def is_proper(self):
        """
        checks if it's a proper fraction
        """
        return abs(self.n) < self.d

    def is_improper(self):
        """
        checks if it's not a proper fraction 
        """
        return not self.is_proper()
        
    def are_like(self, other):
        """
        checks if two args are like fractions 
        """
        if type(self) != type(other):
            other = rational(other)
        return self.q == other.q
        
    def are_unlike(self, other):
        """
        checks if isn't a like fraction
        """
        return not self.are_like(other)
    
    def __and__(self, other):
        """
        just a random bullshit, it returns the version of fraction addition we wanted, never got
        """
        other = self.__cast__(other)
        return rational(self.p + other.p, self.q + other.p)
        
    def __or__(self, other):
        """
        it's still bullshit 
        """
        other = self.__cast__(other)
        return rational(self.p + self.q , other.p + other.q)
        
    def __xor__(self, other):
        """
        bullshit 
        """
        other = self.__cast__(other)
        return rational(self.p + other.q, self.q + other.p)
        
    def __lshift__(self, other):
        """
        bullshit 
        """
        other = self.__cast__(other)
        return rational(self.p * self.q, other.p * other.q)
        
    def __rshift__(self, other):
        """
        bullshit 
        """
        other = self.__cast__(other)
        return rational(self.p * other.q, other.p * self.q)
    
    def __invert__(self):
        """
        returns the reciprocal 
        """
        return rational(self.q , self.p)
    
    def __pos__(self):
        """
        leaves it unchanged 
        """
        return self
    
    def __neg__(self):
        """
        makes it the additive inverse 
        """
        return rational(-self.p, self.q)
    
    def __abs__(self):
        """
        returns the absolute distance of the fraction from zero
        """
        return rational(abs(self.p), abs(self.q))
    
    def __cast__(self, other):
        """
        it may look like a dunder method, it isn't. it's a normal function
        it just changes the other to the type rational if it isn't one already 
        """
        if type(self) != type(other):
            other = rational(other)
        return other 
        
    def __matmul__(self, other):
        """
        matrix multiplication symbol is used to make two rational like fractions.
        ---DON'T EXPECT IT TO MATRIX MULTIPLY---
        """
        other = self.__cast__(other)
        ns = rational(self.p * other.q, self.q * other.q)
        no = rational(other.p * self.q, other.q * self.q)
        return ns, no
        
    def __add__(self, other):
        """
        simple arithmetic addition of two rationals
        """
        ns, no = self @ other 
        return rational(ns.p + no.p, ns.q)
        
    def __sub__(self, other):
        """
        subtraction 
        """
        ns, no = self @ other 
        return rational(ns.p - no.p, ns.q)
        
    def __mul__(self, other):
        """
        multiplication 
        """
        other = self.__cast__(other)
        return rational(self.p * other.p, self.q * other.q)
        
    def __truediv__(self, other):
        """
        division 
        """
        other = self.__cast__(other)
        return rational(self.p * other.q, self.q * other.p)
        
    def __floordiv__(self, other):
        """
        floor division 
        """
        return floor(self/other)
        
    def __mod__(self, other):
        """
        modulus 
        """
        return (self/other) - (self//other)
        
    def __pow__(self, other):
        """
        exponentiation 
        """
        try:
            return rational(self.p ** other, self.q ** other)
        except:
            return self.p ** other / self.q ** other 
    
    def __divmod__(self, other):
        """
        return floor division and modulus result 
        """
        return self//other, self%other
        
    def __imatmul__(self, other):
        """
        in place version of the @ or make_like operater 
        """
        ns, no= self @ other 
        self.p, self.q, self.n, self.d, other.p, other.q, other.n, other.d = ns.p, ns.q, ns.n, ns.d, no.p, no.q, no.n, no.d
        return self, other 
        
    def __iadd__(self, other):
        """
        in place addition 
        """
        new = self + other 
        self.p, self.q, self.n, self.d = new.p, new.q, new.n, new.d
        return self 
        
    def __isub__(self, other):
        """
        in place subtraction 
        """
        new = self - other 
        self.p, self.q, self.n, self.d = new.p, new.q, new.n, new.d
        return self 
        
    def __imul__(self, other):
        """
        in place multiplication 
        """
        new = self * other 
        self.p, self.q, self.n, self.d = new.p, new.q, new.n, new.d
        return self
        
    def __itruediv__(self, other):
        """
        in place division 
        """
        new = self / other 
        self.p, self.q, self.n, self.d = new.p, new.q, new.n, new.d
        return self 
        
    def __ifloordiv__(self, other):
        """
        in place floor division 
        """
        new = self // other 
        self.p, self.q, self.n, self.d = new.p, new.q, new.n, new.d
        return self 
        
    def __imod__(self, other):
        """
        in place modulus 
        """
        new = self % other 
        self.p, self.q, self.n, self.d = new.p, new.q, new.n, new.d
        return self 
        
    def __ipow__(self, other):
        """
        in place exponentiation 
        """
        new = self ** other 
        self.p, self.q, self.n, self.d = new.p, new.q, new.n, new.d
        return self 
                
    def __rmatmul__(self, other):
        """
        right hand side @
        """
        ns, no = self @ other 
        return no, ns
        
    def __radd__(self, other):
        """
        right hand side +
        """
        return self + other 
        
    def __rsub__(self, other):
        """
        right hand side -
        """
        return -self + other 
        
    def __rmul__(self, other):
        """
        right hand side *
        """
        return self * other 
        
    def __rtruediv__(self, other):
        """
        right hand side /
        """
        return ~self * other 
        
    def __rfloordiv__(self, other):
        """
        right hand side //
        """
        return other/self - (other/self) % 1
        
    def __rmod__(self, other):
        """
        right hand side %
        """
        return ((other/self) % 1) * self
        
    def __rpow__(self, other):
        """
        right hand side **
        """
        return other ** float(self)
        
    def __hash__(self):
        """
        to be used as a key in a dictionary, a __hash__ method should be defined 
        """
        return hash((self.n, self.d))
       
    def __eq__(self, other):
        """
        ==
        """
        other = self.__cast__(other)
        no, ns = self @ other 
        return ns.p == no.p
        
    def __ne__(self, other):
        """
        !=
        """
        return not (self == other)
        
    def __lt__(self, other):
        """
        <
        """
        other = self.__cast__(other)
        ns, no= self @ other 
        return ns.p < no.p
        
    def __le__(self, other):
        """
        <=
        """
        return (self < other) or (self == other)
        
    def __gt__(self, other):
        """
        >
        """
        return not ( self <= other )
        
    def __ge__(self, other):
        """
        >=
        """
        return not (self < other)
        
    def __round__(self, digits=0):
        """
        rounds it to a specific digit
        """
        return round(float(self), digits)

    def __trunc__(self):
        """
        truncates it
        """
        return int(self)

    def __ceil__(self):
        """
        finds the ceiling 
        """
        return ceil(float(self))

    def __floor__(self):
        """
        finds the floor 
        """
        return floor(float(self))      
        
    def __bytes__(self, encoding = "utf-8"):
        """
        return it in a binary encoding 
        """
        return bytes(str(self), encoding)
        
    def __bin__(self):
        """
        returns the binary format 
        """
        return bin(int(self))
        
    def __oct__(self):
        """
        returns the octa format 
        """
        return oct(int(self))
        
    def __hex__(self):
        """
        returns the hexadecimal format 
        """
        return hex(int(self))       
    def sign(self):
        """
        returns the sign of the fraction
        """
        return sign(self.n) * sign(self.d)
        
if __name__ == "__main__":
    print("=== Rational Class Demo ===\n")

    # Create some rationals
    a = rational(3, 4)
    b = rational(2, 5)
    c = rational(-6, 8)
    d = rational(7, -3)
    e = rational(10, 2)

    print("Initial values:")
    print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
    print()

    # Arithmetic
    print("Arithmetic:")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a ** 2 = {a ** 2}")
    print(f"b ** -1 = {b ** -1}")
    print()

    # In-place ops
    print("In-place arithmetic:")
    a_cpy = rational(3, 4)
    a_cpy += b
    print(f"a += b → {a_cpy}")
    a_cpy *= rational(2)
    print(f"a *= 2 → {a_cpy}")
    print()

    # Comparison
    print("Comparison:")
    print(f"a == b: {a == b}")
    print(f"a < b: {a < b}")
    print(f"a >= b: {a >= b}")
    print(f"c.is_proper(): {c.is_proper()}")
    print(f"e.is_improper(): {e.is_improper()}")
    print()

    # Casting
    print("Casting:")
    print(f"float(a) = {float(a)}")
    print(f"int(e) = {int(e)}")
    print(f"complex(b) = {complex(b)}")
    print()

    # Weird math ops
    print("Bitwise-inspired operators:")
    print(f"a & b (min) = {a & b}")
    print(f"a | b (max) = {a | b}")
    print(f"a ^ b (mean) = {a ^ b}")
    print(f"~c (negate) = {~c}")
    print(f"a << 1 = {a << 1}")
    print(f"a >> 1 = {a >> 1}")
    print(f"a @ 3 (scale up) = {a @ 3}")
    print()

    # Formatting
    print("String formatting:")
    print(f"Default: {a}")
    print(f"Decimal: {format(a, '.3f')}")
    print()

    # Edge cases
    print("Edge cases:")
    try:
        print(rational(1, 0))
    except Exception as x:
        print(f"rational(1, 0) → Exception: {x}")
    try:
        print(rational(5, 1) / rational(0, 1))
    except Exception as x:
        print(f"5/1 ÷ 0/1 → Exception: {x}")
    print()

    # Utility methods
    print("Utilities:")
    print(f"repr(b) = {repr(b)}")
    print(f"hash(c) = {hash(c)}")
    print(f"sign(d) = {d.sign()}")
    print()

    print("=== End of Demo ===")        