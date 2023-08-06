import importlib.metadata
try:
    __version__ = importlib.metadata.version(__name__ or __package__)
except Exception:
    __version__ = "0.0.0"
