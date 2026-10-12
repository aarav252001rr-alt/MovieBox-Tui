from app.providers.base import Provider

# Register a real, compatible provider adapter here once its API is verified.
# MovieBox-TUI is a terminal UI, not itself a documented HTTP API.
_provider: Provider | None = None

def get_provider() -> Provider | None:
    return _provider

def register_provider(provider: Provider) -> None:
    global _provider
    _provider = provider
