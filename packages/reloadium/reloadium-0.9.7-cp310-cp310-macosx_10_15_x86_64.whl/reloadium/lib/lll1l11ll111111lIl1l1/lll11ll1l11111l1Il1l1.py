import types
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Tuple, Type, Union, cast

from reloadium.lib.lll1l11ll111111lIl1l1.ll11ll11ll1llll1Il1l1 import ll1l1l1ll11lll1lIl1l1
from reloadium.lib import l1ll111lll111ll1Il1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field
else:
    from reloadium.vendored.dataclasses import dataclass, field


@dataclass
class ll11111l1lll1ll1Il1l1(ll1l1l1ll11lll1lIl1l1):
    llllllll1l1111llIl1l1 = 'Multiprocessing'

    def __post_init__(l111l1ll1llll111Il1l1) -> None:
        super().__post_init__()

    def l1111111111l111lIl1l1(l111l1ll1llll111Il1l1, l111111l11llll1lIl1l1: types.ModuleType) -> None:
        if (l111l1ll1llll111Il1l1.llll111l1111l1llIl1l1(l111111l11llll1lIl1l1, 'multiprocessing.popen_spawn_posix')):
            l111l1ll1llll111Il1l1.l1lllll1l1lll1l1Il1l1(l111111l11llll1lIl1l1)

        if (l111l1ll1llll111Il1l1.llll111l1111l1llIl1l1(l111111l11llll1lIl1l1, 'multiprocessing.popen_spawn_win32')):
            l111l1ll1llll111Il1l1.lll11l1lll1111llIl1l1(l111111l11llll1lIl1l1)

    def l1lllll1l1lll1l1Il1l1(l111l1ll1llll111Il1l1, l111111l11llll1lIl1l1: types.ModuleType) -> None:
        import multiprocessing.popen_spawn_posix
        multiprocessing.popen_spawn_posix.Popen._launch = l1ll111lll111ll1Il1l1.lll11ll1l11111l1Il1l1.l111ll1ll1l1l1llIl1l1  # type: ignore

    def lll11l1lll1111llIl1l1(l111l1ll1llll111Il1l1, l111111l11llll1lIl1l1: types.ModuleType) -> None:
        import multiprocessing.popen_spawn_win32
        multiprocessing.popen_spawn_win32.Popen.__init__ = l1ll111lll111ll1Il1l1.lll11ll1l11111l1Il1l1.__init__  # type: ignore
