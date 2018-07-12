### UWG overview (latent heat centric for now)

- problem is that the moisture conditions of of the canyon is not informed by any vegetative evapotranspiration, bodies of water, or collected stagnant water.

- UCM.sensHeat function of heat flux from surfaces, waste heat from building
- which feeds into UBL model, which calculates heat difference between rural and canyon to update epw file  

- buildings do have a complete account of latent advHeat
- for infiltration, ventilation, calculated by volumetric flow minimums set in DOE references, and humidity difference between the modelled urban canyon, and the program type setpoints




- for horizontal surfaces (roof, mass, road):

- element.lat = soilLat + vegLat
- soilLat
    - based on waterStorage variable which is thickness of water Film
    - which is hardcoded as a global parameter, and then increased depth based on surface temperature, humidity, precipitation
    - currently this is zero
- vegLat
    - fraction of surface covered in grass or vegetation has fraction of absorbed solar radiation converted to latent heat based on lat heat fraction entered by user
- this then gets added to total surface flux:
  - self.flux = -self.sens + self.solAbs + self.infra - self.lat # (W m-2)

- vertical walls no latent heat considered
