from game import game
def test_game_01():
    assert game('piedra','tijera')== 'gana p1', 'Unexpected result'
    assert game('tijera','piedra')== 'gana p2', 'Unexpected result'
    assert game('tijera','papel')== 'gana p1', 'el p1 debio ganar'
    
