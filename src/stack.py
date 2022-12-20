from typing import TypeVar, Union

# Generic type variabe (ex. template<class T> class ...).
T = TypeVar("T")

class Stack(list[T]):
	def push(self, object: T) -> None:
		super().append(object)

	def pop(self) -> Union[T, None]:
		return super().pop() if len(self) > 0 else None

	def empty(self) -> bool:
		return len(self) == 0
