from src.stack import Stack

ATTEMPTS = 3

def test_Stack() -> None:
	s = Stack[int]()

	assert s.isEmpty()
	assert len(s) == 0

	for i in range(ATTEMPTS):
		s.push(i)
	
	assert not s.isEmpty()
	assert len(s) == ATTEMPTS
	
	for i in range(ATTEMPTS):
		assert ATTEMPTS - i - 1 == s.pop()
	
	assert s.pop() == None

	assert s.isEmpty()
	assert len(s) == 0
