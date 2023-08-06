from pathlib import Path
import types
from typing import TYPE_CHECKING, Any, List

from reloadium.lib.lll1l11ll111111lIl1l1.ll11ll11ll1llll1Il1l1 import ll1l1l1ll11lll1lIl1l1
from reloadium.corium.ll1ll11llll1ll11Il1l1 import ll11ll11l11l1111Il1l1
from reloadium.corium.l1111l1lll1111llIl1l1 import llll1llllll1ll11Il1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field
else:
    from reloadium.vendored.dataclasses import dataclass, field


@dataclass
class llll1l1lllllll1lIl1l1(ll1l1l1ll11lll1lIl1l1):
    llllllll1l1111llIl1l1 = 'PyGame'

    l1111l111lllll11Il1l1: bool = field(init=False, default=False)

    def l1111111111l111lIl1l1(l111l1ll1llll111Il1l1, l1ll1111l11ll1l1Il1l1: types.ModuleType) -> None:
        if (l111l1ll1llll111Il1l1.llll111l1111l1llIl1l1(l1ll1111l11ll1l1Il1l1, 'pygame.base')):
            l111l1ll1llll111Il1l1.l11l11ll11111111Il1l1()

    def l11l11ll11111111Il1l1(l111l1ll1llll111Il1l1) -> None:
        import pygame.display

        l11ll111lll1llllIl1l1 = pygame.display.update

        def l11l1ll1l1ll1lllIl1l1(*l1l111l1lllll111Il1l1: Any, **l1l1ll11lll1lll1Il1l1: Any) -> None:
            if (l111l1ll1llll111Il1l1.l1111l111lllll11Il1l1):
                llll1llllll1ll11Il1l1.l111ll1l1ll1l111Il1l1(0.1)
                return None
            else:
                return l11ll111lll1llllIl1l1(*l1l111l1lllll111Il1l1, **l1l1ll11lll1lll1Il1l1)

        pygame.display.update = l11l1ll1l1ll1lllIl1l1

    def lll1l111l1111l11Il1l1(l111l1ll1llll111Il1l1, l11ll11llll111llIl1l1: Path) -> None:
        l111l1ll1llll111Il1l1.l1111l111lllll11Il1l1 = True

    def ll111111l111ll1lIl1l1(l111l1ll1llll111Il1l1, l11ll11llll111llIl1l1: Path, ll1lllll11l1l1l1Il1l1: List[ll11ll11l11l1111Il1l1]) -> None:
        l111l1ll1llll111Il1l1.l1111l111lllll11Il1l1 = False

    def l11l1llll1l11lllIl1l1(l111l1ll1llll111Il1l1, lll11ll1l1ll1l11Il1l1: Exception) -> None:
        l111l1ll1llll111Il1l1.l1111l111lllll11Il1l1 = False
