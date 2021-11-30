from typing import Any, Callable, List, TypeVar
from dms2122common.data.role import Role

F = TypeVar("F", bound=Callable[..., Any])

# https://stackoverflow.com/a/26151604/11810358
def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)

        return repl

    return layer


@parametrized
def protected_endpoint(route: Any = None, roles: List[Role] = []) -> Any:
    print(route, flush=True)
    print(roles, flush=True)

    def route_aux(*args, **kwargs) -> None:

        if not route:
            return None

        print(args, flush=True)
        print(kwargs, flush=True)
        return route(*args, **kwargs)

    return route_aux

