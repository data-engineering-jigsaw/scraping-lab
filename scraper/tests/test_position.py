from src.models.position import Position

def test_init_position():
    position = Position(*['8cba12eacacdf624', 'Data Engineer', [70, 73], 'Ana-Data Consulting Inc', 'New York', 'NY'])
    assert list(position.__dict__.values()) == ['8cba12eacacdf624', 'Data Engineer', [70, 73], 'Ana-Data Consulting Inc', 'New York', 'NY']