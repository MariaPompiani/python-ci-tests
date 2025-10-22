from app.calculator import soma

def test_soma():
    """Verifica se a função soma retorna o valor correto."""
    assert soma(2, 3) == 5
