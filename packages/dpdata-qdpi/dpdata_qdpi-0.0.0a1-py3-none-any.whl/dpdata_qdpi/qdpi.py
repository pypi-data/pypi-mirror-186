from dpdata.driver import Driver


@Driver.register('qdpi')
class QDPiDriver(Driver.get_driver("hybrid")):
    """QDPi."""
    def __init__(self, model: str, charge: int = 0, backend="sqm") -> None:
        if backend == 'sqm':
            dftb3 = {"type": "sqm", "qm_theory": "dftb3", "charge": charge}
        elif backend == 'dftb+':
            dftb3 = {"type": "dftb3", "charge": charge}
        super().__init__([
            dftb3,
            {'type':'dp', "dp": model},
            ])
