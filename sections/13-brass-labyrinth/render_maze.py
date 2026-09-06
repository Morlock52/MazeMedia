"""Original Maze Media architectural emblem; Blender 4.4, no external models."""
import bpy, math, pathlib
from mathutils import Vector
out = pathlib.Path(__file__).resolve().parent
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
def material(name,color,metal=0,rough=.4,emission=0):
 m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
 p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*color,1);p.inputs['Metallic'].default_value=metal;p.inputs['Roughness'].default_value=rough
 if emission:p.inputs['Emission Color'].default_value=(*color,1);p.inputs['Emission Strength'].default_value=emission
 return m
iron=material('Charcoal iron',(.035,.043,.04),.7,.32)
brass=material('Aged brass',(.64,.39,.135),.8,.26)
light=material('Amber path',(.9,.42,.08),.4,.3,2)
def cube(name,loc,scale,mat,bevel=.055):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=scale;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(mat)
 b=o.modifiers.new('Machined edge','BEVEL');b.width=bevel;b.segments=3;o.modifiers.new('Weighted normals','WEIGHTED_NORMAL');return o
def rail(a,b,mat=brass,z=.32,w=.15):
 mid=((a[0]+b[0])/2,(a[1]+b[1])/2,z);length=math.dist(a,b)
 o=cube('Labyrinth rail',mid,(length+w,w,.32),mat);o.rotation_euler.z=math.atan2(b[1]-a[1],b[0]-a[0]);return o
cube('Monolithic foundation',(0,0,-.2),(7.5,7.5,.45),iron,.14)
# Concentric passages, openings alternate; an M forms the navigable heart.
for r in [3.25,2.65,2.05]:
 points=[(-r,-r),(-r,r),(r,r),(r,-r),(.55,-r)]
 for a,b in zip(points,points[1:]):rail(a,b,z=.23)
 rail((-r,-r),(-.55,-r),z=.23)
for a,b in zip([(-1.4,-1.4),(-1.4,1.35),(0,-.25),(1.4,1.35),(1.4,-1.4)],[(-1.4,1.35),(0,-.25),(1.4,1.35),(1.4,-1.4)]):rail(a,b,z=.43,w=.23)
rail((0,-3.6),(0,-1.9),light,z=.13,w=.07)
cube('Endless dark floor',(0,0,-.5),(200,200,.1),material('Background',(.018,.023,.022),.3,.55))
def area(name,loc,power,color,size):
 bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;o.name=name;o.data.energy=power;o.data.color=color;o.data.shape='DISK';o.data.size=size;o.rotation_euler=(Vector((0,0,0))-o.location).to_track_quat('-Z','Y').to_euler()
area('Warm key',(1,-4,10),1600,(1,.73,.39),7);area('Cool mineral rim',(-5,3,6),1250,(.43,.66,.65),6)
bpy.ops.object.camera_add(location=(8,-10,15));cam=bpy.context.object;cam.rotation_euler=(Vector((0,0,0))-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=12;bpy.context.scene.camera=cam
s=bpy.context.scene;s.render.engine='CYCLES';s.cycles.samples=24;s.cycles.use_denoising=True;s.world.color=(.06,.06,.06);s.render.image_settings.file_format='PNG';s.view_settings.view_transform='AgX';s.render.resolution_percentage=100
s.render.resolution_x=1024;s.render.resolution_y=1024;s.render.filepath=str(out/'maze-emblem.png');bpy.ops.wm.save_as_mainfile(filepath=str(out/'MorlocksMaze.blend'));bpy.ops.render.render(write_still=True)
s.render.resolution_x=1920;s.render.resolution_y=800;cam.data.ortho_scale=23;cam.data.shift_x=-.23;s.render.filepath=str(out/'maze-architecture.png');bpy.ops.render.render(write_still=True)
