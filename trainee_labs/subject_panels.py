from edc_lab import RequisitionPanel, LabProfile
from edc_lab.site_labs import site_labs
from .aliquot_types import wb
from .processing_profiles import viral_load_processing



subject_lab_profile = LabProfile(
    name='trainee_subject_lab_profile',
    requisition_model='trainee_subject.subjectrequisition')


viral_load_panel = RequisitionPanel(
    name='viral_load',
    verbose_name='Viral Load',
    aliquot_type=wb,
    processing_profile=viral_load_processing)




subject_lab_profile.add_panel(viral_load_panel)
site_labs.register(subject_lab_profile)