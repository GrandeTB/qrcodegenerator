# QR Code Generator

A small, safe Python command-line tool that writes a PNG QR code for a URL you explicitly provide.

## Requirements

- Python 3.10 or newer

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Both arguments are required; the program has no default URL or output path.

```bash
python QRCode.py --url "https://example.com" --output "example-qr.png"
```

The URL must be an absolute `http` or `https` URL. The output path must not already exist, which prevents accidental overwrites. Generated PNG files are intentionally ignored by Git.

## Testing

```bash
python -m pytest -q
```

Tests run the CLI and verify that the requested output exists and begins with the standard PNG signature. They do not require an image decoder beyond the QR generator's own dependency.

## Security

See [SECURITY.md](SECURITY.md) for supported-version and vulnerability-reporting guidance.
