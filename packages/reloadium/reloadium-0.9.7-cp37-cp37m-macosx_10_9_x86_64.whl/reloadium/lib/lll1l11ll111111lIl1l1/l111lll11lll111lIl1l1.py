from contextlib import contextmanager
import os
from pathlib import Path
import sys
import types
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Tuple, Type

from reloadium.lib.environ import env
from reloadium.corium.lllll1lllll111l1Il1l1 import lll1ll11l1l111llIl1l1
from reloadium.lib.lll1l11ll111111lIl1l1.ll11ll11ll1llll1Il1l1 import lll11ll11l11ll11Il1l1
from reloadium.lib.lll1l11ll111111lIl1l1.ll1l1l11lll1l111Il1l1 import llll1l1l1l111l11Il1l1
from reloadium.corium.ll1ll11llll1ll11Il1l1 import ll11ll11l11l1111Il1l1, ll11lll1l11111llIl1l1, l11ll111ll11ll1lIl1l1, l1l1l1lll111l11lIl1l1, lll1l111111l1ll1Il1l1
from reloadium.corium.l11lllll111l11llIl1l1 import ll111lll1lll111lIl1l1
from reloadium.corium.ll1l1l11l111llllIl1l1 import l11l1111ll1111l1Il1l1
from reloadium.corium.l1111l1lll1111llIl1l1 import llll1llllll1ll11Il1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field

    from django.db import transaction
    from django.db.transaction import Atomic
else:
    from reloadium.vendored.dataclasses import dataclass, field


@dataclass(**lll1l111111l1ll1Il1l1)
class ll1111lll111ll1lIl1l1(l1l1l1lll111l11lIl1l1):
    ll11111111lllll1Il1l1 = 'Field'

    @classmethod
    def lll111l1l1111lllIl1l1(ll1l111ll1lll11lIl1l1, l11ll1l1ll11ll11Il1l1: l11l1111ll1111l1Il1l1.l1l1l11111llll11Il1l1, lll11lll11l1l111Il1l1: Any, ll1lll111llllll1Il1l1: ll11lll1l11111llIl1l1) -> bool:
        from django.db.models.fields import Field

        if ((hasattr(lll11lll11l1l111Il1l1, 'field') and isinstance(lll11lll11l1l111Il1l1.field, Field))):
            return True

        return False

    def ll111lllll1ll1llIl1l1(l111l1ll1llll111Il1l1, l1l111l111l1l111Il1l1: l11ll111ll11ll1lIl1l1) -> bool:
        return True

    @classmethod
    def ll11ll1ll11l111lIl1l1(ll1l111ll1lll11lIl1l1) -> int:
        return 200


@dataclass(repr=False)
class l1l1l11ll1l111l1Il1l1(lll11ll11l11ll11Il1l1):
    l1l111lll1lll111Il1l1: "Atomic" = field(init=False)

    l1l11ll1111lll11Il1l1: bool = field(init=False, default=False)

    def __post_init__(l111l1ll1llll111Il1l1) -> None:
        super().__post_init__()
        from django.db import transaction

        l111l1ll1llll111Il1l1.l1l111lll1lll111Il1l1 = transaction.atomic()
        l111l1ll1llll111Il1l1.l1l111lll1lll111Il1l1.__enter__()

    def l111l1llll11l11lIl1l1(l111l1ll1llll111Il1l1) -> None:
        super().l111l1llll11l11lIl1l1()
        if (l111l1ll1llll111Il1l1.l1l11ll1111lll11Il1l1):
            return 

        l111l1ll1llll111Il1l1.l1l11ll1111lll11Il1l1 = True
        from django.db import transaction

        transaction.set_rollback(True)
        l111l1ll1llll111Il1l1.l1l111lll1lll111Il1l1.__exit__(None, None, None)

    def l1l1l111l1ll1l11Il1l1(l111l1ll1llll111Il1l1) -> None:
        super().l1l1l111l1ll1l11Il1l1()

        if (l111l1ll1llll111Il1l1.l1l11ll1111lll11Il1l1):
            return 

        l111l1ll1llll111Il1l1.l1l11ll1111lll11Il1l1 = True
        l111l1ll1llll111Il1l1.l1l111lll1lll111Il1l1.__exit__(None, None, None)

    def __repr__(l111l1ll1llll111Il1l1) -> str:
        return 'DbMemento'


@dataclass
class l1ll1lll1ll1l1l1Il1l1(llll1l1l1l111l11Il1l1):
    llllllll1l1111llIl1l1 = 'Django'

    l1llll1ll1111l1lIl1l1: Optional[int] = field(init=False)
    l1lllll111l1l111Il1l1: Optional[Callable[..., Any]] = field(init=False, default=None)

    def __post_init__(l111l1ll1llll111Il1l1) -> None:
        super().__post_init__()
        l111l1ll1llll111Il1l1.l1llll1ll1111l1lIl1l1 = None

    def l111l11l11l111l1Il1l1(l111l1ll1llll111Il1l1) -> List[Type[l11ll111ll11ll1lIl1l1]]:
        return [ll1111lll111ll1lIl1l1]

    @contextmanager
    def l11ll1111l1ll111Il1l1(l111l1ll1llll111Il1l1, l11lll1l1l11l111Il1l1: str, l1111llll111llllIl1l1: Dict[str, Any]) -> Generator[Tuple[str, Dict[str, Any]], None, None]:


        pass

    def l1ll11l111l11111Il1l1(l111l1ll1llll111Il1l1) -> None:
        super().l1ll11l111l11111Il1l1()
        sys.argv.append('--noreload')

    def l1111111111l111lIl1l1(l111l1ll1llll111Il1l1, l111111l11llll1lIl1l1: types.ModuleType) -> None:
        if (l111l1ll1llll111Il1l1.llll111l1111l1llIl1l1(l111111l11llll1lIl1l1, 'django.core.management.commands.runserver')):
            l111l1ll1llll111Il1l1.l1111lll1lll1lllIl1l1()
            l111l1ll1llll111Il1l1.lll1ll1111l1lll1Il1l1()

    def lll1111l1ll111llIl1l1(l111l1ll1llll111Il1l1, llllllll1l1111llIl1l1: str) -> Optional["ll111lll1lll111lIl1l1"]:
        if ( not os.environ.get('DJANGO_SETTINGS_MODULE')):
            return None

        lll11111l1llllllIl1l1 = l1l1l11ll1l111l1Il1l1(llllllll1l1111llIl1l1=llllllll1l1111llIl1l1, ll11ll11ll1llll1Il1l1=l111l1ll1llll111Il1l1)
        return lll11111l1llllllIl1l1

    def l1111lll1lll1lllIl1l1(l111l1ll1llll111Il1l1) -> None:
        import django.core.management.commands.runserver

        lll1l1ll1ll1l1l1Il1l1 = django.core.management.commands.runserver.Command.handle

        def l1ll1lll1lll1ll1Il1l1(*l1l111l1lllll111Il1l1: Any, **l11llll11l11ll11Il1l1: Any) -> Any:
            with lll1ll11l1l111llIl1l1():
                ll1l1lll1l111l11Il1l1 = l11llll11l11ll11Il1l1.get('addrport')
                if ( not ll1l1lll1l111l11Il1l1):
                    ll1l1lll1l111l11Il1l1 = django.core.management.commands.runserver.Command.default_port

                ll1l1lll1l111l11Il1l1 = ll1l1lll1l111l11Il1l1.split(':')[ - 1]
                ll1l1lll1l111l11Il1l1 = int(ll1l1lll1l111l11Il1l1)
                l111l1ll1llll111Il1l1.l1llll1ll1111l1lIl1l1 = ll1l1lll1l111l11Il1l1

            return lll1l1ll1ll1l1l1Il1l1(*l1l111l1lllll111Il1l1, **l11llll11l11ll11Il1l1)

        llll1llllll1ll11Il1l1.ll1l1ll1ll1l1l1lIl1l1(django.core.management.commands.runserver.Command, 'handle', l1ll1lll1lll1ll1Il1l1)

    def lll1ll1111l1lll1Il1l1(l111l1ll1llll111Il1l1) -> None:
        import django.core.management.commands.runserver

        lll1l1ll1ll1l1l1Il1l1 = django.core.management.commands.runserver.Command.get_handler

        def l1ll1lll1lll1ll1Il1l1(*l1l111l1lllll111Il1l1: Any, **l11llll11l11ll11Il1l1: Any) -> Any:
            with lll1ll11l1l111llIl1l1():
                assert l111l1ll1llll111Il1l1.l1llll1ll1111l1lIl1l1
                l111l1ll1llll111Il1l1.l1lll1ll1ll1l1l1Il1l1 = l111l1ll1llll111Il1l1.ll11111l11ll11llIl1l1(l111l1ll1llll111Il1l1.l1llll1ll1111l1lIl1l1)
                if (env.page_reload_on_start):
                    l111l1ll1llll111Il1l1.l1lll1ll1ll1l1l1Il1l1.llll11l11ll11l11Il1l1(2.0)

            return lll1l1ll1ll1l1l1Il1l1(*l1l111l1lllll111Il1l1, **l11llll11l11ll11Il1l1)

        llll1llllll1ll11Il1l1.ll1l1ll1ll1l1l1lIl1l1(django.core.management.commands.runserver.Command, 'get_handler', l1ll1lll1lll1ll1Il1l1)

    def l1l11l1l11ll1l11Il1l1(l111l1ll1llll111Il1l1) -> None:
        super().l1l11l1l11ll1l11Il1l1()

        import django.core.handlers.base

        lll1l1ll1ll1l1l1Il1l1 = django.core.handlers.base.BaseHandler.get_response

        def l1ll1lll1lll1ll1Il1l1(l11l1111lllll1llIl1l1: Any, l1l1l1ll11l1l111Il1l1: Any) -> Any:
            l1ll1llll111ll1lIl1l1 = lll1l1ll1ll1l1l1Il1l1(l11l1111lllll1llIl1l1, l1l1l1ll11l1l111Il1l1)

            if ( not l111l1ll1llll111Il1l1.l1lll1ll1ll1l1l1Il1l1):
                return l1ll1llll111ll1lIl1l1

            l11l1ll1lll11ll1Il1l1 = l1ll1llll111ll1lIl1l1.get('content-type')

            if (( not l11l1ll1lll11ll1Il1l1 or 'text/html' not in l11l1ll1lll11ll1Il1l1)):
                return l1ll1llll111ll1lIl1l1

            l1l11l1ll1l111llIl1l1 = l1ll1llll111ll1lIl1l1.content

            if (isinstance(l1l11l1ll1l111llIl1l1, bytes)):
                l1l11l1ll1l111llIl1l1 = l1l11l1ll1l111llIl1l1.decode('utf-8')

            llll111l11l111l1Il1l1 = l111l1ll1llll111Il1l1.l1lll1ll1ll1l1l1Il1l1.l11111ll11ll1l11Il1l1(l1l11l1ll1l111llIl1l1)

            l1ll1llll111ll1lIl1l1.content = llll111l11l111l1Il1l1.encode('utf-8')
            l1ll1llll111ll1lIl1l1['content-length'] = str(len(l1ll1llll111ll1lIl1l1.content)).encode('ascii')
            return l1ll1llll111ll1lIl1l1

        django.core.handlers.base.BaseHandler.get_response = l1ll1lll1lll1ll1Il1l1  # type: ignore

    def lll1l111l1111l11Il1l1(l111l1ll1llll111Il1l1, l11ll11llll111llIl1l1: Path) -> None:
        super().lll1l111l1111l11Il1l1(l11ll11llll111llIl1l1)

        from django.apps.registry import Apps

        l111l1ll1llll111Il1l1.l1lllll111l1l111Il1l1 = Apps.register_model

        def l1ll1llllll1ll11Il1l1(*l1l111l1lllll111Il1l1: Any, **l1l1ll11lll1lll1Il1l1: Any) -> Any:
            pass

        Apps.register_model = l1ll1llllll1ll11Il1l1

    def ll111111l111ll1lIl1l1(l111l1ll1llll111Il1l1, l11ll11llll111llIl1l1: Path, ll1lllll11l1l1l1Il1l1: List[ll11ll11l11l1111Il1l1]) -> None:
        super().ll111111l111ll1lIl1l1(l11ll11llll111llIl1l1, ll1lllll11l1l1l1Il1l1)

        if ( not l111l1ll1llll111Il1l1.l1lllll111l1l111Il1l1):
            return 

        from django.apps.registry import Apps

        Apps.register_model = l111l1ll1llll111Il1l1.l1lllll111l1l111Il1l1
