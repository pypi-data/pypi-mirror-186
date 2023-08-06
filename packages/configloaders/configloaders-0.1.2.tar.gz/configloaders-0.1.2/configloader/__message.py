from .__log import logger

def log_loaded(loader, path):
    logger.info(f"Configuration loaded: {loader.__name__} {path}")

def log_saved(loader, path):
    logger.info(f"Configuration saved: {loader.__name__} {path}")

def log_failed(key, value, e):
    logger.info(f'Serialization failed: key="{key}" value="{value}" exception="{e}"')