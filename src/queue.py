from typing import TypeVar

# Generic type variabe (ex. template<class T> class ...).
T = TypeVar("T")

class Queue(list[T]):
	def enque(self, object: T) -> None:
		super().append(object)
	
	def deque(self) -> T:
		return super().pop(0)
