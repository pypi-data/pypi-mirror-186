'''Specification for `MixinState` possibilities.

This is really initial validation handling.
'''
import typing
import collections
import collections.abc
from dataclasses import dataclass, field as dc_field, InitVar
import operator
from numbers import Number


smvT = typing.TypeVar('smvT')
'''Generic Type for `StaticMap`.

This is a `typing.TypeVar`, to be used only when typechecking. See `typing`.
'''
limT = typing.TypeVar('limT', bound=Number)
'''Generic Type for `Limit`.

This is a `typing.TypeVar`, to be used only when typechecking. See `typing`.
'''


class Spec:
    '''Parent class for specification definitions.

    These are objects that define the specification for the possible states for
    some widgets.

    Note that this might specify a complex validation, not just a list of
    discrete values, nor a continous range, for example.

    See `SpecCountable`.

    .. automethod:: __contains__
    '''

    default: str
    '''The default label to be shown to the user.'''

    def __contains__(self, label: str) -> bool:
        '''Check if the ``label`` label satisfies the specification.

        Should be used as ``label in Spec``.
        '''
        if isinstance(self, collections.abc.Container):
            return label in self
        raise NotImplementedError


class SpecCountable(Spec):
    '''Parent class for static specification definitions.

    This a more narrow definition of `Spec`, for specifications that consist of
    discrete and countable choices between some values.

    .. automethod:: __len__
    '''

    def all(self) -> typing.Iterable[str]:
        '''Get all the possible labels this specification contains.'''
        if isinstance(self, typing.Iterable):
            # Default Implementation
            return (e for e in self)
        raise NotImplementedError

    def __len__(self) -> int:
        '''Count how many labels this specification contains.

        Should be used as ``len(SpecCountable)``.
        '''
        assert isinstance(self, collections.abc.Sized), f'{self.__class__.__name__} is not Sized'
        return len(self)


class StaticList(tuple, SpecCountable):
    '''Specifies a static list of labels, therefore a :py:class:`tuple` of `str`.

    The default must be explicitely given, either directly as ``default``, or
    indirectly as ``defaultIndex``. Either way is validated to verify the
    default is a valid label.

    Args:
        iterable: Values to construct the list.
        default: Default label. Optional
        defaultIndex: Index for the default label, in the ``iterable``. Optional.
    '''
    def __init__(self, iterable: typing.Iterable[str], *,
                 default: typing.Optional[str] = None,
                 defaultIndex: typing.Optional[int] = None):
        assert default is not None or defaultIndex is not None, f'{self.__class__.__name__}: Missing default label'
        super().__init__(*iterable)
        if default is None:
            assert defaultIndex is not None
            default = self[defaultIndex]
        if default not in self:
            raise ValueError(f'{default!r} not in list')
        # Set `Spec` parameters
        self.default = default


class StaticMap(SpecCountable, typing.Generic[smvT]):
    '''Specifies a static list of labels, and its corresponding values.

    The ``mapping`` parameter matches labels to values. This must be
    bi-injective, that is, there cannot be values corresponding to multiple
    labels.

    The default must be explicitely given.
    '''
    def __init__(self, mapping: typing.Mapping[str, smvT], *,
                 defaultValue: typing.Optional[smvT] = None,
                 defaultLabel: typing.Optional[str] = None):
        assert defaultValue is not None or defaultLabel is not None, f'{self.__class__.__name__}: Missing default'
        # Setup label -> value
        self.l2v: typing.Mapping[str, smvT] = mapping
        # Setup value -> label
        self.v2l: typing.Mapping[smvT, str] = {val: lbl for lbl, val in self.l2v.items()}
        if len(self.l2v) != len(self.v2l):
            raise ValueError('Mapping is not bi-injective')
        # Setup the "other" default
        if defaultValue is None:
            if defaultLabel not in self.l2v:
                raise ValueError(f'Label {defaultLabel!r} not in mapping')
            assert defaultLabel is not None
            defaultValue = self.l2v[defaultLabel]
        if defaultLabel is None:
            if defaultValue not in self.v2l:
                raise ValueError(f'Value {defaultValue!r} not in mapping')
            defaultLabel = self.v2l[defaultValue]
        assert defaultValue in self.v2l
        assert defaultLabel in self.l2v
        self.defaultLabel: str = defaultLabel
        self.defaultValue: smvT = defaultValue
        # Set `Spec` parameters
        self.default = defaultLabel

    def __contains__(self, label):
        return label in self.l2v

    def all(self):
        return self.l2v.keys()

    def __len__(self):
        return len(self.l2v)

    # Specific functions

    def value(self, label: str, default: smvT) -> smvT:
        '''Get the value corresponding to the given label.

        Wraps `dict.get`.
        '''
        if label in self.l2v:
            return self.l2v[label]
        else:
            assert default is not None, f'Invalid default value : {default!r}'
            return default

    def label(self, value: smvT, default: str) -> str:
        '''Get the label corresponding to the given value.

        Wraps `dict.get`.
        '''
        if value in self.v2l:
            return self.v2l[value]
        else:
            assert default is not None, f'Invalid default label: {default!r}'
            return default

    def hasValue(self, value: smvT) -> bool:
        '''Checks if the ``value`` statisfies the specification.

        This is the mirror image of `__contains__`, working on values.
        '''
        return value in self.v2l

    def allValues(self) -> typing.Iterable[smvT]:
        '''Get all possible values this specification contains.

        This is the mirror image of `all`, working on values.
        '''
        return self.v2l.keys()


def StaticMapLabels(fn: typing.Callable[[str], smvT], lst: typing.Sequence[str], *, defaultIndex: typing.Optional[int] = None, **kwargs) -> StaticMap:
    '''Turn a list of labels into a mapping, by applying a function to get the value.

    Wrapper for `StaticMap`.
    '''
    if defaultIndex is not None:
        kwargs['defaultLabel'] = lst[defaultIndex]
    return StaticMap({e: fn(e) for e in lst}, **kwargs)


def StaticMapValues(fn: typing.Callable[[smvT], str], lst: typing.Sequence[smvT], *, defaultIndex: typing.Optional[int] = None, **kwargs) -> StaticMap:
    '''Turn a list of values into a mapping, by applying a function to get the label.

    Wrapper for `StaticMap`.
    '''
    if defaultIndex is not None:
        kwargs['defaultValue'] = lst[defaultIndex]
    return StaticMap({fn(e): e for e in lst}, **kwargs)


# TODO: Split into two, by `none`
#       - none=False => SpecCountable
#       - none=True => Spec
@dataclass
class Limit(Spec, typing.Generic[limT]):
    '''Represent a range to limit a value, generic for any `number
    <numbers.Number>` type.

    The range can be made to remove the limits themselves with ``imin`` and
    ``imax``. The default is the limit being closed on both sides.

    Defaults to allowing infinite limits, but this might not make sense, so the
    ``none`` parameter can disallow this.

    Arguments:
        min_entry: Minumum value, as string or number.
            `None` might also be allowed, see ``none``.
        max_entry: Maximum value, as string or number.
            `None` might also be allowed, see ``none``.
        default_entry: Default value to be shown, as string, number, or `None`
            to choose a valid value (the default). Configures `Spec.default`.
        fn: A function that turns a string into `number <numbers.Number>`.
            Usually some kind of parser.
        imin: Include the limit on the minumum value itself.
            Defaults to `True`.
        imax: Include the limit on the maximum value itself.
            Defaults to `True`.
        none: Allow `None` on the limits to represent limits towards infinity.

    The following parameters are also available, calculated from the arguments:

    Parameters:
        min: Minumum value, as number. `None` if allowed.
        min_value: Minumum value, as string. Good for showing to the user.
        max: Maximum value, as number. `None` if allowed.
        max_value: Maximum value, as string. Good for showing to the user.
    '''
    min_entry: InitVar[typing.Union[limT, str, None]]
    max_entry: InitVar[typing.Union[limT, str, None]]
    fn: typing.Callable[[str], limT]
    imin: bool = True
    imax: bool = True
    # Calculations
    min: typing.Optional[limT] = dc_field(init=False)
    max: typing.Optional[limT] = dc_field(init=False)
    min_value: str = dc_field(init=False)
    max_value: str = dc_field(init=False)
    # step: typing.Optional[limT] = None  # TODO: Support
    # __init__ variable
    none: InitVar[bool] = True
    default_entry: InitVar[typing.Union[limT, str, None]] = None
    # Class Variables
    _infinity: typing.ClassVar[str] = '∞'
    _strRange: typing.ClassVar[typing.Mapping[bool, str]] = {
        True: '[',
        False: ']',
    }

    def __post_init__(self, min_entry: typing.Union[limT, str, None], max_entry: typing.Union[limT, str, None],
                      none: bool,
                      default_entry: typing.Union[limT, str, None] = None):
        if min_entry is None:
            self.min = None
            self.min_value = f'-{self._infinity}'
            self.imin = False
        elif isinstance(min_entry, str):
            self.min_value = min_entry
            self.min = self.fn(self.min_value)
        else:
            self.min = min_entry
            self.min_value = str(self.min)
        if not none and self.min is None:
            raise ValueError(f'Invalid Minimum: {self.min}')
        if max_entry is None:
            self.max = None
            self.max_value = f'+{self._infinity}'
            self.imax = False
        elif isinstance(max_entry, str):
            self.max_value = max_entry
            self.max = self.fn(self.max_value)
        else:
            self.max = max_entry
            self.max_value = str(self.max)
        if not none and self.max is None:
            raise ValueError(f'Invalid Maximum: {self.max}')
        # TODO: Support "step"
        # if self.step is not None:
        #     # step validation requires both ranges
        #     assert self.min is not None and self.max is not None
        if default_entry is None:
            self.default = {
                (True, True): self.min_value,
                (True, False): self.min_value,
                (False, True): self.max_value,
                (False, False): '0',  # Any number is valid
            }[(self.min is not None, self.max is not None)]
        elif isinstance(default_entry, str):
            self.default = default_entry
        else:  # limT
            self.default = str(default_entry)
        # if self.default is not None and self.default not in self:
        #     raise ValueError(f'Invalid Default: {self.default}')

    @property
    def parsed(self) -> typing.Tuple[typing.Optional[limT], typing.Optional[limT]]:
        '''Get a tuple of limit values, as numbers.'''
        # TODO: Support "step"
        return (self.min, self.max)

    @property
    def value(self):
        '''Get a tuple of limit values, as strings.'''
        # TODO: Support "step"
        return (self.min_value, self.max_value)

    def get_spinargs(self, limit: float = float('+inf')) -> typing.Tuple[float, float, float]:
        '''Get all `Spinbox` value arguments.

        Return Value:
            Returns a tuple with three floating point values:

            - ``from``
            - ``to``
            - ``increment``
        '''
        sincrement = 1.0  # TODO: Support "step"
        sfrom: float
        if self.min is None:
            sfrom = -1 * limit
        else:
            assert isinstance(self.min, typing.SupportsFloat), f'Invalid min value: {self.min!r}'
            sfrom = float(self.min)
        sto: float
        if self.max is None:
            sto = +1 * limit
        else:
            assert isinstance(self.max, typing.SupportsFloat), f'Invalid max value: {self.max!r}'
            sto = float(self.max)
        if not self.imin:
            sfrom += sincrement
        if not self.imax:
            sto -= sincrement
        return sfrom, sto, sincrement

    def __str__(self):
        lrange = self._strRange[self.imin]
        rrange = self._strRange[not self.imax]
        return '%s%s, %s%s' % (
            lrange,
            self.min_value,
            self.max_value,
            rrange,
        )

    def __contains__(self, string: str) -> bool:
        OPERATOR: typing.Mapping[bool, typing.Callable[..., bool]] = {True: operator.le, False: operator.lt}
        number: limT = self.fn(string)
        omin = OPERATOR[self.imin]
        omax = OPERATOR[self.imax]
        return all((
            (omin(self.min, number) if self.min is not None else True),  # vmin
            (omax(number, self.max) if self.max is not None else True),  # vmax
            # TODO: Support "step"
            # ((number - self.min) % self.step == 0 if self.step is not None else True)  # step
        ))
