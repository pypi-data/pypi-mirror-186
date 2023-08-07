# AUTO-GENERATED FILE. Do not edit. Run chalkpy stubgen to generate.
# fmt: off
# isort: skip_file
from __future__ import annotations

from chalk.features import DataFrame as DataFrame
from chalk.features import Features as Features
from chalk.features import Tags as Tags
from chalk.features.feature_set import FeaturesMeta as FeaturesMeta
from chalk.streams._windows import Windowed as Windowed
from chalk.utils.duration import Duration as Duration
from datetime import date as __stubgen_datetime_date
from datetime import datetime as __stubgen_datetime_datetime
from tests.client.test_client_printing import User as __stubgen_tests_client_test__client__printing_User
from tests.features.test_chained_feature_time import Homeowner as __stubgen_tests_features_test__chained__feature__time_Homeowner
from tests.features.test_chained_has_one import ExampleFraudOrg as __stubgen_tests_features_test__chained__has__one_ExampleFraudOrg
from tests.features.test_chained_has_one import ExampleFraudUser as __stubgen_tests_features_test__chained__has__one_ExampleFraudUser
from tests.features.test_df import Foo as __stubgen_tests_features_test__df_Foo
from tests.features.test_df import PydanticFoo as __stubgen_tests_features_test__df_PydanticFoo
from tests.features.test_df import Topping as __stubgen_tests_features_test__df_Topping
from tests.features.test_df import ToppingPrice as __stubgen_tests_features_test__df_ToppingPrice
from tests.features.test_features import SingleChildFS as __stubgen_tests_features_test__features_SingleChildFS
from tests.features.test_features import SingleParentFS as __stubgen_tests_features_test__features_SingleParentFS
from tests.features.test_iter import NoFunFeatures as __stubgen_tests_features_test__iter_NoFunFeatures
from tests.serialization.test_codec import Color as __stubgen_tests_serialization_test__codec_Color
from tests.serialization.test_codec import CustomClass as __stubgen_tests_serialization_test__codec_CustomClass
from tests.serialization.test_codec import MyDataclass as __stubgen_tests_serialization_test__codec_MyDataclass
from tests.sql.test_execute import EnumFeature as __stubgen_tests_sql_test__execute_EnumFeature
from tests.sql.test_execute import SQLExecuteNestedFeatures as __stubgen_tests_sql_test__execute_SQLExecuteNestedFeatures
from tests.sql.test_sql_file_resolver import Burrito as __stubgen_tests_sql_test__sql__file__resolver_Burrito
from tests.streams.test_window import ChildWindow as __stubgen_tests_streams_test__window_ChildWindow
from tests.streams.test_window import GrandchildWindow as __stubgen_tests_streams_test__window_GrandchildWindow
from typing import Optional as Optional
from typing import Protocol as Protocol
from typing import Type as Type
from typing import Union as Union
from typing import overload as overload

class TacoMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def user_id(self) -> Type[str]: ...

    @property
    def price(self) -> Type[int]: ...

    @property
    def maybe_price(self) -> Type[Union[int, None]]: ...

    @property
    def maybe_str(self) -> Type[Union[str, None]]: ...

    @property
    def hat(self) -> Type[str]: ...

    @property
    def topping_id(self) -> Type[str]: ...

    @property
    def ts(self) -> Type[__stubgen_datetime_datetime]: ...

    @property
    def unzoned_ts(self) -> Type[__stubgen_datetime_datetime]: ...

    @property
    def nicknames(self) -> Type[DataFrame]: ...

    @property
    def topping(self) -> Type[__stubgen_tests_features_test__df_Topping]: ...

    @property
    def foo(self) -> Type[__stubgen_tests_features_test__df_Foo]: ...

    @property
    def pydantic_foo(self) -> Type[__stubgen_tests_features_test__df_PydanticFoo]: ...

    @property
    def foos(self) -> Type[list[__stubgen_tests_features_test__df_Foo]]: ...

    @property
    def float_list(self) -> Type[list[float]]: ...

class Taco(Features, metaclass=TacoMetaclass):
    def __init__(
        self,
        id: str = ...,
        user_id: str = ...,
        price: int = ...,
        maybe_price: Union[int, None] = ...,
        maybe_str: Union[str, None] = ...,
        hat: str = ...,
        topping_id: str = ...,
        ts: __stubgen_datetime_datetime = ...,
        unzoned_ts: __stubgen_datetime_datetime = ...,
        nicknames: DataFrame = ...,
        topping: __stubgen_tests_features_test__df_Topping = ...,
        foo: __stubgen_tests_features_test__df_Foo = ...,
        pydantic_foo: __stubgen_tests_features_test__df_PydanticFoo = ...,
        foos: list[__stubgen_tests_features_test__df_Foo] = ...,
        float_list: list[float] = ...,
    ):
        self.id: str
        self.user_id: str
        self.price: int
        self.maybe_price: Union[int, None]
        self.maybe_str: Union[str, None]
        self.hat: str
        self.topping_id: str
        self.ts: __stubgen_datetime_datetime
        self.unzoned_ts: __stubgen_datetime_datetime
        self.nicknames: DataFrame
        self.topping: __stubgen_tests_features_test__df_Topping
        self.foo: __stubgen_tests_features_test__df_Foo
        self.pydantic_foo: __stubgen_tests_features_test__df_PydanticFoo
        self.foos: list[__stubgen_tests_features_test__df_Foo]
        self.float_list: list[float]

class TacoProtocol(Protocol):
    id: str
    user_id: str
    price: int
    maybe_price: Union[int, None]
    maybe_str: Union[str, None]
    hat: str
    topping_id: str
    ts: __stubgen_datetime_datetime
    unzoned_ts: __stubgen_datetime_datetime
    nicknames: DataFrame
    topping: __stubgen_tests_features_test__df_Topping
    foo: __stubgen_tests_features_test__df_Foo
    pydantic_foo: __stubgen_tests_features_test__df_PydanticFoo
    foos: list[__stubgen_tests_features_test__df_Foo]
    float_list: list[float]

class SQLExecuteFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[int]: ...

    @property
    def ts(self) -> Type[__stubgen_datetime_datetime]: ...

    @property
    def str_feature(self) -> Type[str]: ...

    @property
    def int_feature(self) -> Type[int]: ...

    @property
    def bool_feature(self) -> Type[bool]: ...

    @property
    def enum_feature(self) -> Type[__stubgen_tests_sql_test__execute_EnumFeature]: ...

    @property
    def date_feature(self) -> Type[__stubgen_datetime_date]: ...

    @property
    def timestamp_feature(self) -> Type[__stubgen_datetime_datetime]: ...

    @property
    def float_feature(self) -> Type[float]: ...

    @property
    def datetime_feature(self) -> Type[__stubgen_datetime_datetime]: ...

    @property
    def list_feature(self) -> Type[list[str]]: ...

    @property
    def nested_features_id(self) -> Type[int]: ...

    @property
    def nested_features(self) -> Type[__stubgen_tests_sql_test__execute_SQLExecuteNestedFeatures]: ...

class SQLExecuteFeatures(Features, metaclass=SQLExecuteFeaturesMetaclass):
    def __init__(
        self,
        id: int = ...,
        ts: __stubgen_datetime_datetime = ...,
        str_feature: str = ...,
        int_feature: int = ...,
        bool_feature: bool = ...,
        enum_feature: __stubgen_tests_sql_test__execute_EnumFeature = ...,
        date_feature: __stubgen_datetime_date = ...,
        timestamp_feature: __stubgen_datetime_datetime = ...,
        float_feature: float = ...,
        datetime_feature: __stubgen_datetime_datetime = ...,
        list_feature: list[str] = ...,
        nested_features_id: int = ...,
        nested_features: __stubgen_tests_sql_test__execute_SQLExecuteNestedFeatures = ...,
    ):
        self.id: int
        self.ts: __stubgen_datetime_datetime
        self.str_feature: str
        self.int_feature: int
        self.bool_feature: bool
        self.enum_feature: __stubgen_tests_sql_test__execute_EnumFeature
        self.date_feature: __stubgen_datetime_date
        self.timestamp_feature: __stubgen_datetime_datetime
        self.float_feature: float
        self.datetime_feature: __stubgen_datetime_datetime
        self.list_feature: list[str]
        self.nested_features_id: int
        self.nested_features: __stubgen_tests_sql_test__execute_SQLExecuteNestedFeatures

class SQLExecuteFeaturesProtocol(Protocol):
    id: int
    ts: __stubgen_datetime_datetime
    str_feature: str
    int_feature: int
    bool_feature: bool
    enum_feature: __stubgen_tests_sql_test__execute_EnumFeature
    date_feature: __stubgen_datetime_date
    timestamp_feature: __stubgen_datetime_datetime
    float_feature: float
    datetime_feature: __stubgen_datetime_datetime
    list_feature: list[str]
    nested_features_id: int
    nested_features: __stubgen_tests_sql_test__execute_SQLExecuteNestedFeatures

class WowFSMetaclass(FeaturesMeta):
    @property
    def something(self) -> Type[str]: ...

    @property
    def something_else(self) -> Type[str]: ...

    @property
    def nocomment(self) -> Type[str]: ...

    @property
    def nope(self) -> Type[str]: ...

    @property
    def assigned(self) -> Type[str]: ...

    @property
    def bizarre(self) -> Type[str]: ...

    @property
    def goofy(self) -> Type[str]: ...

    @property
    def assigned_comment(self) -> Type[str]: ...

    @property
    def explicit(self) -> Type[str]: ...

    @property
    def assigned_comment_multiline(self) -> Type[str]: ...

    @property
    def time(self) -> Type[__stubgen_datetime_datetime]: ...

    @property
    def nope_nope(self) -> Type[__stubgen_datetime_datetime]: ...

class WowFS(Features, metaclass=WowFSMetaclass):
    def __init__(
        self,
        something: str = ...,
        something_else: str = ...,
        nocomment: str = ...,
        nope: str = ...,
        assigned: str = ...,
        bizarre: str = ...,
        goofy: str = ...,
        assigned_comment: str = ...,
        explicit: str = ...,
        assigned_comment_multiline: str = ...,
        time: __stubgen_datetime_datetime = ...,
        nope_nope: __stubgen_datetime_datetime = ...,
    ):
        self.something: str
        self.something_else: str
        self.nocomment: str
        self.nope: str
        self.assigned: str
        self.bizarre: str
        self.goofy: str
        self.assigned_comment: str
        self.explicit: str
        self.assigned_comment_multiline: str
        self.time: __stubgen_datetime_datetime
        self.nope_nope: __stubgen_datetime_datetime

class WowFSProtocol(Protocol):
    something: str
    something_else: str
    nocomment: str
    nope: str
    assigned: str
    bizarre: str
    goofy: str
    assigned_comment: str
    explicit: str
    assigned_comment_multiline: str
    time: __stubgen_datetime_datetime
    nope_nope: __stubgen_datetime_datetime

class StreamFeaturesWindowMetaclass(FeaturesMeta):
    @property
    def uid(self) -> Type[str]: ...

    @property
    def scalar_feature__600__(self) -> Type[str]: ...

    @property
    def scalar_feature__1200__(self) -> Type[str]: ...

    @property
    def scalar_feature(self) -> Type[Windowed[str]]: ...

    @property
    def scalar_feature_2__600__(self) -> Type[str]: ...

    @property
    def scalar_feature_2__1200__(self) -> Type[str]: ...

    @property
    def scalar_feature_2(self) -> Type[Windowed[str]]: ...

    @property
    def basic(self) -> Type[str]: ...

    @property
    def child_id(self) -> Type[str]: ...

    @property
    def child(self) -> Type[__stubgen_tests_streams_test__window_ChildWindow]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class StreamFeaturesWindow(Features, metaclass=StreamFeaturesWindowMetaclass):
    def __init__(
        self,
        uid: str = ...,
        scalar_feature__600__: str = ...,
        scalar_feature__1200__: str = ...,
        scalar_feature: Windowed[str] = ...,
        scalar_feature_2__600__: str = ...,
        scalar_feature_2__1200__: str = ...,
        scalar_feature_2: Windowed[str] = ...,
        basic: str = ...,
        child_id: str = ...,
        child: __stubgen_tests_streams_test__window_ChildWindow = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.uid: str
        self.scalar_feature__600__: str
        self.scalar_feature__1200__: str
        self.scalar_feature: Windowed[str]
        self.scalar_feature_2__600__: str
        self.scalar_feature_2__1200__: str
        self.scalar_feature_2: Windowed[str]
        self.basic: str
        self.child_id: str
        self.child: __stubgen_tests_streams_test__window_ChildWindow
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class StreamFeaturesWindowProtocol(Protocol):
    uid: str
    scalar_feature: Windowed[str]
    scalar_feature_2: Windowed[str]
    basic: str
    child_id: str
    child: __stubgen_tests_streams_test__window_ChildWindow

class HelloMetaclass(FeaturesMeta):
    @property
    def a(self) -> Type[str]: ...

    @property
    def b(self) -> Type[int]: ...

    @property
    def c(self) -> Type[__stubgen_datetime_datetime]: ...

    @property
    def d(self) -> Type[__stubgen_tests_serialization_test__codec_Color]: ...

    @property
    def e(self) -> Type[__stubgen_datetime_date]: ...

    @property
    def f(self) -> Type[__stubgen_tests_serialization_test__codec_MyDataclass]: ...

    @property
    def y(self) -> Type[set[int]]: ...

    @property
    def z(self) -> Type[list[str]]: ...

    @property
    def fancy(self) -> Type[__stubgen_tests_serialization_test__codec_CustomClass]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class Hello(Features, metaclass=HelloMetaclass):
    def __init__(
        self,
        a: str = ...,
        b: int = ...,
        c: __stubgen_datetime_datetime = ...,
        d: __stubgen_tests_serialization_test__codec_Color = ...,
        e: __stubgen_datetime_date = ...,
        f: __stubgen_tests_serialization_test__codec_MyDataclass = ...,
        y: set[int] = ...,
        z: list[str] = ...,
        fancy: __stubgen_tests_serialization_test__codec_CustomClass = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.a: str
        self.b: int
        self.c: __stubgen_datetime_datetime
        self.d: __stubgen_tests_serialization_test__codec_Color
        self.e: __stubgen_datetime_date
        self.f: __stubgen_tests_serialization_test__codec_MyDataclass
        self.y: set[int]
        self.z: list[str]
        self.fancy: __stubgen_tests_serialization_test__codec_CustomClass
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class HelloProtocol(Protocol):
    a: str
    b: int
    c: __stubgen_datetime_datetime
    d: __stubgen_tests_serialization_test__codec_Color
    e: __stubgen_datetime_date
    f: __stubgen_tests_serialization_test__codec_MyDataclass
    y: set[int]
    z: list[str]
    fancy: __stubgen_tests_serialization_test__codec_CustomClass

class FSWithStalenessMetaclass(FeaturesMeta):
    @property
    def parent_id(self) -> Type[str]: ...

    @property
    def scalar(self) -> Type[int]: ...

    @property
    def windowed_int__600__(self) -> Type[int]: ...

    @property
    def windowed_int(self) -> Type[Windowed[int]]: ...

    @property
    def scalar_override(self) -> Type[int]: ...

    @property
    def windowed_int_override__600__(self) -> Type[int]: ...

    @property
    def windowed_int_override(self) -> Type[Windowed[int]]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class FSWithStaleness(Features, metaclass=FSWithStalenessMetaclass):
    def __init__(
        self,
        parent_id: str = ...,
        scalar: int = ...,
        windowed_int__600__: int = ...,
        windowed_int: Windowed[int] = ...,
        scalar_override: int = ...,
        windowed_int_override__600__: int = ...,
        windowed_int_override: Windowed[int] = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.parent_id: str
        self.scalar: int
        self.windowed_int__600__: int
        self.windowed_int: Windowed[int]
        self.scalar_override: int
        self.windowed_int_override__600__: int
        self.windowed_int_override: Windowed[int]
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class FSWithStalenessProtocol(Protocol):
    parent_id: str
    scalar: int
    windowed_int: Windowed[int]
    scalar_override: int
    windowed_int_override: Windowed[int]

class MappingFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[int]: ...

    @property
    def u_from(self) -> Type[str]: ...

    @property
    def u_to(self) -> Type[str]: ...

    @property
    def column_a(self) -> Type[str]: ...

    @property
    def swap_b(self) -> Type[str]: ...

    @property
    def swap_c(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class MappingFeatures(Features, metaclass=MappingFeaturesMetaclass):
    def __init__(
        self,
        id: int = ...,
        u_from: str = ...,
        u_to: str = ...,
        column_a: str = ...,
        swap_b: str = ...,
        swap_c: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: int
        self.u_from: str
        self.u_to: str
        self.column_a: str
        self.swap_b: str
        self.swap_c: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class MappingFeaturesProtocol(Protocol):
    id: int
    u_from: str
    u_to: str
    column_a: str
    swap_b: str
    swap_c: str

class CommentBaseOwnerMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def empty(self) -> Type[str]: ...

    @property
    def email(self) -> Type[str]: ...

    @property
    def email_commas(self) -> Type[str]: ...

    @property
    def email_single(self) -> Type[str]: ...

    @property
    def email_all_kinds(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class CommentBaseOwner(Features, metaclass=CommentBaseOwnerMetaclass):
    def __init__(
        self,
        id: str = ...,
        empty: str = ...,
        email: str = ...,
        email_commas: str = ...,
        email_single: str = ...,
        email_all_kinds: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.empty: str
        self.email: str
        self.email_commas: str
        self.email_single: str
        self.email_all_kinds: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class CommentBaseOwnerProtocol(Protocol):
    id: str
    empty: str
    email: str
    email_commas: str
    email_single: str
    email_all_kinds: str

class WindowTypeMetaclass(FeaturesMeta):
    @property
    def uid(self) -> Type[str]: ...

    @property
    def str_window__600__(self) -> Type[str]: ...

    @property
    def str_window(self) -> Type[Windowed[str]]: ...

    @property
    def int_window__600__(self) -> Type[int]: ...

    @property
    def int_window(self) -> Type[Windowed[int]]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class WindowType(Features, metaclass=WindowTypeMetaclass):
    def __init__(
        self,
        uid: str = ...,
        str_window__600__: str = ...,
        str_window: Windowed[str] = ...,
        int_window__600__: int = ...,
        int_window: Windowed[int] = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.uid: str
        self.str_window__600__: str
        self.str_window: Windowed[str]
        self.int_window__600__: int
        self.int_window: Windowed[int]
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class WindowTypeProtocol(Protocol):
    uid: str
    str_window: Windowed[str]
    int_window: Windowed[int]

class MeatMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[int]: ...

    @property
    def name(self) -> Type[str]: ...

    @property
    def calories(self) -> Type[float]: ...

    @property
    def burrito_id(self) -> Type[str]: ...

    @property
    def burrito(self) -> Type[__stubgen_tests_sql_test__sql__file__resolver_Burrito]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class Meat(Features, metaclass=MeatMetaclass):
    def __init__(
        self,
        id: int = ...,
        name: str = ...,
        calories: float = ...,
        burrito_id: str = ...,
        burrito: __stubgen_tests_sql_test__sql__file__resolver_Burrito = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: int
        self.name: str
        self.calories: float
        self.burrito_id: str
        self.burrito: __stubgen_tests_sql_test__sql__file__resolver_Burrito
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class MeatProtocol(Protocol):
    id: int
    name: str
    calories: float
    burrito_id: str
    burrito: __stubgen_tests_sql_test__sql__file__resolver_Burrito

class HomeFeaturesChainedFeatureTimeMetaclass(FeaturesMeta):
    @property
    def home_id(self) -> Type[str]: ...

    @property
    def address(self) -> Type[str]: ...

    @property
    def price(self) -> Type[int]: ...

    @property
    def sq_ft(self) -> Type[int]: ...

    @property
    def homeowner(self) -> Type[__stubgen_tests_features_test__chained__feature__time_Homeowner]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class HomeFeaturesChainedFeatureTime(Features, metaclass=HomeFeaturesChainedFeatureTimeMetaclass):
    def __init__(
        self,
        home_id: str = ...,
        address: str = ...,
        price: int = ...,
        sq_ft: int = ...,
        homeowner: __stubgen_tests_features_test__chained__feature__time_Homeowner = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.home_id: str
        self.address: str
        self.price: int
        self.sq_ft: int
        self.homeowner: __stubgen_tests_features_test__chained__feature__time_Homeowner
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class HomeFeaturesChainedFeatureTimeProtocol(Protocol):
    home_id: str
    address: str
    price: int
    sq_ft: int
    homeowner: __stubgen_tests_features_test__chained__feature__time_Homeowner

class ChildWindowMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def childfeat__600__(self) -> Type[str]: ...

    @property
    def childfeat__1200__(self) -> Type[str]: ...

    @property
    def childfeat(self) -> Type[Windowed[str]]: ...

    @property
    def grand(self) -> Type[__stubgen_tests_streams_test__window_GrandchildWindow]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class ChildWindow(Features, metaclass=ChildWindowMetaclass):
    def __init__(
        self,
        id: str = ...,
        childfeat__600__: str = ...,
        childfeat__1200__: str = ...,
        childfeat: Windowed[str] = ...,
        grand: __stubgen_tests_streams_test__window_GrandchildWindow = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.childfeat__600__: str
        self.childfeat__1200__: str
        self.childfeat: Windowed[str]
        self.grand: __stubgen_tests_streams_test__window_GrandchildWindow
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class ChildWindowProtocol(Protocol):
    id: str
    childfeat: Windowed[str]
    grand: __stubgen_tests_streams_test__window_GrandchildWindow

class TransactionMetaclass(FeaturesMeta):
    @property
    def user_id(self) -> Type[str]: ...

    @property
    def amount(self) -> Type[int]: ...

    @property
    def source_account_id(self) -> Type[int]: ...

    @property
    def dest_account_id(self) -> Type[int]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class Transaction(Features, metaclass=TransactionMetaclass):
    def __init__(
        self,
        user_id: str = ...,
        amount: int = ...,
        source_account_id: int = ...,
        dest_account_id: int = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.user_id: str
        self.amount: int
        self.source_account_id: int
        self.dest_account_id: int
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class TransactionProtocol(Protocol):
    user_id: str
    amount: int
    source_account_id: int
    dest_account_id: int

class ToppingMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def value(self) -> Type[int]: ...

    @property
    def ts(self) -> Type[__stubgen_datetime_datetime]: ...

    @property
    def nicknames(self) -> Type[DataFrame]: ...

    @property
    def price(self) -> Type[__stubgen_tests_features_test__df_ToppingPrice]: ...

class Topping(Features, metaclass=ToppingMetaclass):
    def __init__(
        self,
        id: str = ...,
        value: int = ...,
        ts: __stubgen_datetime_datetime = ...,
        nicknames: DataFrame = ...,
        price: __stubgen_tests_features_test__df_ToppingPrice = ...,
    ):
        self.id: str
        self.value: int
        self.ts: __stubgen_datetime_datetime
        self.nicknames: DataFrame
        self.price: __stubgen_tests_features_test__df_ToppingPrice

class ToppingProtocol(Protocol):
    id: str
    value: int
    ts: __stubgen_datetime_datetime
    nicknames: DataFrame
    price: __stubgen_tests_features_test__df_ToppingPrice

class StoreFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def purchases__600__(self) -> Type[float]: ...

    @property
    def purchases__1200__(self) -> Type[float]: ...

    @property
    def purchases(self) -> Type[Windowed[float]]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class StoreFeatures(Features, metaclass=StoreFeaturesMetaclass):
    def __init__(
        self,
        id: str = ...,
        purchases__600__: float = ...,
        purchases__1200__: float = ...,
        purchases: Windowed[float] = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.purchases__600__: float
        self.purchases__1200__: float
        self.purchases: Windowed[float]
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class StoreFeaturesProtocol(Protocol):
    id: str
    purchases: Windowed[float]

class MypyUserFeaturesMetaclass(FeaturesMeta):
    @property
    def uid(self) -> Type[str]: ...

    @property
    def name(self) -> Type[str]: ...

    @property
    def bday(self) -> Type[str]: ...

    @property
    def age(self) -> Type[int]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class MypyUserFeatures(Features, metaclass=MypyUserFeaturesMetaclass):
    def __init__(
        self,
        uid: str = ...,
        name: str = ...,
        bday: str = ...,
        age: int = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.uid: str
        self.name: str
        self.bday: str
        self.age: int
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class MypyUserFeaturesProtocol(Protocol):
    uid: str
    name: str
    bday: str
    age: int

class MaxStalenessFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[int]: ...

    @property
    def name(self) -> Type[str]: ...

    @property
    def woohoo(self) -> Type[str]: ...

    @property
    def boop(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class MaxStalenessFeatures(Features, metaclass=MaxStalenessFeaturesMetaclass):
    def __init__(
        self,
        id: int = ...,
        name: str = ...,
        woohoo: str = ...,
        boop: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: int
        self.name: str
        self.woohoo: str
        self.boop: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class MaxStalenessFeaturesProtocol(Protocol):
    id: int
    name: str
    woohoo: str
    boop: str

class HomeFeaturesMetaclass(FeaturesMeta):
    @property
    def home_id(self) -> Type[str]: ...

    @property
    def address(self) -> Type[str]: ...

    @property
    def price(self) -> Type[int]: ...

    @property
    def sq_ft(self) -> Type[int]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class HomeFeatures(Features, metaclass=HomeFeaturesMetaclass):
    def __init__(
        self,
        home_id: str = ...,
        address: str = ...,
        price: int = ...,
        sq_ft: int = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.home_id: str
        self.address: str
        self.price: int
        self.sq_ft: int
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class HomeFeaturesProtocol(Protocol):
    home_id: str
    address: str
    price: int
    sq_ft: int

class GrandchildWindowMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def grandchildfeat__600__(self) -> Type[str]: ...

    @property
    def grandchildfeat__1200__(self) -> Type[str]: ...

    @property
    def grandchildfeat(self) -> Type[Windowed[str]]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class GrandchildWindow(Features, metaclass=GrandchildWindowMetaclass):
    def __init__(
        self,
        id: str = ...,
        grandchildfeat__600__: str = ...,
        grandchildfeat__1200__: str = ...,
        grandchildfeat: Windowed[str] = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.grandchildfeat__600__: str
        self.grandchildfeat__1200__: str
        self.grandchildfeat: Windowed[str]
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class GrandchildWindowProtocol(Protocol):
    id: str
    grandchildfeat: Windowed[str]

class ContinuousFeatureClassMetaclass(FeaturesMeta):
    @property
    def c_feat__600__(self) -> Type[int]: ...

    @property
    def c_feat(self) -> Type[Windowed[int]]: ...

    @property
    def t_feat__600__(self) -> Type[int]: ...

    @property
    def t_feat(self) -> Type[Windowed[int]]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class ContinuousFeatureClass(Features, metaclass=ContinuousFeatureClassMetaclass):
    def __init__(
        self,
        c_feat__600__: int = ...,
        c_feat: Windowed[int] = ...,
        t_feat__600__: int = ...,
        t_feat: Windowed[int] = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.c_feat__600__: int
        self.c_feat: Windowed[int]
        self.t_feat__600__: int
        self.t_feat: Windowed[int]
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class ContinuousFeatureClassProtocol(Protocol):
    c_feat: Windowed[int]
    t_feat: Windowed[int]

class UserProfileMetaclass(FeaturesMeta):
    @property
    def user_id(self) -> Type[str]: ...

    @property
    def profile_id(self) -> Type[str]: ...

    @property
    def address(self) -> Type[int]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class UserProfile(Features, metaclass=UserProfileMetaclass):
    def __init__(
        self,
        user_id: str = ...,
        profile_id: str = ...,
        address: int = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.user_id: str
        self.profile_id: str
        self.address: int
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class UserProfileProtocol(Protocol):
    user_id: str
    profile_id: str
    address: int

class ToppingPriceMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def topping_id(self) -> Type[str]: ...

    @property
    def wow(self) -> Type[str]: ...

    @property
    def ts(self) -> Type[__stubgen_datetime_datetime]: ...

class ToppingPrice(Features, metaclass=ToppingPriceMetaclass):
    def __init__(
        self,
        id: str = ...,
        topping_id: str = ...,
        wow: str = ...,
        ts: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.topping_id: str
        self.wow: str
        self.ts: __stubgen_datetime_datetime

class ToppingPriceProtocol(Protocol):
    id: str
    topping_id: str
    wow: str
    ts: __stubgen_datetime_datetime

class TagFeaturesMetaclass(FeaturesMeta):
    @property
    def empty(self) -> Type[str]: ...

    @property
    def one(self) -> Type[str]: ...

    @property
    def many(self) -> Type[str]: ...

    @property
    def ft(self) -> Type[__stubgen_datetime_datetime]: ...

class TagFeatures(Features, metaclass=TagFeaturesMetaclass):
    def __init__(
        self,
        empty: str = ...,
        one: str = ...,
        many: str = ...,
        ft: __stubgen_datetime_datetime = ...,
    ):
        self.empty: str
        self.one: str
        self.many: str
        self.ft: __stubgen_datetime_datetime

class TagFeaturesProtocol(Protocol):
    empty: str
    one: str
    many: str
    ft: __stubgen_datetime_datetime

class SQLFriendsWithRowMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[int]: ...

    @property
    def u_from(self) -> Type[str]: ...

    @property
    def u_to(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class SQLFriendsWithRow(Features, metaclass=SQLFriendsWithRowMetaclass):
    def __init__(
        self,
        id: int = ...,
        u_from: str = ...,
        u_to: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: int
        self.u_from: str
        self.u_to: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class SQLFriendsWithRowProtocol(Protocol):
    id: int
    u_from: str
    u_to: str

class PlaidAccountMetaclass(FeaturesMeta):
    @property
    def user_id(self) -> Type[str]: ...

    @property
    def user(self) -> Type[__stubgen_tests_client_test__client__printing_User]: ...

    @property
    def bank_name(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class PlaidAccount(Features, metaclass=PlaidAccountMetaclass):
    def __init__(
        self,
        user_id: str = ...,
        user: __stubgen_tests_client_test__client__printing_User = ...,
        bank_name: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.user_id: str
        self.user: __stubgen_tests_client_test__client__printing_User
        self.bank_name: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class PlaidAccountProtocol(Protocol):
    user_id: str
    user: __stubgen_tests_client_test__client__printing_User
    bank_name: str

class ParentFSMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def children(self) -> Type[DataFrame]: ...

    @property
    def single_child(self) -> Type[__stubgen_tests_features_test__features_SingleChildFS]: ...

    @property
    def ts(self) -> Type[__stubgen_datetime_datetime]: ...

class ParentFS(Features, metaclass=ParentFSMetaclass):
    def __init__(
        self,
        id: str = ...,
        children: DataFrame = ...,
        single_child: __stubgen_tests_features_test__features_SingleChildFS = ...,
        ts: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.children: DataFrame
        self.single_child: __stubgen_tests_features_test__features_SingleChildFS
        self.ts: __stubgen_datetime_datetime

class ParentFSProtocol(Protocol):
    id: str
    children: DataFrame
    single_child: __stubgen_tests_features_test__features_SingleChildFS
    ts: __stubgen_datetime_datetime

class OwnerFeaturesMetaclass(FeaturesMeta):
    @property
    def plain(self) -> Type[str]: ...

    @property
    def cached(self) -> Type[str]: ...

    @property
    def andy(self) -> Type[str]: ...

    @property
    def ft(self) -> Type[__stubgen_datetime_datetime]: ...

class OwnerFeatures(Features, metaclass=OwnerFeaturesMetaclass):
    def __init__(
        self,
        plain: str = ...,
        cached: str = ...,
        andy: str = ...,
        ft: __stubgen_datetime_datetime = ...,
    ):
        self.plain: str
        self.cached: str
        self.andy: str
        self.ft: __stubgen_datetime_datetime

class OwnerFeaturesProtocol(Protocol):
    plain: str
    cached: str
    andy: str
    ft: __stubgen_datetime_datetime

class OtherPrimaryKeyFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def nah_really_this_is_id(self) -> Type[str]: ...

    @property
    def other(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class OtherPrimaryKeyFeatures(Features, metaclass=OtherPrimaryKeyFeaturesMetaclass):
    def __init__(
        self,
        id: str = ...,
        nah_really_this_is_id: str = ...,
        other: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.nah_really_this_is_id: str
        self.other: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class OtherPrimaryKeyFeaturesProtocol(Protocol):
    id: str
    nah_really_this_is_id: str
    other: str

class FunFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def nope(self) -> Type[str]: ...

    @property
    def single_parent(self) -> Type[__stubgen_tests_features_test__iter_NoFunFeatures]: ...

    @property
    def ts(self) -> Type[__stubgen_datetime_datetime]: ...

class FunFeatures(Features, metaclass=FunFeaturesMetaclass):
    def __init__(
        self,
        id: str = ...,
        nope: str = ...,
        single_parent: __stubgen_tests_features_test__iter_NoFunFeatures = ...,
        ts: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.nope: str
        self.single_parent: __stubgen_tests_features_test__iter_NoFunFeatures
        self.ts: __stubgen_datetime_datetime

class FunFeaturesProtocol(Protocol):
    id: str
    nope: str
    single_parent: __stubgen_tests_features_test__iter_NoFunFeatures
    ts: __stubgen_datetime_datetime

class ETLFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[int]: ...

    @property
    def name(self) -> Type[str]: ...

    @property
    def woohoo(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class ETLFeatures(Features, metaclass=ETLFeaturesMetaclass):
    def __init__(
        self,
        id: int = ...,
        name: str = ...,
        woohoo: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: int
        self.name: str
        self.woohoo: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class ETLFeaturesProtocol(Protocol):
    id: int
    name: str
    woohoo: str

class ColNameMappingFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def foo(self) -> Type[str]: ...

    @property
    def bar(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class ColNameMappingFeatures(Features, metaclass=ColNameMappingFeaturesMetaclass):
    def __init__(
        self,
        id: str = ...,
        foo: str = ...,
        bar: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.foo: str
        self.bar: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class ColNameMappingFeaturesProtocol(Protocol):
    id: str
    foo: str
    bar: str

class ChildFSMetaclass(FeaturesMeta):
    @property
    def parent_id(self) -> Type[str]: ...

    @property
    def parents(self) -> Type[DataFrame]: ...

    @property
    def single_parent(self) -> Type[__stubgen_tests_features_test__features_SingleParentFS]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class ChildFS(Features, metaclass=ChildFSMetaclass):
    def __init__(
        self,
        parent_id: str = ...,
        parents: DataFrame = ...,
        single_parent: __stubgen_tests_features_test__features_SingleParentFS = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.parent_id: str
        self.parents: DataFrame
        self.single_parent: __stubgen_tests_features_test__features_SingleParentFS
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class ChildFSProtocol(Protocol):
    parent_id: str
    parents: DataFrame
    single_parent: __stubgen_tests_features_test__features_SingleParentFS

class BurritoMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def name(self) -> Type[str]: ...

    @property
    def size(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class Burrito(Features, metaclass=BurritoMetaclass):
    def __init__(
        self,
        id: str = ...,
        name: str = ...,
        size: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.name: str
        self.size: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class BurritoProtocol(Protocol):
    id: str
    name: str
    size: str

class UserMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def email(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class User(Features, metaclass=UserMetaclass):
    def __init__(
        self,
        id: str = ...,
        email: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.email: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class UserProtocol(Protocol):
    id: str
    email: str

class UnassignedIdFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def other(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class UnassignedIdFeatures(Features, metaclass=UnassignedIdFeaturesMetaclass):
    def __init__(
        self,
        id: str = ...,
        other: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.other: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class UnassignedIdFeaturesProtocol(Protocol):
    id: str
    other: str

class UnassignedDecoratedIdFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def other(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class UnassignedDecoratedIdFeatures(Features, metaclass=UnassignedDecoratedIdFeaturesMetaclass):
    def __init__(
        self,
        id: str = ...,
        other: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.other: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class UnassignedDecoratedIdFeaturesProtocol(Protocol):
    id: str
    other: str

class TxnMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def amount(self) -> Type[float]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class Txn(Features, metaclass=TxnMetaclass):
    def __init__(
        self,
        id: str = ...,
        amount: float = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.amount: float
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class TxnProtocol(Protocol):
    id: str
    amount: float

class TheArtistFormerlyKnownAsPrinceMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def favorite_color(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class TheArtistFormerlyKnownAsPrince(Features, metaclass=TheArtistFormerlyKnownAsPrinceMetaclass):
    def __init__(
        self,
        id: str = ...,
        favorite_color: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.favorite_color: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class TheArtistFormerlyKnownAsPrinceProtocol(Protocol):
    id: str
    favorite_color: str

class SingleParentFSMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def children(self) -> Type[DataFrame]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class SingleParentFS(Features, metaclass=SingleParentFSMetaclass):
    def __init__(
        self,
        id: str = ...,
        children: DataFrame = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.children: DataFrame
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class SingleParentFSProtocol(Protocol):
    id: str
    children: DataFrame

class SingleChildFSMetaclass(FeaturesMeta):
    @property
    def parent_id(self) -> Type[str]: ...

    @property
    def parent(self) -> Type[DataFrame]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class SingleChildFS(Features, metaclass=SingleChildFSMetaclass):
    def __init__(
        self,
        parent_id: str = ...,
        parent: DataFrame = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.parent_id: str
        self.parent: DataFrame
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class SingleChildFSProtocol(Protocol):
    parent_id: str
    parent: DataFrame

class SillyMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def name(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class Silly(Features, metaclass=SillyMetaclass):
    def __init__(
        self,
        id: str = ...,
        name: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.name: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class SillyProtocol(Protocol):
    id: str
    name: str

class SQLUserFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def name(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class SQLUserFeatures(Features, metaclass=SQLUserFeaturesMetaclass):
    def __init__(
        self,
        id: str = ...,
        name: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.name: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class SQLUserFeaturesProtocol(Protocol):
    id: str
    name: str

class SQLExecuteNestedFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[int]: ...

    @property
    def nested_int(self) -> Type[int]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class SQLExecuteNestedFeatures(Features, metaclass=SQLExecuteNestedFeaturesMetaclass):
    def __init__(
        self,
        id: int = ...,
        nested_int: int = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: int
        self.nested_int: int
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class SQLExecuteNestedFeaturesProtocol(Protocol):
    id: int
    nested_int: int

class PrimaryCls2Metaclass(FeaturesMeta):
    @property
    def myid(self) -> Type[str]: ...

    @property
    def id(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class PrimaryCls2(Features, metaclass=PrimaryCls2Metaclass):
    def __init__(
        self,
        myid: str = ...,
        id: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.myid: str
        self.id: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class PrimaryCls2Protocol(Protocol):
    myid: str
    id: str

class NotIdIsIdFeaturesMetaclass(FeaturesMeta):
    @property
    def not_id(self) -> Type[str]: ...

    @property
    def other(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class NotIdIsIdFeatures(Features, metaclass=NotIdIsIdFeaturesMetaclass):
    def __init__(
        self,
        not_id: str = ...,
        other: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.not_id: str
        self.other: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class NotIdIsIdFeaturesProtocol(Protocol):
    not_id: str
    other: str

class IdIsNotIdFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def other(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class IdIsNotIdFeatures(Features, metaclass=IdIsNotIdFeaturesMetaclass):
    def __init__(
        self,
        id: str = ...,
        other: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.other: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class IdIsNotIdFeaturesProtocol(Protocol):
    id: str
    other: str

class HomeownerMetaclass(FeaturesMeta):
    @property
    def fullname(self) -> Type[str]: ...

    @property
    def home_id(self) -> Type[str]: ...

    @property
    def ts(self) -> Type[__stubgen_datetime_datetime]: ...

class Homeowner(Features, metaclass=HomeownerMetaclass):
    def __init__(
        self,
        fullname: str = ...,
        home_id: str = ...,
        ts: __stubgen_datetime_datetime = ...,
    ):
        self.fullname: str
        self.home_id: str
        self.ts: __stubgen_datetime_datetime

class HomeownerProtocol(Protocol):
    fullname: str
    home_id: str
    ts: __stubgen_datetime_datetime

class FTCls2Metaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def ts(self) -> Type[__stubgen_datetime_datetime]: ...

    @property
    def timestamp(self) -> Type[__stubgen_datetime_datetime]: ...

class FTCls2(Features, metaclass=FTCls2Metaclass):
    def __init__(
        self,
        id: str = ...,
        ts: __stubgen_datetime_datetime = ...,
        timestamp: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.ts: __stubgen_datetime_datetime
        self.timestamp: __stubgen_datetime_datetime

class FTCls2Protocol(Protocol):
    id: str
    ts: __stubgen_datetime_datetime
    timestamp: __stubgen_datetime_datetime

class ExplicitIdFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def other(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class ExplicitIdFeatures(Features, metaclass=ExplicitIdFeaturesMetaclass):
    def __init__(
        self,
        id: str = ...,
        other: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.other: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class ExplicitIdFeaturesProtocol(Protocol):
    id: str
    other: str

class ExampleFraudUserMetaclass(FeaturesMeta):
    @property
    def uid(self) -> Type[str]: ...

    @property
    def org(self) -> Type[__stubgen_tests_features_test__chained__has__one_ExampleFraudOrg]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class ExampleFraudUser(Features, metaclass=ExampleFraudUserMetaclass):
    def __init__(
        self,
        uid: str = ...,
        org: __stubgen_tests_features_test__chained__has__one_ExampleFraudOrg = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.uid: str
        self.org: __stubgen_tests_features_test__chained__has__one_ExampleFraudOrg
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class ExampleFraudUserProtocol(Protocol):
    uid: str
    org: __stubgen_tests_features_test__chained__has__one_ExampleFraudOrg

class ExampleFraudProfileMetaclass(FeaturesMeta):
    @property
    def uid(self) -> Type[str]: ...

    @property
    def user(self) -> Type[__stubgen_tests_features_test__chained__has__one_ExampleFraudUser]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class ExampleFraudProfile(Features, metaclass=ExampleFraudProfileMetaclass):
    def __init__(
        self,
        uid: str = ...,
        user: __stubgen_tests_features_test__chained__has__one_ExampleFraudUser = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.uid: str
        self.user: __stubgen_tests_features_test__chained__has__one_ExampleFraudUser
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class ExampleFraudProfileProtocol(Protocol):
    uid: str
    user: __stubgen_tests_features_test__chained__has__one_ExampleFraudUser

class ExampleFraudOrgMetaclass(FeaturesMeta):
    @property
    def uid(self) -> Type[str]: ...

    @property
    def org_name(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class ExampleFraudOrg(Features, metaclass=ExampleFraudOrgMetaclass):
    def __init__(
        self,
        uid: str = ...,
        org_name: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.uid: str
        self.org_name: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class ExampleFraudOrgProtocol(Protocol):
    uid: str
    org_name: str

class CustomNameClassMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def other(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class CustomNameClass(Features, metaclass=CustomNameClassMetaclass):
    def __init__(
        self,
        id: str = ...,
        other: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.other: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class CustomNameClassProtocol(Protocol):
    id: str
    other: str

class BogusIdFeature2Metaclass(FeaturesMeta):
    @property
    def id(self) -> Type[DataFrame]: ...

    @property
    def other(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class BogusIdFeature2(Features, metaclass=BogusIdFeature2Metaclass):
    def __init__(
        self,
        id: DataFrame = ...,
        other: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: DataFrame
        self.other: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class BogusIdFeature2Protocol(Protocol):
    id: DataFrame
    other: str

class BogusIdFeature1Metaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def other(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class BogusIdFeature1(Features, metaclass=BogusIdFeature1Metaclass):
    def __init__(
        self,
        id: str = ...,
        other: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.other: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class BogusIdFeature1Protocol(Protocol):
    id: str
    other: str

class AcctMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def balance(self) -> Type[float]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class Acct(Features, metaclass=AcctMetaclass):
    def __init__(
        self,
        id: str = ...,
        balance: float = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.balance: float
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class AcctProtocol(Protocol):
    id: str
    balance: float

class AccountMetaclass(FeaturesMeta):
    @property
    def account_id(self) -> Type[str]: ...

    @property
    def balance(self) -> Type[int]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class Account(Features, metaclass=AccountMetaclass):
    def __init__(
        self,
        account_id: str = ...,
        balance: int = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.account_id: str
        self.balance: int
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class AccountProtocol(Protocol):
    account_id: str
    balance: int

class UserFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class UserFeatures(Features, metaclass=UserFeaturesMetaclass):
    def __init__(
        self,
        id: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class UserFeaturesProtocol(Protocol):
    id: str

class StreamFeaturesMetaclass(FeaturesMeta):
    @property
    def scalar_feature(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class StreamFeatures(Features, metaclass=StreamFeaturesMetaclass):
    def __init__(
        self,
        scalar_feature: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.scalar_feature: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class StreamFeaturesProtocol(Protocol):
    scalar_feature: str

class PrimaryClsMetaclass(FeaturesMeta):
    @property
    def myid(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class PrimaryCls(Features, metaclass=PrimaryClsMetaclass):
    def __init__(
        self,
        myid: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.myid: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class PrimaryClsProtocol(Protocol):
    myid: str

class NoFunFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class NoFunFeatures(Features, metaclass=NoFunFeaturesMetaclass):
    def __init__(
        self,
        id: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class NoFunFeaturesProtocol(Protocol):
    id: str

class NicknameMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class Nickname(Features, metaclass=NicknameMetaclass):
    def __init__(
        self,
        id: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class NicknameProtocol(Protocol):
    id: str

class MaxStalenessFeatures2Metaclass(FeaturesMeta):
    @property
    def id(self) -> Type[int]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class MaxStalenessFeatures2(Features, metaclass=MaxStalenessFeatures2Metaclass):
    def __init__(
        self,
        id: int = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: int
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class MaxStalenessFeatures2Protocol(Protocol):
    id: int

class LibraryFeaturesMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class LibraryFeatures(Features, metaclass=LibraryFeaturesMetaclass):
    def __init__(
        self,
        id: str = ...,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class LibraryFeaturesProtocol(Protocol):
    id: str

class FTCls1Metaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def ts(self) -> Type[__stubgen_datetime_datetime]: ...

class FTCls1(Features, metaclass=FTCls1Metaclass):
    def __init__(
        self,
        id: str = ...,
        ts: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.ts: __stubgen_datetime_datetime

class FTCls1Protocol(Protocol):
    id: str
    ts: __stubgen_datetime_datetime

class FTClsMetaclass(FeaturesMeta):
    @property
    def id(self) -> Type[str]: ...

    @property
    def timestamp(self) -> Type[__stubgen_datetime_datetime]: ...

class FTCls(Features, metaclass=FTClsMetaclass):
    def __init__(
        self,
        id: str = ...,
        timestamp: __stubgen_datetime_datetime = ...,
    ):
        self.id: str
        self.timestamp: __stubgen_datetime_datetime

class FTClsProtocol(Protocol):
    id: str
    timestamp: __stubgen_datetime_datetime

class BogusIdFeature3Metaclass(FeaturesMeta):
    @property
    def id(self) -> Type[__stubgen_datetime_datetime]: ...

    @property
    def other(self) -> Type[str]: ...

class BogusIdFeature3(Features, metaclass=BogusIdFeature3Metaclass):
    def __init__(
        self,
        id: __stubgen_datetime_datetime = ...,
        other: str = ...,
    ):
        self.id: __stubgen_datetime_datetime
        self.other: str

class BogusIdFeature3Protocol(Protocol):
    id: __stubgen_datetime_datetime
    other: str

class FeaturesClassWithoutTimestampMetaclass(FeaturesMeta):
    @property
    def __chalk_observed_at__(self) -> Type[__stubgen_datetime_datetime]: ...

class FeaturesClassWithoutTimestamp(Features, metaclass=FeaturesClassWithoutTimestampMetaclass):
    def __init__(
        self,
        __chalk_observed_at__: __stubgen_datetime_datetime = ...,
    ):
        self.__chalk_observed_at__: __stubgen_datetime_datetime

class FeaturesClassWithoutTimestampProtocol(Protocol):
    ...

class FeaturesClassWithNamedTsMetaclass(FeaturesMeta):
    @property
    def ts(self) -> Type[__stubgen_datetime_datetime]: ...

class FeaturesClassWithNamedTs(Features, metaclass=FeaturesClassWithNamedTsMetaclass):
    def __init__(
        self,
        ts: __stubgen_datetime_datetime = ...,
    ):
        self.ts: __stubgen_datetime_datetime

class FeaturesClassWithNamedTsProtocol(Protocol):
    ts: __stubgen_datetime_datetime

class FeaturesClassWithCustomTsNameMetaclass(FeaturesMeta):
    @property
    def ts_custom_name(self) -> Type[__stubgen_datetime_datetime]: ...

class FeaturesClassWithCustomTsName(Features, metaclass=FeaturesClassWithCustomTsNameMetaclass):
    def __init__(
        self,
        ts_custom_name: __stubgen_datetime_datetime = ...,
    ):
        self.ts_custom_name: __stubgen_datetime_datetime

class FeaturesClassWithCustomTsNameProtocol(Protocol):
    ts_custom_name: __stubgen_datetime_datetime

@overload
def features(item: Type[TacoProtocol]) -> Type[Taco]: ...

@overload
def features(item: Type[SQLExecuteFeaturesProtocol]) -> Type[SQLExecuteFeatures]: ...

@overload
def features(item: Type[WowFSProtocol]) -> Type[WowFS]: ...

@overload
def features(item: Type[StreamFeaturesWindowProtocol]) -> Type[StreamFeaturesWindow]: ...

@overload
def features(item: Type[HelloProtocol]) -> Type[Hello]: ...

@overload
def features(item: Type[FSWithStalenessProtocol]) -> Type[FSWithStaleness]: ...

@overload
def features(item: Type[MappingFeaturesProtocol]) -> Type[MappingFeatures]: ...

@overload
def features(item: Type[CommentBaseOwnerProtocol]) -> Type[CommentBaseOwner]: ...

@overload
def features(item: Type[WindowTypeProtocol]) -> Type[WindowType]: ...

@overload
def features(item: Type[MeatProtocol]) -> Type[Meat]: ...

@overload
def features(item: Type[HomeFeaturesChainedFeatureTimeProtocol]) -> Type[HomeFeaturesChainedFeatureTime]: ...

@overload
def features(item: Type[ChildWindowProtocol]) -> Type[ChildWindow]: ...

@overload
def features(item: Type[TransactionProtocol]) -> Type[Transaction]: ...

@overload
def features(item: Type[ToppingProtocol]) -> Type[Topping]: ...

@overload
def features(item: Type[StoreFeaturesProtocol]) -> Type[StoreFeatures]: ...

@overload
def features(item: Type[MypyUserFeaturesProtocol]) -> Type[MypyUserFeatures]: ...

@overload
def features(item: Type[MaxStalenessFeaturesProtocol]) -> Type[MaxStalenessFeatures]: ...

@overload
def features(item: Type[HomeFeaturesProtocol]) -> Type[HomeFeatures]: ...

@overload
def features(item: Type[GrandchildWindowProtocol]) -> Type[GrandchildWindow]: ...

@overload
def features(item: Type[ContinuousFeatureClassProtocol]) -> Type[ContinuousFeatureClass]: ...

@overload
def features(item: Type[UserProfileProtocol]) -> Type[UserProfile]: ...

@overload
def features(item: Type[ToppingPriceProtocol]) -> Type[ToppingPrice]: ...

@overload
def features(item: Type[TagFeaturesProtocol]) -> Type[TagFeatures]: ...

@overload
def features(item: Type[SQLFriendsWithRowProtocol]) -> Type[SQLFriendsWithRow]: ...

@overload
def features(item: Type[PlaidAccountProtocol]) -> Type[PlaidAccount]: ...

@overload
def features(item: Type[ParentFSProtocol]) -> Type[ParentFS]: ...

@overload
def features(item: Type[OwnerFeaturesProtocol]) -> Type[OwnerFeatures]: ...

@overload
def features(item: Type[OtherPrimaryKeyFeaturesProtocol]) -> Type[OtherPrimaryKeyFeatures]: ...

@overload
def features(item: Type[FunFeaturesProtocol]) -> Type[FunFeatures]: ...

@overload
def features(item: Type[ETLFeaturesProtocol]) -> Type[ETLFeatures]: ...

@overload
def features(item: Type[ColNameMappingFeaturesProtocol]) -> Type[ColNameMappingFeatures]: ...

@overload
def features(item: Type[ChildFSProtocol]) -> Type[ChildFS]: ...

@overload
def features(item: Type[BurritoProtocol]) -> Type[Burrito]: ...

@overload
def features(item: Type[UserProtocol]) -> Type[User]: ...

@overload
def features(item: Type[UnassignedIdFeaturesProtocol]) -> Type[UnassignedIdFeatures]: ...

@overload
def features(item: Type[UnassignedDecoratedIdFeaturesProtocol]) -> Type[UnassignedDecoratedIdFeatures]: ...

@overload
def features(item: Type[TxnProtocol]) -> Type[Txn]: ...

@overload
def features(item: Type[TheArtistFormerlyKnownAsPrinceProtocol]) -> Type[TheArtistFormerlyKnownAsPrince]: ...

@overload
def features(item: Type[SingleParentFSProtocol]) -> Type[SingleParentFS]: ...

@overload
def features(item: Type[SingleChildFSProtocol]) -> Type[SingleChildFS]: ...

@overload
def features(item: Type[SillyProtocol]) -> Type[Silly]: ...

@overload
def features(item: Type[SQLUserFeaturesProtocol]) -> Type[SQLUserFeatures]: ...

@overload
def features(item: Type[SQLExecuteNestedFeaturesProtocol]) -> Type[SQLExecuteNestedFeatures]: ...

@overload
def features(item: Type[PrimaryCls2Protocol]) -> Type[PrimaryCls2]: ...

@overload
def features(item: Type[NotIdIsIdFeaturesProtocol]) -> Type[NotIdIsIdFeatures]: ...

@overload
def features(item: Type[IdIsNotIdFeaturesProtocol]) -> Type[IdIsNotIdFeatures]: ...

@overload
def features(item: Type[HomeownerProtocol]) -> Type[Homeowner]: ...

@overload
def features(item: Type[FTCls2Protocol]) -> Type[FTCls2]: ...

@overload
def features(item: Type[ExplicitIdFeaturesProtocol]) -> Type[ExplicitIdFeatures]: ...

@overload
def features(item: Type[ExampleFraudUserProtocol]) -> Type[ExampleFraudUser]: ...

@overload
def features(item: Type[ExampleFraudProfileProtocol]) -> Type[ExampleFraudProfile]: ...

@overload
def features(item: Type[ExampleFraudOrgProtocol]) -> Type[ExampleFraudOrg]: ...

@overload
def features(item: Type[CustomNameClassProtocol]) -> Type[CustomNameClass]: ...

@overload
def features(item: Type[BogusIdFeature2Protocol]) -> Type[BogusIdFeature2]: ...

@overload
def features(item: Type[BogusIdFeature1Protocol]) -> Type[BogusIdFeature1]: ...

@overload
def features(item: Type[AcctProtocol]) -> Type[Acct]: ...

@overload
def features(item: Type[AccountProtocol]) -> Type[Account]: ...

@overload
def features(item: Type[UserFeaturesProtocol]) -> Type[UserFeatures]: ...

@overload
def features(item: Type[StreamFeaturesProtocol]) -> Type[StreamFeatures]: ...

@overload
def features(item: Type[PrimaryClsProtocol]) -> Type[PrimaryCls]: ...

@overload
def features(item: Type[NoFunFeaturesProtocol]) -> Type[NoFunFeatures]: ...

@overload
def features(item: Type[NicknameProtocol]) -> Type[Nickname]: ...

@overload
def features(item: Type[MaxStalenessFeatures2Protocol]) -> Type[MaxStalenessFeatures2]: ...

@overload
def features(item: Type[LibraryFeaturesProtocol]) -> Type[LibraryFeatures]: ...

@overload
def features(item: Type[FTCls1Protocol]) -> Type[FTCls1]: ...

@overload
def features(item: Type[FTClsProtocol]) -> Type[FTCls]: ...

@overload
def features(item: Type[BogusIdFeature3Protocol]) -> Type[BogusIdFeature3]: ...

@overload
def features(item: Type[FeaturesClassWithoutTimestampProtocol]) -> Type[FeaturesClassWithoutTimestamp]: ...

@overload
def features(item: Type[FeaturesClassWithNamedTsProtocol]) -> Type[FeaturesClassWithNamedTs]: ...

@overload
def features(item: Type[FeaturesClassWithCustomTsNameProtocol]) -> Type[FeaturesClassWithCustomTsName]: ...

@overload
def features(
    *,
    owner: Optional[str] = ...,
    tags: Optional[Tags] = ...,
    max_staleness: Optional[Duration] = ...,
    etl_offline_to_online: Optional[bool] = ...,
) -> __stubgen__features_proto: ...

class __stubgen__features_proto(Protocol):
    @overload
    def __call__(self, item: Type[TacoProtocol]) -> Type[Taco]: ...

    @overload
    def __call__(self, item: Type[SQLExecuteFeaturesProtocol]) -> Type[SQLExecuteFeatures]: ...

    @overload
    def __call__(self, item: Type[WowFSProtocol]) -> Type[WowFS]: ...

    @overload
    def __call__(self, item: Type[StreamFeaturesWindowProtocol]) -> Type[StreamFeaturesWindow]: ...

    @overload
    def __call__(self, item: Type[HelloProtocol]) -> Type[Hello]: ...

    @overload
    def __call__(self, item: Type[FSWithStalenessProtocol]) -> Type[FSWithStaleness]: ...

    @overload
    def __call__(self, item: Type[MappingFeaturesProtocol]) -> Type[MappingFeatures]: ...

    @overload
    def __call__(self, item: Type[CommentBaseOwnerProtocol]) -> Type[CommentBaseOwner]: ...

    @overload
    def __call__(self, item: Type[WindowTypeProtocol]) -> Type[WindowType]: ...

    @overload
    def __call__(self, item: Type[MeatProtocol]) -> Type[Meat]: ...

    @overload
    def __call__(self, item: Type[HomeFeaturesChainedFeatureTimeProtocol]) -> Type[HomeFeaturesChainedFeatureTime]: ...

    @overload
    def __call__(self, item: Type[ChildWindowProtocol]) -> Type[ChildWindow]: ...

    @overload
    def __call__(self, item: Type[TransactionProtocol]) -> Type[Transaction]: ...

    @overload
    def __call__(self, item: Type[ToppingProtocol]) -> Type[Topping]: ...

    @overload
    def __call__(self, item: Type[StoreFeaturesProtocol]) -> Type[StoreFeatures]: ...

    @overload
    def __call__(self, item: Type[MypyUserFeaturesProtocol]) -> Type[MypyUserFeatures]: ...

    @overload
    def __call__(self, item: Type[MaxStalenessFeaturesProtocol]) -> Type[MaxStalenessFeatures]: ...

    @overload
    def __call__(self, item: Type[HomeFeaturesProtocol]) -> Type[HomeFeatures]: ...

    @overload
    def __call__(self, item: Type[GrandchildWindowProtocol]) -> Type[GrandchildWindow]: ...

    @overload
    def __call__(self, item: Type[ContinuousFeatureClassProtocol]) -> Type[ContinuousFeatureClass]: ...

    @overload
    def __call__(self, item: Type[UserProfileProtocol]) -> Type[UserProfile]: ...

    @overload
    def __call__(self, item: Type[ToppingPriceProtocol]) -> Type[ToppingPrice]: ...

    @overload
    def __call__(self, item: Type[TagFeaturesProtocol]) -> Type[TagFeatures]: ...

    @overload
    def __call__(self, item: Type[SQLFriendsWithRowProtocol]) -> Type[SQLFriendsWithRow]: ...

    @overload
    def __call__(self, item: Type[PlaidAccountProtocol]) -> Type[PlaidAccount]: ...

    @overload
    def __call__(self, item: Type[ParentFSProtocol]) -> Type[ParentFS]: ...

    @overload
    def __call__(self, item: Type[OwnerFeaturesProtocol]) -> Type[OwnerFeatures]: ...

    @overload
    def __call__(self, item: Type[OtherPrimaryKeyFeaturesProtocol]) -> Type[OtherPrimaryKeyFeatures]: ...

    @overload
    def __call__(self, item: Type[FunFeaturesProtocol]) -> Type[FunFeatures]: ...

    @overload
    def __call__(self, item: Type[ETLFeaturesProtocol]) -> Type[ETLFeatures]: ...

    @overload
    def __call__(self, item: Type[ColNameMappingFeaturesProtocol]) -> Type[ColNameMappingFeatures]: ...

    @overload
    def __call__(self, item: Type[ChildFSProtocol]) -> Type[ChildFS]: ...

    @overload
    def __call__(self, item: Type[BurritoProtocol]) -> Type[Burrito]: ...

    @overload
    def __call__(self, item: Type[UserProtocol]) -> Type[User]: ...

    @overload
    def __call__(self, item: Type[UnassignedIdFeaturesProtocol]) -> Type[UnassignedIdFeatures]: ...

    @overload
    def __call__(self, item: Type[UnassignedDecoratedIdFeaturesProtocol]) -> Type[UnassignedDecoratedIdFeatures]: ...

    @overload
    def __call__(self, item: Type[TxnProtocol]) -> Type[Txn]: ...

    @overload
    def __call__(self, item: Type[TheArtistFormerlyKnownAsPrinceProtocol]) -> Type[TheArtistFormerlyKnownAsPrince]: ...

    @overload
    def __call__(self, item: Type[SingleParentFSProtocol]) -> Type[SingleParentFS]: ...

    @overload
    def __call__(self, item: Type[SingleChildFSProtocol]) -> Type[SingleChildFS]: ...

    @overload
    def __call__(self, item: Type[SillyProtocol]) -> Type[Silly]: ...

    @overload
    def __call__(self, item: Type[SQLUserFeaturesProtocol]) -> Type[SQLUserFeatures]: ...

    @overload
    def __call__(self, item: Type[SQLExecuteNestedFeaturesProtocol]) -> Type[SQLExecuteNestedFeatures]: ...

    @overload
    def __call__(self, item: Type[PrimaryCls2Protocol]) -> Type[PrimaryCls2]: ...

    @overload
    def __call__(self, item: Type[NotIdIsIdFeaturesProtocol]) -> Type[NotIdIsIdFeatures]: ...

    @overload
    def __call__(self, item: Type[IdIsNotIdFeaturesProtocol]) -> Type[IdIsNotIdFeatures]: ...

    @overload
    def __call__(self, item: Type[HomeownerProtocol]) -> Type[Homeowner]: ...

    @overload
    def __call__(self, item: Type[FTCls2Protocol]) -> Type[FTCls2]: ...

    @overload
    def __call__(self, item: Type[ExplicitIdFeaturesProtocol]) -> Type[ExplicitIdFeatures]: ...

    @overload
    def __call__(self, item: Type[ExampleFraudUserProtocol]) -> Type[ExampleFraudUser]: ...

    @overload
    def __call__(self, item: Type[ExampleFraudProfileProtocol]) -> Type[ExampleFraudProfile]: ...

    @overload
    def __call__(self, item: Type[ExampleFraudOrgProtocol]) -> Type[ExampleFraudOrg]: ...

    @overload
    def __call__(self, item: Type[CustomNameClassProtocol]) -> Type[CustomNameClass]: ...

    @overload
    def __call__(self, item: Type[BogusIdFeature2Protocol]) -> Type[BogusIdFeature2]: ...

    @overload
    def __call__(self, item: Type[BogusIdFeature1Protocol]) -> Type[BogusIdFeature1]: ...

    @overload
    def __call__(self, item: Type[AcctProtocol]) -> Type[Acct]: ...

    @overload
    def __call__(self, item: Type[AccountProtocol]) -> Type[Account]: ...

    @overload
    def __call__(self, item: Type[UserFeaturesProtocol]) -> Type[UserFeatures]: ...

    @overload
    def __call__(self, item: Type[StreamFeaturesProtocol]) -> Type[StreamFeatures]: ...

    @overload
    def __call__(self, item: Type[PrimaryClsProtocol]) -> Type[PrimaryCls]: ...

    @overload
    def __call__(self, item: Type[NoFunFeaturesProtocol]) -> Type[NoFunFeatures]: ...

    @overload
    def __call__(self, item: Type[NicknameProtocol]) -> Type[Nickname]: ...

    @overload
    def __call__(self, item: Type[MaxStalenessFeatures2Protocol]) -> Type[MaxStalenessFeatures2]: ...

    @overload
    def __call__(self, item: Type[LibraryFeaturesProtocol]) -> Type[LibraryFeatures]: ...

    @overload
    def __call__(self, item: Type[FTCls1Protocol]) -> Type[FTCls1]: ...

    @overload
    def __call__(self, item: Type[FTClsProtocol]) -> Type[FTCls]: ...

    @overload
    def __call__(self, item: Type[BogusIdFeature3Protocol]) -> Type[BogusIdFeature3]: ...

    @overload
    def __call__(self, item: Type[FeaturesClassWithoutTimestampProtocol]) -> Type[FeaturesClassWithoutTimestamp]: ...

    @overload
    def __call__(self, item: Type[FeaturesClassWithNamedTsProtocol]) -> Type[FeaturesClassWithNamedTs]: ...

    @overload
    def __call__(self, item: Type[FeaturesClassWithCustomTsNameProtocol]) -> Type[FeaturesClassWithCustomTsName]: ...
