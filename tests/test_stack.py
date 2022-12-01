from src.stack import Stack

ATTEMPTS = 3

def test_Stack() -> None:
	s = Stack[int]()
	assert len(s) == 0

	for i in range(ATTEMPTS):
		s.push(i)
	
	assert len(s) == ATTEMPTS
	
	for i in range(ATTEMPTS):
		assert ATTEMPTS - i - 1 == s.pop()
	
	assert s.pop() == None
	assert len(s) == 0
