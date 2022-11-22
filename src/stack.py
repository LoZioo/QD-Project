from typing import TypeVar

# Generic type variabe (ex. template<class T> class ...).
T = TypeVar("T")

class Stack(list[T]):
	def push(self, object: T) -> None:
		super().append(object)

a = Stack[int]()
