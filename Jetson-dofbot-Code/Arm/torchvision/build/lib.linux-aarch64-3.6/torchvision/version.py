__version__ = '0.7.0a0+78ed10c'
git_version = '78ed10cc51067f1a6bac9352831ef37a3f842784'
from torchvision.extension import _check_cuda_version
if _check_cuda_version() > 0:
    cuda = _check_cuda_version()
