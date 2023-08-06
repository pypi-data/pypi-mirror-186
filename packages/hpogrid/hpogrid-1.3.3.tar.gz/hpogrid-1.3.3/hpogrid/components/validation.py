from hpogrid.core.defaults import kHPOGridMetadataFormat

def validate_job_metadata(data):
    if not isinstance(data, dict):
        return False
    return all(key in kHPOGridMetadataFormat for key in data)