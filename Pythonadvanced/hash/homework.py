
# Homework: Hash, Equality, *args, **kwargs


# ========================================
# Question 1 - Version A
# ========================================

class AlwaysEqual:

    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 999

    def __eq__(self, other):
        if not isinstance(other, AlwaysEqual):
            return False
        return True


# ========================================
# Question 1 - Version B
# ========================================

class NeverEqual:

    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return 999

    def __eq__(self, other):
        if not isinstance(other, NeverEqual):
            return False
        return False


# ========================================
# Question 2 - *args
# ========================================

def has_duplicates(*args):
    """Return True if any value appears twice."""
    seen = set()

    for value in args:
        if value in seen:
            return True

        seen.add(value)

    return False


# Bonus: return all duplicated values.
def find_duplicates(*args):
    seen = set()
    duplicates = set()

    for value in args:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)

    return duplicates


# ========================================
# Question 3 - **kwargs
# ========================================

def pick_keys(prefix="is_", **kwargs):
    """Return a new dict with matching keys."""
    result = {}

    for key, value in kwargs.items():
        if key.startswith(prefix):
            result[key] = value

    return result


# ========================================
# Demo / Tests
# ========================================

if __name__ == "__main__":

    print("QUESTION 1 - VERSION A")

    obj_a = AlwaysEqual(10)
    obj_b = AlwaysEqual(10)

    s = set()
    s.add(obj_a)
    s.add(obj_b)

    print("Set length:", len(s))

    d = {}
    d[obj_a] = "apple"
    d[obj_b] = "banana"

    print("Dict length:", len(d))
    print("d[obj_a]:", d[obj_a])

    print("\nQUESTION 1 - VERSION B")

    obj_a = NeverEqual(10)
    obj_b = NeverEqual(10)

    s = set()
    s.add(obj_a)
    s.add(obj_b)

    print("Set length:", len(s))

    d = {}
    d[obj_a] = "cat"
    d[obj_b] = "dog"

    print("Dict length:", len(d))
    print("d[obj_a]:", d[obj_a])

    print("\nQUESTION 2 - *args")

    print(has_duplicates(1, 2, 3))
    print(has_duplicates(1, 2, 2, 3))
    print(has_duplicates("a", "b", "a"))

    print("\nBONUS - FIND DUPLICATES")

    print(find_duplicates(1, 2, 2, 3, 3, 3))

    print("\nQUESTION 3 - **kwargs")

    result = pick_keys(
        name="Dana",
        is_admin=True,
        age=20,
        is_active=False
    )

    print(result)

    print("\nBONUS - CUSTOM PREFIX")

    result = pick_keys(
        prefix="user_",
        user_name="Dana",
        user_age=20,
        is_admin=True
    )

    print(result)