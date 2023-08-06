# dpdata_qdpi

[dpdata](https://github.com/deepmodeling/dpdata) plugin for [QDπ](https://github.com/njzjz/qdpi).

## Features

* `qdpi` driver

## Installation

```sh
pip install dpdata_qdpi[gpu]
# or for the CPU version of TensorFlow
pip install dpdata_qdpi[cpu]
```

At this time, you need to install either [AMBERTools](ambermd.org/) SQM (`sqm`) or [DFTB+](https://github.com/dftbplus/dftbplus/) (`dftb+`).

## Usage

Download the QDπ model from [njzjz/qdpi](https://github.com/njzjz/qdpi).

```py
from dpdata_qdpi import QDPiDriver

qdpi = QDPiDriver(
    model="qdpi-1.0.pb",
    charge=0,
    backend="sqm",
)
```
`backend` can be either `sqm` or `dftb+`.

Assume you have an XYZ file `ch4.xyz`

```xyz
5

C          0.92334        0.06202        0.01660
H          2.01554        0.06202        0.01660
H          0.55927        1.09164        0.03247
H          0.55927       -0.46653        0.90033
H          0.55927       -0.43903       -0.88301
```

Load the structure:

```py
from dpdata import System

ch4 = System("ch4.xyz")
```

Perform single point calculation using the QDπ model:

```py
p = ch4.predict(driver=qdpi)
print("Energies:", p['energies'][0])
print("Forces:", p['forces'][0])
```

```
Energies: -1102.0472189112793
Forces: [[-4.92853860e-05  3.71129259e-04 -1.00154387e-04]
 [ 2.07637527e-02 -1.98691092e-06 -7.85158242e-07]
 [-6.81949398e-03  1.93688568e-02  3.32209598e-04]
 [-6.96972976e-03 -1.01335356e-02  1.69318148e-02]
 [-6.92524354e-03 -9.60446352e-03 -1.71630849e-02]]
```

Or do an optimization:
```py
from dpdata.plugins.ase import ASEMinimizer

lbfgs = ASEMinimizer(
    driver=qdpi,
)
p = ch4.minimize(minimizer=lbfgs)
print("Coordinates:", p['coords'][0])
print("Energies:", p['energies'][0])
print("Forces:", p['forces'][0])
```

```
Coordinates: [[ 0.92333966  0.06202338  0.01659862]
 [ 2.0161223   0.06202041  0.0165999 ]
 [ 0.55907714  1.0921887   0.03247964]
 [ 0.559075   -0.46681303  0.9008036 ]
 [ 0.5590758  -0.43929946 -0.88349175]]
Energies: -1102.0472
Forces: [[-1.0836746e-04  9.8321143e-05 -2.5905898e-05]
 [ 6.7257555e-05  8.3519126e-06 -2.5666191e-06]
 [ 4.4526685e-05 -5.3852447e-05  1.7676884e-05]
 [-9.4877823e-06 -1.9283394e-05  2.8249622e-05]
 [ 6.0710017e-06 -3.3537217e-05 -1.7453991e-05]]
```

Read [dpdata's documentation](https://docs.deepmodeling.com/projects/dpdata) for more usage of dpdata.
