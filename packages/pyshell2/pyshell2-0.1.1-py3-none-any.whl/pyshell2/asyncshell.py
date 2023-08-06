import asyncio
import logging
from asyncio import StreamReader, subprocess
from subprocess import CalledProcessError
from typing import List, NamedTuple, Optional

# Defaults
DEFAULT_STDOUT_LOG_LEVEL = logging.INFO
DEFAULT_STDERR_LOG_LEVEL = logging.ERROR
DEFAULT_CHECK_EXITCODE = True


class ProcessInfo(NamedTuple):
    exitcode: int
    stdout: str
    stderr: str


async def _read_stream(stream: Optional[StreamReader], loglevel: int) -> str:
    lines: List[str] = []

    if stream is not None:
        while bdata := await stream.readline():
            line = bdata.decode().rstrip("\n")  # Decode and remove trailing newline

            lines.append(line)
            logging.log(loglevel, line)

    return "\n".join(lines)


async def sh(
    args: List[str],
    stdout_log_level: int = DEFAULT_STDOUT_LOG_LEVEL,
    stderr_log_level: int = DEFAULT_STDERR_LOG_LEVEL,
    check_exitcode: bool = DEFAULT_CHECK_EXITCODE,
) -> ProcessInfo:
    """Runs a shell command.

    Args:
        args: Command arguments to run. Arguments containing spaces will be wrapped in
            quotes.
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
    # Wrap args containing whitespace with quotes
    args = [f'"{arg}"' if " " in arg else arg for arg in args]
    cmd = " ".join(args)

    process = await subprocess.create_subprocess_shell(
        cmd=cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    exitcode, stdout, stderr = await asyncio.gather(
        process.wait(),
        _read_stream(process.stdout, stdout_log_level),
        _read_stream(process.stderr, stderr_log_level),
    )

    if check_exitcode and exitcode != 0:
        raise CalledProcessError(exitcode, cmd, stdout, stderr)

    return ProcessInfo(exitcode, stdout, stderr)
