import math
class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
        
    def evaluate_at(self, s):
        result = 0
        for a in range(len(self.coeffs)):
            result += self.coeffs[a]*math.pow(s,(len(self.coeffs)-1-a))
        return int(result)

    def __str__(self):
        s=""
        for a in range(len(self.coeffs)):
            if a!= len(self.coeffs)-1:
                print(str(self.coeffs[a]),"x^",str(len(self.coeffs)-1-a),sep="",end = "")
                print(" + ",end="")
            else:
                print(self.coeffs[a],end="")
        return s

    def __iadd__(self, other):
        listA = self.coeffs
        listA.reverse()
        listB = other.coeffs
        listB.reverse()
        if len(listA)>=len(listB):
            for a in range(len(listB)):
                listA[a] +=listB[a]
            listA.reverse()
            self.coeffs = listA
        else:
            for a in range(len(listA)):
                listB[a] +=listA[a]
            listB.reverse()
            self.coeffs = listB
        return self
        
def main():
	# 1x^4 + 2x^3 + 3x^2 + 4x + 5
	coeffs = [1,2,3,4,5]
	poly = Polynomial(coeffs)
	print(poly.evaluate_at(2))   # 57
	print(poly.evaluate_at(3))   # 179
	print(poly)	 # Outputs: 1x^4 + 2x^3 + 3x^2 + 4x^1 + 5

	# 4x^3 + 6x^2 + 8x^1 + 10
	coeffs = [4,6,8,10]
	poly2 = Polynomial(coeffs)
	print(poly2)	 # Outputs: 4x^3 + 6x^2 + 8x^1 + 10
	poly += poly2
	print(poly)

main()
