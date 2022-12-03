from src.stack import Stack

ATTEMPTS = 3

def test_Stack() -> None:
	s = Stack[int]()

	# ---| isEmpty and len |---
	assert s.isEmpty()
	assert len(s) == 0

	# ---| push |---
	for i in range(ATTEMPTS):
		s.push(i)

	# ---| isEmpty and len |---
	assert not s.isEmpty()
	assert len(s) == ATTEMPTS

	# ---| content check |---
	for i in range(ATTEMPTS):
		assert s[i] == i

	# ---| pop |---
	for i in range(ATTEMPTS):
		assert ATTEMPTS - i - 1 == s.pop()

	# ---| empty pop |---
	assert s.pop() == None

	# ---| isEmpty and len |---
	assert s.isEmpty()
	assert len(s) == 0
