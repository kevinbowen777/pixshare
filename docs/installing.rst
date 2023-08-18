Installation
============

Cloning the project
-------------------

To install the ``pixshare`` project, run the following command in your terminal:

.. code-block:: console

   $ git clone https://github.com/kevinbowen777/pixshare.git
   $ cd pixshare 

Local installation
^^^^^^^^^^^^^^^^^^

.. code-block:: console

   $ poetry shell
   $ poetry install
   $ python manage.py migrate
   $ python manage.py createsuperuser

Docker installation
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   $ docker compose up --build
   $ docker compose python manage.py migrate
   $ docker compose python manage.py createsuperuser

   Additional commands:
   $ docker compose exec web python manage.py shell_plus
     (loads Django shell autoloading the project models & classes)
   $ docker run -it pixshare-web bash
     (CLI access to container)

Pre-commit installation
^^^^^^^^^^^^^^^^^^^^^^^
To add the pre-commit hooks, run the following command in the poetry shell:

.. code-block:: console

   $ pre-commit install
   $ pre-commit autoupdate

After the repository has been successfully cloned and installed, see the :doc:`configuring` section for instructions to set up your environment and start the application.
