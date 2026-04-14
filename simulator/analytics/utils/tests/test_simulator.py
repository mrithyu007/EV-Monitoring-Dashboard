def test_speed_range():
    speed = 60
    assert 0 <= speed <= 120

def test_battery_range():
    battery = 80
    assert 0 <= battery <= 100

def test_temperature_range():
    temp = 35
    assert 0 <= temp <= 100
