Create new users
================


Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python man# date_of_birth.py shell_plus

Sample user list
----------------

.. code-block:: console

    User = get_user_model()
    User.objects.create_user(
        username = "jdoe",
        first_name = "John",
        last_name = "Doe",
        email = "john@example.com",
        # date_of_birth = 1953-02-25,
        password="P@ssword!",
    )
    User.objects.create_user(
        username = "ssontag",
        first_name = "Susan",
        last_name = "Sontag",
        email = "susan@example.com",
        # date_of_birth = 1933-01-16,
        password="P@ssword!",
    )
    User.objects.create_user(
        username = "mshelley",
        first_name = "Mary",
        last_name = "Shelley",
        email = "mary@example.com",
        # date_of_birth = 1797-08-30,
        password="P@ssword!",
    )
    User.objects.create_user(
        username = "dhockney",
        first_name = "David",
        last_name = "Hockney",
        email = "david@example.com",
        # date_of_birth = 1937-07-09,
        password="P@ssword!",
    )
    User.objects.create_user(
        username = "acoltrane",
        first_name = "Alice",
        last_name = "Coltrane",
        email = "alice@example.com",
        # date_of_birth = 1937-08-27,
        password="P@ssword!",
    )
    User.objects.create_user(
        username = "testuser",
        first_name = "Test",
        last_name = "User",
        email = "testuser@example.com",
        # date_of_birth = 2000-07-01,
        password="P@ssword!",
        is_staff=True,
    )
