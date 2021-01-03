# Metric names for Kepler and Volta
METRIC_NAMES = {
    # Double arithmetic
    "flop_count_dp_fma": "DFMA", "flop_count_dp_mul": "DMUL", "flop_count_dp_add": "DADD",
    # Single arithmetic
    "flop_count_sp_add": "FADD", "flop_count_sp_mul": "FMUL", "flop_count_sp_fma": "FFMA",
    "flop_count_sp_special": "FSPC",
    # # Half arithmetic
    "flop_count_hp_add": "HADD", "flop_count_hp_mul": "HMUL", "flop_count_hp_fma": "HFMA",
    # LD/ST, IF, and INT
    "inst_compute_ld_st": "LDST", "inst_control": "IF",
    # Communication, MISC, and conversion
    "inst_inter_thread_communication": "THCOMM", "inst_misc": "MISC", "inst_bit_convert": "BITCONV",
    # Atomic functions
    "atomic_transactions": "ATOMIC",
    # GPR
    "GPR": "GPR",
    # Tensor
    "tensor_count": "MMA",
    # Int
    "inst_integer": "INT"
}

# Register BIT size
REGISTER_BIT_SIZE = 32
# SETUP INFORMATION ABOUT KEPLER AND VOLTA
# Volta
# board: TITAN V number_sms: 80 shared_mem: 98304 l2_size: 4718592
# The header says 96KB but it is 48KB
VOLTA_SM = 80
VOLTA_RF_PER_THREAD = 256
VOLTA_MAX_WARPS_SM = 64
VOLTA_THREAD_PER_WARP = 32
VOLTA_RF_PER_SM = 65536
VOLTA_RF_GPU = VOLTA_SM * VOLTA_RF_PER_SM
VOLTA_SHARED_STATIC_PER_SM = 49152
VOLTA_SHARED_DYNAMIC_PER_SM = 49152
VOLTA_SHARED_GPU = VOLTA_SM * VOLTA_SHARED_STATIC_PER_SM
VOLTA_RF_BIT_SIZE = REGISTER_BIT_SIZE * VOLTA_RF_GPU
VOLTA_SHARED_BIT_SIZE = VOLTA_SHARED_GPU * 8

# K20
# board: Tesla K20c number_sms: 13 shared_mem: 49152
KEPLER_SM = 13
KEPLER_RF_PER_THREAD = 256
KEPLER_MAX_WARPS_SM = 64
KEPLER_THREAD_PER_WARP = 32
KEPLER_RF_PER_SM = 65536
KEPLER_RF_GPU = KEPLER_SM * KEPLER_RF_PER_SM
KEPLER_SHARED_STATIC_PER_SM = 49152
KEPLER_SHARED_DYNAMIC_PER_SM = 16384
KEPLER_SHARED_GPU = KEPLER_SM * KEPLER_SHARED_STATIC_PER_SM
KEPLER_RF_BIT_SIZE = REGISTER_BIT_SIZE * KEPLER_RF_GPU
KEPLER_SHARED_BIT_SIZE = KEPLER_SHARED_GPU * 8

STANDARD_NAMES_VOLTA = {
    'hhotspot': "HHOTSPOT",
    'fhotspot': "FHOTSPOT",
    'dhotspot': "DHOTSPOT",

    "hlava": "HLAVA",
    "flava": "FLAVA",
    "dlava": "DLAVA",

    "hmxm": "HMXM",
    "fmxm": "FMXM",
    "dmxm": "DMXM",

    'hgemm_cublas_notensor': "HGEMM",
    'fgemm_cublas_notensor': "FGEMM",
    'dgemm_cublas': "DGEMM",

    "hgemm-mma": "HGEMM-MMA",
    "fgemm-mma": "FGEMM-MMA",

    "hdarknet_v3": "HYOLOV3",
    "fdarknet_v3": "FYOLOV3",
}

STANDARD_NAMES_KEPLER = {
    # Kepler
    "hotspot": "FHOTSPOT",
    "lava_mp": "FLAVA",
    "mxm": "FMXM",
    "lud": "FLUD",
    "gaussian": "FGAUSSIAN",
    "accl": "CCL",
    "bfs": "BFS",
    "nw": "NW",
    "mergesort": "MERGESORT",
    "quicksort": "QUICKSORT",
    "gemm_tensorcores": "FGEMM",
    "darknet_v3": "FYOLOV3",
}
