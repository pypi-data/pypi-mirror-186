'''
All the mixin classes, to be reused internally
'''
import logging
import warnings
import typing
from dataclasses import dataclass
import collections
from functools import cached_property, partial

from . import fn
from . import model
from . import var as tkmilan_var  # Possible name alias
from . import autolayout
from . import spec

import tkinter as tk

ProxyWidgetT = typing.TypeVar('ProxyWidgetT', bound='MixinWidget')
if typing.TYPE_CHECKING:
    from . import RootWindow

logger = logging.getLogger(__name__)

WEIRD_WIDGET_NAME = [  # Weird Widget `dir` names, these cause trouble
    '_last_child_ids',
    'wroot',
]


# Technically a model, but internal
@dataclass
class ContainerState:
    '''Full container state.

    Args:
        swidgets: Single Widgets
        cwidgets: Container Widgets
        variables: Attached Variables
        wvariables: Mapping VariableID -> Variable object
        vwidgets: Mapping VariableID -> Widget Name list
        vid_upstream: Set of upstream VariableID
    '''
    swidgets: 'typing.Mapping[str, SingleWidget]'
    cwidgets: 'typing.Mapping[str, ContainerWidget]'
    variables: 'typing.Mapping[str, tkmilan_var.Variable]'
    wvariables: 'typing.Mapping[str, tkmilan_var.Variable]'
    vwidgets: typing.Mapping[str, typing.Sequence[str]]
    vid_upstream: typing.Set[str]


class MixinState:
    '''Mixin for all stateful widgets.'''

    wstate_static: bool = True
    '''
    Define if the `MixinState.setup_state` cache is static. or a callable for dynamic
    calculations.

    See `stateSetup`.
    '''

    isNoneable: typing.Optional[bool] = None
    '''Define if a `None` result leads to skipping this widget on the state result.

    This applies to both static and dynamic state calculations. Defaults to
    `None`, so that it can be overriden by subclasses.

    For dynamic calculations, the results for some widgets might vary depending
    on where the root state starts, so they will be unpredictable. When the
    state is taken as a whole (the simple usage), it is predictable.

    Note:
        The default `None` value for this variable is invalid. The subclass
        **must** define this.
    '''

    def setup_state(self):
        '''Define an object that will be cached forever.

        This can have a static object, or a dynamic `callable`.

        See `MixinState.wstate_static`, `stateSetup`.
        '''
        raise NotImplementedError

    @cached_property
    def stateSetup(self):
        '''Obtain the state setup.

        This takes into account the `wstate_static` flag, producing a static object
        or a callable.

        This should always be used, `MixinState.setup_state` is only a definition.
        '''
        assert self.isNoneable is not None, f'{self} needs `isNoneable` choice'
        if self.wstate_static is True:
            return self.setup_state()
        else:
            return self.setup_state

    def state_get(self, *args, **kwargs):
        '''Define how to get the widget state.

        The kwargs are only passed for Dynamic State widgets
        '''
        raise NotImplementedError

    '''
    Define how to set the widget state.

    The kwargs are only passed for Dynamic State widgets
    '''
    def state_set(self, state, substate: bool, **kwargs):
        raise NotImplementedError

    # Wrapper functions for the property
    def wstate_get(self, *args, **kwargs):
        return self.state_get(*args, **kwargs)

    def wstate_set(self, state, *args, substate=False, **kwargs):
        return self.state_set(state, *args, substate=substate, **kwargs)

    wstate = property(wstate_get, wstate_set, doc='Widget State')


class MixinStateSingle(MixinState):
    '''
    Mixin class for single widgets.

    Note:
        When subclassing this, define `MixinState.setup_state` to return the
        variable containing the widget state.
    '''
    wstate_static: bool = True

    def state_get(self):
        return self.stateSetup.get()

    def state_set(self, state, substate):
        if __debug__:
            if substate is True:  # Just skip it silently?
                warnings.warn("`substate` doesn't apply here", stacklevel=3)
        self.stateSetup.set(state)


class MixinStateContainer(MixinState):
    '''Mixin class for container widgets.

    To ignore a container state, define this on the subclass:

    .. code:: python

        def setup_state(self, **kwargs):
            return {}

    Note:
        When subclassing this, define `MixinState.setup_state` to return a
        dictionary mapping subwidget identifier to `WidgetDynamicState`.
    '''
    wstate_static: bool = False
    wstate_single: typing.Optional[str] = None
    '''
    Mark the container state as "single", including only the state for this child.

    Should only be enabled where there is a single child element, this is
    verified when getting the value. Use `MixinWidget.ignoreContainerState` to
    ignore other widgets.

    This creates no performance improvements, it is only useful to simplify the
    state.
    '''

    def state_get(self, **kwargs):
        state = {}
        for identifier, wds in self.stateSetup(**kwargs).items():
            result = wds.getter()
            if wds.noneable and result is None:
                pass  # Skip
            else:
                state[identifier] = result
        if self.wstate_single is None:
            # - Multiple WState
            if len(state) == 0:
                return None
            else:
                if __debug__:
                    if len(state) == 1:
                        # TODO: Use `warnings.warn`, but this is used from an `after` function, the trace is lost.
                        logger.warning('%s: This widget can be marked "wstate_single": `%s`', self, list(state)[0])
                return state
        else:
            # - Single WState (wstate_single)
            assert len(state) == 1, f'{self}: Invalid "wstate_single" marking, {len(state)} elements'
            return state[self.wstate_single]

    def state_set(self, state, substate, **kwargs) -> None:
        # # Debug container state flow
        # self_names = None
        # if __debug__:
        #     self_names = str(self).split('.')[1:]
        #     logger.debug('%s: %s%s',
        #                  '>' * len(self_names),
        #                  self,
        #                  '' if self.wstate_single is None else f' [{self.wstate_single}]',
        #                  )
        for identifier, wds in self.stateSetup(**kwargs).items():
            # Skip State Setup:
            # - "noneable" and the state is None
            if wds.noneable and state is None:
                skip = True
            else:
                if self.wstate_single is None:
                    # - Multiple WState
                    #   - Check for "noneable"
                    #   - Check for (substate=True)
                    skip = (substate or wds.noneable) and identifier not in state
                else:
                    # - Single WState (wstate_single)
                    skip = self.wstate_single != identifier
            if skip:
                # if __debug__:
                #     logger.debug('%s|> Skip "%s"', ' ' * len(self_names), identifier)
                pass
            else:
                # if __debug__:
                #     logger.debug('%s|>  Set "%s"', ' ' * len(self_names), identifier)
                if self.wstate_single:
                    widget_state = state
                else:
                    widget_state = state[identifier]
                if wds.container:
                    wds.setter(widget_state, substate, **kwargs)
                else:
                    wds.setter(widget_state)


class MixinWidget:
    '''Parent class of all widgets.

    Args:
        gkeys: Append widget-specific `GuiState` keys to common list
            `model.GUI_STATES_common`.

    .. autoattribute:: _bindings
    .. autoattribute:: _tidles
    '''

    wparent: 'typing.Optional[MixinWidget]' = None
    '''A reference to the parent widget.'''
    gkeys: typing.FrozenSet[str]
    '''The supported `GuiState` keys.'''
    isHelper: bool
    '''Marker that indicates the widget is not part of the automatic state.'''
    ignoreContainerState: bool = False
    '''Ignore this widget's state when included on a container.'''
    styleID: typing.Optional[str] = None
    '''StyleID for this widget. See `RootWindow.styleIDs`.'''
    wproxy: 'typing.Optional[MixinWidget]' = None
    '''Link to the corresponding proxy widget, if exists.

    See Also:
        The base `ProxyWidget` class.
    '''
    proxee: 'typing.Optional[MixinWidget]' = None
    '''Link to the corresponding proxied widget, if exists.

    See Also:
        The base `ProxyWidget` class.
    '''
    _bindings: typing.MutableMapping[str, model.Binding]
    '''Store all widget `Binding` objects, keyed by name (see `binding`).'''
    _tidles: typing.MutableMapping[str, model.TimeoutIdle]
    '''Store some widget `TimeoutIdle` objects, keyed by name (see `tidle`).'''

    def __init__(self, *, gkeys: typing.Optional[typing.Iterable[str]] = None):
        self.isHelper: bool = getattr(self, 'isHelper', False)
        self._bindings = {}
        self._tidles = {}
        gk = set(model.GUI_STATES_common)
        if gkeys is not None:
            gk.update(gkeys)
        self.gkeys = frozenset(gk)

    @cached_property
    def wroot(self) -> 'RootWindow':
        '''Get the root widget, directly.

        Does not use the ``wparent`` property to crawl the widget tree to the
        top, so that it might be called before that setup is done (during setup
        of lower widgets, for example).
        '''
        assert isinstance(self, (tk.Widget, tk.Tk)), f'{self} is not a valid widget'
        widget = self.nametowidget('.')
        if __debug__:
            from . import RootWindow  # For typechecking
        assert isinstance(widget, RootWindow)
        return widget

    def wroot_search(self) -> 'RootWindow':
        '''Alternative to `wroot` that crawls the widget tree.

        Use the `wparent` proprety.

        See Also:
            `wroot`: Simpler alternative to this function, crawling the widget
            tree. Requires all widgets to be stable.
        '''
        if self.wparent is None:
            # This might be triggered if called before all widgets are stable
            if __debug__:
                from . import RootWindow  # For typechecking
            assert isinstance(self, RootWindow), f'Invalid "root" widget: {self!r}'
            return self
        else:
            return self.wparent.wroot_search()

    def binding(self, sequence: str, *args, key: typing.Optional[str] = None, immediate: bool = True, **kwargs) -> model.Binding:
        '''Create a `model.Binding` for this widget.

        Stores all widget bindings on a per-instance dictionary, for later
        usage. Note that all dictionary keys must be different. For the same
        bindings on a single widget, this requires passing the ``key``
        argument.

        See the ``Tk`` `bind <https://www.tcl.tk/man/tcl/TkCmd/bind.html>`_ documentation.

        Args:
            key: Optional. Defaults to the ``sequence`` itself. Useful to
                support multiple bindings on the same sequence.
            immediate: Passed to the upstream object, default to enabling the
                binding on creation. This is the opposite from upstream.

        All other arguments are passed to the `model.Binding` object.
        '''
        name = key or sequence
        if name in self._bindings:
            raise ValueError(f'Repeated Binding for "{sequence}" in {self!r}. Change the "key" parameter.')
        self._bindings[name] = model.Binding(self, sequence, *args, immediate=immediate, **kwargs)
        return self._bindings[name]

    def tidle(self, action: typing.Callable, *args, key: typing.Optional[str] = None, **kwargs) -> model.TimeoutIdle:
        '''Create a `model.TimeoutIdle` for this widget.

        Stores all idle timeouts created using this function on a per-instance
        dictionary, for later usage. If the ``action`` is not a "real"
        function, this requires passing the ``key`` argument.

        Args:
            key: Optional. Defaults to the ``action`` name.

        All other arguments are passed to `model.Binding` object.
        '''
        name = key or action.__name__
        if name in self._tidles:
            raise ValueError(f'Repeated TimeoutIdle for "{name}" in {self!r}.')
        self._tidles[name] = model.TimeoutIdle(self, action, *args, *kwargs)
        return self._tidles[name]

    @property
    def size_vroot(self) -> 'model.PixelSize':
        '''The VirtualRoot size.

        This is a global property, but it's available in every widget.
        '''
        assert isinstance(self, (tk.Widget, tk.Tk)), f'{self} is not a valid tkinter.Widget'
        return model.PixelSize(
            width=self.winfo_vrootwidth(),
            height=self.winfo_vrootheight(),
        )

    @property
    def size_screen(self) -> 'model.PixelSize':
        '''The screen size.

        This is a global property, but it's available in every widget.
        '''
        assert isinstance(self, (tk.Widget, tk.Tk)), f'{self} is not a valid tkinter.Widget'
        return model.PixelSize(
            width=self.winfo_screenwidth(),
            height=self.winfo_screenheight(),
        )

    def setup_grid(self, fmt: typing.Union[str, model.GridCoordinates], **kwargs) -> None:
        '''Configure the grid for the current widget.

        ``fmt`` can be given as a `model.GridCoordinates`, or as a single
        `str`, to be parsed by `model.GridCoordinates.parse`.

        Args:
            fmt: The grid configuration format. Specified above.
            kwargs: Passed upstream

        See Also:
            `wgrid`: Get the current widget grid coordinates.
        '''
        assert isinstance(self, (tk.Widget, tk.Tk)), f'{self} is not a valid tkinter.Widget'
        if isinstance(fmt, str):
            fmt = model.GridCoordinates.parse(fmt)
        kwargs.update(fmt.dict())
        self.grid(**kwargs)

    @property
    def wgrid(self) -> typing.Optional[model.GridCoordinates]:
        '''Get the widget grid coordinates, if the widget is visible.

        Returns:
            Return a `model.GridCoordinates` object with the widget information. If
            the wiget was hidden, return `None`.

            This is also available for the root widget (`wroot`) for
            completeness, but that doesn't really correspond to any grid,
            return `None`.

        See Also:
            `setup_grid`: Change the widget grid coordinates.
        '''
        if self == self.wroot:
            assert isinstance(self, tk.Tk)
            return None
        else:
            assert isinstance(self, tk.Widget), f'{self} is not a valid tkinter.Widget'
            # If the grid information doesn't exist, default to a single frame
            # Force elements to integer, on tcl v8.5 they are returned as strings
            ginfo = self.grid_info()
            if ginfo:
                return model.GridCoordinates(
                    row=int(ginfo.get('row', 0)),
                    rowspan=int(ginfo.get('rowspan', 1)),
                    column=int(ginfo.get('column', 0)),
                    columnspan=int(ginfo.get('columnspan', 1)),
                )
            else:
                return None

    def get_gui_state(self) -> model.GuiState:
        if __debug__:
            from . import RootWindow  # For typechecking
        assert isinstance(self, (tk.ttk.Widget, RootWindow)), f'{self} is not a valid tkinter.ttk.Widget'
        state: typing.MutableMapping[str, typing.Optional[bool]] = {}
        for estr in self.gkeys:
            itk = model.GUI_STATES[estr]
            state[estr] = self.instate([itk.gstr()])
            # logger.debug('  [%s] » %s', itk.gstr(), state[estr])
        rval = model.GuiState(**state)
        # if __debug__:
        #     logger.debug('State > %r', rval)
        return rval

    def set_gui_state(self, state: typing.Optional[model.GuiState] = None, **kwargs) -> model.GuiState:
        assert isinstance(self, tk.ttk.Widget), f'{self} is not a valid tkinter.ttk.Widget'
        if state is None:
            state = model.GuiState(**kwargs)
        states = []
        # if __debug__:
        #     logger.debug('State < %r', state)
        for estr, sval, itk in state.items_tk():
            if sval is not None:
                assert estr in self.gkeys, f'{self.__class__.__name__}| Invalid GuiState: {estr}'
                # Invert `sval` when `itk.invert` == `sval XOR itk.invert`
                if sval is not itk.invert:
                    tkstr = '%s' % itk.string
                else:
                    tkstr = '!%s' % itk.string
                # logger.debug('  [%s %s] » %s', sval, itk.invert, tkstr)
                states.append(tkstr)
        self.state(states)
        assert state is not None
        return state

    # Wrapper functions for the property
    def gstate_get(self):
        return self.get_gui_state()

    def gstate_set(self, state: model.GuiState):
        # Don't store the return object
        self.set_gui_state(state)

    # TODO: This can be even better
    # Support `widget.gstate.enabled = NEW_VALUE`
    # Not a property, but a class that changes `self`
    gstate = property(gstate_get, gstate_set, doc='GUI State')

    # TODO: On Python 3.11:: -> typing.Self
    def putHelper(self, value: bool = True) -> 'MixinWidget':
        '''Set the `isHelper` marker on itself.

        This is designed to be used inside the `setup_widgets
        <ContainerWidget.setup_widgets>` function, like this:

        .. code:: python

            def setup_widgets(self, ...):
                self.w1 = Widget(self, ...).putHelper()

        This is usually called "method chaining", or "fluent interface".
        '''
        self.isHelper = value
        return self

    # TODO: On Python 3.11:: -> typing.Self
    def putIgnoreState(self, value: bool = True) -> 'MixinWidget':
        '''Set the `ignoreContainerState` marker on itself.

        This is designed to be used inside the `setup_widgets
        <ContainerWidget.setup_widgets>` function, like this:

        .. code:: python

            def setup_widgets(self, ...):
                self.w1 = Widget(self, ...).putIgnoreState()

        This is usually called "method chaining", or "fluent interface".
        '''
        # TODO: Move this "method chaining" to a common document.
        self.ignoreContainerState
        return self


class MixinTraces:
    '''Mixin class for variable traces.

    Supported for `SingleWidget` only.
    '''
    def init_traces(self) -> None:
        self._traces: typing.MutableMapping[str, str] = {}
        assert isinstance(self, SingleWidget), f'{self.__class__.__name__}: Unsupported tracing for this Widget'
        assert self.variable is not None, f'{self}: Widget untraceable'

    def trace(self, function: typing.Callable, *, trace_mode: model.TraceModeT = 'write', trace_name: typing.Optional[str] = None, **kwargs: typing.Any) -> str:
        '''Trace the variable associated to the current `SingleWidget`.

        There is no Python documentation, see ``Tk`` `trace variable <https://www.tcl.tk/man/tcl/TclCmd/trace.html#M14>`_ documentation.

        Args:
            function: The callback function.
            trace_mode: The trace mode, when should the callback be invoked.
            trace_name: A name for the trace reference. Optional, uses an
                automatic name otherwise.
            kwargs: Passed to the ``Tk`` ``trace_add`` function.

        See Also:
            Uses `fn.generate_trace` under the hood.
        '''
        assert isinstance(self, SingleWidget), f'{self.__class__.__name__}: Unsupported tracing for this Widget'
        assert self.variable is not None, f'{self}: Widget untraceable'
        function_name = self.variable.trace_add(
            trace_mode,
            fn.generate_trace(
                self.variable,
                function,
                **kwargs,
            ),
        )
        key = trace_name or function_name
        assert key not in self._traces, f'{self}: Repeated trace name: {key}'
        self._traces[key] = function_name
        return function_name


# High-Level Mixins


class SingleWidget(MixinWidget, MixinStateSingle, MixinTraces):
    '''Parent class of all single widgets.'''
    variable: typing.Optional[tkmilan_var.Variable] = None
    state_type: typing.Optional[typing.Type[tkmilan_var.Variable]] = None

    def init_single(self, variable: typing.Optional[tkmilan_var.Variable] = None, gkeys: typing.Optional[typing.Iterable[str]] = None) -> None:
        '''Setup all single widget stuff.

        Includes:
        - Variable settings
        - `tkmilan.mixin.MixinState.isNoneable` calculation
        '''
        MixinWidget.__init__(self, gkeys=gkeys)
        self.variable = self.setup_variable(variable)
        MixinTraces.init_traces(self)
        if self.isNoneable is None:
            # Calculate isNoneable option
            self.isNoneable = self.state_type is tkmilan_var.nothing

    def setup_variable(self, variable: typing.Optional[tkmilan_var.Variable]) -> tkmilan_var.Variable:
        assert self.state_type is not None
        if variable is None:
            variable = self.state_type()
        assert isinstance(variable, self.state_type), f'Incompatible variable type ({type(variable).__name__}/{self.state_type.__name__})'
        return variable

    def setup_state(self):
        return self.variable

    def wimage(self, key: str) -> typing.Optional[tk.Image]:
        '''Wraper for `RootWindow.wimage`.'''
        return self.wroot.wimage(key)

    # TODO: Move here from Combobox
    # specValues: typing.Optional[spec.Spec]
    # def setDefault(self) -> None:
    #     if self.specValues:
    #         self.wstate = self.specValues.default
    #
    # def eSet(self, value: typing.Any) -> typing.Callable[..., None]:
    #    ...  # To Be overriden


class ProxyWidget(SingleWidget):
    '''Parent class of all proxy widgets. Special case of `SingleWidget`.

    This is implemented as a class initializer that sets up the `wproxy
    <MixinWidget.wproxy>`/`proxee <MixinWidget.proxee>` references, and returns
    the child instance.

    Note that creating an instance of this type will return the child widget
    instance, not the proxy object. The rest of the library is aware of this.
    The `ProxyWidget` object is available on the `wproxy <MixinWidget.wproxy>`
    value.

    See Also:
        Check the Python documentation for the difference between
        `object.__new__` and `object.__init__`.
    '''
    def __new__(cls: typing.Type[ProxyWidgetT], *args, **kwargs) -> ProxyWidgetT:
        assert issubclass(cls, ProxyWidget)
        proxy = super(ProxyWidget, cls).__new__(cls)
        # Manually call the __init__ method (required since the class changes)
        cls.__init__(proxy, *args, **kwargs)
        proxee = proxy.proxee
        assert proxee is not None
        # Save a reference to the proxy object
        proxee.wproxy = proxy
        # Return a different type from `cls`:
        return typing.cast(ProxyWidgetT, proxee)


# TODO: Support MixinTraces? Synthetic trace of all sub widgets?
class ContainerWidget(MixinWidget, MixinStateContainer):
    '''Parent class of all containers.'''
    layout: typing.Optional[str] = ''  # Automatic AUTO
    layout_expand: bool = True
    '''Should this container expand to fill the space on the parent widget.

    Note this affects the **parent** grid, not the child grid on this container.
    '''
    layout_autogrow: bool = True
    '''Should this container have its child columns and rows grow automatically.

    This is equivalent to configuring the grid with the option ``weigth=1``.
    '''

    def init_container(self, *args, layout: typing.Optional[str] = '', **kwargs) -> None:
        '''
        Setup all the container stuff.

        Includes:
        - Variable settings
        - Sub-Widget settings
        - Layout
        - Defaults
        '''
        assert isinstance(self, (tk.Widget, tk.Tk)), f'{self} is not a valid tkinter.Widget'
        MixinWidget.__init__(self)
        self._variables: typing.MutableMapping[str, tk.Variable] = {}  # Allow attaching variables to containers
        # Calculate child widgets
        _existing_names = set(dir(self))
        _existing_ids = None
        if __debug__:
            _existing_ids = {
                name: id(self.__dict__.get(name, None))
                for name in _existing_names
                if name not in WEIRD_WIDGET_NAME
            }
        widgets = self.setup_widgets(*args, **kwargs)
        if __debug__:
            assert _existing_ids is not None
            overriden_names = [name for name, eid in _existing_ids.items() if id(self.__dict__.get(name, None)) != eid]
            assert len(overriden_names) == 0, f'{self}: Overriden Names: {" ".join(overriden_names)}'
        _new_names = set(dir(self)) - _existing_names
        if widgets is None:
            children = [w for _, w in self.children.items()]
            # logger.debug('tk C: %r', self.children)
            widgets = {}
            dir_names = {id(getattr(self, name, None)): name for name in _new_names}
            for widget_raw in children:
                assert isinstance(widget_raw, MixinWidget), '{widget_raw} is not a valid tkmilan widget'
                widget = widget_raw.proxee or widget_raw  # Save the child widget
                if not (widget).isHelper:
                    wid = id(widget)
                    assert wid in dir_names, f'{self}: Missing "{widget}"[{widget!r}]'
                    name = dir_names[wid]
                    widgets[name] = widget
        # logger.debug('Widgets: %r', widgets)
        self.widgets: typing.Mapping[str, MixinWidget] = widgets
        for w in self.widgets.values():
            w.wparent = self
        if self.isNoneable is None:
            # Calculate isNoneable option: containers are always noneable
            self.isNoneable = True

        if layout is None or self.layout is None:
            # Allow for explicit `None` layouts
            chosen_layout = None
        elif layout != '':
            # Use the per-instance setting
            chosen_layout = layout
        elif self.layout != '':
            # Use the class setting
            chosen_layout = self.layout
        else:
            # Fallback
            chosen_layout = autolayout.AUTO
        self.layout_container(chosen_layout)
        self.setup_defaults()
        self.after_idle(lambda: self.setup_adefaults())  # No need for a `TimeoutIdle` here
        assert hasattr(self, 'grid'), f'{self!r} should have a grid method'
        if __debug__:
            aliases = set(self._variables.keys()).intersection(set(self.widgets.keys()))
            assert len(aliases) == 0, f'{self!r}: Aliased var/widgets: {" ".join(aliases)}'

    def setup_widgets(self, *args, **kwargs) -> typing.Optional[typing.Mapping[str, MixinWidget]]:
        '''Define the sub widgets here.

        Return a :py:class:`dict` for a custom mapping, or `None` for automatic mapping.
        '''
        raise NotImplementedError

    def var(self, cls: 'typing.Type[tkmilan_var.Variable]', *,
            value=None,
            name=None,
            ) -> 'tkmilan_var.Variable':
        '''"Attach" a new variable to this container.

        Args:
            cls: The variable class.

            value: The default value. Optional, defaults to `None`.
            name: The variable name. Optional, defaults to an autogenerated name.

        See Also:
            - `varSpecced`: Attach a specified variable to this container, with a name.
            - `gvar`: Access the variable by name.
        '''
        vobj = cls(value=value)
        assert isinstance(vobj, tkmilan_var.Variable), f'Class "{cls}" is not a "tk.Variable"'
        # Save the variables on the instance object
        vname = name or str(vobj)
        self._variables[vname] = vobj
        return vobj

    def varSpecced(self, cls: 'typing.Type[tkmilan_var.VariableSpecced]', *,
                   spec: spec.SpecCountable,
                   value=None,
                   name=None,
                   ) -> 'tkmilan_var.VariableSpecced':
        '''"Attach" a new specified variable to this container.

        Args:
            cls: The variable class.
            spec: The variable specification.

            value: Th default value. Optional, default to `None`.
            name: The variable name. Optional, defaults to an autogenerated name.

        See Also:
            - `var`: Attach a non-speficied variable to this container, with a name.
            - `gvar`: Access the variable by name.
        '''
        vobj = cls(value=value, spec=spec)
        assert isinstance(vobj, tkmilan_var.Variable), f'Class "{cls}" is not a "tk.Variable"'
        # Save the variables on the instance object
        vname = name or str(vobj)
        self._variables[vname] = vobj
        # Set the default ASAP, on the root widget
        # - This is to make sure this is only set once, even if used in several locations
        # - Errors if this is called twice for the same name
        self.wroot.tidle(vobj.setDefault, key=f'__:varSpecced_default:{vname}')
        return vobj

    def gvar(self, name: str):
        '''Get a variable attached to this container, by name.

        Fails if it does not exist.

        Args:
            name: The variable name to search for.

        See Also:
            - `var`: Attach a non-speficied variable to this container, with a name.
            - `varSpecced`: Attach a specified variable to this container, with a name.
        '''
        return self._variables[name]

    def layout_container(self, layout: typing.Optional[str]):
        assert isinstance(self, (tk.Widget, tk.Tk)), f'{self} is not a valid tkinter.Widget'
        if self.layout_expand:
            assert isinstance(self, tk.ttk.Widget), f'{self} is not a valid tkinter.ttk.Widget'
            self.grid(sticky=tk.NSEW)
        # Automatic Layout
        layout, args = autolayout.do(layout, len(self.widgets))
        if layout:
            # if __debug__:
            #     logger.debug(f'{self}: => {len(self.widgets)} widgets')
            for idx, (arg, widget) in enumerate(zip(args, self.widgets.values())):
                widget_real = widget.wproxy or widget
                assert isinstance(widget_real, tk.Widget)
                widget_real.grid(**arg.dict())  # Change the grid on the proxy widget
        self.layout = layout  # Setup the final layout setting
        if self.layout_autogrow:
            if size := self.gsize:
                fn.configure_grid(self, [1] * size.columns, [1] * size.rows)
        self.setup_layout(layout)  # Custom adjustments, after all automatic changes

    @property
    def gsize(self) -> model.GridSize:
        '''GUI grid size (according to the current child widgets).'''
        return fn.grid_size(*[w.wproxy or w for w in self.widgets.values()])  # Use the proxy widget

    def state_c(self, *, vid_upstream: typing.Optional[typing.Set[str]] = None) -> ContainerState:
        swidgets = {}
        cwidgets = {}
        wvariables = {}
        vid_upstream = set(vid_upstream or ())
        vid_variables = set(fn.vname(v) for v in self._variables.values())
        vwidgets = collections.defaultdict(lambda: [])
        # logger.debug('%r START | %r', self, vid_upstream)
        for name, widget in self.widgets.items():
            # logger.debug('%s: %r', name, widget)
            if widget.ignoreContainerState:
                # logger.debug('| Skipping Widget')
                continue
            if isinstance(widget, SingleWidget):
                assert widget.variable is not None
                vid = fn.vname(widget.variable)
                # logger.debug('| Variable: %s[%r]', vid, widget.variable)
                if vid in vid_upstream:
                    # logger.debug('  @Upstream, skipping')
                    continue
                elif vid in vid_variables:
                    # logger.debug('  @Container Variables, skipping')
                    continue
                swidgets[name] = widget
                wvariables[vid] = widget.variable
                vwidgets[vid].append(name)
            elif isinstance(widget, ContainerWidget):
                # logger.debug('| Container: @%s', name)
                cwidgets[name] = widget
        vid_upstream.update(wvariables, vid_variables)
        # logger.debug('%r STOP', self)
        return ContainerState(swidgets, cwidgets, self._variables, wvariables, dict(vwidgets),
                              vid_upstream=vid_upstream)

    def setup_state(self, **kwargs) -> typing.Mapping[str, model.WidgetDynamicState]:
        # Default State:
        # - All the attached variables
        # - All the shared variables
        # - All the single-variable widgets
        # - The container widgets, taking the existing variables into account
        container_state = self.state_c(**kwargs)
        rvalue: typing.MutableMapping[str, model.WidgetDynamicState] = {}
        wids_done: typing.MutableSequence[str] = []
        for vn, vobj in container_state.variables.items():
            rvalue[vn] = model.WidgetDynamicState(vobj.get, vobj.set, noneable=False)
        for vname, ws in container_state.vwidgets.items():
            if vname is not None and len(ws) > 1:
                wv = container_state.wvariables[vname]
                assert vname not in rvalue, f'{self!r}: Aliased vwidgets "{vname}"'
                rvalue[vname] = model.WidgetDynamicState(wv.get, wv.set, noneable=False)
                wids_done.extend(ws)
        for n, w in container_state.swidgets.items():
            if n not in wids_done:
                assert n not in rvalue, f'{self!r}: Aliased swidgets "{n}"'
                rvalue[n] = model.WidgetDynamicState(
                    w.wstate_get,
                    w.wstate_set,
                    noneable=w.isNoneable is True,
                )
        vid_upstream = container_state.vid_upstream
        for n, wc in container_state.cwidgets.items():
            assert n not in rvalue, f'{self!r}: Aliased cwidgets "{n}"'
            rvalue[n] = model.WidgetDynamicState(
                partial(wc.state_get, vid_upstream=vid_upstream),
                partial(wc.state_set, vid_upstream=vid_upstream),
                noneable=wc.isNoneable is True,
                container=True,  # Propagate container data
            )
        return rvalue

    def setup_layout(self, layout: typing.Optional[str]) -> None:
        '''Useful for manual adjustments to the automatic layout.

        This runs after all automatic layout settings are configured.

        Args:
            layout: This is the string passed to the upstream function.

        Note:
            Available for subclass redefinition.
        '''
        pass

    def set_gui_state(self, state: typing.Optional[model.GuiState] = None, _sub: bool = True, **kwargs) -> model.GuiState:
        '''Set GUI State for itself, and optionally, for all sub-widgets.

        .. warning:: Don't use this directly, unless you **really** know what you are doing.

        Args:
            _sub: Automatically run `set_gui_substate` with the same
                `model.GuiState` object. Defaults to `True`.
                Useful only for implementing special containers.

        See Also:
            `MixinWidget.gstate`: Property changed for all sub-widgets.
        '''
        self_state = super().set_gui_state(state, **kwargs)
        if _sub:
            self.set_gui_substate(self_state)
        return self_state

    def set_gui_substate(self, state: model.GuiState) -> None:
        '''Set GUI State for all sub-widgets.

        .. warning:: Don't use this directly, unless you **really** know what you are doing.


        .. note::

            To control the GUI subwidget handling, this function can be
            redefined (using extra care), using something like this:

            .. code:: python

                def set_gui_substate(self, state: tkmilan.model.GuiState):
                    if self.some_condition is True:
                        # Manipulate the `model.GuiState` object
                        state.enabled = False
                    super().set_gui_substate(state)

        See Also:
            `MixinWidget.gstate`: Property changed for all sub-widgets.
        '''
        for _, subwidget in self.widgets.items():
            subwidget.gstate = state

    def setup_defaults(self) -> None:
        '''Runs after the widget is completely setup.

        Note this runs before the parent widget is complete ready.

        Useful to set default values.
        Do not configure layout-related settings here, see `setup_layout`.

        Note:
            Available for subclass redefinition.

        See Also:
            `setup_adefaults`: Run code after all widgets are stable (including
            parent widgets in the tree).
        '''
        pass

    def setup_adefaults(self) -> None:
        '''Runs after all widgets are stable.

        Avoid changing state on this function.

        Note:
            Available for subclass redefinition.

        See Also:
            `setup_defaults`: Run code right after this widget is setup, before
            all widgets are stable.
        '''
        pass

    def wimage(self, key: str) -> typing.Optional[tk.Image]:
        '''Wraper for `RootWindow.wimage`.'''
        return self.wroot.wimage(key)
