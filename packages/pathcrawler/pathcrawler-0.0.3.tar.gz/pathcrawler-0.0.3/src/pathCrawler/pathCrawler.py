from pathlib import Path

from printBuddies import clear, printInPlace


def crawl(startDir: Path | str, quiet: bool = False) -> list[Path]:
    """Recursively crawl a directory tree
    and return a list of files as pathlib.Path objects.
    :param quiet: If True, don't print information about the crawl."""
    files = []
    for path in Path(startDir).iterdir():
        if not quiet:
            printInPlace(f"Crawling {path}")
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(crawl(path))
    if not quiet:
        clear()
    return files


def getDirectorySize(startDir: Path | str) -> int:
    """Return the size of a directory tree in bytes."""
    return sum(file.stat().st_size for file in crawl(startDir, quite=True))


def formatSize(sizeBytes: int) -> str:
    """Return a string with appropriate unit suffix
    and rounded to two decimal places.
    i.e. formatSize(1572166) returns "1.57 mb" """
    if sizeBytes < 1000:
        return f"{round(sizeBytes, 2)} bytes"
    for unit in ["kb", "mb", "gb", "tb"]:
        sizeBytes /= 1000
        if sizeBytes < 1000:
            return f"{round(sizeBytes, 2)} {unit}"
