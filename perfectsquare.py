def perfectsquare(num: int) -> bool:
    k = 1
    r = num

    while k <= r:
        m_square = (k + r) // 2
        sq = m_square * m_square
        if num == sq:
            return True
        elif sq < num:
            k = m_square + 1  # fixed variable name
        else:
            r = m_square - 1

    return False

num = 16
print(perfectsquare(num))