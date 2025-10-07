def isanagrm(s: str, t: str) -> bool:
    """Check if two strings are anagrams of each other.

    Args:
        s (str): First string.
        t (str): Second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    Examples:
        >>> isanagrm("listen", "silent")
        True
        >>> isanagrm("hello", "world")
        False
    """
    from collections import Counter

    return Counter(s) == Counter(t)


s = "listen"
t = "silent"
print(isanagrm(s, t))  # Output: True

