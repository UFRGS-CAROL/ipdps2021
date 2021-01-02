# Unveiling GPU Vulnerabilities: Comparing and Combining Beam, Fault Simulation, and Profiling

## 1. Abstract
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
(differences lower than 5×) to the experimentally measured FIT
rates. In our study we also analyze the reliability of the main
GPUs function units (including mixed-precision and tensor core),
we find out that the way that GPU resources are instantiated
plays a critical role in the overall system reliability, and that
faults outside the functional units generate most of the DUEs.


## 2. Data used in the paper



## 3. Citing

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