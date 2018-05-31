from honeybee.room import Room
from honeybee.radiance.material.glass import Glass
from honeybee.radiance.sky.certainIlluminance import CertainIlluminanceLevel
from honeybee.radiance.recipe.pointintime.gridbased import GridBased

# create a test room
room = Room(origin=(0, 0, 3.2), width=4.2, depth=6, height=3.2,
            rotation_angle=45)

# add fenestration
#  # add a window to the back wall
room.add_fenestration_surface(wall_name='back', width=2, height=2, sill_height=0.7)

# add another window with custom material. This time to the right wall
glass_60 = Glass.by_single_trans_value('tvis_0.6', 0.6)
room.add_fenestration_surface('right', 4, 1.5, 1.2, radiance_material=glass_60)

# run a grid-based analysis for this room
# generate the sky
sky = CertainIlluminanceLevel(illuminance_value=2000)

# Swap this and try and get from open_mesh
# generate grid of test points
test_points = room.generate_test_points(grid_size=0.5, height=0.75)

# put the recipe together
rp = GridBased(sky=sky, point_groups=(test_points,), simulation_type=0, hb_objects=(room,))

# write and run the analysis
rp.write_to_file(target_folder=r'c:\ladybug', project_name='room')
rp.run(debug=False)

results = rp.results()
