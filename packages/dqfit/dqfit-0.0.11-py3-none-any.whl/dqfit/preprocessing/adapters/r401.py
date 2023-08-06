import pandas as pd

SUPPORTED_RESOURCES = [
    "Patient",
    "Procedure",
    "Condition",
    "Observation",
    # "Immunization",
    # "MedicationDispense",
    # "Claim",
    # "ClaimResponse",
    # "Coverage",
    # "Encounter", #DSFE
    # "AllergyIntolerance", getting erros on synthrea
]

CURRENT_YEAR = pd.to_datetime("today").year

def _get_subject_patient_reference(resource) -> str:
    subject = resource.get("subject")
    ref = subject.get("reference")
    ref = ref.replace("urn:uuid:","") # from synthea
    return ref

def _get_code_0(resource):
    concept = resource.get("code")
    return concept.get("coding")[0]['code']

def _get_system_0(resource):
    concept = resource.get("code")
    return concept.get("coding")[0]['system']

def get_patient_features(resource: dict) -> dict:
    assert(resource.get("resourceType") == "Patient")
    
    def _get_age_decile(resource):
        birth_year = int(resource["birthDate"][0:4]) # revisit data types
        age = CURRENT_YEAR - birth_year
        if age > 84:
            return 9
        else:
            return int(age / 10)

    def _get_ref(resource):
        ref = resource.get("id")
        return ref.replace("Patient.","")

    
    return dict(
        _ref = _get_ref(resource),
        id = resource.get("id"),
        resource_type = resource.get("resourceType"), 
        gender = resource.get("gender"),
        age_decile = _get_age_decile(resource)
    )

def get_procedure_features(resource: dict) -> dict:
    # DATE_FIELD = "performedPeriod"
    def _get_iso_date(resource: dict) -> str:
        if resource.get("performedPeriod"):
            return resource.get("performedPeriod").get("start")[0:10]
        if resource.get("performedDateTime"):
            return resource.get("performedDateTime")[0:10]
    
    return dict(
        _ref = _get_subject_patient_reference(resource),
        id = resource.get("id"),
        resource_type = resource.get("resourceType"),
        date = _get_iso_date(resource),
        code = _get_code_0(resource),
        system = _get_system_0(resource),
    )

def get_condition_features(resource: dict) -> dict:
    DATE_FIELD = "onsetDateTime"
    def _get_iso_date(resource: dict) -> str:
        return resource.get(DATE_FIELD)[0:10]
    
    return dict(
        _ref = _get_subject_patient_reference(resource),
        id = resource.get("id"),
        resource_type = resource.get("resourceType"),
        date = _get_iso_date(resource),
        code = _get_code_0(resource),
        system = _get_system_0(resource),
    )

def get_observation_features(resource: dict) -> dict:
    
    DATE_FIELD = "effectiveDateTime"
    def _get_iso_date(resource: dict) -> str:
        return resource.get(DATE_FIELD)[0:10]
    
    def _get_value(resource):
        if resource.get("valueQuantity"):
            return resource.get("valueQuantity").get("value")

    def _get_unit(resource):
        if resource.get("valueQuantity"):
            return resource.get("valueQuantity").get("unit")
    
    return dict(
        _ref = _get_subject_patient_reference(resource),
        id = resource.get("id"),
        resource_type = resource.get("resourceType"),
        date = _get_iso_date(resource),
        system = _get_system_0(resource),
        code = _get_code_0(resource),
        value = _get_value(resource),
        unit = _get_unit(resource),
    )


def get_fhir_features(resource: dict) -> dict:
    resource_type = resource['resourceType']
    if resource_type == "Patient":
        return get_patient_features(resource)
    elif resource_type == "Procedure":
        return get_procedure_features(resource)
    elif resource_type == "Condition":
        return get_condition_features(resource)
    elif resource_type == "Observation":
        return get_observation_features(resource)
    else:
        return {
            "id": resource.get('id'),
            "resource_type": resource.get('resourceType')
        }
