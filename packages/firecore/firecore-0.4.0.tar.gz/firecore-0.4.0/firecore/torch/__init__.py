from firecore.logging import get_logger

logger = get_logger(__name__)
try:
    import torch
except ImportError:
    logger.exception("please install pytorch first")
finally:
    from . import cudnn_utils
    from . import jit_utils
    from . import module_utils
    from . import optimizer_utils
