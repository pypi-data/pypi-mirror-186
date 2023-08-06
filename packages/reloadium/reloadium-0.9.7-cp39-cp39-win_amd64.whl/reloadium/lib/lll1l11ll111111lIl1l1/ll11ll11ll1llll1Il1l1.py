from abc import ABC
from contextlib import contextmanager
from pathlib import Path
import sys
import types
from typing import TYPE_CHECKING, Any, ClassVar, Dict, Generator, List, Optional, Tuple, Type

from reloadium.corium.l1lll1l1lll11l1lIl1l1 import lll1111lll1ll111Il1l1, l1lll1l1lll11l1lIl1l1
from reloadium.corium.ll1ll11llll1ll11Il1l1 import ll11ll11l11l1111Il1l1, l11ll111ll11ll1lIl1l1
from reloadium.corium.l11lllll111l11llIl1l1 import ll111lll1lll111lIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field

    from reloadium.lib.lll1l11ll111111lIl1l1.l11l11111l1l1l1lIl1l1 import l1l1l1l111111ll1Il1l1
else:
    from reloadium.vendored.dataclasses import dataclass, field


@dataclass
class ll1l1l1ll11lll1lIl1l1:
    l11l11111l1l1l1lIl1l1: "l1l1l1l111111ll1Il1l1"

    llllllll1l1111llIl1l1: ClassVar[str] = NotImplemented
    llllll11l1l1l111Il1l1: bool = field(init=False, default=False)

    l1l1l1l111l1lll1Il1l1: lll1111lll1ll111Il1l1 = field(init=False)

    def __post_init__(l111l1ll1llll111Il1l1) -> None:
        l111l1ll1llll111Il1l1.l1l1l1l111l1lll1Il1l1 = l1lll1l1lll11l1lIl1l1.l1111l111ll1lll1Il1l1(l111l1ll1llll111Il1l1.llllllll1l1111llIl1l1)
        l111l1ll1llll111Il1l1.l1l1l1l111l1lll1Il1l1.ll1lll111lll1ll1Il1l1('Creating extension')
        l111l1ll1llll111Il1l1.l11l11111l1l1l1lIl1l1.l1l1ll1l11l1lll1Il1l1.lll111ll1llll11lIl1l1.ll11l11l11l1llllIl1l1(l111l1ll1llll111Il1l1.ll11l1l1111l1111Il1l1())

    def ll11l1l1111l1111Il1l1(l111l1ll1llll111Il1l1) -> List[Type[l11ll111ll11ll1lIl1l1]]:
        lll11111l1llllllIl1l1 = []
        ll1ll11llll1ll11Il1l1 = l111l1ll1llll111Il1l1.l111l11l11l111l1Il1l1()
        for l11l1lll11ll111lIl1l1 in ll1ll11llll1ll11Il1l1:
            l11l1lll11ll111lIl1l1.l1l11ll1l1l11lllIl1l1 = l111l1ll1llll111Il1l1.llllllll1l1111llIl1l1

        lll11111l1llllllIl1l1.extend(ll1ll11llll1ll11Il1l1)
        return lll11111l1llllllIl1l1

    def ll11ll1111l111l1Il1l1(l111l1ll1llll111Il1l1) -> None:
        l111l1ll1llll111Il1l1.llllll11l1l1l111Il1l1 = True

    def l1111111111l111lIl1l1(l111l1ll1llll111Il1l1, l111111l11llll1lIl1l1: types.ModuleType) -> None:
        pass

    @contextmanager
    def l11ll1111l1ll111Il1l1(l111l1ll1llll111Il1l1, l11lll1l1l11l111Il1l1: str, l1111llll111llllIl1l1: Dict[str, Any]) -> Generator[Tuple[str, Dict[str, Any]], None, None]:


        yield (l11lll1l1l11l111Il1l1, l1111llll111llllIl1l1, )

    def l1ll11l111l11111Il1l1(l111l1ll1llll111Il1l1) -> None:
        pass

    def l11l1llll1l11lllIl1l1(l111l1ll1llll111Il1l1, lll11ll1l1ll1l11Il1l1: Exception) -> None:
        pass

    def lll1111l1ll111llIl1l1(l111l1ll1llll111Il1l1, llllllll1l1111llIl1l1: str) -> Optional[ll111lll1lll111lIl1l1]:
        return None

    def lll11lllll1l11llIl1l1(l111l1ll1llll111Il1l1, llllllll1l1111llIl1l1: str) -> Optional[ll111lll1lll111lIl1l1]:
        return None

    def lll1lll1l1lll1llIl1l1(l111l1ll1llll111Il1l1, llllllll1l1111llIl1l1: str) -> Optional[ll111lll1lll111lIl1l1]:
        return None

    def l1l1l111l111l111Il1l1(l111l1ll1llll111Il1l1, l11ll11llll111llIl1l1: Path) -> None:
        pass

    def lll1l111l1111l11Il1l1(l111l1ll1llll111Il1l1, l11ll11llll111llIl1l1: Path) -> None:
        pass

    def ll111111l111ll1lIl1l1(l111l1ll1llll111Il1l1, l11ll11llll111llIl1l1: Path, ll1lllll11l1l1l1Il1l1: List[ll11ll11l11l1111Il1l1]) -> None:
        pass

    def __eq__(l111l1ll1llll111Il1l1, l1l11lllllll11l1Il1l1: Any) -> bool:
        return id(l1l11lllllll11l1Il1l1) == id(l111l1ll1llll111Il1l1)

    def l111l11l11l111l1Il1l1(l111l1ll1llll111Il1l1) -> List[Type[l11ll111ll11ll1lIl1l1]]:
        return []

    def llll111l1111l1llIl1l1(l111l1ll1llll111Il1l1, l111111l11llll1lIl1l1: types.ModuleType, llllllll1l1111llIl1l1: str) -> bool:
        lll11111l1llllllIl1l1 = (hasattr(l111111l11llll1lIl1l1, '__name__') and l111111l11llll1lIl1l1.__name__ == llllllll1l1111llIl1l1)
        return lll11111l1llllllIl1l1


@dataclass(repr=False)
class lll11ll11l11ll11Il1l1(ll111lll1lll111lIl1l1):
    ll11ll11ll1llll1Il1l1: ll1l1l1ll11lll1lIl1l1

    def __repr__(l111l1ll1llll111Il1l1) -> str:
        return 'ExtensionMemento'
