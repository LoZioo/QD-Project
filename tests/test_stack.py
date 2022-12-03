from src.stack import Stack

ATTEMPTS = 3

def test_Stack() -> None:
	s = Stack[int]()

	# ---| empty and len |---
	assert s.empty()
	assert len(s) == 0

	# ---| push |---
	for i in range(ATTEMPTS):
		s.push(i)

	# ---| empty and len |---
	assert not s.empty()
	assert len(s) == ATTEMPTS

	# ---| content check |---
	for i in range(ATTEMPTS):
		assert s[i] == i

	# ---| pop |---
	for i in range(ATTEMPTS):
		assert ATTEMPTS - i - 1 == s.pop()

	# ---| empty pop |---
	assert s.pop() == None

	# ---| empty and len |---
	assert s.empty()
	assert len(s) == 0
