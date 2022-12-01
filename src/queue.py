from typing import TypeVar, Union

# Generic type variabe (ex. template<class T> class ...).
T = TypeVar("T")

class Queue(list[T]):
	def enque(self, object: T) -> None:
		super().append(object)

	def deque(self) -> Union[T, None]:
		return super().pop(0) if len(self) > 0 else None
	
	def isEmpty(self) -> bool:
		return len(self) == 0
