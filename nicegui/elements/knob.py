from typing import Optional

from ..colors import set_text_color
from .label import Label
from .mixins.value_element import ValueElement


class Knob(ValueElement):

    def __init__(self,
                 value: float = 0.0,
                 *,
                 min: float = 0.0,
                 max: float = 1.0,
                 step: float = 0.01,
                 color: Optional[str] = 'primary',
                 center_color: Optional[str] = None,
                 track_color: Optional[str] = None,
                 size: Optional[str] = None,
                 show_value: bool = False,
                 ) -> None:
        """Knob

        This element is based on Quasar's `QKnob <https://quasar.dev/vue-components/knob>`_ component.
        The element is used to take a number input from the user through mouse/touch panning.

        :param value: the initial value (default: 0.0)
        :param min: the minimum value (default: 0.0)
        :param max: the maximum value (default: 1.0)
        :param step: the step size (default: 0.01)
        :param color: knob color (either a Quasar, Tailwind, or CSS color or `None`, default: "primary")
        :param center_color: color name for the center part of the component, examples: primary, teal-10
        :param track_color: color name for the track of the component, examples: primary, teal-10
        :param size: size in CSS units, including unit name or standard size name (xs|sm|md|lg|xl), examples: 16px, 2rem
        :param show_value: whether to show the value as text
        """
        super().__init__(tag='q-knob', value=value, on_value_change=None, throttle=0.05)

        self._props['min'] = min
        self._props['max'] = max
        self._props['step'] = step
        set_text_color(self, color)
        self._props['show-value'] = True  # NOTE: enable default slot, e.g. for nested icon

        if center_color:
            self._props['center-color'] = center_color

        if track_color:
            self._props['track-color'] = track_color

        if size:
            self._props['size'] = size

        self.label: Optional[Label] = None
        if show_value:
            with self:
                self.label = Label().bind_text_from(self, 'value')
