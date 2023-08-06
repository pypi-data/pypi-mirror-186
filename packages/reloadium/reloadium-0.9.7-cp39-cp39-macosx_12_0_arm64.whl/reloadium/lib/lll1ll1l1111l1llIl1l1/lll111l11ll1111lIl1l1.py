from pathlib import Path
import sys
import threading
from types import CodeType, FrameType, ModuleType
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Set, cast

from reloadium.corium import lll11l11l1ll1lllIl1l1, lllll1lllll111l1Il1l1, public, l11ll11ll1lll1llIl1l1, l1111l1lll1111llIl1l1
from reloadium.corium.ll1lll1l1lll111lIl1l1 import l1lll11ll1ll1111Il1l1, l1ll111111lll1l1Il1l1
from reloadium.corium.lllll1lllll111l1Il1l1 import llll1l1111111l1lIl1l1, lll1ll11l1l111llIl1l1
from reloadium.corium.ll11l1ll1lllll11Il1l1 import llll11111111111lIl1l1
from reloadium.corium.l1lll1l1lll11l1lIl1l1 import l1lll1l1lll11l1lIl1l1
from reloadium.corium.l1l11l111ll1l1l1Il1l1 import l1l1l1l1l1l11l1lIl1l1
from reloadium.corium.l11lllll111l11llIl1l1 import ll111lll1lll111lIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field
else:
    from reloadium.vendored.dataclasses import dataclass, field


__all__ = ['l111111lll111ll1Il1l1', 'l1111llll11111l1Il1l1', 'l1l1ll1l11l11ll1Il1l1']


lll11l1ll1l1l11lIl1l1 = l1lll1l1lll11l1lIl1l1.l1111l111ll1lll1Il1l1(__name__)


class l111111lll111ll1Il1l1:
    @classmethod
    def ll111111l1lll111Il1l1(ll1l111ll1lll11lIl1l1, ll11l11111l1ll11Il1l1: List[ll111lll1lll111lIl1l1]) -> None:
        for l1lll1lllll1lll1Il1l1 in ll11l11111l1ll11Il1l1:
            l1lll1lllll1lll1Il1l1.l111l1llll11l11lIl1l1()

    @classmethod
    def ll1l1lll1l1ll1llIl1l1(l111l1ll1llll111Il1l1) -> Optional[FrameType]:
        ll1llll1l1l111llIl1l1: FrameType = sys._getframe(2)
        lll11111l1llllllIl1l1 = next(l1111l1lll1111llIl1l1.ll1llll1l1l111llIl1l1.lll11l11l11l1ll1Il1l1(ll1llll1l1l111llIl1l1))
        return lll11111l1llllllIl1l1


class l1111llll11111l1Il1l1(l111111lll111ll1Il1l1):
    @classmethod
    def lll1ll1ll1ll11l1Il1l1(ll1l111ll1lll11lIl1l1, l1l111l1lllll111Il1l1: List[Any], l1l1ll11lll1lll1Il1l1: Dict[str, Any], ll11l11111l1ll11Il1l1: Optional[List[ll111lll1lll111lIl1l1]]) -> Any:  # type: ignore
        with lll1ll11l1l111llIl1l1():
            assert llll11111111111lIl1l1.l1l1ll1l11l1lll1Il1l1.lll1ll1l1111l1llIl1l1
            ll1llll1l1l111llIl1l1 = llll11111111111lIl1l1.l1l1ll1l11l1lll1Il1l1.lll1ll1l1111l1llIl1l1.l1ll11l1111l11llIl1l1.ll11l111111l1l11Il1l1()
            ll1llll1l1l111llIl1l1.ll1ll11l1111ll1lIl1l1()

            lll11l11l1l11111Il1l1 = llll11111111111lIl1l1.l1l1ll1l11l1lll1Il1l1.ll1ll11l111l1lllIl1l1.ll11111ll11ll1l1Il1l1(ll1llll1l1l111llIl1l1.l1l1ll1ll1l11111Il1l1, ll1llll1l1l111llIl1l1.lll11l11l11l1111Il1l1.l111lll1l11l1l11Il1l1())
            assert lll11l11l1l11111Il1l1
            ll111l11ll1l111lIl1l1 = ll1l111ll1lll11lIl1l1.ll1l1lll1l1ll1llIl1l1()

            if (ll11l11111l1ll11Il1l1):
                ll1l111ll1lll11lIl1l1.ll111111l1lll111Il1l1(ll11l11111l1ll11Il1l1)


        lll11111l1llllllIl1l1 = lll11l11l1l11111Il1l1(*l1l111l1lllll111Il1l1, **l1l1ll11lll1lll1Il1l1);        ll1llll1l1l111llIl1l1.ll1l11lll1111l1lIl1l1.additional_info.pydev_step_stop = ll111l11ll1l111lIl1l1  # type: ignore

        return lll11111l1llllllIl1l1

    @classmethod
    async def l111ll1111111ll1Il1l1(ll1l111ll1lll11lIl1l1, l1l111l1lllll111Il1l1: List[Any], l1l1ll11lll1lll1Il1l1: Dict[str, Any], ll11l11111l1ll11Il1l1: Optional[List[ll111lll1lll111lIl1l1]]) -> Any:  # type: ignore
        with lll1ll11l1l111llIl1l1():
            assert llll11111111111lIl1l1.l1l1ll1l11l1lll1Il1l1.lll1ll1l1111l1llIl1l1
            ll1llll1l1l111llIl1l1 = llll11111111111lIl1l1.l1l1ll1l11l1lll1Il1l1.lll1ll1l1111l1llIl1l1.l1ll11l1111l11llIl1l1.ll11l111111l1l11Il1l1()
            ll1llll1l1l111llIl1l1.ll1ll11l1111ll1lIl1l1()

            lll11l11l1l11111Il1l1 = llll11111111111lIl1l1.l1l1ll1l11l1lll1Il1l1.ll1ll11l111l1lllIl1l1.ll11111ll11ll1l1Il1l1(ll1llll1l1l111llIl1l1.l1l1ll1ll1l11111Il1l1, ll1llll1l1l111llIl1l1.lll11l11l11l1111Il1l1.l111lll1l11l1l11Il1l1())
            assert lll11l11l1l11111Il1l1
            ll111l11ll1l111lIl1l1 = ll1l111ll1lll11lIl1l1.ll1l1lll1l1ll1llIl1l1()

            if (ll11l11111l1ll11Il1l1):
                ll1l111ll1lll11lIl1l1.ll111111l1lll111Il1l1(ll11l11111l1ll11Il1l1)


        lll11111l1llllllIl1l1 = await lll11l11l1l11111Il1l1(*l1l111l1lllll111Il1l1, **l1l1ll11lll1lll1Il1l1);        ll1llll1l1l111llIl1l1.ll1l11lll1111l1lIl1l1.additional_info.pydev_step_stop = ll111l11ll1l111lIl1l1  # type: ignore

        return lll11111l1llllllIl1l1


class l1l1ll1l11l11ll1Il1l1(l111111lll111ll1Il1l1):
    @classmethod
    def lll1ll1ll1ll11l1Il1l1(ll1l111ll1lll11lIl1l1) -> Optional[ModuleType]:  # type: ignore
        with lll1ll11l1l111llIl1l1():
            assert llll11111111111lIl1l1.l1l1ll1l11l1lll1Il1l1.lll1ll1l1111l1llIl1l1
            ll1llll1l1l111llIl1l1 = llll11111111111lIl1l1.l1l1ll1l11l1lll1Il1l1.lll1ll1l1111l1llIl1l1.l1ll11l1111l11llIl1l1.ll11l111111l1l11Il1l1()

            ll111ll11ll1lll1Il1l1 = Path(ll1llll1l1l111llIl1l1.lll11lll11l1l111Il1l1.f_globals['__spec__'].origin).absolute()
            ll1ll1ll11ll1lllIl1l1 = ll1llll1l1l111llIl1l1.lll11lll11l1l111Il1l1.f_globals['__name__']
            ll1llll1l1l111llIl1l1.ll1ll11l1111ll1lIl1l1()
            l111ll1ll1ll1111Il1l1 = llll11111111111lIl1l1.l1l1ll1l11l1lll1Il1l1.l1lll1111111ll1lIl1l1.l1111l1llllll111Il1l1(ll111ll11ll1lll1Il1l1)

            if ( not l111ll1ll1ll1111Il1l1):
                lll11l1ll1l1l11lIl1l1.llllll1l1ll11111Il1l1('Could not retrieve src.', l1ll11l1l1l11l1lIl1l1={'file': l1l1l1l1l1l11l1lIl1l1.l11ll11llll111llIl1l1(ll111ll11ll1lll1Il1l1), 
'fullname': l1l1l1l1l1l11l1lIl1l1.ll1ll1ll11ll1lllIl1l1(ll1ll1ll11ll1lllIl1l1)})

            assert l111ll1ll1ll1111Il1l1

        try:
            l111ll1ll1ll1111Il1l1.l11ll1ll111l111lIl1l1()
            l111ll1ll1ll1111Il1l1.ll11l1l1l11ll1l1Il1l1(l1lll1llll11l11lIl1l1=False)
            l111ll1ll1ll1111Il1l1.l111l1ll11111l1lIl1l1(l1lll1llll11l11lIl1l1=False)
        except llll1l1111111l1lIl1l1 as l111l1111llllll1Il1l1:
            ll1llll1l1l111llIl1l1.l1111ll11111l11lIl1l1(l111l1111llllll1Il1l1)
            return None

        import importlib.util

        l1l1ll1lll1l1ll1Il1l1 = ll1llll1l1l111llIl1l1.lll11lll11l1l111Il1l1.f_locals['__spec__']
        l111111l11llll1lIl1l1 = importlib.util.module_from_spec(l1l1ll1lll1l1ll1Il1l1)

        l111ll1ll1ll1111Il1l1.l1l11lll1ll11111Il1l1(l111111l11llll1lIl1l1)
        return l111111l11llll1lIl1l1


l1ll111111lll1l1Il1l1.l11l11lll11ll11lIl1l1(l1lll11ll1ll1111Il1l1.l1111111l1llll1lIl1l1, l1111llll11111l1Il1l1.lll1ll1ll1ll11l1Il1l1)
l1ll111111lll1l1Il1l1.l11l11lll11ll11lIl1l1(l1lll11ll1ll1111Il1l1.lll1l1111ll11l11Il1l1, l1111llll11111l1Il1l1.l111ll1111111ll1Il1l1)
l1ll111111lll1l1Il1l1.l11l11lll11ll11lIl1l1(l1lll11ll1ll1111Il1l1.ll111111lllll111Il1l1, l1l1ll1l11l11ll1Il1l1.lll1ll1ll1ll11l1Il1l1)
