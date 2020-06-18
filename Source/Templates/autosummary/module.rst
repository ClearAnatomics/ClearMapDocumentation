{{ name | escape | underline }}

.. currentmodule:: {{ fullname }}


.. autopackagesummary:: {{ fullname }}
   :toctree: .
   :template: autosummary/module.rst


.. automodule:: {{ fullname }}



{#
.. automodule:: {{ fullname }}
   :no-members:


{% if classes %}
.. rubric:: Classes

{% for class in classes %}
.. autoclass:: {{ class }}
{% endfor %}
{% endif %}


{% if functions %}
.. rubric:: Methods

{% for function in functions %}
.. autofunction:: {{ function }}
{% endfor %}
{% endif %}


{% if exceptions %}
.. rubric:: Exceptions
   
.. autosummary::
   {% for item in exceptions %}
   {{ item }}
   {%- endfor %}
{% endif %}


{% if members %}
.. rubric:: Data
   
   {% for item in members %}
   {% if not item in functions and not item in methods %}
   .. autodata:: {{ item }}
   :annotation:
   
   {% endif %}
   {%- endfor %}
{% endif %}
#}



{#
{% if classes %}
.. rubric:: Classes

.. autosummary::
    :toctree: .
    {% for class in Classes %}
    {{ class }}
    {% endfor %}
{% endif %}

{% if functions %}
.. rubric:: Functions

.. autosummary::
    :toctree: .
    {% for function in functions %}
    {{ function }}
    {% endfor %}
{% endif %}


{% if exceptions %}
.. rubric:: Exceptions
   
.. autosummary::
   {% for item in exceptions %}
   {{ item }}
   {%- endfor %}
{% endif %}
#}
