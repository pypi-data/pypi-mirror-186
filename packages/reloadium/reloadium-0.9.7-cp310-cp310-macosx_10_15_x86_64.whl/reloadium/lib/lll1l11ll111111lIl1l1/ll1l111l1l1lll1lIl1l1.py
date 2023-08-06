import sys

from reloadium.corium.l1111l1lll1111llIl1l1.l111l111l11111l1Il1l1 import l1l1111111l1l11lIl1l1

l1l1111111l1l11lIl1l1()


try:
    import _pytest.assertion.rewrite
except ImportError:
    class l1111l11lll1l111Il1l1:
        pass

    _pytest = lambda :None  # type: ignore
    sys.modules['_pytest'] = _pytest

    _pytest.assertion = lambda :None  # type: ignore
    sys.modules['_pytest.assertion'] = _pytest.assertion

    _pytest.assertion.rewrite = lambda :None  # type: ignore
    _pytest.assertion.rewrite.AssertionRewritingHook = l1111l11lll1l111Il1l1  # type: ignore
    sys.modules['_pytest.assertion.rewrite'] = _pytest.assertion.rewrite
