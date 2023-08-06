from torch.backends import cudnn
import torch
from firecore.logging import get_logger

logger = get_logger(__name__)


def setup_cudnn_benchmark():
    if torch.cuda.is_available() and cudnn.is_available():
        cudnn.benchmark = True
        logger.info('setup cudnn.benchmark', flag=cudnn.benchmark)
    else:
        logger.warning('cudnn is not availiable, please check your pytorch')
