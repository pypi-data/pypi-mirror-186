from contextlib import contextmanager
from pathlib import Path
import types
from typing import TYPE_CHECKING, Any, Dict, Generator, List, Tuple, Type

from reloadium.lib.environ import env
from reloadium.corium.lllll1lllll111l1Il1l1 import lll1ll11l1l111llIl1l1
from reloadium.lib.lll1l11ll111111lIl1l1.ll1l1l11lll1l111Il1l1 import llll1l1l1l111l11Il1l1
from reloadium.corium.ll1ll11llll1ll11Il1l1 import ll11lll1l11111llIl1l1, l11ll111ll11ll1lIl1l1, l1l1l1lll111l11lIl1l1, lll1l111111l1ll1Il1l1
from reloadium.corium.ll1l1l11l111llllIl1l1 import l11l1111ll1111l1Il1l1
from reloadium.corium.l1111l1lll1111llIl1l1 import llll1llllll1ll11Il1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass
else:
    from reloadium.vendored.dataclasses import dataclass


@dataclass(**lll1l111111l1ll1Il1l1)
class l11l11ll1l1l11l1Il1l1(l1l1l1lll111l11lIl1l1):
    ll11111111lllll1Il1l1 = 'FlaskApp'

    @classmethod
    def lll111l1l1111lllIl1l1(ll1l111ll1lll11lIl1l1, l11ll1l1ll11ll11Il1l1: l11l1111ll1111l1Il1l1.l1l1l11111llll11Il1l1, lll11lll11l1l111Il1l1: Any, ll1lll111llllll1Il1l1: ll11lll1l11111llIl1l1) -> bool:
        import flask

        if (isinstance(lll11lll11l1l111Il1l1, flask.Flask)):
            return True

        return False

    def ll1ll1ll111l111lIl1l1(l111l1ll1llll111Il1l1) -> bool:
        return True

    @classmethod
    def ll11ll1ll11l111lIl1l1(ll1l111ll1lll11lIl1l1) -> int:
        return (super().ll11ll1ll11l111lIl1l1() + 10)


@dataclass(**lll1l111111l1ll1Il1l1)
class l11111l1llll1lllIl1l1(l1l1l1lll111l11lIl1l1):
    ll11111111lllll1Il1l1 = 'Request'

    @classmethod
    def lll111l1l1111lllIl1l1(ll1l111ll1lll11lIl1l1, l11ll1l1ll11ll11Il1l1: l11l1111ll1111l1Il1l1.l1l1l11111llll11Il1l1, lll11lll11l1l111Il1l1: Any, ll1lll111llllll1Il1l1: ll11lll1l11111llIl1l1) -> bool:
        if (repr(lll11lll11l1l111Il1l1) == '<LocalProxy unbound>'):
            return True

        return False

    def ll1ll1ll111l111lIl1l1(l111l1ll1llll111Il1l1) -> bool:
        return True

    @classmethod
    def ll11ll1ll11l111lIl1l1(ll1l111ll1lll11lIl1l1) -> int:

        return int(10000000000.0)


@dataclass
class l11111llll1l11llIl1l1(llll1l1l1l111l11Il1l1):
    llllllll1l1111llIl1l1 = 'Flask'

    @contextmanager
    def l11ll1111l1ll111Il1l1(l111l1ll1llll111Il1l1, l11lll1l1l11l111Il1l1: str, l1111llll111llllIl1l1: Dict[str, Any]) -> Generator[Tuple[str, Dict[str, Any]], None, None]:






        from flask import Flask as FlaskLib 

        def l11lll1l11ll111lIl1l1(*l1l111l1lllll111Il1l1: Any, **l1l1ll11lll1lll1Il1l1: Any) -> Any:
            def ll1l1ll11l11ll1lIl1l1(l11111ll1111111lIl1l1: Any) -> Any:
                return l11111ll1111111lIl1l1

            return ll1l1ll11l11ll1lIl1l1

        lllll11ll11ll1l1Il1l1 = FlaskLib.route
        FlaskLib.route = l11lll1l11ll111lIl1l1  # type: ignore

        try:
            yield (l11lll1l1l11l111Il1l1, l1111llll111llllIl1l1, )
        finally:
            FlaskLib.route = lllll11ll11ll1l1Il1l1  # type: ignore

    def l111l11l11l111l1Il1l1(l111l1ll1llll111Il1l1) -> List[Type[l11ll111ll11ll1lIl1l1]]:
        return [l11l11ll1l1l11l1Il1l1, l11111l1llll1lllIl1l1]

    def l1111111111l111lIl1l1(l111l1ll1llll111Il1l1, l1ll1111l11ll1l1Il1l1: types.ModuleType) -> None:
        if (l111l1ll1llll111Il1l1.llll111l1111l1llIl1l1(l1ll1111l11ll1l1Il1l1, 'flask.app')):
            l111l1ll1llll111Il1l1.ll1l111l1ll1lll1Il1l1()
            l111l1ll1llll111Il1l1.l11lllll1ll11ll1Il1l1()
            l111l1ll1llll111Il1l1.lll11ll1l1l1llllIl1l1()

        if (l111l1ll1llll111Il1l1.llll111l1111l1llIl1l1(l1ll1111l11ll1l1Il1l1, 'flask.cli')):
            l111l1ll1llll111Il1l1.l11111l1111ll111Il1l1()

    def ll1l111l1ll1lll1Il1l1(l111l1ll1llll111Il1l1) -> None:
        try:
            import werkzeug.serving
            import flask.cli
        except ImportError:
            return 

        lll1l1ll1ll1l1l1Il1l1 = werkzeug.serving.run_simple

        def l1ll1lll1lll1ll1Il1l1(*l1l111l1lllll111Il1l1: Any, **l1l1ll11lll1lll1Il1l1: Any) -> Any:
            with lll1ll11l1l111llIl1l1():
                ll1l1lll1l111l11Il1l1 = l1l1ll11lll1lll1Il1l1.get('port')
                if ( not ll1l1lll1l111l11Il1l1):
                    ll1l1lll1l111l11Il1l1 = l1l111l1lllll111Il1l1[1]

                l111l1ll1llll111Il1l1.l1lll1ll1ll1l1l1Il1l1 = l111l1ll1llll111Il1l1.ll11111l11ll11llIl1l1(ll1l1lll1l111l11Il1l1)
                if (env.page_reload_on_start):
                    l111l1ll1llll111Il1l1.l1lll1ll1ll1l1l1Il1l1.llll11l11ll11l11Il1l1(1.0)
            lll1l1ll1ll1l1l1Il1l1(*l1l111l1lllll111Il1l1, **l1l1ll11lll1lll1Il1l1)

        llll1llllll1ll11Il1l1.ll1l1ll1ll1l1l1lIl1l1(werkzeug.serving, 'run_simple', l1ll1lll1lll1ll1Il1l1)
        llll1llllll1ll11Il1l1.ll1l1ll1ll1l1l1lIl1l1(flask.cli, 'run_simple', l1ll1lll1lll1ll1Il1l1)

    def lll11ll1l1l1llllIl1l1(l111l1ll1llll111Il1l1) -> None:
        try:
            import flask
        except ImportError:
            return 

        lll1l1ll1ll1l1l1Il1l1 = flask.app.Flask.__init__

        def l1ll1lll1lll1ll1Il1l1(ll11ll1lll1ll11lIl1l1: Any, *l1l111l1lllll111Il1l1: Any, **l1l1ll11lll1lll1Il1l1: Any) -> Any:
            lll1l1ll1ll1l1l1Il1l1(ll11ll1lll1ll11lIl1l1, *l1l111l1lllll111Il1l1, **l1l1ll11lll1lll1Il1l1)
            with lll1ll11l1l111llIl1l1():
                ll11ll1lll1ll11lIl1l1.config['TEMPLATES_AUTO_RELOAD'] = True

        llll1llllll1ll11Il1l1.ll1l1ll1ll1l1l1lIl1l1(flask.app.Flask, '__init__', l1ll1lll1lll1ll1Il1l1)

    def l11lllll1ll11ll1Il1l1(l111l1ll1llll111Il1l1) -> None:
        try:
            import waitress  # type: ignore
        except ImportError:
            return 

        lll1l1ll1ll1l1l1Il1l1 = waitress.serve


        def l1ll1lll1lll1ll1Il1l1(*l1l111l1lllll111Il1l1: Any, **l1l1ll11lll1lll1Il1l1: Any) -> Any:
            with lll1ll11l1l111llIl1l1():
                ll1l1lll1l111l11Il1l1 = l1l1ll11lll1lll1Il1l1.get('port')
                if ( not ll1l1lll1l111l11Il1l1):
                    ll1l1lll1l111l11Il1l1 = int(l1l111l1lllll111Il1l1[1])

                ll1l1lll1l111l11Il1l1 = int(ll1l1lll1l111l11Il1l1)

                l111l1ll1llll111Il1l1.l1lll1ll1ll1l1l1Il1l1 = l111l1ll1llll111Il1l1.ll11111l11ll11llIl1l1(ll1l1lll1l111l11Il1l1)
                if (env.page_reload_on_start):
                    l111l1ll1llll111Il1l1.l1lll1ll1ll1l1l1Il1l1.llll11l11ll11l11Il1l1(1.0)

            lll1l1ll1ll1l1l1Il1l1(*l1l111l1lllll111Il1l1, **l1l1ll11lll1lll1Il1l1)

        llll1llllll1ll11Il1l1.ll1l1ll1ll1l1l1lIl1l1(waitress, 'serve', l1ll1lll1lll1ll1Il1l1)

    def l11111l1111ll111Il1l1(l111l1ll1llll111Il1l1) -> None:
        try:
            from flask import cli
        except ImportError:
            return 

        l1l1l111ll1lll11Il1l1 = Path(cli.__file__).read_text(encoding='utf-8')
        l1l1l111ll1lll11Il1l1 = l1l1l111ll1lll11Il1l1.replace('.tb_next', '.tb_next.tb_next')

        exec(l1l1l111ll1lll11Il1l1, cli.__dict__)

    def l1l11l1l11ll1l11Il1l1(l111l1ll1llll111Il1l1) -> None:
        super().l1l11l1l11ll1l11Il1l1()
        import flask.app

        lll1l1ll1ll1l1l1Il1l1 = flask.app.Flask.dispatch_request

        def l1ll1lll1lll1ll1Il1l1(*l1l111l1lllll111Il1l1: Any, **l1l1ll11lll1lll1Il1l1: Any) -> Any:
            l1ll1llll111ll1lIl1l1 = lll1l1ll1ll1l1l1Il1l1(*l1l111l1lllll111Il1l1, **l1l1ll11lll1lll1Il1l1)

            if ( not l111l1ll1llll111Il1l1.l1lll1ll1ll1l1l1Il1l1):
                return l1ll1llll111ll1lIl1l1

            if (isinstance(l1ll1llll111ll1lIl1l1, str)):
                lll11111l1llllllIl1l1 = l111l1ll1llll111Il1l1.l1lll1ll1ll1l1l1Il1l1.l11111ll11ll1l11Il1l1(l1ll1llll111ll1lIl1l1)
                return lll11111l1llllllIl1l1
            elif ((isinstance(l1ll1llll111ll1lIl1l1, flask.app.Response) and 'text/html' in l1ll1llll111ll1lIl1l1.content_type)):
                l1ll1llll111ll1lIl1l1.data = l111l1ll1llll111Il1l1.l1lll1ll1ll1l1l1Il1l1.l11111ll11ll1l11Il1l1(l1ll1llll111ll1lIl1l1.data.decode('utf-8')).encode('utf-8')
                return l1ll1llll111ll1lIl1l1
            else:
                return l1ll1llll111ll1lIl1l1

        flask.app.Flask.dispatch_request = l1ll1lll1lll1ll1Il1l1  # type: ignore
