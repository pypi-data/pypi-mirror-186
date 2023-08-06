from .import_utils import require
from typing import Dict, Any, List
from firecore.logging import get_logger
import functools

logger = get_logger(__name__)

KEY_CALL = '_call'
KEY_PARTIAL = '_partial'


def resolve(cfg: Any):
    """
    _0, _1 should be args
    _call should be require name
    others are kwargs
    """

    if isinstance(cfg, dict):
        if KEY_CALL in cfg:
            return _resolve_object(cfg)
        elif KEY_PARTIAL in cfg:
            return _resolve_partial(cfg)
        else:
            return _resolve_dict(cfg)
    elif isinstance(cfg, list):
        return _resolve_list(cfg)
    else:
        return cfg


def _resolve_dict(cfg: Dict[str, Any]) -> Dict[str, Any]:
    return {k: resolve(v) for k, v in cfg.items()}


def _resolve_object(cfg: Dict[str, Any]) -> Any:
    call_name = cfg[KEY_CALL]
    args, kwargs = _resolve_args_kwargs(KEY_CALL, cfg)
    return require(call_name)(*args, **kwargs)


def _resolve_partial(cfg: Dict[str, Any]) -> functools.partial:
    call_name = cfg[KEY_PARTIAL]
    args, kwargs = _resolve_args_kwargs(KEY_PARTIAL, cfg)
    return functools.partial(require(call_name), *args, **kwargs)


def _resolve_list(cfg: List[Any]) -> List[Any]:
    return [resolve(x) for x in cfg]


def _resolve_args_kwargs(key: str, cfg: Dict[str, Any]):
    call_name = cfg[key]

    args = {}
    arg_idx = 0
    while True:
        arg_name = '_{}'.format(arg_idx)
        if arg_name in cfg:
            args[arg_name] = cfg[arg_name]
            arg_idx += 1
        else:
            break

    kwargs = {k: v for k, v in cfg.items() if k != key and k not in args}

    logger.debug(
        'Start resolving object',
        name=call_name,
        args=list(args.values()), kwargs=kwargs
    )
    args_resolved = _resolve_list(args.values())
    kwargs_resolved = _resolve_dict(kwargs)
    return args_resolved, kwargs_resolved
