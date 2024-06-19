import os
import logging
from typing import Any, Union, Optional

from jinja2 import TemplateNotFound
from sphinx.ext.autosummary import import_by_name, ImportExceptionGroup, import_ivar_by_name
from sphinx.ext.autosummary.generate import AutosummaryRenderer, find_autosummary_in_files, generate_autosummary_content
from sphinx.util import ensuredir

from sphinx.locale import get_translation


__ = get_translation('sphinx', 'console')
logger = logging.getLogger(__name__)


def custom_generate_autosummary_docs(sources: list[str],
                                     output_dir: Optional[Union[str, os.PathLike[str]]] = None,
                                     suffix: str = '.rst',
                                     base_path: Optional[Union[str, os.PathLike[str]]] = None,
                                     imported_members: bool = False, app: Any = None,
                                     overwrite: bool = True, encoding: str = 'utf-8') -> None:
    showed_sources = sorted(sources)
    if len(showed_sources) > 20:
        showed_sources = showed_sources[:10] + ['...'] + showed_sources[-10:]
    logger.info(__('[autosummary] generating autosummary for: %s') %
                ', '.join(showed_sources))

    if output_dir:
        logger.info(__('[autosummary] writing to %s') % output_dir)

    if base_path is not None:
        sources = [os.path.join(base_path, filename) for filename in sources]

    template = AutosummaryRenderer(app)

    # read
    items = find_autosummary_in_files(sources)

    # keep track of new files
    new_files = []

    if app:
        filename_map = app.config.autosummary_filename_map
    else:
        filename_map = {}

    # write
    for entry in sorted(set(items), key=lambda entry: entry.name.casefold()):
        print(f'\tProcessing {entry}')
        if entry.path is None:
            # The corresponding autosummary:: directive did not have
            # a :toctree: option
            continue

        path = output_dir or os.path.abspath(entry.path)
        ensuredir(path)

        try:
            name, obj, parent, modname = import_by_name(entry.name)
            qualname = name.replace(modname + ".", "")
        except ImportExceptionGroup as exc:
            try:
                # try to import as an instance attribute
                name, obj, parent, modname = import_ivar_by_name(entry.name)
                qualname = name.replace(modname + ".", "")
            except ImportError as exc2:
                if exc2.__cause__:
                    exceptions: list[BaseException] = [*exc.exceptions, exc2.__cause__]
                else:
                    exceptions = [*exc.exceptions, exc2]

                errors = list({f"* {type(e).__name__}: {e}" for e in exceptions})
                logger.warning(__('[autosummary] failed to import %s.\nPossible hints:\n%s'),
                               entry.name, '\n'.join(errors))
                continue

        context: dict[str, Any] = {}
        if app:
            context.update(app.config.autosummary_context)

        content = generate_autosummary_content(name, obj, parent, template, entry.template,
                                               imported_members, app, entry.recursive, context,
                                               modname, qualname)

        filename = os.path.join(path, filename_map.get(name, name) + suffix)
        if os.path.isfile(filename):
            with open(filename, encoding=encoding) as f:
                old_content = f.read()

            if content == old_content:
                continue
            if overwrite:  # content has changed
                with open(filename, 'w', encoding=encoding) as f:
                    f.write(content)
                new_files.append(filename)
        else:
            with open(filename, 'w', encoding=encoding) as f:
                f.write(content)
            new_files.append(filename)

    # descend recursively to new files
    if new_files:
        custom_generate_autosummary_docs(new_files, output_dir=output_dir,
                                         suffix=suffix, base_path=base_path,
                                         imported_members=imported_members, app=app,
                                         overwrite=overwrite)


class CustomAutosummaryRenderer(AutosummaryRenderer):
    # def __init__(self, app):
    #     super().__init__(app)
    #
    #     # Add your function to the Jinja2 environment
    #     self.env.globals.update(has_submodules=has_submodules)

    def render(self, template_name: str, context: dict) -> str:
        """Render a template file."""
        # if not context['classes'] and not context['functions']:  # Probably a package
        if '__path__' in context['members']:  # Package definition from sphinx autosummary.generate
            template_name = 'autosummary/package.rst'
        else:
            template_name = 'autosummary/module.rst'
        try:
            template = self.env.get_template(template_name)
        except TemplateNotFound:
            try:
                # objtype is given as template_name
                template = self.env.get_template('autosummary/%s.rst' % template_name)
            except TemplateNotFound:
                # fallback to base.rst
                template = self.env.get_template('autosummary/base.rst')

        return template.render(context)
