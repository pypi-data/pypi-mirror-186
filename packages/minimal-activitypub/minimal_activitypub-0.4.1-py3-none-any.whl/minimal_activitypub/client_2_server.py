"""Simplifies interacting with an ActivityPub server / instance.

This is a minimal implementation only implementing some API calls. API
calls supported will likely be expanded over time. However, do not
expect a full or complete implementation of the ActivityPub API.
"""
import asyncio
import json
import logging
import mimetypes
import random
import uuid
from typing import Any
from typing import BinaryIO
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import Union
from urllib.parse import parse_qs
from urllib.parse import urlparse

import aiohttp
import arrow

from . import __display_name__
from . import USER_AGENT

logger = logging.getLogger(__display_name__)


ActivityPubClass = TypeVar("ActivityPubClass", bound="ActivityPub")
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"


class ActivityPub:
    """Simplifies interacting with an ActivityPub server / instance.

    This is a minimal implementation only implementing methods needed
    for the function of MastodonAmnesia
    """

    # It's not that many over. It's using 9 instance attributes (opposed to 7 being
    # deemed the max attributes a class should have)
    # pylint: disable-msg=too-many-instance-attributes

    def __init__(
        self: ActivityPubClass,
        instance: str,
        session: aiohttp.ClientSession,
        access_token: str,
    ) -> None:
        self.instance = instance
        self.authorization = f"Bearer {access_token}"
        self.session = session
        self.pagination: dict[str, dict[str, Optional[str]]] = {
            "next": {"max_id": None, "min_id": None},
            "prev": {"max_id": None, "min_id": None},
        }
        self.is_instance_pleroma = False
        self.ratelimit_limit = 300
        self.ratelimit_remaining = 300
        self.ratelimit_reset = arrow.now()

    async def verify_credentials(self: ActivityPubClass) -> Any:
        """It verifies the credentials of the user.

        :param self: ActivityPubClass
        :type self: ActivityPubClass
        :return: The response is a JSON object containing the account's information.
        """
        headers = {"Authorization": self.authorization}
        url = f"{self.instance}/api/v1/accounts/verify_credentials"
        async with self.session.get(url=url, headers=headers) as response:
            logger.debug(
                "ActivityPub.verify_credentials - response: \n%s",
                response,
            )
            self.__update_ratelimit(response.headers)
            await ActivityPub.__check_exception(response=response)
            self.__parse_next_prev(links=response.headers.get("Link"))
            json_response = await response.json()

        logger.debug(
            "ActivityPub.verify_credentials -> json_response: \n%s",
            json.dumps(json_response, indent=4),
        )
        return json_response

    async def determine_instance_type(self: ActivityPubClass) -> None:
        """It checks if the instance is a Pleroma instance or not.

        :param self: The class itself
        :type self: ActivityPubClass
        """
        instance = self.instance
        if "http" not in self.instance:
            instance = f"https://{self.instance}"

        async with self.session.get(url=f"{instance}/api/v1/instance") as response:
            await ActivityPub.__check_exception(response=response)
            response_dict = await response.json()
        self.instance = instance
        if "Pleroma" in response_dict["version"]:
            self.is_instance_pleroma = True
        logger.debug(
            "ActivityPub.determine_instance_type -> response.dict:\n%s",
            json.dumps(response_dict, indent=4),
        )

    async def get_account_statuses(
        self: ActivityPubClass,
        account_id: str,
        max_id: Optional[str] = None,
        min_id: Optional[str] = None,
    ) -> Any:
        """It gets the statuses of a given account.

        :param self: The class instance
        :type self: ActivityPubClass
        :param account_id: The account ID of the account you want to get the statuses of
        :type account_id: str
        :param max_id: The ID of the last status you want to get
        :type max_id: Optional[str]
        :param min_id: The ID of the oldest status you want to retrieve
        :type min_id: Optional[str]
        :return: A list of statuses.
        """

        logger.debug(
            "ActivityPub.get_account_statuses(account_id=%s, max_id=%s, min_id=%s)",
            account_id,
            max_id,
            min_id,
        )

        await self.__pre_call_checks()

        headers = {"Authorization": self.authorization}
        paging = "?"
        url = f"{self.instance}/api/v1/accounts/{account_id}/statuses"
        if max_id:
            paging += f"max_id={max_id}"
        if min_id:
            if len(paging) > 1:
                paging += "&"
            paging += f"min_id={min_id}"
        if max_id or min_id:
            url += paging
        logger.debug("ActivityPub.get_account_statuses - url = %s", url)
        async with self.session.get(url=url, headers=headers) as response:
            self.__update_ratelimit(response.headers)
            await ActivityPub.__check_exception(response=response)
            self.__parse_next_prev(links=response.headers.get("Link"))
            result = await response.json()

        logger.debug(
            "ActivityPub.get_account_statuses -> result:\n%s",
            json.dumps(result, indent=4),
        )
        return result

    async def delete_status(
        self: ActivityPubClass,
        status: Union[str, dict[Any, Any]],
    ) -> Any:
        """It deletes a status.

        :param self: The class that inherits from ActivityPub
        :type self: ActivityPubClass
        :param status: The ID of the status you want to delete or a dict containing the
        status details
        :type status: str or dict
        :return: The response from the server.
        """

        # add random delay of up to 3 seconds in case we are deleting many
        # statuses in a batch
        sleep_for = random.SystemRandom().random() * 3
        logger.debug(
            "ActivityPub.delete_status - status_id = %s - sleep_for = %s",
            status if isinstance(status, str) else status["id"],
            sleep_for,
        )
        await asyncio.sleep(delay=sleep_for)

        if isinstance(status, str):
            status_id = status
        elif isinstance(status, dict):
            status_id = status["id"]
            if self.is_instance_pleroma and status["reblogged"]:
                response = await self.undo_reblog(status=status)
                return response
            if self.is_instance_pleroma and status["favourited"]:
                response = await self.undo_favourite(status=status)
                return response

        await self.__pre_call_checks()

        headers = {"Authorization": self.authorization}
        url = f"{self.instance}/api/v1/statuses/{status_id}"
        async with self.session.delete(url=url, headers=headers) as response:
            self.__update_ratelimit(response.headers)
            await ActivityPub.__check_exception(response=response)
            self.__parse_next_prev(links=response.headers.get("Link"))
            result = await response.json()

        logger.debug(
            "ActivityPub.delete_status -> result:\n%s",
            json.dumps(result, indent=4),
        )
        return result

    async def undo_reblog(
        self: ActivityPubClass, status: Union[str, dict[Any, Any]]
    ) -> Any:
        """Removes a reblog.

        :param self: The class that inherits from ActivityPub
        :type self: ActivityPubClass
        :param status: The ID of the status you want to delete or a dict containing the
        status details
        :type status: str or dict
        :return: The response from the server.
        """
        logger.debug(
            "ActivityPub.undo_reblog(status=%s",
            status,
        )

        if isinstance(status, str):
            status_id = status
        elif isinstance(status, dict):
            status_id = status["reblog"]["id"]

        await self.__pre_call_checks()
        headers = {"Authorization": self.authorization}
        url = f"{self.instance}/api/v1/statuses/{status_id}/unreblog"
        async with self.session.post(url=url, headers=headers) as response:
            self.__update_ratelimit(response.headers)
            await ActivityPub.__check_exception(response=response)
            self.__parse_next_prev(links=response.headers.get("Link"))
            result = await response.json()

        logger.debug(
            "ActivityPub.undo_reblog -> result:\n%s",
            json.dumps(result, indent=4),
        )
        return result

    async def undo_favourite(
        self: ActivityPubClass,
        status: Union[str, dict[Any, Any]],
    ) -> Any:
        """Removes a favourite.

        :param self: The class that inherits from ActivityPub
        :type self: ActivityPubClass
        :param status: The ID of the status you want to delete or a dict containing the
        status details
        :type status: str or dict
        :return: The response from the server.
        """
        logger.debug(
            "ActivityPub.undo_favourite(status=%s)",
            status,
        )

        if isinstance(status, str):
            status_id = status
        elif isinstance(status, dict):
            status_id = status["id"]

        await self.__pre_call_checks()
        headers = {"Authorization": self.authorization}
        url = f"{self.instance}/api/v1/statuses/{status_id}/unfavourite"
        async with self.session.post(url=url, headers=headers) as response:
            self.__update_ratelimit(response.headers)
            await ActivityPub.__check_exception(response=response)
            self.__parse_next_prev(links=response.headers.get("Link"))
            result = await response.json()

        logger.debug(
            "ActivityPub.undo_favourite -> result:\n%s",
            json.dumps(result, indent=4),
        )
        return result

    @staticmethod
    async def get_auth_token(
        instance_url: str,
        username: str,
        password: str,
        session: aiohttp.ClientSession,
        user_agent: str = USER_AGENT,
        client_website: str = "https://pypi.org/project/minimal-activitypub/",
    ) -> str:
        """It creates an app, then uses that app to get an access token.

        :param instance_url: The URL of the Mastodon instance you want to connect to
        :type instance_url: str
        :param username: The username of the account you want to get an auth_token for
        :type username: str
        :param password: The password of the account you want to get an auth_token for
        :type password: str
        :param session: aiohttp.ClientSession
        :type session: aiohttp.ClientSession
        :param user_agent: User agent identifier to use. Defaults to
        minimal_activitypub related one.
        :type user_agent: str
        :param client_website: Link to site for user_agent. Defaults to link to
        minimal_activitypub on Pypi.org
        :return: The access token is being returned.
        """

        # Two of the arguements have sensible default values so only 4 are really
        # necessary.
        # pylint: disable-msg=too-many-arguments

        if "http" not in instance_url:
            instance_url = f"https://{instance_url}"

        form_data = aiohttp.FormData()
        form_data.add_field("client_name", user_agent)
        form_data.add_field("client_website", client_website)
        form_data.add_field("scopes", "read write")
        form_data.add_field("redirect_uris", REDIRECT_URI)
        async with session.post(
            url=f"{instance_url}/api/v1/apps",
            data=form_data,
        ) as response:
            logger.debug(
                "ActivityPub.get_auth_token apps response: \n%s",
                response,
            )
            await ActivityPub.__check_exception(response)
            response_dict = await response.json()

        logger.debug(
            "ActivityPub.get_auth_token apps response.json: \n%s",
            json.dumps(response_dict, indent=4),
        )

        client_id = response_dict["client_id"]
        client_secret = response_dict["client_secret"]
        form_data = aiohttp.FormData()
        form_data.add_field("client_id", client_id)
        form_data.add_field("client_secret", client_secret)
        form_data.add_field("scope", "read write")
        form_data.add_field("redirect_uris", REDIRECT_URI)
        form_data.add_field("grant_type", "password")
        form_data.add_field("username", username)
        form_data.add_field("password", password)
        async with session.post(
            url=f"{instance_url}/oauth/token",
            data=form_data,
        ) as response:
            logger.debug(
                "ActivityPub.get_auth_token token response: \n%s",
                response,
            )
            await ActivityPub.__check_exception(response)
            response_dict = await response.json()

        logger.debug(
            "ActivityPub.get_auth_token apps response.json: \n%s",
            json.dumps(response_dict, indent=4),
        )
        return str(response_dict["access_token"])

    async def post_status(
        self: ActivityPubClass,
        status: str,
        visibility: str = "public",
        media_ids: Optional[list[str]] = None,
        sensitive: bool = False,
        spoiler_text: Optional[str] = None,
    ) -> Any:
        """Posts a status to the fediverse.

        :param status: The text to be posted on the timeline.
        :param visibility: Visibility of the posted status. Enumerable one of `public`,
        `unlisted`, `private`, or `direct`. Defaults to `public`
        :param media_ids: List of ids for media (pictures, videos, etc) to be attached
        to this post. Can be `None` if no media is to be attached. Defaults to `None`
        :param sensitive: Set to true the post is of a sensitive nature and should be
        marked as such. For example overly political or explicit material is often
        marked as sensitive. Applies particularly to attached media. Defaults to `False`
        :param spoiler_text: Text to be shown as a warning or subject before the actual
        content. Statuses are generally collapsed behind this field. Defaults to `None`
        :return: Dict of the status just posted.
        """
        # pylint: disable=too-many-arguments

        logger.debug(
            "ActivityPub.post_status(status=%s, visibility=%s, media_ids=%s, sensitive=%s, spoiler_text=%s)",
            status,
            visibility,
            media_ids,
            sensitive,
            spoiler_text,
        )
        await self.__pre_call_checks()

        headers = {
            "Authorization": self.authorization,
            "Idempotency-Key": uuid.uuid4().hex,
        }
        url = f"{self.instance}/api/v1/statuses/"
        data = aiohttp.FormData()
        data.add_field("status", status)
        data.add_field("visibility", visibility)
        data.add_field("sensitive", sensitive)
        if media_ids:
            data.add_field("media_ids[]", media_ids)
        if spoiler_text:
            data.add_field("spoiler_text", spoiler_text)

        logger.debug("ActivityPub.post_status - posting data=%s", data)
        async with self.session.post(
            url=url,
            headers=headers,
            data=data,
        ) as response:

            self.__update_ratelimit(headers=response.headers)
            await ActivityPub.__check_exception(response=response)
            result = await response.json()

        logger.debug(
            "ActivityPub.post_status -> result:\n%s",
            json.dumps(result, indent=4),
        )
        return result

    async def post_media(
        self: ActivityPubClass,
        file: BinaryIO,
        mime_type: str,
        description: Optional[str] = None,
        focus: Optional[Tuple[float, float]] = None,
    ) -> Any:
        """Post a media file (image or video)

        :param file: The file to be uploaded
        :param mime_type: Mime type
        :param description: A plain-text description of the media, for accessibility purposes
        :param focus: Two floating points (x,y), comma-delimited, ranging from -1.0 to 1.0
        (see “Focal points <https://docs.joinmastodon.org/methods/statuses/media/#focal-points>”_)
        :return: Dict containing details for this media on server, such a `id`, `url` etc
        """

        logger.debug(
            "ActivityPub.post_media(file=..., mime_type=%s, description=%s, focus=%s)",
            mime_type,
            description,
            focus,
        )

        await self.__pre_call_checks()

        file_extension = mimetypes.guess_extension(mime_type)
        if file_extension is None:
            raise ClientError(
                f"Cannot determine file type based on passed in mime-type: {mime_type}"
            )

        headers = {"Authorization": self.authorization}
        url = f"{self.instance}/api/v1/media"
        data = aiohttp.FormData()
        data.add_field(
            name="file",
            value=file,
            filename=uuid.uuid4().hex + file_extension,
            content_type=mime_type,
        )
        if description:
            data.add_field(name="description", value=description)
        if focus and len(focus) >= 2:
            data.add_field(name="focus", value=f"{focus[0]},{focus[1]}")

        async with self.session.post(
            url=url,
            headers=headers,
            data=data,
        ) as response:

            self.__update_ratelimit(headers=response.headers)
            await ActivityPub.__check_exception(response=response)
            result = await response.json()

        logger.debug(
            "ActivityPub.post_media -> result:\n%s",
            json.dumps(result, indent=4),
        )
        return result

    async def __pre_call_checks(self: ActivityPubClass) -> None:
        """Checks to perform before contacting the instance server.

        For now just looking at rate limits by checking if the rate
        limit is 0 and the rate limit reset time is in the future, raise
        a RatelimitError
        """
        logger.debug(
            "ActivityPub.__pre_call_checks "
            "- Limit remaining: %s "
            "- Limit resetting at %s",
            self.ratelimit_remaining,
            self.ratelimit_reset,
        )
        if self.ratelimit_remaining == 0 and self.ratelimit_reset > arrow.now():
            raise RatelimitError(429, None, "Rate limited")

    def __parse_next_prev(self: ActivityPubClass, links: Optional[str]) -> None:
        """It takes a string of the form `https://example.com/api/v1/timelines/
        home?min_id=12345&max_id=67890` and extracts the values of `min_id` and
        `max_id` from it and stores them in the instance attributes
        pagination_min_id and pagination_max_id.

        :param self: The class that is being parsed
        :type self: ActivityPubClass
        :param links: The links header from the response
        :type links: Optional[str]
        """
        logger.debug("ActivityPub.__parse_next_prev - links = %s", links)

        if links:
            self.pagination = {
                "next": {"max_id": None, "min_id": None},
                "prev": {"max_id": None, "min_id": None},
            }

            for comma_links in links.split(sep=", "):
                pagination_rel: Optional[str] = None
                if 'rel="next"' in comma_links:
                    pagination_rel = "next"
                elif 'rel="prev"' in comma_links:
                    pagination_rel = "prev"

                if pagination_rel:
                    urls = comma_links.split(sep="; ")

                    logger.debug(
                        "ActivityPub.__parse_next_prev - rel = %s - urls = %s",
                        pagination_rel,
                        urls,
                    )

                    for url in urls:
                        parsed_url = urlparse(url=url.lstrip("<").rstrip(">"))
                        queries_dict = parse_qs(str(parsed_url.query))
                        logger.debug(
                            "ActivityPub.__parse_next_prev - queries_dict = %s",
                            queries_dict,
                        )
                        min_id = queries_dict.get("min_id")
                        max_id = queries_dict.get("max_id")
                        if min_id:
                            self.pagination[pagination_rel]["min_id"] = min_id[0]
                        if max_id:
                            self.pagination[pagination_rel]["max_id"] = max_id[0]

        logger.debug("ActivityPub.__parse_next_prev - pagination = %s", self.pagination)

    def __update_ratelimit(self: ActivityPubClass, headers: Any) -> None:
        """If the instance is not Pleroma, update the ratelimit variables.

        :param self: The class that is being updated
        :type self: ActivityPubClass
        :param headers: The headers of the response
        :type headers: Any
        """
        temp_ratelimit_limit = temp_ratelimit_remaining = temp_ratelimit_reset = None
        if not self.is_instance_pleroma:
            temp_ratelimit_limit = headers.get("X-RateLimit-Limit")
            temp_ratelimit_remaining = headers.get("X-RateLimit-Remaining")
            temp_ratelimit_reset = headers.get("X-RateLimit-Reset")

        if temp_ratelimit_limit:
            self.ratelimit_limit = int(temp_ratelimit_limit)
        if temp_ratelimit_remaining:
            self.ratelimit_remaining = int(temp_ratelimit_remaining)
        if temp_ratelimit_reset:
            self.ratelimit_reset = arrow.get(temp_ratelimit_reset)

        logger.debug(
            "ActivityPub.__update_ratelimit "
            "- Pleroma Instance: %s "
            "- RateLimit Limit %s",
            self.is_instance_pleroma,
            self.ratelimit_limit,
        )
        logger.debug(
            "ActivityPub.__update_ratelimit "
            "- Limit remaining: %s "
            "- Limit resetting at %s",
            self.ratelimit_remaining,
            self.ratelimit_reset,
        )

    @staticmethod
    async def __check_exception(response: aiohttp.ClientResponse) -> None:
        """If the response status is greater than or equal to 400, then raise
        an appropriate exception.

        :param response: aiohttp.ClientResponse
        :type response: aiohttp.ClientResponse
        """
        logger.debug(
            "ActivityPub.__check_exception - response.headers = %s", response.headers
        )
        logger.debug(
            "ActivityPub.__check_exception - response.status = %s", response.status
        )
        if response.status >= 400:

            error_message = await ActivityPub.__determine_error_message(response)

            if response.status == 401:
                raise UnauthorizedError(response.status, response.reason, error_message)
            if response.status == 403:
                raise ForbiddenError(response.status, response.reason, error_message)
            if response.status == 404:
                raise NotFoundError(response.status, response.reason, error_message)
            if response.status == 409:
                raise ConflictError(response.status, response.reason, error_message)
            if response.status == 410:
                raise GoneError(response.status, response.reason, error_message)
            if response.status == 422:
                raise UnprocessedError(response.status, response.reason, error_message)
            if response.status == 429:
                raise RatelimitError(response.status, response.reason, error_message)
            if response.status < 500:
                raise ClientError(response.status, response.reason, error_message)

            raise ServerError(response.status, response.reason, error_message)

    @staticmethod
    async def __determine_error_message(response: aiohttp.ClientResponse) -> str:
        """If the response is JSON, return the error message from the JSON,
        otherwise return the response text.

        :param response: aiohttp.ClientResponse
        :type response: aiohttp.ClientResponse
        :return: The error message is being returned.
        """

        error_message = "Exception has occurred"
        try:
            content = await response.json()
            error_message = content["error"]
        except (aiohttp.ClientError, KeyError):
            try:
                error_message = await response.text()
            except (aiohttp.ClientError, LookupError):
                pass
        logger.debug(
            "ActivityPub.__determine_error_message - error_message = %s", error_message
        )
        return error_message


class ActivityPubError(Exception):
    """Base class for all mastodon exceptions."""


class NetworkError(ActivityPubError):
    """`NetworkError` is a subclass of `ActivityPubError` that is raised when
    there is a network error."""

    pass


class ApiError(ActivityPubError):
    """`ApiError` is a subclass of `ActivityPubError` that is raised when there
    is an API error."""

    pass


class ClientError(ActivityPubError):
    """`ClientError` is a subclass of `ActivityPubError` that is raised when
    there is a client error."""

    pass


class UnauthorizedError(ClientError):
    """`UnauthorizedError` is a subclass of `ClientError` that is raised when
    the user represented by the auth_token is not authorized to perform a
    certain action."""

    pass


class ForbiddenError(ClientError):
    """`ForbiddenError` is a subclass of `ClientError` that is raised when the
    user represented by the auth_token is forbidden to perform a certain
    action."""

    pass


class NotFoundError(ClientError):
    """`NotFoundError` is a subclass of `ClientError` that is raised when an
    object for an action cannot be found."""

    pass


class ConflictError(ClientError):
    """`ConflictError` is a subclass of `ClientError` that is raised when there
    is a conflict with performing an action."""

    pass


class GoneError(ClientError):
    """`GoneError` is a subclass of `ClientError` that is raised when an object
    for an action has gone / been deleted."""

    pass


class UnprocessedError(ClientError):
    """`UnprocessedError` is a subclass of `ClientError` that is raised when an
    action cannot be processed."""

    pass


class RatelimitError(ClientError):
    """`RatelimitError` is a subclass of `ClientError` that is raised when
    we've reached a limit of number of actions performed quickly."""

    pass


class ServerError(ActivityPubError):
    """`ServerError` is a subclass of `ActivityPubError` that is raised when
    the server / instance encountered an error."""

    pass
