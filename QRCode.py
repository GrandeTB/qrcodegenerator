"""Generate a QR-code PNG from an explicitly supplied URL."""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import urlparse

import qrcode


def http_url(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise argparse.ArgumentTypeError("URL must be an absolute http(s) URL")
    return value


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True, type=http_url, help="URL to encode in the QR code")
    parser.add_argument("--output", required=True, type=Path, help="PNG file to create")
    return parser.parse_args()


def generate_qr_code(url: str, output_path: Path) -> None:
    qr_code = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr_code.add_data(url)
    qr_code.make(fit=True)
    image = qr_code.make_image(fill_color="black", back_color="white")
    image.save(output_path)


def main() -> None:
    arguments = parse_arguments()
    if arguments.output.exists():
        raise SystemExit(f"error: output file already exists: {arguments.output}")
    generate_qr_code(arguments.url, arguments.output)


if __name__ == "__main__":
    main()
