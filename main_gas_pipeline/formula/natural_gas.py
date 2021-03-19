def density_standard(components):
    """
    Natural gas density at standard temperature, kg/m3
    Parameters
    ----------
    components: list
                The list of natural gas components. Each component is an
    """


    density_standard = 0
    for component in self.components:
        density_standard += component.density_standard * component.volume_percentage * 0.01
    return density_standard