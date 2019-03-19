class Array(object):
    """ARRAY CLASS"""

    def __init__(self, size):
        self.size = size
        self.n = 0  # Count actual elements (Default is 0)
        self.A = [None] * size

    def get(self, k):
        """
        Return element at index k
        """
        if not 0 <= k < self.n:
            # Check it k index is in bounds of array
            return IndexError("K is out of bounds !")

        return self.A[k]

    def append(self, element):
        """
        Add element to end of the array
        """
        if self.n == self.size:
            return IndexError("The array is full !")

        self.A[self.n] = element
        self.n += 1

    def delete(self, k):
        """
        Delete element at index k
        """
        if not 0 <= k < self.n:
            # Check it k index is in bounds of array
            return IndexError("K is out of bounds !")

        for idx in range(k, self.n - 1):
            self.A[idx] = self.A[idx + 1]

        self.A[self.n - 1] = None
        self.n -= 1


if __name__ == "__main__":
    array = Array(3)
    print(f"Array size: {array.size}")

    array.append(1)
    array.append(2)
    array.append(3)
    print(f"Element at index 2: {array.get(2)}")

    print(f"Element at index 0: {array.get(0)}")
    array.delete(0)
    print(f"Element at index 0: {array.get(0)}")
