import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Union

from . import asyncdocker
from .shell import (
    DEFAULT_CHECK_EXITCODE,
    DEFAULT_STDERR_LOG_LEVEL,
    DEFAULT_STDOUT_LOG_LEVEL,
    ProcessInfo,
)


def docker_sh(
    image: str,
    args: List[Union[str, Path]],
    user: Optional[str] = None,
    entrypoint: Optional[str] = None,
    network: Optional[str] = None,
    stdout_log_level: int = DEFAULT_STDOUT_LOG_LEVEL,
    stderr_log_level: int = DEFAULT_STDERR_LOG_LEVEL,
    check_exitcode: bool = DEFAULT_CHECK_EXITCODE,
) -> ProcessInfo:
    """Runs a shell command inside a docker image.

    This is a easier to use version of docker_run with some automagic features. The
    current automagic features include:
    - Automatic mounting of files and directories in the command args.

    The benefit of using this function is cleaner code and you less to think about. The
    downside is less control. If you need full functionality use the parent function
    docker_run instead.

    Args:
        args: Command arguments to run. Paths will be mounted into the container and
            the args will be replaced with the mount location. Arguments containing
            spaces will be wrapped in quotes.
        user: User to run the command as. See "--user" arg for docker run for more info.
        entrypoint: Sets the entrypoint of the image. See "--entrypoint" arg for docker
            run for more info.
        network: Network setting for the container. See "--network" arg for docker run
            for more info.
        stdout_log_level: Log level of the stdout of the shell command.
        stderr_log_level: Log level of the stderr of the shell command.
        check_exitcode: Whether to check if the exit code is zero or not. If true and
            exitcode is non-zero, a CalledProcessError will be raised.
    Returns:
        A ProcessInfo containing the exitcode, stdout, and stderr from the command.
    Raises:
        CalledProcessError: If the shell command exited with a non-zero exitcode and
            check_exitcode is true.
    """
    return asyncio.run(
        asyncdocker.docker_sh(
            image=image,
            args=args,
            user=user,
            entrypoint=entrypoint,
            network=network,
            stdout_log_level=stdout_log_level,
            stderr_log_level=stderr_log_level,
            check_exitcode=check_exitcode,
        )
    )


def docker_run(
    image: str,
    args: List[str],
    detached: bool = False,
    cleanup: bool = True,
    user: Optional[str] = None,
    entrypoint: Optional[str] = None,
    volumes: Optional[Dict[Path, Path]] = None,
    network: Optional[str] = None,
    stdout_log_level: int = DEFAULT_STDOUT_LOG_LEVEL,
    stderr_log_level: int = DEFAULT_STDERR_LOG_LEVEL,
    check_exitcode: bool = DEFAULT_CHECK_EXITCODE,
) -> ProcessInfo:
    """Runs a docker run command."""
    return asyncio.run(
        asyncdocker.docker_run(
            image=image,
            args=args,
            detached=detached,
            cleanup=cleanup,
            user=user,
            entrypoint=entrypoint,
            volumes=volumes,
            network=network,
            stdout_log_level=stdout_log_level,
            stderr_log_level=stderr_log_level,
            check_exitcode=check_exitcode,
        )
    )
