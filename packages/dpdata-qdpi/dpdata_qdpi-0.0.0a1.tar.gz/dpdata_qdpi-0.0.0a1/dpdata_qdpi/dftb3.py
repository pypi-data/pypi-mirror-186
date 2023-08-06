import os

from dpdata.driver import Driver
from ase.calculators.dftb import Dftb


@Driver.register('dftb3')
class DFTB3Driver(Driver.get_driver("ase")):
    """DFTB3 3ob driven by DFTB+."""
    def __init__(self, charge: int = 0) -> None:
        # disable OpenMP, which makes DFTB+ slower
        os.environ['OMP_NUM_THREADS'] = '1'
        slko_dir = os.path.join(os.path.dirname(__file__), '3ob', 'skfiles')
        calc = Dftb(Hamiltonian_='DFTB',
            Hamiltonian_SCC='Yes',
            # enable DFTB3
            Hamiltonian_ThirdOrderFull='Yes',
            Hamiltonian_HubbardDerivs_='',
            # from DOI: 10.1021/ct300849w
            Hamiltonian_HubbardDerivs_H=-0.1857,
            Hamiltonian_HubbardDerivs_N=-0.1535,
            Hamiltonian_HubbardDerivs_O=-0.1575,
            Hamiltonian_HubbardDerivs_C=-0.1492,
            Hamiltonian_HCorrection_='',
            Hamiltonian_HCorrection_Damping_='',
            Hamiltonian_HCorrection_Damping_Exponent=4.0,
            Hamiltonian_charge=charge,
            Hamiltonian_MaxSCCIterations=200,
            slako_dir=os.path.join(slko_dir, ''),
            Hamiltonian_Solver='MAGMA{}',
        )
        super().__init__(calc)
