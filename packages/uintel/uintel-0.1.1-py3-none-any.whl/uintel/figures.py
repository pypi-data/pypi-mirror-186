"""Make figures and plot to the Urban Intelligence style guide.

This module aims to assist in creating figures to a single style across the organisation. The colour palletes are engrained in this module and the core function is to modify the pallete to fit the need of the users figure.
"""

__all__ = ["generate_colour_palette"]

import colour

COLOUR_PALETTES = {
    "planning": {
        "monochromatic": ["#5aa33b", "#48942e", "#358520", "#207611", "#006700"],
        "divergent": ["#5aa33b", "#76b05a", "#8fbd77", "#a8ca95", "#c0d7b3", "#d9e4d2", "#f1f1f1", "#f1d4d4", "#f0b8b8", "#ec9c9d", "#e67f83", "#de6069", "#d43d51"], 
    },
    "access": {
        "monochromatic": ["#246783", "#21779a", "#1b86b2", "#1396cb", "#09a7e5", "#00b7ff"],
        "divergent": ["#246783", "#307d91", "#44929d", "#5ca8a8", "#78beb1", "#97d3bb", "#93daa7", "#9fdd8c", "#b7de6a", "#d8dc44", "#ffd416"], 
    },
    "risk": {
        "monochromatic": ["#0b2948", "#344a69", "#596d8d", "#7f93b1", "#a7bad8", "#d1e3ff"],
        "divergent": ["#0b2948", "#3b4b67", "#657187", "#9198a8", "#bfc2ca", "#eeeeee", "#fad3c1", "#ffb896", "#ff9d6b", "#fe813f", "#f86302"], 
    }
}


def generate_colour_palette(palette: str = "risk", scheme: str = "divergent", n: int = 5) -> list:
    """Generate a specific colour palette resembling a Urban Intelligence product.

    Return a list of hex strings that relate to an Urban Intelligence colour palette (planning, access or risk) for a given colour scheme (monochromatic or divergent). Colours are always returned in the order of positive to worst (in respect of what the palette is defining as a good and poor colour).

    Args:
        palette: The Urban Intelligence product to mimic the palette off.
        scheme: The colour scheme required ('divergent' or 'monochromatic').
        n: The number of unique colours required.
    
    Returns:
        A list of n hex codes relating to the requested palette and scheme.
    """

    if palette not in COLOUR_PALETTES.keys():
        raise ValueError(f"The given pallete: {palette} is not acceptable. Please choose from: {list(COLOUR_PALETTES.keys())}")
    if scheme not in COLOUR_PALETTES[palette].keys():
        raise ValueError(f"The given scheme: {scheme} is not acceptable. Please choose from: {list(COLOUR_PALETTES[palette].keys())}")
    
    default_colours = COLOUR_PALETTES[palette][scheme]
    if len(default_colours) == 0:
        raise NotImplementedError(f"Unfortunately, there is no colour scheme for the {palette} palette using a {scheme} scheme. Apologies for the inconvenience.")
    elif len(default_colours) == n:
        return default_colours
    else:
        return [color.get_hex() for color in colour.Color(default_colours[0]).range_to(colour.Color(default_colours[-1]), steps=n)]
