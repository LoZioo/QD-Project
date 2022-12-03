from src.queue import Queue

ATTEMPTS = 3

def test_Queue() -> None:
	q = Queue[int]()

	# ---| empty and len |---
	assert q.empty()
	assert len(q) == 0

	# ---| enque |---
	for i in range(ATTEMPTS):
		q.enque(i)

	# ---| empty and len |---
	assert not q.empty()
	assert len(q) == ATTEMPTS

	# ---| content check |---
	for i in range(ATTEMPTS):
		assert q[i] == i

	# ---| deque |---
	for i in range(ATTEMPTS):
		assert i == q.deque()

	# ---| empty deque |---
	assert q.deque() == None

	# ---| empty and len |---
	assert q.empty()
	assert len(q) == 0
