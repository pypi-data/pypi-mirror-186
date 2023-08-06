from __future__ import annotations

from abc import ABC, abstractmethod
from contextlib import AbstractContextManager
from types import TracebackType
from typing import Generic, Iterable, List, Optional, Type, Union

from benchling_api_client.v2.alpha.models.session import Session
from benchling_api_client.v2.alpha.models.session_create import SessionCreate
from benchling_api_client.v2.alpha.models.session_message_create import SessionMessageCreate
from benchling_api_client.v2.alpha.models.session_message_style import SessionMessageStyle
from benchling_api_client.v2.alpha.models.session_status import SessionStatus
from benchling_api_client.v2.alpha.models.session_update import SessionUpdate
from benchling_api_client.v2.alpha.models.session_update_status import SessionUpdateStatus
from benchling_api_client.v2.beta.models.canvas_update import CanvasUpdate
from benchling_api_client.v2.stable.types import Unset, UNSET
from typing_extensions import Protocol

from benchling_sdk.apps.framework import AppType
from benchling_sdk.helpers.logging_helpers import log_stability_warning, sdk_logger, StabilityLevel
from benchling_sdk.models import (
    AaSequence,
    Blob,
    Box,
    Container,
    CustomEntity,
    DnaOligo,
    DnaSequence,
    Entry,
    Folder,
    Location,
    Mixture,
    Molecule,
    Plate,
    Request,
    RnaOligo,
    RnaSequence,
    WorkflowOutput,
    WorkflowTask,
)

# Taken from CHIP_SUPPORTED_COLUMN_TYPES in Benchling server
# Anything we miss, they can still embed the ID themselves in a message
_ReferencedSessionLinkType = Union[
    AaSequence,
    Blob,
    Box,
    Container,
    CustomEntity,
    DnaSequence,
    DnaOligo,
    Entry,
    Folder,
    Location,
    Mixture,
    Plate,
    RnaOligo,
    Molecule,
    RnaSequence,
    Request,
    WorkflowOutput,
    WorkflowTask,
]

_DEFAULT_APP_ERROR_MESSAGE = "An unexpected error occurred in the app"

log_stability_warning(StabilityLevel.ALPHA)


class SessionClosedError(Exception):
    """
    Session Closed Error.

    A session was inoperable because its status in Benchling was terminal.
    """

    pass


class SessionContextClosedError(Exception):
    """
    Session Context Closed Error.

    An operation was attempted using the session context manager after it was closed.
    """

    pass


class InvalidSessionTimeoutError(Exception):
    """
    Invalid Session Timeout Error.

    A session's timeout value was set to an invalid value.
    """

    pass


class MissingAttachedCanvasError(Exception):
    """
    Missing Attached Canvas Error.

    A canvas operation was requested, but a session context has no attached canvas.
    """

    pass


class AppUserFacingError(Exception):
    """
    App User Facing Error.

    Extend this class with custom exceptions you want to be written back to the user as a SessionMessage.

    SessionClosingContextExitHandler will invoke messages() and write them to a user. Callers choosing to
    write their own SessionContextExitHandler may need to replicate this behavior themselves.

    This is useful for control flow where an app wants to terminate with an error state that is resolvable
    by the user.

    For example:

    class InvalidUserInputError(AppUserFacingError):
        pass

    raise InvalidUserInputError("Please enter a number between 1 and 10")

    This would create a message shown to the user like:

    SessionMessageCreate("Please enter a number between 1 and 10", style=SessionMessageStyle.ERROR)
    """

    def messages(self) -> List[SessionMessageCreate]:
        """Create a series of SessionMessageCreate to write to a Session and displayed to the user."""
        return [SessionMessageCreate(content=str(self), style=SessionMessageStyle.ERROR)]


class SessionProvider(Protocol):
    """Provide a Session to convey app status."""

    def __call__(self) -> Session:
        """Provide a session when called."""
        pass


class SessionContextErrorProcessor(ABC):
    """
    Session Context Error Processor.

    Implement to match a one or more exception types specified by handles to be processed by process_error
    in the event of a session context exit with errors.

    process_error() does not assume a context's session is active. If using the session with process_error(),
    this should be checked.

    For user with SessionClosingContextExitHandler or its subclasses.
    """

    @classmethod
    @abstractmethod
    def handles(cls) -> List[Type[Exception]]:
        """
        List exception types which should be delegated to this handler.

        Will also match subclasses of that exception type.
        """
        pass

    @classmethod
    @abstractmethod
    def process_error(
        cls,
        context: SessionContextManager[AppType],
        exc_type: Type[BaseException],
        exc_value: BaseException,
        exc_traceback: TracebackType,
    ) -> bool:
        """
        Process error.

        Receives one of the exception types matched by handles() and takes further action.
        Returns bool to the __exit__ of the context manager.

        If an exception is supplied, and the method wishes to suppress the exception
        (i.e., prevent it from being propagated), it should return a True value.
        Otherwise, the exception will be processed normally upon exit from this method.
        """
        pass


class AppUserFacingErrorProcessor(SessionContextErrorProcessor):
    """
    App User Facing Error Processor.

    An error processor for surfacing error messages directly back to a user.

    Most uncaught exceptions should not be exposed to users to avoid leaking information. App developers
    may curate specific exception types that extend AppUserFacingError. They may stop control flow
    and also write the message directly back to the user.
    """

    @classmethod
    def handles(cls) -> List[Type[Exception]]:
        """Register AppUserFacingError as the types to process."""
        return [AppUserFacingError]

    @classmethod
    def process_error(
        cls,
        context: SessionContextManager[AppType],
        exc_type: Type[BaseException],
        exc_value: BaseException,
        exc_traceback: TracebackType,
    ) -> bool:
        """
        Process AppUserFacingError.

        Writes a message back to the user with the error's messages and closes the session as FAILED.

        If an exception is supplied, and the method wishes to suppress the exception
        (i.e., prevent it from being propagated), it should return a True value.
        Otherwise, the exception will be processed normally upon exit from this method.
        """
        assert issubclass(
            exc_type, tuple(cls.handles())
        ), f"Expected one of error type {cls.handles()} but got {exc_type}"
        if context.has_active_session():
            assert isinstance(exc_value, AppUserFacingError)
            messages = exc_value.messages()
            context.close_session(status=SessionUpdateStatus.FAILED, messages=messages)
            return False
        else:
            raise SessionClosedError(
                f"Unable to process error of type {exc_type} in exit handler,"
                f" the session is already closed",
                exc_value,
            )


class SessionContextEnterHandler(ABC, Generic[AppType]):
    """
    Session Context Enter Handler.

    An abstract class for defining behavior when a session context's __enter__ method is called.
    """

    @abstractmethod
    def on_enter(self, context: SessionContextManager[AppType]) -> None:
        """Perform on session context enter after a Session has been started with Benchling."""
        pass


class SessionContextExitHandler(ABC, Generic[AppType]):
    """
    Session Context Exit Handler.

    An abstract class for defining behavior when a session context's __exit__ method is called.
    """

    @abstractmethod
    def on_success(self, context: SessionContextManager[AppType]) -> bool:
        """
        Perform on session context exit when no errors are present.

        Returns a bool to indicate context __exit__ behavior.

        If an exception is supplied, and the method wishes to suppress the exception
        (i.e., prevent it from being propagated), it should return a True value.
        Otherwise, the exception will be processed normally upon exit from this method.
        """
        pass

    @abstractmethod
    def on_error(
        self,
        context: SessionContextManager[AppType],
        exc_type: Type[BaseException],
        exc_value: BaseException,
        exc_traceback: TracebackType,
    ) -> bool:
        """
        Perform when an error caused the session context to exit.

        Returns a bool to indicate context __exit__ behavior.

        If an exception is supplied, and the method wishes to suppress the exception
        (i.e., prevent it from being propagated), it should return a True value.
        Otherwise, the exception will be processed normally upon exit from this method.
        """
        pass


class SessionClosingContextExitHandler(SessionContextExitHandler):
    """
    Session Closing Context Exit Handler.

    Defines behavior when exiting a session context. This implementation only calls the handler

    On success: close the Session with Benchling with SessionStatusUpdate.SUCCEEDED.
    If success_messages were specified, those will also be written to the Session when setting the status.

    On error: close the Session with Benchling with SessionStatusUpdate.FAILED.
    If error_messages were specified, those will also be written to the Session when setting the status.

    As a best practice, error messages are not written to the session to avoid leaking
    potentially sensitive information.
    """

    _success_messages: Optional[Iterable[SessionMessageCreate]]
    _error_messages: Optional[Iterable[SessionMessageCreate]]
    _error_processors: List[Type[SessionContextErrorProcessor]]

    def __init__(
        self,
        success_messages: Optional[Iterable[SessionMessageCreate]] = None,
        error_messages: Optional[Iterable[SessionMessageCreate]] = [
            SessionMessageCreate(_DEFAULT_APP_ERROR_MESSAGE, style=SessionMessageStyle.ERROR)
        ],
        error_processors: List[Type[SessionContextErrorProcessor]] = [AppUserFacingErrorProcessor],
    ):
        """
        Init Session Closing Context Exit Handler.

        Specify an ordered list of SessionContextErrorProcessor types to error_processors for custom
        handling of specific exception types. Processors earlier in the list are matched first.
        """
        self._success_messages = success_messages
        self._error_messages = error_messages
        self._error_processors = error_processors

    def on_success(self, context: SessionContextManager[AppType]) -> bool:
        """
        Close Active Session on Success.

        A SessionSuccessExitHandler which will close an active session when the wrapping session
        context exits.

        Sets the status as SessionUpdateStatus.SUCCEEDED and will set the message to the specified
        text, if provided, with a SessionMessageStyle.SUCCESS.

        Generally prefer apps to manually close_session() with more informative success
        messages, but this provides a fallback in case the context exits without error first.
        """
        active_session = context.active_session()
        if active_session:
            sdk_logger.debug(
                "Exiting session context, automatically closing session ID %s as %s",
                active_session.id,
                SessionUpdateStatus.SUCCEEDED,
            )
            if self._success_messages:
                message_creates = _ordered_messages(self._success_messages)
                context.close_session(SessionUpdateStatus.SUCCEEDED, messages=message_creates)
            else:
                context.close_session(SessionUpdateStatus.SUCCEEDED)
        else:
            sdk_logger.debug("Exiting session context, no active session present")
        return True

    def on_error(
        self,
        context: SessionContextManager[AppType],
        exc_type: Type[BaseException],
        exc_value: BaseException,
        exc_traceback: TracebackType,
    ) -> bool:
        """
        Close Active Session on Error.

        A SessionErrorExitHandler which will close an active session when the wrapping session
        context exits with any type of Exception.

        Sets the status as SessionUpdateStatus.FAILED and will set the message to the specified
        text, if provided, with a SessionMessageStyle.ERROR.

        If an exception is supplied, and the method wishes to suppress the exception
        (i.e., prevent it from being propagated), it should return a True value.
        Otherwise, the exception will be processed normally upon exit from this method.
        """
        active_session = context.active_session()
        if active_session:
            optional_error_processor = self._error_processor_type(exc_type)
            # Pluggable specific error handling
            if optional_error_processor:
                sdk_logger.debug("Exiting session context with error, matched handler for %s", str(exc_type))
                return optional_error_processor.process_error(context, exc_type, exc_value, exc_traceback)
            # Fallback to general error handling
            sdk_logger.debug(
                "Exiting session context with error, automatically closing session ID %s as %s",
                active_session.id,
                SessionUpdateStatus.FAILED,
            )
            sdk_logger.debug(exc_value)
            sdk_logger.debug(exc_traceback)
            if self._error_messages:
                message_creates = _ordered_messages(self._error_messages)
                context.close_session(SessionUpdateStatus.FAILED, messages=message_creates)
            else:
                context.close_session(SessionUpdateStatus.FAILED)
        else:
            sdk_logger.debug("Exiting session context, no active session present")
        return False

    def _error_processor_type(
        self, exc_type: Type[BaseException]
    ) -> Optional[Type[SessionContextErrorProcessor]]:
        for processor in self._error_processors:
            for error_type in processor.handles():
                if issubclass(exc_type, error_type):
                    return processor
        return None


def create_session_provider(app: AppType, label: str, timeout_seconds: int) -> SessionProvider:
    """
    Create Session Provider.

    Create a SessionProvider that will create a new session with the specified app. This is the
    preferred way of working with sessions for most apps.
    """

    def _new_session() -> Session:
        session_create = SessionCreate(app_id=app.id, label=label, timeout_seconds=timeout_seconds)
        return app.benchling.v2.alpha.apps.create_session(session_create)

    return _new_session


def existing_session_provider(app: AppType, session_id: str) -> SessionProvider:
    """
    Existing Session Provider.

    Create a SessionProvider that will fetch the existing session by ID using the app's Benchling instance.
    This might be used in cases like distributed apps which may be sharing a session and passing a
    reference to the handle (session ID).
    """

    def _existing_session() -> Session:
        session = app.benchling.v2.alpha.apps.get_session_by_id(session_id)
        if session.status != SessionStatus.RUNNING:
            raise SessionClosedError(
                f"Cannot continue session with ID {session_id} with status {session.status}"
            )
        return session

    return _existing_session


def _ordered_messages(messages: Iterable[SessionMessageCreate]) -> List[SessionMessageCreate]:
    """Coerce messages into an ordered list."""
    return list(messages)


class SessionContextManager(AbstractContextManager, Generic[AppType]):
    """
    Manage Benchling App Session.

    On init, will invoke SessionProvider to get a session accordingly. When exiting the session context,
    will invoke error_exit_handler if an exception is encountered. Otherwise, invokes the
    success_exit_handler.
    """

    _app: AppType
    _session_provider: SessionProvider
    _context_enter_handler: Optional[SessionContextEnterHandler[AppType]]
    _context_exit_handler: SessionContextExitHandler[AppType]
    _session: Optional[Session]
    _attached_canvas_id: Optional[str]

    def __init__(
        self,
        app: AppType,
        session_provider: SessionProvider,
        context_enter_handler: Optional[SessionContextEnterHandler[AppType]] = None,
        context_exit_handler: Optional[SessionContextExitHandler[AppType]] = None,
    ):
        """
        Initialize SessionContextManager.

        Prefer new_session_context() or continue_session_context() over initializing this directly
        unless it's necessary to extend this class.
        """
        self._app = app
        self._session_provider = session_provider
        self._context_enter_handler = context_enter_handler
        self._context_exit_handler = (
            context_exit_handler if context_exit_handler is not None else SessionClosingContextExitHandler()
        )
        self._session = None
        self._attached_canvas_id = None

    def __enter__(self):
        self._session = self._session_provider()
        if self._context_enter_handler:
            self._context_enter_handler.on_enter(self)
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        exc_traceback: Optional[TracebackType],
    ) -> bool:
        if exc_type:
            # Appease MyPy
            assert exc_value is not None
            assert exc_traceback is not None
            return self._context_exit_handler.on_error(self, exc_type, exc_value, exc_traceback)
        return self._context_exit_handler.on_success(self)

    @property
    def app(self) -> AppType:
        """Return the app for the session."""
        return self._app

    def write_strings(
        self, contents: Union[str, Iterable[str]], style: Union[SessionMessageStyle, Unset] = UNSET
    ) -> None:
        """
        Write Session Messages from string contents.

        Shorthand for writing session messages without creating a SessionMessageCreate instance.

        Write one or more messages to app's session from the specified contents string(s). If passed an iterable,
        each element will create its own session message. If style is specified, it will be applied to all
        messages.

        For more granular control, use write_messages().

        Requires an active session which is unclosed.
        """
        if isinstance(contents, str):
            messages_to_create = [SessionMessageCreate(contents, style=style)]
        else:
            messages_to_create = [SessionMessageCreate(text, style=style) for text in contents]
        session_update = SessionUpdate(messages=messages_to_create)
        self._update_session(session_update)

    def write_messages(self, messages: Iterable[SessionMessageCreate]) -> None:
        """
        Write Session Messages.

        Write one or more messages to app's session. Requires an active session which is unclosed.
        """
        session_update = SessionUpdate(messages=_ordered_messages(messages))
        self._update_session(session_update)

    def add_timeout_seconds(self, seconds_to_add: int) -> None:
        """
        Add Session Timeout Seconds.

        Add seconds to the session's timeout in Benchling. Requires an active session which is unclosed.
        """
        if seconds_to_add < 1:
            raise InvalidSessionTimeoutError("The session timeout must be a positive integer in seconds.")
        self._require_session()
        # Appease MyPy
        assert self._session is not None
        new_timeout = self._session.timeout_seconds + seconds_to_add
        session_update = SessionUpdate(timeout_seconds=new_timeout)
        self._update_session(session_update)

    def set_timeout_seconds(self, timeout_seconds: int) -> None:
        """
        Set Session Timeout.

        Sets the session's timeout in Benchling. Requires an active session which is unclosed.

        Timeouts may only be increased, up to the Benchling allowed maximum.
        """
        self._require_session()
        # Appease MyPy
        assert self._session is not None
        if timeout_seconds < self._session.timeout_seconds:
            raise InvalidSessionTimeoutError(
                f"The session timeout must be a positive integer in seconds larger than the "
                f"existing timeout ({self._session.timeout_seconds} seconds)"
            )
        session_update = SessionUpdate(timeout_seconds=timeout_seconds)
        self._update_session(session_update)

    def close_session(
        self, status: SessionUpdateStatus, messages: Optional[Iterable[SessionMessageCreate]] = None
    ):
        """
        Close Session.

        Closes the session with Benchling on the server. This MUST be the last call in the session
        context.

        This will close the session. Subsequent attempts to perform session operations
        may raise SessionContextClosedError.

        Do not continue performing operations in the session context after calling close_session().
        """
        self._require_session()
        messages_or_unset: Union[List[SessionMessageCreate], Unset] = (
            _ordered_messages(messages) if messages is not None else UNSET
        )
        session_update = SessionUpdate(status=status, messages=messages_or_unset)
        self._update_session(session_update)
        self._session = None

    def _update_session(self, session_update: SessionUpdate) -> None:
        self._require_session()
        active_session = self.active_session()
        # Appease MyPy, which isn't aware of how _require_session() asserts this isn't none
        assert active_session is not None
        self._session = self._app.benchling.v2.alpha.apps.update_session(active_session.id, session_update)

    def active_session(self) -> Optional[Session]:
        """
        Active Session.

        Return an active Session held by the session context. Return None if the context does not have
        an active Session.
        """
        return self._session

    def has_active_session(self) -> bool:
        """
        Has Active Session.

        Return True if the active Session with Benchling has not been closed by the session context.
        """
        return self._session is not None

    def attach_canvas(self, canvas_id: str) -> None:
        """
        Attach Canvas.

        Updates the specified canvas_id with the active session_id,
        causing session information to display on the specified canvas.
        """
        self._require_session()
        active_session = self.active_session()
        # Appease MyPy, which isn't aware of how _require_session() asserts this isn't none
        assert active_session is not None
        # TODO BNCH-57234 we can't update canvas without setting blocks and featureId
        canvas = self.app.benchling.v2.beta.apps.get_canvas(canvas_id)
        canvas_update = CanvasUpdate(
            session_id=active_session.id, blocks=canvas.blocks, feature_id=canvas.feature_id
        )
        updated_canvas = self.app.benchling.v2.beta.apps.update_canvas(canvas_id, canvas_update)
        sdk_logger.debug(
            "Attached session context with session id %s to canvas id %s",
            active_session.id,
            updated_canvas.id,
        )
        self._attached_canvas_id = updated_canvas.id

    def detach_canvas(self) -> None:
        """
        Detach Canvas.

        Updates the attached canvas in the context to remove the session_id. This will cause the canvas to cease
        displaying session information and messages.

        Requires that attach_canvas() was called previously, or an error will be raised.
        """
        if self._attached_canvas_id:
            # TODO BNCH-57234 we can't update canvas without setting blocks and featureId
            canvas = self.app.benchling.v2.beta.apps.get_canvas(self._attached_canvas_id)
            canvas_update = CanvasUpdate(session_id=None, blocks=canvas.blocks, feature_id=canvas.feature_id)
            updated_canvas = self.app.benchling.v2.beta.apps.update_canvas(
                self._attached_canvas_id, canvas_update
            )
            self._attached_canvas_id = None
            sdk_logger.debug("Detached session context from canvas id %s", updated_canvas.id)
        else:
            raise MissingAttachedCanvasError("The session context does not have an attached canvas to detach")

    def _require_session(self):
        """Raise SessionContextClosedError if a context operation requires an active session."""
        if not self.has_active_session():
            raise SessionContextClosedError("The app session in the context has already been closed")


def new_session_context(
    app: AppType,
    label: str,
    timeout_seconds: int,
    context_enter_handler: Optional[SessionContextEnterHandler] = None,
    context_exit_handler: Optional[SessionContextExitHandler] = None,
) -> SessionContextManager[AppType]:
    """
    Create New Session Context.

    Create a context manager that will provision a new app Session with Benchling.
    """
    return SessionContextManager(
        app,
        create_session_provider(app, label, timeout_seconds),
        context_enter_handler,
        context_exit_handler,
    )


def continue_session_context(
    app: AppType,
    session_id: str,
    context_enter_handler: Optional[SessionContextEnterHandler] = None,
    context_exit_handler: Optional[SessionContextExitHandler] = None,
) -> SessionContextManager[AppType]:
    """
    Continue Session Context.

    Create a context manager that will fetch an existing Session from Benchling and create a context with it.
    """
    return SessionContextManager(
        app,
        existing_session_provider(app, session_id),
        context_enter_handler,
        context_exit_handler,
    )


def ref(reference: _ReferencedSessionLinkType) -> str:
    """
    Ref.

    Helper method for easily serializing a referenced object into a string embeddable in SessionMessageCreate
    content.

    Example:
        dna_sequence = benchling.dna_sequences.get_by_id("seq_1234")
        SessionMessageCreate(f"This is my DNA sequence {ref(dna_sequence)} for analysis"
    """
    # Not sure {} are possible in Benchling IDs, but the spec says we're escaping
    unescape_id = reference.id
    escaped_id = unescape_id.replace("{", "\\{").replace("}", "\\}")
    return f"{{id:{escaped_id}}}"
