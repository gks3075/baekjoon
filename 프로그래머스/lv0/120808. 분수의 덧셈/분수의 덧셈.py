from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    answer = []
    b = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    answer = [b.numerator, b.denominator]
    return answer