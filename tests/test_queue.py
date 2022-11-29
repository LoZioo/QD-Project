from src.queue import Queue

ATTEMPTS = 3

def test_Queue() -> None:
	q = Queue[int]()
	assert len(q) == 0

	for i in range(ATTEMPTS):
		q.enque(i)
	
	assert len(q) == ATTEMPTS
	
	for i in range(ATTEMPTS):
		assert i == q.deque()
	
	assert len(q) == 0