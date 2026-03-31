import os
import platform

class HHaiSConfig:
    # 1. Hardware Detection
    IS_JETSON = os.path.exists("/etc/nv_tegra_release")
    PROCESSOR = platform.processor()
    
    # 2. Performance Profiles
    if IS_JETSON:
        # JetPack 6.2 Optimized Mode (67 TOPS)
        COMPUTE_MODE = "NVIDIA_CUDA_ORIN"
        DEFAULT_MODEL = "llama-3-8b-instruct" # Fast local model for PAL
        GOVERNANCE_MODEL = "llama-3-70b-instruct" # Heavy model for Socratic
    else:
        # Cloud/Laptop Dev Mode
        COMPUTE_MODE = "CPU_MOCK"
        DEFAULT_MODEL = "gpt-4o-mini"
        GOVERNANCE_MODEL = "gpt-4o"

    # 3. Governance Settings
    INTERRUPT_REQUIRED = True
    MAX_DEBATE_STEPS = 5

config = HHaiSConfig()
print(f"--- HARDWARE HANDSHAKE: Running on {config.COMPUTE_MODE} ---")
