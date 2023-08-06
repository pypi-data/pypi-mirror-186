from contextlib import contextmanager
from pathlib import Path
import sys
import types
from typing import TYPE_CHECKING, Any, Dict, Generator, List, Tuple, Type

import reloadium.lib.extensions.pytest_extension_guard
from reloadium.corium import audit
from reloadium.lib.extensions.django import Django
from reloadium.lib.extensions.extension import Extension
from reloadium.lib.extensions.flask import Flask
from reloadium.lib.extensions.graphene import Graphene
from reloadium.lib.extensions.pandas import Pandas
from reloadium.lib.extensions.pygame import PyGame
from reloadium.fast.extensions.pytest import Pytest
from reloadium.lib.extensions.sqlalchemy import Sqlalchemy
from reloadium.lib.extensions.multiprocessing import Multiprocessing
from reloadium.corium.loggium import loggium

if TYPE_CHECKING:
    from dataclasses import dataclass, field

    from reloadium.corium.core import Core
    from reloadium.corium.objects import Action

else:
    from reloadium.vendored.dataclasses import dataclass, field


logger = loggium.factory(__name__)


@dataclass
class ExtensionManager:
    core: "Core"

    extensions: List[Extension] = field(init=False, default_factory=list)

    already_imported: List[types.ModuleType] = field(init=False, default_factory=list)

    klasses: List[Type[Extension]] = field(
        init=False, default_factory=lambda: [Flask, Pandas, Django, Sqlalchemy, PyGame, Graphene, Pytest, Multiprocessing]
    )

    def start(self) -> None:
        pass

    def on_import(self, python_module_obj: types.ModuleType) -> None:
        for et in self.klasses.copy():
            assert hasattr(python_module_obj, "__name__")
            if python_module_obj.__name__.split(".")[0].lower() == et.name.lower():
                self._create_extension(et)

        if python_module_obj in self.already_imported:
            return

        for p in self.extensions:
            p.on_import(python_module_obj)

        self.already_imported.append(python_module_obj)

    def _create_extension(self, et: Type[Extension]) -> None:
        ext = et(self)

        self.core.user.run.send_event(audit.ExtensionUse(ext))
        ext.on_start()
        self.extensions.append(ext)
        self.klasses.remove(et)

    @contextmanager
    def on_rewrite_source(
        self, new_source: str, context: Dict[str, Any]
    ) -> Generator[Tuple[str, Dict[str, Any]], None, None]:
        context_mans = [p.on_rewrite_source(new_source, context) for p in self.extensions]

        for c in context_mans:
            new_source, context = c.__enter__()

        yield new_source, context

        for c in context_mans:
            c.__exit__(*sys.exc_info())

    def before_reload(self, path: Path) -> None:
        for p in self.extensions:
            p.before_reload(path)

    def on_other_modify(self, path: Path) -> None:
        for p in self.extensions:
            p.on_other_modify(path)

    def on_error(self, exc: Exception) -> None:
        for p in self.extensions:
            p.on_error(exc)

    def after_reload(self, path: Path, actions: List["Action"]) -> None:
        for p in self.extensions:
            p.after_reload(path, actions)

    def reset(self) -> None:
        self.extensions.clear()
