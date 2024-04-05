from edc_lab import Process, ProcessingProfile

from .aliquot_types import wb, pl, bc

viral_load_processing = ProcessingProfile(name='viral_load', aliquot_type=wb)
vl_pl_process = Process(aliquot_type=pl, aliquot_count=3)
vl_bc_process = Process(aliquot_type=bc, aliquot_count=1)


viral_load_processing.add_processes(vl_pl_process, vl_bc_process)