from typing import Optional
from dataclasses import dataclass

from click import ClickException


GRN_TYPE_KEY_MODEL = "m"
GRN_TYPE_KEY_SAVED_VIEW = "sv"
GRN_TYPE_KEY_DASHBOARD = "dsb"
GRN_TYPE_KEY_COLOR_PALETTE = "palette"


@dataclass
class GRNComponents:
    resource_type: str
    gluid: Optional[str] = None
    alias: Optional[str] = None


def parse_grn(grn: str) -> GRNComponents:
    components = grn.split(":")

    resource_type = components[0]
    if resource_type not in [
        GRN_TYPE_KEY_MODEL,
        GRN_TYPE_KEY_SAVED_VIEW,
        GRN_TYPE_KEY_DASHBOARD,
        GRN_TYPE_KEY_COLOR_PALETTE,
    ]:
        raise ClickException(
            f"""Invalid GRN. {resource_type} is not a valid resource type.
        The valid resource types are:
        - "{GRN_TYPE_KEY_MODEL}" for models
        - "{GRN_TYPE_KEY_SAVED_VIEW}" for saved views
        - "{GRN_TYPE_KEY_DASHBOARD}" for dashboards
        - "{GRN_TYPE_KEY_COLOR_PALETTE}" for color palettes"""
        )

    if len(components) == 2:
        return GRNComponents(
            resource_type=components[0],
            gluid=components[1],
        )
    elif len(components) == 3:
        has_gluid = components[2] != ""
        return GRNComponents(
            resource_type=components[0],
            gluid=components[1] if has_gluid else None,
            alias=components[2],
        )

    raise ClickException(
        """Invalid GRN. The GRN should be in one of these formats:
    \n <resource_type>:<gluid>
    \n <resource_type>:<gluid>:<alias>
    \n <resource_type>::<alias>
    """
    )
