# variable declarations
transparent = True
transparency = 2
is_cube = False
glass = False
translucent = False

colliders = [
	[
		(-0.5, -0.5000, -0.5),
		( 0.5, -0.4375,  0.5)
	]
]
# vertices positions
vertex_positions = [
	[ 0.5, -0.4375,  0.5,   0.5, -0.4375, -0.5,  -0.5, -0.4375, -0.5,  -0.5, -0.4375,  0.5], # top
	[-0.5, -0.4375,  0.5,  -0.5, -0.4375, -0.5,   0.5, -0.4375, -0.5,   0.5, -0.4375,  0.5], # bottom
]
# textures coordinates
tex_coords = [
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
]
# shading values
shading_values = [
	[1.0, 1.0, 1.0, 1.0],
	[0.4, 0.4, 0.4, 0.4],
]


assert transparent == True
assert transparency == 2
assert is_cube == False
assert glass == False
assert translucent == False

assert colliders == [
	[
		(-0.5, -0.5000, -0.5),
		( 0.5, -0.4375,  0.5)
	]
        ]


assert vertex_positions == [
	[ 0.5, -0.4375,  0.5,   0.5, -0.4375, -0.5,  -0.5, -0.4375, -0.5,  -0.5, -0.4375,  0.5], # top
	[-0.5, -0.4375,  0.5,  -0.5, -0.4375, -0.5,   0.5, -0.4375, -0.5,   0.5, -0.4375,  0.5], # bottom
]

assert tex_coords == [
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
]

assert shading_values == [
	[1.0, 1.0, 1.0, 1.0],
	[0.4, 0.4, 0.4, 0.4],
]

 