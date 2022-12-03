from src.queue import Queue

ATTEMPTS = 3

def test_Queue() -> None:
	q = Queue[int]()

	# ---| isEmpty and len |---
	assert q.isEmpty()
	assert len(q) == 0

	# ---| enque |---
	for i in range(ATTEMPTS):
		q.enque(i)

	# ---| isEmpty and len |---
	assert not q.isEmpty()
	assert len(q) == ATTEMPTS

	# ---| content check |---
	for i in range(ATTEMPTS):
		assert q[i] == i

	# ---| deque |---
	for i in range(ATTEMPTS):
		assert i == q.deque()

	# ---| empty deque |---
	assert q.deque() == None

	# ---| isEmpty and len |---
	assert q.isEmpty()
	assert len(q) == 0
