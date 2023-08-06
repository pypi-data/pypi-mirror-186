class OMITTED:
    """used as singleton for omitted values in validation"""

    def __repr__(self) -> str:
        return "omitted"

    def __str__(self) -> str:
        return "omitted"

    def __bool__(self) -> bool:
        return False


omitted = OMITTED()


class EMPTY:
    """used as singleton for omitted options/kwargs"""

    def __repr__(self) -> str:
        return "empty"

    def __str__(self) -> str:
        return "empty"


empty = EMPTY()
