# Stubs for itertools

# Based on http://docs.python.org/3.2/library/itertools.html

from typing import (Iterator, TypeVar, Iterable, overload, Any, Callable, Tuple,
                    Union, Sequence)

_T = TypeVar('_T')
_S = TypeVar('_S')

def count(start: int = ...,
          step: int = ...) -> Iterator[int]: ... # more general types?
def cycle(iterable: Iterable[_T]) -> Iterator[_T]: ...

@overload
def repeat(object: _T) -> Iterator[_T]: ...
@overload
def repeat(object: _T, times: int) -> Iterator[_T]: ...

def accumulate(iterable: Iterable[_T]) -> Iterator[_T]: ...
def chain(*iterables: Iterable[_T]) -> Iterator[_T]: ...
# TODO chain.from_Iterable
def compress(data: Iterable[_T], selectors: Iterable[Any]) -> Iterator[_T]: ...
def dropwhile(predicate: Callable[[_T], Any],
              iterable: Iterable[_T]) -> Iterator[_T]: ...
def filterfalse(predicate: Callable[[_T], Any],
                iterable: Iterable[_T]) -> Iterator[_T]: ...

@overload
def groupby(iterable: Iterable[_T]) -> Iterator[Tuple[_T, Iterator[_T]]]: ...
@overload
def groupby(iterable: Iterable[_T],
            key: Callable[[_T], _S]) -> Iterator[Tuple[_S, Iterator[_T]]]: ...

@overload
def islice(iterable: Iterable[_T], stop: int) -> Iterator[_T]: ...
@overload
def islice(iterable: Iterable[_T], start: int, stop: int,
           step: int = ...) -> Iterator[_T]: ...

def starmap(func: Any, iterable: Iterable[Any]) -> Iterator[Any]: ...
def takewhile(predicate: Callable[[_T], Any],
              iterable: Iterable[_T]) -> Iterator[_T]: ...
def tee(iterable: Iterable[Any], n: int = ...) -> Iterator[Any]: ...
def zip_longest(*p: Iterable[Any],
                fillvalue: Any = ...) -> Iterator[Any]: ...

# TODO: Return type should be Iterator[Tuple[..]], but unknown tuple shape.
#       Iterator[Sequence[_T]] loses this type information.
def product(*p: Iterable[_T], repeat: int = ...) -> Iterator[Sequence[_T]]: ...

def permutations(iterable: Iterable[_T],
                 r: Union[int, None] = ...) -> Iterator[Sequence[_T]]: ...
def combinations(iterable: Iterable[_T],
                 r: int) -> Iterable[Sequence[_T]]: ...
def combinations_with_replacement(iterable: Iterable[_T],
                                  r: int) -> Iterable[Sequence[_T]]: ...
