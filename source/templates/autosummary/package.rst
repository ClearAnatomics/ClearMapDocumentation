{{ fullname | escape | underline }}

.. automodule:: {{ fullname }}

=============================================

{% if members %}

Sub-packages and modules
========================

    .. autopackagesummary:: {{ fullname }}
        :toctree: .
        :template: autosummary/package.rst

{% endif %}