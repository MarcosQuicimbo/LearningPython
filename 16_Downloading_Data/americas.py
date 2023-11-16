from pygal_maps_world import World

wm = World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['CA', 'MX', 'US'])
wm.add('Central America', ['BZ', 'CR', 'GT', 'HN', 'NI', 'PA', 'SV'])
wm.add('South America', ['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'GF', 'GY', 'PE', 'PY', 'SR', 'UY', 'VE'])

wm.render_to_file('americas.svg')
