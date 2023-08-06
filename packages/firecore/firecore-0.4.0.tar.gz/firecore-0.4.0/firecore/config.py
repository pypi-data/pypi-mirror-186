from rjsonnet import evaluate_file, evaluate_snippet
import json
from typing import Dict, Any, overload, Optional, Union, List, Callable, Tuple
from .logging import get_logger


logger = get_logger(__name__)

ImportCallback = Callable[[str, str], Tuple[str, Optional[str]]]


@overload
def from_file(
    filename: str,
    jpathdir: Optional[Union[str, List[str]]] = None,
    max_stack: int = 500,
    gc_min_objects: int = 1000,
    gc_growth_trigger: float = 2.0,
    ext_vars: Dict[str, str] = {},
    ext_codes: Dict[str, str] = {},
    tla_vars: Dict[str, str] = {},
    tla_codes: Dict[str, str] = {},
    max_trace: int = 20,
    import_callback: Optional[ImportCallback] = None,
    native_callbacks: Dict[str, Tuple[str, Callable]] = {},
) -> Dict[str, Any]: ...


def from_file(filename: str, **kwargs) -> Dict[str, Any]:
    logger.debug('eval file', filename=filename, kwargs=kwargs)
    json_str = evaluate_file(filename, **kwargs)
    config = json.loads(json_str)
    return config


@overload
def from_snippet(
    snippet: str,
    filename: str = "snippet.jsonnet",
    jpathdir: Optional[Union[str, List[str]]] = None,
    max_stack: int = 500,
    gc_min_objects: int = 1000,
    gc_growth_trigger: float = 2.0,
    ext_vars: Dict[str, str] = {},
    ext_codes: Dict[str, str] = {},
    tla_vars: Dict[str, str] = {},
    tla_codes: Dict[str, str] = {},
    max_trace: int = 20,
    import_callback: Optional[ImportCallback] = None,
    native_callbacks: Dict[str, Tuple[str, Callable]] = {},
) -> Dict[str, Any]: ...


def from_snippet(snippet: str, filename: str = 'snippet.jsonnet', **kwargs) -> Dict[str, Any]:
    logger.debug('eval snippet', filename=filename, kwargs=kwargs)
    json_str = evaluate_snippet(filename, snippet, **kwargs)
    config = json.loads(json_str)
    return config
