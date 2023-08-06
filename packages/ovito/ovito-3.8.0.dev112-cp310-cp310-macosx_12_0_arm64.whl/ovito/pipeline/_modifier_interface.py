import ovito
import ovito.pipeline
from ..data import DataCollection
from ..modifiers import PythonScriptModifier
import abc
import traits.api
from typing import List, Optional, Any, Generator, Union

class ModifierInterface(traits.api.ABCHasStrictTraits):
    """
    Base: :py:class:`traits.has_traits.ABCHasStrictTraits`

    Abstract base class for Python script modifiers that make use of the advanced programming interface.

    .. versionadded:: 3.8.0
    """

    # Import the InputSlot helper class defined by the C++ code into the namespace of this class.
    InputSlot = PythonScriptModifier.InputSlot

    # The number of additional input pipeline slots used by the modifier.
    extra_input_slots = traits.api.Range(low=0, transient=True, visible=False)

    # Event trait which sub-classes should trigger whenver the number of output frames changes.
    update_output_frame_count = traits.api.Event(descr='Requests recomputation of the number of output animation frames')

    # Abstract method that must be implemented by all sub-classes:
    @abc.abstractmethod
    def modify(self, data: DataCollection, *, frame: int, input_slots: List[InputSlot], data_cache: DataCollection, **kwargs: Any) -> Optional[Generator[Union[str, float], None, None]]:
        raise NotImplementedError

    # Optional methods that may be implemented by sub-classes:
    #
    #if TYPE_CHECKING:
    #    def output_frame_count(self, input_slots: List[InputSlot]) -> int:
    #        raise NotImplementedError
    #    def input_frame_cache(self, output_frame: int, input_slots: List[InputSlot]) -> Mapping[InputSlot, int | Sequence[int]]:
    #        raise NotImplementedError

ovito.pipeline.ModifierInterface = ModifierInterface
