import re
from contextlib import contextmanager
import os
import sys
import types
from pathlib import Path
from textwrap import dedent
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Set, Tuple, Union

from reloadium.corium.lllll1lllll111l1Il1l1 import lll1ll11l1l111llIl1l1
from reloadium.lib.lll1l11ll111111lIl1l1.ll11ll11ll1llll1Il1l1 import ll1l1l1ll11lll1lIl1l1, lll11ll11l11ll11Il1l1
from reloadium.corium.l11lllll111l11llIl1l1 import ll111lll1lll111lIl1l1
from reloadium.corium.l1111l1lll1111llIl1l1 import llll1llllll1ll11Il1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field

    from sqlalchemy.engine.base import Engine, Transaction
    from sqlalchemy.orm.session import Session
else:
    from reloadium.vendored.dataclasses import dataclass, field


@dataclass(repr=False)
class l1l1l11ll1l111l1Il1l1(lll11ll11l11ll11Il1l1):
    ll11ll11ll1llll1Il1l1: "ll1l1111l1l1111lIl1l1"
    l1llll111l111111Il1l1: List["Transaction"] = field(init=False, default_factory=list)

    def __post_init__(l111l1ll1llll111Il1l1) -> None:
        from sqlalchemy.orm.session import _sessions

        super().__post_init__()

        lll1l1l1lll1ll11Il1l1 = list(_sessions.values())

        for l11l11llllll1l1lIl1l1 in lll1l1l1lll1ll11Il1l1:
            if ( not l11l11llllll1l1lIl1l1.is_active):
                continue

            l1l1111l11lll1l1Il1l1 = l11l11llllll1l1lIl1l1.begin_nested()
            l111l1ll1llll111Il1l1.l1llll111l111111Il1l1.append(l1l1111l11lll1l1Il1l1)

    def __repr__(l111l1ll1llll111Il1l1) -> str:
        return 'DbMemento'

    def l111l1llll11l11lIl1l1(l111l1ll1llll111Il1l1) -> None:
        super().l111l1llll11l11lIl1l1()

        while l111l1ll1llll111Il1l1.l1llll111l111111Il1l1:
            l1l1111l11lll1l1Il1l1 = l111l1ll1llll111Il1l1.l1llll111l111111Il1l1.pop()
            if (l1l1111l11lll1l1Il1l1.is_active):
                try:
                    l1l1111l11lll1l1Il1l1.rollback()
                except :
                    pass

    def l1l1l111l1ll1l11Il1l1(l111l1ll1llll111Il1l1) -> None:
        super().l1l1l111l1ll1l11Il1l1()

        while l111l1ll1llll111Il1l1.l1llll111l111111Il1l1:
            l1l1111l11lll1l1Il1l1 = l111l1ll1llll111Il1l1.l1llll111l111111Il1l1.pop()
            if (l1l1111l11lll1l1Il1l1.is_active):
                try:
                    l1l1111l11lll1l1Il1l1.commit()
                except :
                    pass


@dataclass
class ll1l1111l1l1111lIl1l1(ll1l1l1ll11lll1lIl1l1):
    llllllll1l1111llIl1l1 = 'Sqlalchemy'

    l1l111ll1l1lllllIl1l1: List["Engine"] = field(init=False, default_factory=list)
    lll1l1l1lll1ll11Il1l1: Set["Session"] = field(init=False, default_factory=set)
    l11lll1l1l1l1l11Il1l1: Tuple[int, ...] = field(init=False)

    @contextmanager
    def l11ll1111l1ll111Il1l1(l111l1ll1llll111Il1l1, l11lll1l1l11l111Il1l1: str, l1111llll111llllIl1l1: Dict[str, Any]) -> Generator[Tuple[str, Dict[str, Any]], None, None]:


        pass

    def l1111111111l111lIl1l1(l111l1ll1llll111Il1l1, l111111l11llll1lIl1l1: types.ModuleType) -> None:
        if (l111l1ll1llll111Il1l1.llll111l1111l1llIl1l1(l111111l11llll1lIl1l1, 'sqlalchemy')):
            l111l1ll1llll111Il1l1.llll111l1l111l11Il1l1(l111111l11llll1lIl1l1)

        if (l111l1ll1llll111Il1l1.llll111l1111l1llIl1l1(l111111l11llll1lIl1l1, 'sqlalchemy.engine.base')):
            l111l1ll1llll111Il1l1.l11l1l1ll1lll1llIl1l1(l111111l11llll1lIl1l1)

    def llll111l1l111l11Il1l1(l111l1ll1llll111Il1l1, l111111l11llll1lIl1l1: Any) -> None:
        l1l11l1ll1l111llIl1l1 = Path(l111111l11llll1lIl1l1.__file__).read_text(encoding='utf-8')
        __version__ = re.findall('__version__\\s*?=\\s*?"(.*?)"', l1l11l1ll1l111llIl1l1)[0]

        ll1l1ll1l1ll1l11Il1l1 = [int(l1lll1l11llll111Il1l1) for l1lll1l11llll111Il1l1 in __version__.split('.')]
        l111l1ll1llll111Il1l1.l11lll1l1l1l1l11Il1l1 = tuple(ll1l1ll1l1ll1l11Il1l1)

    def lll1111l1ll111llIl1l1(l111l1ll1llll111Il1l1, llllllll1l1111llIl1l1: str) -> Optional["ll111lll1lll111lIl1l1"]:
        lll11111l1llllllIl1l1 = l1l1l11ll1l111l1Il1l1(llllllll1l1111llIl1l1=llllllll1l1111llIl1l1, ll11ll11ll1llll1Il1l1=l111l1ll1llll111Il1l1)
        return lll11111l1llllllIl1l1

    def l11l1l1ll1lll1llIl1l1(l111l1ll1llll111Il1l1, l111111l11llll1lIl1l1: Any) -> None:
        ll111llllll1l11lIl1l1 = locals().copy()

        ll111llllll1l11lIl1l1.update({'original': l111111l11llll1lIl1l1.Engine.__init__, 'reloader_code': lll1ll11l1l111llIl1l1, 'engines': l111l1ll1llll111Il1l1.l1l111ll1l1lllllIl1l1})





        ll1l11l11l1l1ll1Il1l1 = dedent('\n            def patched(\n                    self2: Any,\n                    pool: Any,\n                    dialect: Any,\n                    url: Any,\n                    logging_name: Any = None,\n                    echo: Any = None,\n                    proxy: Any = None,\n                    execution_options: Any = None,\n                    hide_parameters: Any = None,\n            ) -> Any:\n                original(self2,\n                         pool,\n                         dialect,\n                         url,\n                         logging_name,\n                         echo,\n                         proxy,\n                         execution_options,\n                         hide_parameters\n                         )\n                with reloader_code():\n                    engines.append(self2)')
























        l1lll1lll11l11l1Il1l1 = dedent('\n            def patched(\n                    self2: Any,\n                    pool: Any,\n                    dialect: Any,\n                    url: Any,\n                    logging_name: Any = None,\n                    echo: Any = None,\n                    query_cache_size: Any = 500,\n                    execution_options: Any = None,\n                    hide_parameters: Any = False,\n            ) -> Any:\n                original(self2,\n                         pool,\n                         dialect,\n                         url,\n                         logging_name,\n                         echo,\n                         query_cache_size,\n                         execution_options,\n                         hide_parameters)\n                with reloader_code():\n                    engines.append(self2)\n        ')
























        if (l111l1ll1llll111Il1l1.l11lll1l1l1l1l11Il1l1 <= (1, 3, 24, )):
            exec(ll1l11l11l1l1ll1Il1l1, {**globals(), **ll111llllll1l11lIl1l1}, ll111llllll1l11lIl1l1)
        else:
            exec(l1lll1lll11l11l1Il1l1, {**globals(), **ll111llllll1l11lIl1l1}, ll111llllll1l11lIl1l1)

        llll1llllll1ll11Il1l1.ll1l1ll1ll1l1l1lIl1l1(l111111l11llll1lIl1l1.Engine, '__init__', ll111llllll1l11lIl1l1['patched'])
