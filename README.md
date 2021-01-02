# Unveiling GPU Vulnerabilities: Comparing and Combining Beam, Fault Simulation, and Profiling

## About the data
This repository contains almost all data presented in the paper. 
In the following section there is a description for each Jupyter
noteboot with the data.
Radiation data is normalized to protect NVIDIA sensitive data. 
So, all data relative to Beam experiments cannot be revelead and 
are normalized by the smallest value for each device 
(Kepler and Volta).

## Data used in the paper

The data is divided by device.
1. Kepler - Tesla K20
    - Profiler data:
    - Benchmark fault injection:
    - Profiling:
    - Prediction:
2. Volta - Tesla V100
    - Profiler data:
    - Benchmark fault injection:
    - Profiling:
    - Prediction:

### Final result comparing radiation vs prediction

- Kepler - Tesla K20
![](figures/prediction_kepler.svg)

- Volta - Tesla V100
![](figures/prediction_volta.svg)


## Abstract
Graphics Processing Units (GPUs) have moved from
being dedicated devices for multimedia and gaming applications
to general-purpose accelerators employed in High-Performance
Computing (HPC) and safety-critical applications such as au-
tonomous vehicles. This market shift led to a burst in the GPU’s
computing capabilities and efficiency, significant improvements in
the programming frameworks and performance evaluation tools,
and a sudden concern about their hardware reliability.
In this paper, we compare and combine high-energy neutron
beam experiments, that account for more than 13 million years
of natural terrestrial exposure, extensive architectural-level fault
simulation, requiring more than 350 GPU hours (using SASSIFI
and NVBitFI), and detailed application-level profiling. Our main
goal is to answer one of the fundamental open questions in
GPU reliability evaluation: whether fault simulation provides
representative results and can be used to predict the FIT rates
of codes running on GPUs. We show that, in most cases,
fault simulation FIT prediction for SDCs is sufficiently close
(differences lower than 5x) to the experimentally measured FIT
rates. In our study we also analyze the reliability of the main
GPUs function units (including mixed-precision and tensor core),
we find out that the way that GPU resources are instantiated
plays a critical role in the overall system reliability, and that
faults outside the functional units generate most of the DUEs.






## Citing

```bibtex
@INPROCEEDINGS{ipdps2021,
    author={Fernando Fernandes dos Santos and 
            Siva Kumar Sastry Hari and 
            Pedro Martins Basso and
            Luigi Carro and Paolo Rech},
    booktitle={35th IEEE International Parallel & 
            Distributed Processing Symposium {IPDPS}},
    title={Unveiling GPU Vulnerabilities: 
    Comparing and Combining Beam, Fault Simulation, and Profiling},
    year={2021},
    month={May}
}
```