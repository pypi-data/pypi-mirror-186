Minimal-ActivityPub
===================

|Repo| |CI| |Downloads|

|Safety| |pip-audit| |Interrogate|

|Codestyle| |Version| |Wheel|

|AGPL|


Minimal-ActivityPub is a minimal Python implementation of the ActivityPub rest API used by
`Mastodon <https://joinmastodon.org/>`_,
`Pleroma <https://pleroma.social/>`_,
and others. This implementation makes use of asyncio where appropriate. It is intended to be used as a library by other
applications. No standalone functionality is provided.

Minimal refers to the fact that only API calls I need for my other projects;
`MastodonAmnesia <https://codeberg.org/MarvinsMastodonTools/mastodonamnesia>`_ and
`TootBot <https://codeberg.org/MarvinsMastodonTools/tootbot>`_ are implemented.

**DO NOT** expect a full or complete implementation of all `ActivityPub API <https://activitypub.rocks/>`_ functionality.

API Methods Currently Implemented
==================================

Client to Server Methods
----------------------------------
- get_auth_token
- verify_credentials
- determine_instance_type
- get_account_statuses
- delete_status
- post_status
- post_media
- undo_reblog
- undo_favourite

Server to Server Methods
----------------------------------
No API methods for server to server communications have been implemented.

Usage
==================================
Minimal-ActivityPub is available on `PyPi <https://pypi.org/>`_ as `minimal-activitypub` and can be added to an
application the same as any other python library.

Add `minimal-activitypub` as a requirement to your project and/or install using pip::

    pip install minimal-activitypub

Workflow overview
----------------------------------
In general you need the authenticate to an ActivityPub server instance. To do so you require an `access_token`, so generally
you'll want to use the method ``get_auth_token`` when setting up the initial connection.

After that I think it is a good idea to verify the credentials using the ``verify_credentials`` method and determine the
server type using the ``determine_instance_type`` method.

After that you use which ever method(s) that are needed for your use case.

.. Todo: Add individual explanation for each method.

Example for ``get_auth_token(...)``
-----------------------------------------
To get an Auth Token (also referred to as an access token) your code needs to be able to login to the Fediverse instance.
In this API implementation we do so using the user_name (email for Mastodon instances) and the user's password.
Neither of these values is being stored after an auth token has been obtained.

.. code-block:: python

    async def example(instance, user_name, password):
        async with aiohttp.ClientSession() as session:
            access_token = await ActivityPub.get_auth_token(
                instance_url=instance,
                username=user_name,
                password=password,
                session=session,
        )

Example for ``verify_credentials(...)``
-----------------------------------------
``verify_credentials(...)`` ensures that the access_token is valid and returns information about the user that the
access_token has been created for. It is good practice to check the validity of the access_token with this method call
before any further interaction with the Fediverse instance.

.. code-block:: python

    async def example(instance, access_token):
        async with aiohttp.ClientSession() as session:
            instance = ActivityPub(
                instance=instance,
                access_token=access_token,
                session=session,
            )
            user_info = await instance.verify_credentials()
            account_id = user_info["id"]
            user_name = user_info["username"]

Example for ``determine_instance_type()``
-----------------------------------------
``determine_instance_type()`` checks what type of server we are interacting with. At this time minimal-activitypub only
check for Pleroma and otherwise defaults to Mastodon.
This method updates the instance variable ``is_instance_pleroma`` to ``True`` if the Fediverse server is
running Pleroma

.. code-block:: python

    async def example(instance, access_token):
        async with aiohttp.ClientSession() as session:
            instance = ActivityPub(
                instance=instance,
                access_token=access_token,
                session=session,
            )
            await instance.determine_instance_type()

Example for ``get_account_statuses(...)``
-----------------------------------------
``get_account_statuses(...)`` retrieves a list of the most recent toots posted by the account identified by its id.
This method updates the instance variables ``pagination_max_id`` and ``pagination_min_id`` with the values for ``min_id``
and ``max_id`` returned by the server in the http response header.
These values can be used to paginate forward and backwards through the history of toots.

.. code-block:: python

    async def example(account_id):
        async with aiohttp.ClientSession() as session:
            instance = ActivityPub(
                instance=instance,
                access_token=access_token,
                session=session,
            )
            toots = await instance.get_account_statuses(account_id=account_id)

            # retrieving the next set of toots
            if instance.pagination_max_id:
                toots = await instance.get_account_statuses(
                    account_id=account_id,
                    max_id=instance.pagination_max_id,
                )

Example for ``delete_status(...)``
-----------------------------------------
``delete_status(...)`` deletes a toot / post / status identified by its id.
This method returns the deleted toot / post / status.

.. code-block:: python

    async def example(toot_id):
        async with aiohttp.ClientSession() as session:
            instance = ActivityPub(
                instance=instance,
                access_token=access_token,
                session=session,
            )
            deleted_toot = await instance.delete_status(status_id=toot_id)

Example for ``post_status(...)``
-----------------------------------------
``post_status(...)`` creates a toot / post / status identified.
This method returns the created toot / post / status.

.. code-block:: python

    async def example(status_text: str):
        async with aiohttp.ClientSession() as session:
            instance = ActivityPub(
                instance=instance,
                access_token=access_token,
                session=session,
            )

            toot = await instance.post_status(
                status=status_text,
            )

Example for ``post_media(...)``
-----------------------------------------
``post_media(...)`` sends an image or video to the server. This needs to be done to be able to attach an image or
video to a toot / post / status
This method returns a dictionary containing details for this media on server, such a `id`, `url` etc.

.. code-block:: python

    async def example(media_path: str):
        async with aiohttp.ClientSession() as session:
            instance = ActivityPub(
                instance=instance,
                access_token=access_token,
                session=session,
            )

            mime_type = magic.from_file(media_path, mime=True)
            async with aiofiles.open(file=media_path, mode="rb") as upload:
                media = await instance.post_media(
                    file=upload,
                    mime_type=mime_type,
                )

            media_ids = [media['id'], ]
            toot = await instance.post_status(
                status="Test status with media attached",
                media_ids=media_ids,
            )

Contributing
==================================
Issues and pull requests are welcome.

Minimal-ActivityPub is using `pre-commit <https://pre-commit.com/>`_ and `Poetry <https://python-poetry.org/>`_.
Please install and use both pre-commit and Poetry if you'd like to contribute.

To make sure you have all required python modules installed with Poetry is as easy as ``poetry install`` in the root of the
project directory

Licensing
==================================
Minimal-ActivityPub is licences under licensed under the `GNU Affero General Public License v3.0 <http://www.gnu.org/licenses/agpl-3.0.html>`_

Supporting Minimal-ActivityPub
==================================

There are a number of ways you can support Minimal-ActivityPub:

- Create an issue with problems or ideas you have with/for Minimal-ActivityPub
- You can `buy me a coffee <https://www.buymeacoffee.com/marvin8>`_.
- You can send me small change in Monero to the address below:

Monero donation address:
----------------------------------
`8ADQkCya3orL178dADn4bnKuF1JuVGEG97HPRgmXgmZ2cZFSkWU9M2v7BssEGeTRNN2V5p6bSyHa83nrdu1XffDX3cnjKVu`


.. |AGPL| image:: https://www.gnu.org/graphics/agplv3-with-text-162x68.png
    :alt: AGLP 3 or later
    :target:  https://codeberg.org/MarvinsMastodonTools/minimal-activitypub/src/branch/main/LICENSE.md

.. |Repo| image:: https://img.shields.io/badge/repo-Codeberg.org-blue
    :alt: Repo at Codeberg.org
    :target: https://codeberg.org/MarvinsMastodonTools/minimal-activitypub

.. |Downloads| image:: https://pepy.tech/badge/minimal-activitypub
    :alt: Download count
    :target: https://pepy.tech/project/minimal-activitypub

.. |Codestyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :alt: Code style: black
    :target: https://github.com/psf/black

.. |Safety| image:: https://img.shields.io/badge/Safety--DB-checked-green
    :alt: Checked against PyUp Safety DB
    :target: https://pyup.io/safety/

.. |pip-audit| image:: https://img.shields.io/badge/pip--audit-checked-green
    :alt: Checked with pip-audit
    :target: https://pypi.org/project/pip-audit/

.. |Version| image:: https://img.shields.io/pypi/pyversions/minimal-activitypub
    :alt: PyPI - Python Version

.. |Wheel| image:: https://img.shields.io/pypi/wheel/minimal-activitypub
    :alt: PyPI - Wheel

.. |CI| image:: https://ci.codeberg.org/api/badges/MarvinsMastodonTools/minimal-activitypub/status.svg
    :alt: CI / Woodpecker
    :target: https://ci.codeberg.org/MarvinsMastodonTools/minimal-activitypub

.. |Interrogate| image:: https://codeberg.org/MarvinsMastodonTools/minimal-activitypub/raw/branch/main/interrogate_badge.svg
    :alt: Doc-string coverage
    :target: https://interrogate.readthedocs.io/en/latest/
