from __future__ import annotations

from pathlib import Path
import subprocess
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPOSITORY_ROOT / "QRCode.py"


def test_cli_writes_a_png_for_the_supplied_url(tmp_path: Path) -> None:
    output_path = tmp_path / "code.png"

    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--url",
            "https://example.invalid/hello",
            "--output",
            str(output_path),
        ],
        cwd=REPOSITORY_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stderr
    assert output_path.exists()
    assert output_path.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")


def test_cli_rejects_a_non_http_url(tmp_path: Path) -> None:
    output_path = tmp_path / "code.png"

    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--url",
            "file:///sensitive-data",
            "--output",
            str(output_path),
        ],
        cwd=REPOSITORY_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert completed.returncode != 0
    assert "http" in completed.stderr.lower()
    assert not output_path.exists()


def test_cli_does_not_overwrite_an_existing_file(tmp_path: Path) -> None:
    output_path = tmp_path / "code.png"
    output_path.write_bytes(b"original")

    completed = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--url",
            "https://example.invalid/hello",
            "--output",
            str(output_path),
        ],
        cwd=REPOSITORY_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert completed.returncode != 0
    assert "already exists" in completed.stderr.lower()
    assert output_path.read_bytes() == b"original"
