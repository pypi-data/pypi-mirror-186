import os

from .log import logger

ENABLED = os.getenv('VALIDATE_SPATIAL', 'true') == 'true'
MAX_AREA_SIZE = int(os.getenv('MAX_AREA_SIZE', '5000'))


def init_gee_by_nodes(nodes: list):
    should_init = any([n.get('@type', n.get('type')) in ['Site', 'Organisation'] for n in nodes])
    if should_init and ENABLED:
        try:
            from hestia_earth.earth_engine import init_gee
        except ImportError:
            logger.error("Run `pip install hestia_earth.earth_engine` to use geospatial validation")
        return init_gee()
    return None


def is_enabled():
    try:
        from hestia_earth.earth_engine.version import VERSION
        logger.debug("Using earth_engine version %s", VERSION)
        return ENABLED
    except ImportError:
        logger.error("Run `pip install hestia_earth.earth_engine` to use geospatial validation")
        return False


def id_to_level(id: str): return id.count('.')


def fetch_data_by_coordinates(**kwargs):
    from hestia_earth.earth_engine.coordinates import run
    return run(kwargs).get('features', [])[0].get('properties')


def get_region_id(gid: str, **kwargs):
    try:
        level = id_to_level(gid)
        field = f"GID_{level}"
        id = fetch_data_by_coordinates(
            collection=f"users/hestiaplatform/gadm36_{level}",
            ee_type='vector',
            fields=field,
            **kwargs
        ).get(field)
        return None if id is None else f"GADM-{id}"
    except Exception:
        return None
