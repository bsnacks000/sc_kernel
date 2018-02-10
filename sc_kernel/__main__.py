from ipykernel.kernelapp import IPKernelApp
from .kernel import SuperColliderKernel

IPKernelApp.launch_instance(kernel_class=SuperColliderKernel)
