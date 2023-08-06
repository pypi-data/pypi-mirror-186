from pathlib import Path

import dpdata
import pytest
from dpdata_qdpi import QDPiDriver
from dpdata.plugins.ase import ASEMinimizer

@pytest.fixture
def ch4():
    this_dir = Path(__file__).parent
    ch4 = dpdata.System(str(this_dir / "ch4.xyz"))
    return ch4

@pytest.fixture
def qdpi():
    qdpi = QDPiDriver(
        model="qdpi-1.0.pb",
        charge=0,
        backend="sqm",
    )
    return qdpi

@pytest.mark.skip
def test_single_point(ch4, qdpi):
    # single point calculation
    p = ch4.predict(driver=qdpi)
    print("Energies:", p['energies'][0])
    print("Forces:", p['forces'][0])

@pytest.mark.skip
def test_optimization(ch4, qdpi):
    # Optimization
    lbfgs = ASEMinimizer(
        driver=qdpi,
    )
    p = ch4.minimize(minimizer=lbfgs)
    print("Coordinates:", p['coords'][0])
    print("Energies:", p['energies'][0])
    print("Forces:", p['forces'][0])
