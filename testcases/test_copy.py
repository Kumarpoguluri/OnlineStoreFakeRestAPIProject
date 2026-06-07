import copy

class Testclass:
    def test_copy(self):
        original = [[1, 2], [3, 4]]

        shallow = copy.copy(original)
        deep = copy.deepcopy(original)
        original[0][0] = 99

        print("shallow copy",shallow)
        print("deep copy",deep)


#✅ Modifying a nested mutable object affects both.
#❌ Modifying the outer container affects only the copy.
    def test_shallowcopy(self):

        original = [[1, 2], [3, 4]]
        shallow = copy.copy(original)

        shallow[0] = ["new", "list"]

        print("Original:", original)
        print("Shallow :", shallow)