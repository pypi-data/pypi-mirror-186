from typing import Union, TypeVar, Generic, Any
import abc

from pint import UnitRegistry, __version__ as pint_version


# Diako provided this fix to bridge 0.19 to 0.20 versions:

try:
    from pint.facets.plain.definitions import ScaleConverter
    from pint.facets.plain.definitions import UnitDefinition
except ImportError:  # For pint versions < 0.20.1
    from pint.converters import ScaleConverter
    from pint.definitions import UnitDefinition


class State:
    unit_registry = UnitRegistry()
    unit_registry.define("Mm3 = 1000000 m**3")
    unit_registry.define("EUR = [euro]")
    unit_registry.define("RUB = [rubles]")
    unit_registry.define("NOK = [norske_kroner]")
    unit_registry.define("euro = EUR")
    unit_registry.define("ºC = 273.16 K = degC")
    unit_registry.define("º = deg")
    if pint_version < '0.20.0':  # not allowed in later versions
        unit_registry.define(UnitDefinition('percent', 'pct', (), ScaleConverter(1/100.0)))
        unit_registry.define("mm/h = mm/hr")
    else:
        unit_registry.define(UnitDefinition('percent', 'pct', (), ScaleConverter(1/100.0), {}))
    Quantity = unit_registry.Quantity
    unit_convert = None


Unit = Union[str, State.unit_registry.Unit]


T = TypeVar("T")


class Quantity(Generic[T]):
    """Meta Quantity, used for type annotation, ONLY!!!!"""

    @abc.abstractmethod
    def __init__(self) -> None:
        """"""

    @property
    def magnitude(self) -> T:
        return T

    @property
    def units(self) -> Any:
        return

    def to(self, other) -> Any:
        return
