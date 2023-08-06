import os
from pathlib import Path
from typing import Dict, List, Optional, Union

from pyshell2.asyncshell import (
    DEFAULT_CHECK_EXITCODE,
    DEFAULT_STDERR_LOG_LEVEL,
    DEFAULT_STDOUT_LOG_LEVEL,
    ProcessInfo,
    sh,
)

# Constants
DOCKER_USER_ME = f"{os.getuid()}:{os.getgid()}"
DOCKER_USER_ROOT = "0:0"


async def docker_sh(
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
    files = dict.fromkeys([arg for arg in args if isinstance(arg, Path)])

    volumes: Dict[Path, Path] = {}
    for i, file in enumerate(files):
        volumes[file] = Path(f"/mnt/{i}/{file.name}")

    return await docker_run(
        image=image,
        args=[
            volumes[arg].as_posix() if isinstance(arg, Path) else arg for arg in args
        ],
        detached=False,
        cleanup=True,
        user=user,
        entrypoint=entrypoint,
        volumes=volumes,
        network=network,
        stdout_log_level=stdout_log_level,
        stderr_log_level=stderr_log_level,
        check_exitcode=check_exitcode,
    )


async def docker_run(
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
    cmd = [
        "docker",
        "run",
        f"-d={str(detached).lower()}",
        f"--rm={str(cleanup).lower()}",
    ]

    if user is not None:
        cmd += ["--user", user]

    if entrypoint is not None:
        cmd += ["--entrypoint", entrypoint]

    if volumes is not None:
        for src, dst in volumes.items():
            escaped_quote = '\\"'
            mount = [
                "type=bind",
                f"{escaped_quote}src={src.resolve()}{escaped_quote}",
                f"{escaped_quote}dst={dst.resolve()}{escaped_quote}",
            ]
            cmd += ["--mount", ",".join(mount)]

    if network is not None:
        cmd += ["--network", network]

    cmd += [image, *args]
    return await sh(
        args=cmd,
        stdout_log_level=stdout_log_level,
        stderr_log_level=stderr_log_level,
        check_exitcode=check_exitcode,
    )
