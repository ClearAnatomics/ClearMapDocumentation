# -*- coding: utf-8 -*-



def setup(app):
    import sphinx.ext.autosummary.generate as generate
    from . import autopackagesummary as aps
      
    generate.find_autosummary_in_lines = aps.find_autosummary_in_lines

    app.add_directive('autopackagesummary', aps.Autopackagesummary)
    app.connect('config-inited', aps.on_config_inited)

    return {
        'version': aps.__version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }