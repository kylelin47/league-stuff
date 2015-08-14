from werkzeug.contrib.cache import SimpleCache

id_cache = SimpleCache(default_timeout=60 * 60 * 24 * 7)
history_cache = SimpleCache()


def generate_cache_key(region, name):
    return region.upper() + ''.join(name.lower().split())
