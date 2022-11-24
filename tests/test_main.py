from src.main import sum

def test_sum() -> None:
	assert sum(3,4) == 7
	assert sum(0,0) == 0
