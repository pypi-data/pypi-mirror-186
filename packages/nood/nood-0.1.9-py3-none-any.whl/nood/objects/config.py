from pydantic import BaseModel


class SiteConfig(BaseModel):
    site_id: int
