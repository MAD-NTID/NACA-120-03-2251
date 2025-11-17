import area

def test_area_square():
    # Setup
    length = 8
    expected = 64 # 8 x 8 = 64

    # Invoke (call the actual function in area.py)
    result = area.square(length)

    # Analyze (do asserts)
    assert result == expected

def test_area_circle():
    radius = 3
    expected = 28.274333882308138 

    result = area.circle(radius)

    assert result == expected

def test_area_rectangle():
    length = 3
    width = 2
    expected = 6

    result = area.rectangle(length, width)

    assert result == expected