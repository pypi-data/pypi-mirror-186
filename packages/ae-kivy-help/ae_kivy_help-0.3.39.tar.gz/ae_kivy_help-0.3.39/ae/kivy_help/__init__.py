"""
enhance your app with context help, user onboarding, product tours, walkthroughs and tutorials
==============================================================================================

this ae namespace portion integrates context-sensitive help, user onboarding, product tours, walkthroughs and tutorials
into your kivy app.

the generic class :class:`Tooltip` of this portion displays text blocks that are automatically positioned next to any
widget to providing e.g. i18n context help texts or app tour/onboarding info.

:class:`ModalBehavior` is a generic mix-in class that provides modal behavior to any container widget.

the mixin class :class:`HelpBehavior` provided by this namespace portion extends and prepares any Kivy widget to show an
individual help text for it. the :class:`HelpToggler` toggle button widget switches the app's help mode on and off.

the other classes of this portion are used to overlay or augment the app’s user interface with product tours, tutorials,
walkthroughs and user onboarding/welcome features.

the :class:`AnimatedTourMixin` can be mixed-into a tour class that inherits from :class:`~ae.gui_help.TourBase` to
extend it with animation and glsl shader features.

the class :class:`AnimatedOnboardingTour` is providing an app onboarding tour that covers the core features and can be
easily extended with app-specific tour pages.

finally, the class :class:`TourOverlay` is implementing an overlay layout widget to display the animations, shaders,
tour page texts, tooltip text and the navigation buttons of an active/running app tour.


mixing-in modal behavior
========================

to convert a container widget into a modal dialog, add the :class:`ModalBehavior` mix-in class, provided by this ae
namespace portion.

the following code snippet demonstrates a typical implementation::

    class MyContainer(ModalBehavior, BoxLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def open(self):
            self.activate_modal()

        def close(self):
            self.deactivate_modal()


to activate the modal mode call the method :meth:`~ModalBehavior.activate_modal`. the modal mode can be deactivated by
calling the :meth:`~ModalBehavior.deactivate_modal` method.

all touch, mouse and keyboard user interactions will be consumed or filtered after activating the modal mode. therefore
it is recommended to also visually change the GUI while in the modal mode, which has to be implemented by the mixing-in
container widget.

.. hint::
    usage examples of the :class:`ModalBehavior` mix-in are e.g. the classes :class:`TourOverlay` and
    :class:`~ae.kivy_app.FlowPopup`.


generic widget to display help and tour texts
=============================================

the tooltip class :class:`Tooltip` is targeting any widget by pointing with an arrow to it. the position and size of
this widget gets automatically calculated from the targeted widget position and size and the tooltip text size. and if
the screen/window size is not big enough then the tooltip texts get scrollable.

.. hint::
    use cases of the class :class:`Tooltip` are e.g. the help texts prepared and displayed by the method
    :meth:`~ae.gui_help.HelpAppBase.help_display` as well as the "explaining widget" tooltips in an app tour.


help behaviour mixin
====================

to show a i18n translatable help text for a Kivy widget create either a subclass of the widget. the following example
allows to attach a help text to a Kivy :class:`~kivy.uix.button.Button`::

    from kivy.uix.button import Button
    from ae.kivy_help import HelpBehavior

    class ButtonWithHelpText(HelpBehavior, Button):
        ...

alternatively you can archive this via the definition of a new kv-lang rule, like shown underneath::

    <ButtonWithHelpText@HelpBehavior+Button>

.. note::
    to automatically lock and mark the widget you want to add help texts for, this mixin class has to be specified
    as the first inheriting class in the class or rule declaration.

help activation and de-activation
---------------------------------

use the widget :class:`HelpToggler` provided by this namespace portion in your app to toggle the active state of the
help mode.

.. hint::
    the :class:`HelpToggler` is using the low-level touch events to prevent the dispatch of the Kivy events `on_press`,
    `on_release` and `on_dismiss` to allow to show help texts for opened dropdowns and popups.


animated app tours
==================

the mix-in class :class:`AnimatedTourMixin` extends any tour class inherited from :class:`~ae.gui_help.TourBase` with
animations and glsl shaders.

the class :class:`AnimatedOnboardingTour` uses :class:`AnimatedTourMixin` to extend the generic app onboarding tour
class :class:`~ae.gui_help.OnboardingTour` with animations.

to integrate a more app-specific onboarding tour into your app, simply declare a class with a name composed by the name
of your app (:attr:`~ae.gui_app.MainAppBase.app_name`) in camel-case, followed by the suffix `'OnboardingTour'`.


kivy_help portion dependencies
==============================

although this portion depends only on the `Kivy framework <kivy>`_ and the ae namespace portions :mod:`ae.gui_app`,
:mod:`ae.gui_help` and :mod:`ae.kivy_relief_canvas`, it is recommended also include and use the portion
:mod:`ae.kivy_app` to provide context-help-aware widgets.

this namespace portion is a requirement of the :mod:`ae.kivy_app` module and is tight coupled to it. so when you also
include and use the :mod:`ae.kivy_app` for your app, then you only need to specify the :mod:`ae.kivy_app` portion in the
`requirements.txt` files (of the `pip` package installation tool) to automatically integrate also this module. only for
mobile apps built with buildozer you need also to explicitly add this :mod:`ae.kivy_help` portion to the requirements
list in your `buildozer.spec` file.
"""
import os
import traceback
from copy import deepcopy
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

# noinspection PyProtectedMember
from kivy.animation import Animation, CompoundAnimation                                                 # type: ignore
from kivy.app import App                                                                                # type: ignore
from kivy.clock import Clock                                                                            # type: ignore
from kivy.core.window import Window                                                                     # type: ignore
from kivy.input import MotionEvent                                                                      # type: ignore
from kivy.lang import Builder                                                                           # type: ignore
# pylint: disable=no-name-in-module
from kivy.metrics import sp                                                                             # type: ignore
from kivy.properties import (                                                                           # type: ignore
    BooleanProperty, DictProperty, ListProperty, NumericProperty, ObjectProperty, StringProperty)
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior                                     # type: ignore
from kivy.uix.floatlayout import FloatLayout                                                            # type: ignore
from kivy.uix.image import Image                                                                        # type: ignore
from kivy.uix.relativelayout import RelativeLayout                                                      # type: ignore
from kivy.uix.scrollview import ScrollView                                                              # type: ignore
from kivy.uix.textinput import TextInput                                                                # type: ignore
from kivy.uix.widget import Widget                                                                      # type: ignore

from ae.base import snake_to_camel                                                                      # type: ignore
from ae.dynamicod import try_eval                                                                       # type: ignore
from ae.gui_help import (                                                                               # type: ignore
    REGISTERED_TOURS, anchor_layout_x, anchor_layout_y, anchor_points, anchor_spec, help_id_tour_class,
    HelpAppBase, OnboardingTour, TourBase)
from ae.kivy_glsl import ShaderIdType, ShadersMixin                                                     # type: ignore
from ae.kivy_relief_canvas import ReliefCanvas                                                          # type: ignore


__version__ = '0.3.39'


# load/declared help/tour widgets, based-on Kivy core widgets (without any features from ae.kivy_app/widgets.kv)
Builder.load_file(os.path.join(os.path.dirname(__file__), "widgets.kv"))


ANI_SINE_DEEPER_REPEAT3 = \
    Animation(ani_value=0.99, t='in_out_sine', d=0.9) + Animation(ani_value=0.87, t='in_out_sine', d=1.2) + \
    Animation(ani_value=0.96, t='in_out_sine', d=1.5) + Animation(ani_value=0.75, t='in_out_sine', d=1.2) + \
    Animation(ani_value=0.90, t='in_out_sine', d=0.9) + Animation(ani_value=0.45, t='in_out_sine', d=0.6)
""" sine 3 x deeper repeating animation, used e.g. to animate help layout (ae.kivy_help.Tooltip) """
ANI_SINE_DEEPER_REPEAT3.repeat = True


PosSizeCallable = Callable[[Widget, List[float]], Any]
BoundWidgetPropertyId = Tuple[Widget, str, int]
PropagatedAttributes = Tuple[Any, str, Optional[PosSizeCallable]]


class AbsolutePosSizeBinder:
    """ propagate changes of `pos`/`size` properties of one or more widgets plus their parents to attributes/callbacks.

    create an instance of this class passing the widget(s) to observe on change of their pos/size. then call the methods
    :meth:`pos_to_attribute`, :meth:`pos_to_callback`, :meth:`size_to_attribute` and :meth:`size_to_callback` to specify
    the propagation of the changed `pos` and/or `size`. to remove the change propagation call the method :meth:`unbind`.

    .. note:: the `pos` attribute/callback propagations are providing absolute window coordinates.
    """
    def __init__(self, *widgets: Widget, bind_window_size: bool = False):
        """ instantiate binder specifying the monitored widget(s).

        :param widgets:         widget(s) to observe changes of their `pos` and `size` properties. if specified more
                                than one widget then the pos/size coordinates of the rectangle that is enclosing all
                                specified widgets are propagated.
        :param bind_window_size: pass True to propagate pos and size changes if window size changes.
        """
        self.widgets = widgets
        self.relatives: List[Widget] = []
        self.main_app = App.get_running_app().main_app

        self._pos_attributes: List[PropagatedAttributes] = []
        self._size_attributes: List[PropagatedAttributes] = []
        self._pos_callbacks: List[PosSizeCallable] = []
        self._size_callbacks: List[PosSizeCallable] = []
        self._bound_wid_properties: List[BoundWidgetPropertyId] = []
        self._bound_rel_properties: List[BoundWidgetPropertyId] = []

        self._bind()
        if bind_window_size:
            uid = Window.fbind('size', self._rel_size_changed)
            self._bound_rel_properties.append((Window, 'size', uid))

    def _bind(self):
        for wid in self.widgets:
            uid = wid.fbind('pos', self._wid_pos_changed)
            self._bound_wid_properties.append((wid, 'pos', uid))

            uid = wid.fbind('size', self._wid_size_changed)
            self._bound_wid_properties.append((wid, 'size', uid))

            parent = wid.parent
            while parent and parent != parent.parent:
                if isinstance(parent, (ScrollView, RelativeLayout)) and parent not in self.relatives:
                    uid = parent.fbind('pos', self._rel_pos_changed)
                    self._bound_rel_properties.append((parent, 'pos', uid))

                    uid = parent.fbind('size', self._rel_size_changed)
                    self._bound_rel_properties.append((parent, 'size', uid))

                    self.relatives.append(parent)

                parent = parent.parent

    def _propagate(self, wid, value, attributes, callbacks):
        self.main_app.vpo(f"AbsolutePosSizeBinder._propagate({wid}, {value}, {attributes}, {callbacks})")

        for (target, attribute, converter) in attributes:
            setattr(target, attribute, converter(wid, value) if converter else value)

        for callback in callbacks:
            callback(wid, value)

    def _wid_pos_changed(self, wid: Widget, new_pos: List[float]):
        """ propagate `pos` property change to target attributes and subscribed observers.

        :param wid:             bound widget or a ScrollView that is embedding the bound widget, which pos changed.
        :param new_pos:         new position of the bound widget/ScrollView (unused).
        """
        wgs = self.widgets
        new_pos = self.main_app.widgets_enclosing_rectangle(wgs)[:2] if len(wgs) > 1 else wid.to_window(*new_pos)
        self._propagate(wid, new_pos, self._pos_attributes, self._pos_callbacks)

    def _wid_size_changed(self, wid: Widget, new_size: List[float]):
        """ propagate `size` property change to target attributes and subscribed observers.

        :param wid:             bound widget or a ScrollView that is embedding the bound widget, which pos changed.
        :param new_size:        new position of the bound widget/ScrollView (unused).
        """
        wgs = self.widgets
        if len(wgs) > 1:
            new_size = self.main_app.widgets_enclosing_rectangle(wgs)[2:]
        self._propagate(wid, new_size, self._size_attributes, self._size_callbacks)

    def _rel_pos_changed(self, _rel: Widget, _new_pos: list):
        """ propagate `pos` property change of relative/scrollable layout/container.

        :param _rel:            relative layout or a scroll view, embedding bound widget(s), which pos changed.
        :param _new_pos:        new position of the RelativeLayout/ScrollView (unused).
        """
        wid = self.widgets[0]
        self._wid_pos_changed(wid, wid.pos)

    def _rel_size_changed(self, _rel: Widget, _new_size: list):
        """ propagate size change of relative/scrollable layout/container.

        :param _rel:            relative layout or a scroll view, embedding bound widget(s), which size changed.
        :param _new_size:       new size of the RelativeLayout/ScrollView (unused).
        """
        wid = self.widgets[0]
        self._wid_size_changed(wid, wid.size)
        self._wid_pos_changed(wid, wid.pos)     # layout size change mostly does change also the absolute widget pos

    def pos_to_attribute(self, target: Any, attribute: str, converter: Optional[PosSizeCallable] = None):
        """ request the propagation of the changed (absolute) widget(s) position to an object attribute.

        :param target:          the object which attribute will be changed on change of `pos`.
        :param attribute:       the name of the attribute to assign the new/changed absolute position.
        :param converter:       optional pos value converter, returning the final value assigned to the attribute.
        """
        self._pos_attributes.append((target, attribute, converter))

    def pos_to_callback(self, callback: PosSizeCallable):
        """ bind callable to `pos` change event.

        :param callback:        callable to be called when pos changed with the changed widget and pos as arguments.
        """
        self._pos_callbacks.append(callback)

    def size_to_attribute(self, target: Any, attribute: str, converter: Optional[PosSizeCallable] = None):
        """ request the propagation of the changed widget(s) size to an object attribute.

        :param target:          the object which attribute will be changed on change of `size`.
        :param attribute:       the name of the attribute to assign the new/changed size.
        :param converter:       optional pos value converter, returning the final value assigned to the attribute.
        """
        self._size_attributes.append((target, attribute, converter))

    def size_to_callback(self, callback: PosSizeCallable):
        """ bind callable to `size` change event.

        :param callback:        callable to be called when size changed with the changed widget and size as arguments.
        """
        self._size_callbacks.append(callback)

    def unbind(self):
        """ unbind the widget(s) of this binder instance.

        .. note:: this instance can be destroyed after the call of this method. for new bindings create a new instance.
        """
        for (wid, prop, uid) in reversed(self._bound_rel_properties):
            wid.unbind_uid(prop, uid)
        self._bound_rel_properties.clear()

        for (wid, prop, uid) in reversed(self._bound_wid_properties):
            wid.unbind_uid(prop, uid)
        self._bound_wid_properties.clear()

        self.relatives = self._pos_attributes = self._size_attributes = self._pos_callbacks = self._size_callbacks = []
        self.widgets = ()


class ModalBehavior:                                                                                # pragma: no cover
    """ mix-in to provide a modal mode to a container widget.

    to make the container widget's modal state more obvious, add in your container widget an overlay color with an
    alpha between 0.3 and 0.9, together with the following canvas instructions:

        canvas:
            Color:
                rgba: root.my_overlay_color[:3] + [root.my_overlay_color[-1] if root._window else 0]
            Rectangle:
                size: self._window.size if self._window else (0, 0)

    """
    # abstracts provided by Kivy's :class:`~kivy.uix.widget.Widget` class or by the mixing-in container widget class.
    center: List                #: center position of :class:`~kivy.uix.widget.Widget`
    close: Callable             #: method to dismiss the container widget (provided by self/container-widget)
    collide_point: Callable     #: method to detect collisions with other widgets of :class:`~kivy.uix.widget.Widget`
    disabled: bool              #: disabled property of :class:`~kivy.uix.widget.Widget`
    fbind: Callable             #: fast binding method of :class:`~kivy.uix.widget.Widget`
    funbind: Callable           #: fast unbinding method of :class:`~kivy.uix.widget.Widget`

    auto_dismiss = BooleanProperty()
    """ determines if the container is automatically dismissed when the user hits the Esc/Back key or clicks outside it.

    :attr:`auto_dismiss` is a :class:`~kivy.properties.BooleanProperty` and defaults to True.
    """

    _fast_bound: List = []                                  #: list of arg tuples for fbind/funbind
    _touch_started_inside: Optional[bool] = None            #: flag if touch started inside self (the container widget)
    _window = ObjectProperty(allownone=True, rebind=True)   #: internal flag to store main window instance if open

    def activate_modal(self, align_center: bool = True):
        """ activate or renew modal mode for the mixing-in container widget.

        :param align_center:    pass False to prevent the automatic alignment of :attr:`center` to
                                :attr:`~kivy.core.window.Window.center`
                                on reposition or resize of self or on resize of :class:`~kivy.core.window.Window`.
        """
        self.deactivate_modal()

        Window.add_widget(self)
        Window.bind(on_key_down=self._on_key_down)

        if align_center:
            Window.bind(on_resize=self._align_center)

            fast_bind = self.fbind                                                  # pylint: disable=no-member
            self._fast_bound = [('center', self._align_center), ('size', self._align_center)]
            for fast_binding in self._fast_bound:
                fast_bind(*fast_binding)

        self._window = Window

    def _align_center(self, *_args):
        """ reposition container on window resize. """
        if self._window:
            self.center = Window.center

    def deactivate_modal(self):
        """ de-activate modal mode for the mixing-in container. """
        if self._fast_bound:
            fast_unbind = self.funbind                                              # pylint: disable=no-member
            for fast_unbinding in self._fast_bound:
                fast_unbind(*fast_unbinding)
            self._fast_bound = []

            if self._window:
                Window.unbind(on_resize=self._align_center)

        if self._window:
            Window.unbind(on_resize=self._align_center, on_key_down=self._on_key_down)
            Window.remove_widget(self)
        self._window = None

    def _on_key_down(self, _window, key, _scancode, _codepoint, _modifiers):
        """ close/dismiss this popup if back/Esc key get pressed - allowing stacking with DropDown/FlowDropDown. """
        if key == 27 and self.auto_dismiss and self._window:
            if not App.get_running_app().tour_layout:   # prevent close/dismiss by Esc-key if app tour is active/running
                self.close()
            return True
        return False

    def on_touch_down(self, touch: MotionEvent) -> bool:
        """ touch down event handler, prevents the processing of a touch on the help activator widget by this popup.

        :param touch:           motion/touch event data.
        :return:                True if event got processed/used.
        """
        if App.get_running_app().main_app.help_activator.collide_point(*touch.pos):
            return False  # allow help activator button to process this touch down event
            # .. and leave self._touch_started_inside == None to not initiate popup.close/dismiss in on_touch_up
        self._touch_started_inside = self.collide_point(*touch.pos)

        # pylint: disable=superfluous-parens # false positive
        if not (self.disabled if self._touch_started_inside else self.auto_dismiss):
            super().on_touch_down(touch)    # type: ignore # pylint: disable=no-member # false positive

        return True

    def on_touch_move(self, touch):
        """ touch move event handler. """
        if not self.auto_dismiss or self._touch_started_inside:
            # noinspection PyUnresolvedReferences
            super().on_touch_move(touch)    # pylint: disable=no-member # false positive
        return True

    def on_touch_up(self, touch):
        """ touch up event handler. """
        if self.auto_dismiss and self._touch_started_inside is False:
            self.close()
        else:
            # noinspection PyUnresolvedReferences
            super().on_touch_up(touch)      # pylint: disable=no-member # false positive
        self._touch_started_inside = None
        return True


class Tooltip(ScrollView):                                                           # pragma: no cover
    """ semi-transparent and optional click-through container to display help and tour page texts. """
    targeted_widget = ObjectProperty()
    """ target widget to display tooltip text for (mostly a button, but could any, e.g. a layout widget).

    :attr:`targeted_widget` is a :class:`~kivy.properties.ObjectProperty` and defaults to the main app help_activator.
    """

    tip_text = StringProperty()
    """ tooltip text string to display.

    :attr:`tip_text` is a :class:`~kivy.properties.StringProperty` and defaults to an empty string.
    """

    anchor_spe = ObjectProperty()       #: anchor pos and direction, see :data:`~ae.gui_help.AnchorSpecType` (read-only)
    has_tour = BooleanProperty(False)   #: True if a tour exists for the current app flow/help context (read-only)
    tap_thru = BooleanProperty(False)   #: True if user can tap widgets behind/covered by this tooltip win (read-only)
    tour_start_pos = ListProperty()     #: screen position of the optionally displayed tour start button (read-only)
    tour_start_size = ListProperty()    #: size of the optionally displayed tour start button (read-only)

    def __init__(self, **kwargs):
        self.main_app = App.get_running_app().main_app
        self.targeted_widget = self.main_app.help_activator     # set default-value before calling super()
        # init binder before super().__init__ because calls back on_targeted_widget if targeted_widget is in kwargs
        self._targeted_binder = AbsolutePosSizeBinder(self.targeted_widget)

        super().__init__(**kwargs)

    def _actual_pos(self, *_args) -> Tuple[float, float]:
        wid = self.targeted_widget
        win_w, win_h = Window.size
        self.anchor_spe = anc = anchor_spec(*wid.to_window(*wid.pos), *wid.size, win_w, win_h)
        return anchor_layout_x(anc, self.width, win_w), anchor_layout_y(anc, self.height, win_h)

    def collide_tap_thru_toggler(self, touch_x: float, touch_y: float) -> bool:
        """ check if touch is on the tap through toggler pseudo button.

        :param touch_x:         window x position of touch.
        :param touch_y:         window y position of touch.
        :return:                True if user touched the tap through toggler.
        """
        anchor_pts = anchor_points(self.main_app.font_size, self.anchor_spe)

        x_values = tuple(x for idx, x in enumerate(anchor_pts) if not idx % 2)
        min_x, max_x = min(x_values), max(x_values)
        y_values = tuple(x for idx, x in enumerate(anchor_pts) if idx % 2)
        min_y, max_y = min(y_values), max(y_values)

        return min_x <= touch_x < max_x and min_y <= touch_y < max_y

    def collide_tour_start_button(self, touch_x: float, touch_y: float) -> bool:
        """ check if touch is on the tap through toggler pseudo button.

        :param touch_x:         window x position of touch.
        :param touch_y:         window y position of touch.
        :return:                True if user touched the tap through toggler.
        """
        min_x, min_y = self.tour_start_pos
        width, height = self.tour_start_size
        max_x, max_y = min_x + width, min_y + height

        return min_x <= touch_x < max_x and min_y <= touch_y < max_y

    def on_size(self, *_args):
        """ (re-)position help_activator tooltip correctly after help text loading and layout resizing. """
        self.pos = self._actual_pos()

    def on_targeted_widget(self, *_args):
        """ targeted widget changed event handler.

        :param _args:           change event args (unused).
        """
        self._targeted_binder.unbind()

        wid = self.targeted_widget
        self._targeted_binder = twb = AbsolutePosSizeBinder(wid, bind_window_size=True)
        twb.size_to_attribute(self, 'pos', self._actual_pos)
        twb.pos_to_attribute(self, 'pos', self._actual_pos)

    def on_touch_down(self, touch: MotionEvent) -> bool:
        """ check for additional events added by this class.

        :param touch:           motion/touch event data.
        :return:                True if event got processed/used.
        """
        if self.collide_tap_thru_toggler(*touch.pos):
            self.tap_thru = not self.tap_thru
            ret = True
        elif self.has_tour and self.collide_tour_start_button(*touch.pos):
            ret = self.main_app.start_app_tour(help_id_tour_class(self.targeted_widget.help_id))
        elif self.tap_thru or not self.collide_point(*touch.pos):
            ret = False     # if self.tap_thru then make this tooltip widget transparent and let user click through
        else:
            ret = super().on_touch_down(touch)
        return ret


# ============================   help system   ========================================================================

class HelpBehavior:
    """ behaviour mixin class for widgets providing help texts. """
    help_id = StringProperty()
    """ unique help id of the widget.

    The correct identification of each help-aware widget presuppose that the attribute :attr:`~HelpBehavior.help_id` has
    a unique value for each widget instance. This is done automatically for the widgets provided by the module
    :mod:`~ae.kivy_app` by converting the app flow or app state of these widgets into a help id (see e.g. the
    implementation of the class :class:`~ae.kivy_app.FlowButton`).

    :attr:`help_id` is a :class:`~kivy.properties.StringProperty` and defaults to an empty string.
    """

    help_lock = BooleanProperty(False)
    """ this property is True if the help mode is active and this widget is not the help target.

    :attr:`help_lock` is a :class:`~kivy.properties.BooleanProperty` and defaults to the value `False`.
    """

    help_vars = DictProperty()
    """ dict of extra data to displayed/render the help text of this widget.

    The :attr:`~HelpBehavior.help_vars` is a dict which can be used to provide extra context data to dynamically
    generate, translate and display individual help texts.

    :attr:`help_vars` is a :class:`~kivy.properties.DictProperty` and defaults to an empty dict.
    """

    _shader_args = ObjectProperty()     #: shader internal data / id

    # abstract attributes and methods provided by the class to be mixed into
    collide_point: Callable

    def on_touch_down(self, touch: MotionEvent) -> bool:                                    # pragma: no cover
        """ prevent any processing if touch is done on the help activator widget or in active help mode.

        :param touch:           motion/touch event data.
        :return:                True if event got processed/used.
        """
        main_app = App.get_running_app().main_app

        if main_app.help_activator.collide_point(*touch.pos):
            return False        # allow help activator button to process this touch down event

        if self.help_lock and self.collide_point(*touch.pos) and main_app.help_display(self.help_id, self.help_vars):
            return True         # main_app.help_layout is not None

        return super().on_touch_down(touch)                 # type: ignore # pylint: disable=no-member # false positive


class HelpToggler(ReliefCanvas, Image):                                                               # pragma: no cover
    """ widget to activate and deactivate the help mode.

    To prevent dismiss of opened popups and dropdowns at help mode activation, this singleton instance has to:

    * be registered in its __init__ to the :attr:`~ae.gui_help.HelpAppBase.help_activator` attribute and
    * have a :meth:`~HelpToggler.on_touch_down` method that is eating the activation touch event (returning True) and
    * a :meth:`~HelpToggler.on_touch_down` method not passing an activation touch in all DropDown/Popup widgets.

    """
    ani_value = NumericProperty(0.999)      #: float value (range: 0.0 - 1.0) to animate this button in help/tour mode

    def __init__(self, **kwargs):
        """ initialize an instance of this class and also :attr:`~ae.gui_help.HelpAppBase.help_activator`. """
        self.main_app = App.get_running_app().main_app
        self.main_app.help_activator = self
        super().__init__(**kwargs)

    def ani_start(self):
        """ start animation of this button. """
        ANI_SINE_DEEPER_REPEAT3.start(self)

    def ani_stop(self):
        """ stop animation of this button. """
        ANI_SINE_DEEPER_REPEAT3.stop(self)
        self.ani_value = 0.999

    def on_touch_down(self, touch: MotionEvent) -> bool:
        """ touch down event handler to toggle help mode while preventing dismiss of open dropdowns/popups.

        :param touch:           touch event.
        :return:                True if touch happened on this button (and will get no further processed => eaten).
        """
        if self.collide_point(*touch.pos):
            self.main_app.help_activation_toggle()
            return True
        return False


# ============================   app tours   ==========================================================================


DEF_FADE_OUT_APP = 0.39                                             #: default of tour layout fade out app screen factor


PageAnimationType = Tuple[str, Union[Animation, str]]
""" tuple of a widget id string and an :class:`~kivy.animation.Animation` instance/evaluation-expression.

    if the first character of the widget id is a `@` then the :attr:`~kivy.animation.Animation.repeat` attribute of
    the :class:`~kivy.animation.Animation` instance will be set to True. the rest of the widget id string specifies
    the widget to be animated which is either:

    * one of the widgets of the :class:`TourOverlay` layout class, identified by the on of the following strings:
      `'next_but'`, `'page_lbl'`, `'tap_pointer'`, `'prev_but'`, `'title_lbl'`, `'tooltip'`, `'tour_page_texts'`.
    * the explained widget if an empty string is given.
    * the :class:`TourOverlay` layout class instance for any other string (e.g. `'layout'` or `'overlay'`).

    alternative to an animation instance, a evaluation string can be specified. these evaluations allow to use the
    following globals: :class:`~kivy.animation.Animation` (also abbreviated as `A`), :class:`~kivy.clock.Clock`,
    :attr:`~ae.gui_help.TourBase.layout`, :attr:`~kivy.metrics.sp`, :class:`~kivy.core.window.Window` and a
    reference to the instance of this app tour via `tour`.
"""

PageAnimationsType = Tuple[PageAnimationType, ...]  #: tuple of :data:`PageAnimationType` items

WidgetValues = Dict[str, Union[list, tuple, dict, float]]
""" a key of this dict specifies the name, the dict value the value of a widget property/attribute. """


def ani_start_check(ani: Animation, wid: Widget):
    """ start animation if needed else skip animation start.

    :param ani:                 :class:`~kivy.animation.Animation` instance.
    :param wid:                 widget to start/skip the animation for.
    """
    for attr, value in ani.animated_properties.items():
        if getattr(wid, attr) != value:
            ani.start(wid)
            break


def animated_widget_values(wid: Widget, ani: Union[Animation, CompoundAnimation]) -> WidgetValues:
    """ determine from a widget the attribute/property values animated/changed by an animation.

    :param wid:                 widget of which the animation property values will get retrieved.
    :param ani:                 :class:`~kivy.animation.Animation`/:class:`kivy.animation.CompoundAnimation` instance.
    :return:                    dict with widget property names and values.
    """
    wid_values = {}
    for key in ani.animated_properties.keys():
        wid_values[key] = getattr(wid, key)
    return wid_values


def restore_widget_values(wid: Widget, values: WidgetValues):
    """ restore property values of a widget.

    :param wid:                 widget of which the animation property values will get restored.
    :param values:              attribute/property values to restore on the widget.
    """
    for attr, value in values.items():
        setattr(wid, attr, value)


class AnimatedTourMixin:        # (TourBase):
    """ tour class mixin to add individual shaders to the tour layout and their children widgets. """
    # abstracts
    layout: Widget
    main_app: Any
    page_ids: List[str]
    page_idx: int
    setup_texts: Callable

    def __init__(self, main_app: 'HelpAppBase') -> None:
        super().__init__(main_app)                                          # type: ignore # pylint: disable=no-member

        self._added_animations: List[Tuple[Widget, Animation, WidgetValues]] = []
        self._added_shaders: List[Tuple[Widget, ShaderIdType]] = []
        self._explained_binder = AbsolutePosSizeBinder()

        self.pages_animations: Dict[Optional[str], PageAnimationsType] = {}
        """ dict of compound animation instances of the pages of this tour.

        the key of this dict is the page id or None (for animations available in all pages of this tour).
        each value of this dict is of the type :data:`PageAnimationsType`.
        """

        self.pages_shaders: Dict[Optional[str], Tuple[Tuple[str, ShaderIdType], ...]] = {}
        """ dict of widget shaders for the pages of this tour.

        the key of this dict is the page id or None (for shaders available in all pages of this tour).
        each value of this dict is a tuple of tuples of widget id and add_shader()-kwargs.

        the widget id string specifies the widget to which a shader will be added, which is either:

        * one of the widgets of the :class:`TourOverlay` layout class, identified by the on of the following strings:
          `'next_but'`, `'page_lbl'`, `'tap_pointer'`, `'prev_but'`, `'title_lbl'`, `'tooltip'`, `'tour_page_texts'`.
        * the explained widget if an empty string is given.
        * the :class:`TourOverlay` layout class instance for any other string (e.g. `'layout'` or `'overlay'`).

        before the add_shader()-kwargs dict will be passed to the :meth:`~ae.kivy_glsl.ShadersMixin.add_shader` method,
        all their non-string values, specifying as strings, will be evaluated/converted automatically. the evaluation
        provides the following globals: :attr:`~ae.gui_help.TourBase.layout`, :attr:`~kivy.metrics.sp`,
        :class:`~kivy.clock.Clock`, :class:`~kivy.core.window.Window` and the `tour` instance.
        """

        self.switch_next_animations: Dict[Optional[str], PageAnimationsType] = {}
        """ dict of compound animation instances for the next page switch transition of the pages of this tour.

        the key of this dict is the page id or None (for animations available in all pages of this tour).
        each value of this dict is of the type :data:`PageAnimationsType`.
        """

    def _add_animations(self, animations: PageAnimationsType):
        """ add animations to the tour page currently displayed in the tour layout/overlay.

        :param animations:      tuple of tuples of widget id and animation instance/evaluation-string.
        :return:                length of the longest animation added (in seconds).
        """
        max_len = 0.0
        layout = self.layout
        added = []
        for wid_id, anim in animations:
            if isinstance(anim, str):
                glo_vars = self.main_app.global_variables(layout=layout, sp=sp, tour=self,
                                                          A=Animation, Animation=Animation, Clock=Clock, Window=Window)
                anim = try_eval(anim, glo_vars=glo_vars)
            if wid_id[0:1] == '@':
                wid_id = wid_id[1:]
                anim.repeat = True
            wid = layout.ids.get(wid_id, layout) if wid_id else layout.explained_widget
            start_values = animated_widget_values(wid, anim)
            anim.start(wid)
            added.append((wid, anim, start_values))

            if anim.duration > max_len:
                max_len = anim.duration

        self._added_animations.extend(added)

        return max_len

    def next_page(self):
        """ overridden to add demo animations before/on switch to the next tour page. """
        page_id = self.page_ids[self.page_idx]
        next_animations = self.switch_next_animations.get(None, ()) + self.switch_next_animations.get(page_id, ())
        anim_length = self._add_animations(next_animations)
        if anim_length:
            # noinspection PyUnresolvedReferences
            self.main_app.call_method_delayed(anim_length + 0.123, super().next_page)       # pylint: disable=no-member
        else:
            # noinspection PyUnresolvedReferences
            super().next_page()                                                             # pylint: disable=no-member

    def setup_explained_widget(self) -> list:
        """ overridden to bind pos/size of explained widget(s) to the tour layout/overlay placeholder.

        :return:                list of explained widget instances.
        """
        self._explained_binder.unbind()

        # noinspection PyUnresolvedReferences
        widgets = super().setup_explained_widget()                          # type: ignore # pylint: disable=no-member

        layout = self.layout
        exp_wid = layout.explained_widget
        self._explained_binder = ebi = AbsolutePosSizeBinder(*widgets, bind_window_size=True)
        ebi.size_to_attribute(layout, 'explained_size')
        ebi.pos_to_attribute(layout, 'explained_pos')
        if exp_wid is layout.ids.explained_placeholder:
            ebi.size_to_attribute(exp_wid, 'size')
            ebi.pos_to_attribute(exp_wid, 'pos')

        return widgets

    def setup_page_shaders_and_animations(self):
        """ setup shaders and animations of the current page.

        specified in :attr:`~AnimatedTourMixin.pages_shaders` and :attr:`~AnimatedTourMixin.pages_animations`.
        """
        def _evaluated_shader_kwargs() -> dict:
            tour_shader_kwargs = deepcopy(shader_kwargs)    # pylint: disable=undefined-loop-variable
            glo_vars = self.main_app.global_variables(layout=layout, sp=sp, tour=self, Clock=Clock, Window=Window)
            for key, arg in tour_shader_kwargs.items():
                if isinstance(arg, str) and key not in ('add_to', 'render_shape', 'shader_code', 'shader_file'):
                    tour_shader_kwargs[key] = try_eval(arg, glo_vars=glo_vars)
            return tour_shader_kwargs

        page_id = self.page_ids[self.page_idx]
        page_shaders = self.pages_shaders.get(None, ()) + self.pages_shaders.get(page_id, ())
        layout = self.layout
        added = []
        for wid_id, shader_kwargs in page_shaders:
            wid = layout.ids.get(wid_id, layout) if wid_id else layout.explained_widget
            added.append((wid, wid.add_shader(**_evaluated_shader_kwargs())))
        self._added_shaders = added

        self._add_animations(self.pages_animations.get(None, ()) + self.pages_animations.get(page_id, ()))

    def setup_layout(self):
        """ overridden to set up animations and shaders of the current tour page. """
        # noinspection PyUnresolvedReferences
        super().setup_layout()                                                              # pylint: disable=no-member
        Clock.tick()                # update position of explained widget
        self.setup_page_shaders_and_animations()

    def simulate_text_input(self, text_input: TextInput, text_to_delay: str,
                            text_to_insert: str = "", deltas: Tuple[float, ...] = (1.8, 0.6, 0.3)):
        """ simulate the typing of texts by a user entered into an explained TextInput widget of a tour page.

        :param text_input:      text input widget, either of type :class:`~kivy.textinput.TextInput` or
                                :class:`~ae.kivy_app.FlowInput`.
        :param text_to_delay:   text string to be inserted delayed by the seconds specified in deltas[0].
        :param text_to_insert:  text string to be inserted directly into the passed text input widget.
        :param deltas:          delay deltas in seconds between each character to simulate text inputted by a user.
                                first delta default is a bit higher to finish navigation button y-pos-animation.
        """
        if text_input.get_root_window():
            for char_to_insert in text_to_insert:
                if text_input.interesting_keys.get(ord(char_to_insert), None) == 'backspace':   # chr(8)
                    text_input.do_backspace()
                else:
                    text_input.insert_text(char_to_insert)

            if text_to_delay:
                next_delay = deltas[0]
                self.main_app.call_method_delayed(next_delay, self.simulate_text_input, text_input, text_to_delay[1:],
                                                  text_to_insert=text_to_delay[0], deltas=deltas[1:] + (next_delay, ))

    def tap_animation(self, wid_id: str = '', pos_delay: float = 2.34,
                      press_delay: float = 0.69, release_delay: float = 0.39) -> PageAnimationType:
        """ create a compound animation instance simulating a user touch/tap on the specified widget.

        :param wid_id:          specifies the widget to be tap simulated: either a widget id string (first item of the
                                :data:`PageAnimationType` tuple), or (if prefixed with a column character) tap/focus/
                                state id of a widget, or an empty string (specifies the currently explained widget).
        :param pos_delay:       time in seconds to position/move the pointer from the next button to the widget.
        :param press_delay:     time in seconds of the button press simulation animation.
        :param release_delay:   time in seconds of the button release simulation animation.
        :return:                compound animation instance simulating a tap.

        .. note:: use as animation evaluation expression, to get the widget values on setup-time of the page (not tour).
        """
        layout = self.layout
        if wid_id[0:1] == ':':
            tap_wid = self.main_app.widget_by_flow_id(wid_id[1:])
        else:
            tap_wid = layout.ids.get(wid_id, layout) if wid_id else layout.explained_widget
        tap_wid_x, tap_wid_y = tap_wid.to_window(*tap_wid.center)
        nxt_wid = layout.ids.next_but
        poi_wid = layout.ids.tap_pointer
        poi_w, poi_h = poi_wid.size
        poi_x = tap_wid_x - poi_w * 13.0 / 30.0    # - tap_pointer.png index finger x position offset
        poi_y = tap_wid_y - poi_h * 29.0 / 30.0

        poi_wid.center = nxt_wid.center
        ani = Animation(x=poi_x, y=poi_y, width=poi_w, height=poi_h, opacity=1.0, d=pos_delay, t='in_sine') \
            + Animation(x=poi_x + poi_w * 0.156, y=poi_y + poi_h * 0.153,
                        width=poi_w * 0.69, height=poi_h * 0.69, d=press_delay, t='out_sine')
        poi_values = animated_widget_values(poi_wid, ani)

        if isinstance(tap_wid, ButtonBehavior):
            release_ani = Animation(x=poi_x, y=poi_y, width=poi_w, height=poi_h, opacity=0.39, d=release_delay - 0.03)

            def _touched_anim():
                wid_state = tap_wid.state
                tap_wid.state = 'normal' if wid_state == 'down' else 'down'
                if not isinstance(tap_wid, ToggleButtonBehavior):
                    release_ani.start(poi_wid)
                    self.main_app.call_method_delayed(
                        release_delay, lambda *_args: (setattr(tap_wid, 'state', wid_state), self.setup_texts()))

            ani.bind(on_complete=lambda *_args: (_touched_anim(), self.setup_texts()))
            release_ani.bind(on_complete=lambda *_args: restore_widget_values(poi_wid, poi_values))

        return ani

    def teardown_shaders_and_animations(self):
        """ teardown all added shaders and animations of current tour page (including switch next page animations). """
        for wid, anim, start_values in reversed(self._added_animations):
            anim.stop(wid)
            restore_widget_values(wid, start_values)
        self._added_animations = []

        for wid, shader_id in reversed(self._added_shaders):
            wid.del_shader(shader_id)
        self._added_shaders = []

    def teardown_app_flow(self):
        """ overridden to teardown the animations of the current/last-shown tour page. """
        self.teardown_shaders_and_animations()
        # noinspection PyUnresolvedReferences
        super().teardown_app_flow()                                                         # pylint: disable=no-member


class AnimatedOnboardingTour(AnimatedTourMixin, OnboardingTour):
    """ onboarding tour, extended with animations and glsl shaders. """
    def __init__(self, main_app: 'HelpAppBase') -> None:
        super().__init__(main_app)

        self._bound = None

        self.pages_animations.update({
            None: (
                ('@root',
                 Animation(ani_value=0.999, t='in_out_sine', d=30) + Animation(ani_value=0.0, t='in_out_sine', d=9)),
            ),
            '': (
                ('next_but',
                 "A(font_size=layout.font_height, t='in_out_sine', d=24) + "
                 "A(font_size=layout.main_app.framework_app.min_font_size, t='in_out_sine', d=3) + "
                 "A(font_size=layout.main_app.framework_app.max_font_size, t='in_out_sine', d=6) + "
                 "A(font_size=layout.font_height, t='in_out_sine', d=3)"),
            ),
            'layout_font_size': (
                ('@',
                 "A(value=min(layout.main_app.font_size * 1.5, layout.main_app.framework_app.max_font_size),"
                 "  t='in_out_sine', d=12.9) + "
                 "A(value=max(layout.main_app.font_size * 0.6, layout.main_app.framework_app.min_font_size),"
                 "  t='in_out_sine', d=4.2)"),
            )
        })

        self.pages_shaders.update({
            '': (
                ('layout', dict(
                    alpha="lambda: 0.39 * layout.ani_value",
                    center_pos="lambda: list(map(float, layout.ids.next_but.center))",
                    shader_code="=plunge_waves",
                    time="lambda: -Clock.get_boottime()",
                    tint_ink=[0.21, 0.39, 0.09, 0.9],
                )),
                ('tour_page_texts', dict(add_to='before')),
                ('next_but', dict(
                    add_to='before',
                    alpha="lambda: 0.3 + layout.ani_value / 3",
                    render_shape='Ellipse',
                    shader_code='=plunge_waves',
                )),
            ),
            'page_switching': (
                ('layout', dict(
                    alpha="lambda: 0.39 * layout.ani_value",
                    center_pos="lambda: list(map(float, layout.ids.prev_but.center))",
                    shader_code="=plunge_waves",
                    time="lambda: -Clock.get_boottime()",
                    tint_ink=[0.21, 0.39, 0.09, 0.9],
                )),
                ('tour_page_texts', dict(add_to='before')),
                ('prev_but', dict(
                    add_to='before',
                    alpha="lambda: 0.12 + layout.ani_value / 3",
                    render_shape='Ellipse',
                    shader_code='=plunge_waves',
                    time="lambda: -Clock.get_boottime()",
                )),
            ),
            'tip_help_intro': (
                ('tour_page_texts', dict(
                    add_to='before',
                    alpha="lambda: 0.12 + layout.ani_value / 3",
                    render_shape='RoundedRectangle',
                    shader_code='=worm_whole',
                    tint_ink=[0.021, 0.039, 0.009, 0.9],
                )),
                ('prev_but', dict(
                    add_to='before',
                    alpha="lambda: 0.12 + layout.ani_value / 3",
                    render_shape='Ellipse',
                    shader_code='=worm_whole',
                    time="lambda: -Clock.get_boottime()",
                )),
                ('next_but', dict(
                    add_to='before',
                    alpha="lambda: 0.12 + layout.ani_value / 3",
                    render_shape='Ellipse',
                    shader_code='=worm_whole',
                )),
            ),
            'tip_help_tooltip': (
                ('prev_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    shader_code='=fire_storm',
                    tint_ink=[0.81, 0.39, 0.09, 0.39],
                    time="lambda: -Clock.get_boottime()",
                )),
                ('next_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    shader_code='=fire_storm',
                    tint_ink=[0.03, 0.03, 0.9, 0.39],
                )),
            ),
            'responsible_layout': (
                ('prev_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    shader_code='=colored_smoke',
                    time="lambda: -Clock.get_boottime()",
                )),
                ('next_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    shader_code='=colored_smoke',
                )),
            ),
            'layout_font_size': (
                ('prev_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    shader_code='=circled_alpha',
                    tint_ink=[0.51, 0.39, 0.9, 0.999],
                )),
                ('next_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    shader_code='=circled_alpha',
                    tint_ink=[0.81, 0.39, 0.9, 0.999],
                )),
            ),
            'tour_end': (
                ('tour_page_texts', dict(add_to='before')),
                ('prev_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    tint_ink=[0.51, 0.39, 0.9, 0.999],
                    time="lambda: -Clock.get_boottime()",
                )),
                ('next_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    tint_ink=[0.81, 0.39, 0.9, 0.999],
                )),
            ),
        })

    def next_page(self):
        """ overriding to remove next button size animation only visible in the first tour after app re/start. """
        layout = self.layout
        layout.ani_value = 0.0
        super().next_page()
        if self.last_page_id == '' and self.pages_animations.pop('', False):
            Animation(font_size=layout.font_height).start(layout.ids.next_but)  # set font size back to original value

    def setup_layout(self):
        """ overridden to update layout texts if app window/screen orientation (app.landscape) changes. """
        super().setup_layout()
        page_id = self.page_ids[self.page_idx]
        if page_id == 'responsible_layout':
            self._bound = self.main_app.framework_app.fbind('landscape', lambda *_args: self.setup_texts())
        elif page_id == 'layout_font_size':
            self._bound = self._added_animations[-1][1].fbind('on_progress', lambda *_args: self.setup_texts())

    def teardown_shaders_and_animations(self):
        """ overridden to unbind setup_texts() on leaving the responsible_layout tour page. """
        if self._bound:
            page_id = self.page_ids[self.page_idx]
            if page_id == 'responsible_layout':
                self.main_app.framework_app.unbind_uid('landscape', self._bound)
            elif page_id == 'layout_font_size':
                # noinspection PyUnresolvedReferences
                self._added_animations[-1][1].unbind_uid('on_progress', self._bound)
            self._bound = None

        super().teardown_shaders_and_animations()


class TourOverlay(ModalBehavior, ShadersMixin, FloatLayout):
    """ tour layout/view overlay singleton class to display an active/running modal app tour with optional glsl shaders.
    """
    ani_value = NumericProperty()
    """ animated float value between 0.0 and 1.0, used e.g. by :attr:`AnimatedTourMixin.pages_animations`.

    :attr:`ani_value` is a :class:`~kivy.properties.NumericProperty` and is read-only.
    """

    explained_pos = ListProperty([-9, -9])
    """ window position (absolute x, y window coordinates) of the targeted/explained/highlighted widget.

    :attr:`explained_pos` is a :class:`~kivy.properties.ListProperty` and is read-only.
    """

    explained_size = ListProperty([0, 0])
    """ widget size (width, height) of the targeted/explained/highlighted widget.

    :attr:`explained_size` is a :class:`~kivy.properties.ListProperty` and is read-only.
    """

    explained_widget = ObjectProperty()
    """ explained widget instance on actual tour (page).

    :attr:`explained_widget` is a :class:`~kivy.properties.ObjectProperty` and is read-only.
    """

    fade_out_app = NumericProperty(DEF_FADE_OUT_APP)
    """ fade out app screen factor: 0.0 prevents fade out of the areas around TourPageTexts and the explained widget.

    1.0 results in maximum app screen fade out. configurable for individual tour page via `page_data['fade_out_app']`.

    :attr:`fade_out_app` is a :class:`~kivy.properties.NumericProperty` and defaults to 0.39.
    """

    label_height = NumericProperty()
    """ height in pixels of the page text labels and text lines.

    :attr:`label_height` is a :class:`~kivy.properties.NumericProperty` and is read-only.
    """

    navigation_disabled = BooleanProperty()
    """ if this flag is True then the back/next buttons in the tour layout/overlay are disabled.

    :attr:`navigation_disabled` is a :class:`~kivy.properties.BooleanProperty` and is read-only.
    """

    tour_instance = ObjectProperty()
    """ holding the :class:`~ae.gui_help.TourBase` instance of the current tour, initialized by :meth:`.start_tour`.

    :attr:`tour_instance` is a :class:`~kivy.properties.ObjectProperty` and is read-only.
    """

    def __init__(self, main_app: HelpAppBase, tour_class: Optional[Type['TourBase']] = None, **kwargs):
        """ prepare app and tour overlay (singleton instance of this class) to start tour.

        :param main_app:        main app instance.
        :param tour_class:      optional tour (pages) class, default: tour class of current help id or OnboardingTour.
        """
        self.main_app = main_app
        main_app.vpo("TourOverlay.__init__")

        self._tooltip_animation = None
        self.auto_dismiss = False
        self.explained_widget = main_app.help_activator             # assign dummy init widget to prevent None errors

        super().__init__(**kwargs)

        if main_app.help_layout:
            main_app.help_activation_toggle()   # deactivate help mode if activated

        self.start_tour(tour_class)

    def next_page(self):
        """ switch to next tour page. """
        self.main_app.vpo("TourOverlay.next_page")
        self.navigation_disabled = True
        self.tour_instance.cancel_auto_page_switch_request()
        self.tour_instance.next_page()

    def on_navigation_disabled(self, *_args):
        """ navigation button disabled change event, used to hide page texts (blend-in-anim in page_updated()). """
        if self.navigation_disabled:
            ani = Animation(opacity=0.123, d=0.6)
            ids = self.ids
            ani_start_check(ani, ids.tour_page_texts)
            ani_start_check(ani, ids.prev_but)
            ani_start_check(ani, ids.next_but)
            ani_start_check(ani, ids.stop_but)

    def page_updated(self):
        """ callback from :meth:`~TourBase.setup_layout` for UI-specific patches, after tour layout/overlay setup. """
        tooltip = self.ids.tooltip
        win_height = Window.height
        nav_y = self.label_height * 1.29    # default pos_y of navigation bar with prev/next buttons
        if self.main_app.widget_visible(tooltip):
            exp_y = self.explained_pos[1]
            pos1 = min(exp_y, tooltip.y)
            pos2 = max(exp_y + self.explained_size[1], tooltip.top)
            if pos1 < win_height - pos2:
                nav_y = max(nav_y + pos2, win_height - self.ids.tour_page_texts.height)

        ani_kwargs = dict(t='in_out_sine', d=2.1)
        ani_start_check(Animation(fade_out_app=self.tour_instance.page_data.get('fade_out_app', DEF_FADE_OUT_APP),
                                  navigation_pos_hint_y=nav_y / win_height,
                                  **ani_kwargs),
                        self)
        ani = Animation(opacity=1.0, **ani_kwargs)
        ani_start_check(ani, self.ids.tour_page_texts)
        ani_start_check(ani, self.ids.prev_but)
        ani_start_check(ani, self.ids.next_but)
        ani_start_check(ani, self.ids.stop_but)

        self.navigation_disabled = False

    def prev_page(self):
        """ switch to previous tour page. """
        self.main_app.vpo("TourOverlay.prev_page")
        self.navigation_disabled = True
        self.tour_instance.cancel_auto_page_switch_request()
        self.tour_instance.prev_page()

    def start_tour(self, tour_cls: Optional[Type[TourBase]] = None) -> bool:
        """ reset app state and prepare tour to start.

        :param tour_cls:        optional tour (pages) class, default: tour of currently shown help id or OnboardingTour.
        :return:                True if tour exists and got started.
        """
        main_app = self.main_app
        if not tour_cls:
            tour_cls = help_id_tour_class(main_app.displayed_help_id) \
                or REGISTERED_TOURS.get(snake_to_camel(main_app.app_name) + 'OnboardingTour') \
                or AnimatedOnboardingTour
        main_app.vpo(f"TourOverlay.start_tour tour_cls={tour_cls.__name__}")

        try:
            main_app.change_observable('tour_layout', self)             # set tour layout
            # noinspection PyArgumentList
            self.tour_instance = tour_instance = tour_cls(main_app)     # initialize tour instance
            tour_instance.start()                                       # start tour
            main_app.help_activator.ani_start()
        except Exception as ex:
            main_app.po(f"TourOverlay.start_tour exception {ex}")
            traceback.print_exc()
            main_app.help_activator.ani_stop()
            main_app.change_observable('tour_layout', None)             # reset tour layout
            return False

        ani = Animation(ani_value=0.3, t='in_out_sine', d=6) + Animation(ani_value=0.999, t='in_out_sine', d=3)
        ani.repeat = True
        ani.start(self.ids.tooltip)
        self._tooltip_animation = ani

        self.activate_modal()

        return True

    def stop_tour(self):
        """ stop tour and restore the initially backed-up app state. """
        main_app = self.main_app
        main_app.vpo("TourOverlay.stop_tour")

        self.navigation_disabled = True

        if self._tooltip_animation:
            self._tooltip_animation.stop(self.ids.tooltip)

        if self.tour_instance:
            self.tour_instance.stop()
        else:
            main_app.po("TourOverlay.stop_tour error: called without tour instance")

        main_app.help_activator.ani_stop()
        main_app.change_observable('tour_layout', None)    # set app./main_app.tour_layout to None

        self.deactivate_modal()
