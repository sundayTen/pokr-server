from fastapi_camelcase import CamelModel


class TemplateCreateRequest(CamelModel):
    snapshot: dict


class TemplateUpdateRequest(CamelModel):
    snapshot: dict
