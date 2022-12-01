from src.queue import Queue

ATTEMPTS = 3

def test_Queue() -> None:
	q = Queue[int]()

	assert q.isEmpty()
	assert len(q) == 0

	for i in range(ATTEMPTS):
		q.enque(i)

	assert not q.isEmpty()
	assert len(q) == ATTEMPTS

	for i in range(ATTEMPTS):
		assert i == q.deque()

	assert q.deque() == None

	assert q.isEmpty()
	assert len(q) == 0
