# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "FC_subd_to_nurbs",
    "author" : "Andrea Rastelli",
    "description" : "subd to nurbs delirium converter",
    "blender" : (2, 83, 0),
    "version" : (0, 0, 1),
    "location" : "Item",
    "warning" : "IN DEVELOPMENT, weirdness",
    "category" : "Mesh"
}

import bpy

from bpy.types import (
                        PropertyGroup,
                        Panel
                        )

from bpy.props import ( 
                        BoolProperty,
                        EnumProperty,
                        IntProperty,
                        FloatProperty,
                        StringProperty,
                        PointerProperty
                        )


#GLOBAL PROPS
class GLOBAL_UL_FreeCadBlender_props(PropertyGroup):
    
    ex_dir = StringProperty(name="export folder",subtype="DIR_PATH")
    fc_dir = StringProperty(name="FC37 bin path",subtype="DIR_PATH")
    fname = StringProperty(name="file name",default="filename")

#GLOBAL PANEL
class VIEW3D_PT_FreeCadBlender_tool(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"
    bl_label = "SUBD_TO_NURBS"

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj and obj.type == 'MESH' and context.mode == 'EDIT_MESH')

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        con = context.scene.FreeCadBlender_props
        layout.prop(con, "ex_dir")
        layout.prop(con, "fc_dir")
        layout.prop(con, "fname")
        layout.operator("mesh.fcb_subd_to_nurbs", text="to nurbs...almost") # OPERATOR
        
#OPERATOR 
class MESH_OT_FreeCadBlender_subd_to_nurbs(bpy.types.Operator):
    bl_idname = "mesh.fcb_subd_to_nurbs"
    bl_label = "subd_to_nurbs"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj and obj.type == 'MESH' and context.mode == 'EDIT_MESH')
    
    def execute(self, context):
        SUBD_TO_NURBS()
        return {'FINISHED'}
        
    def invoke(self, context,event):
        self.execute(context)
        return {'FINISHED'}


classes = (
    GLOBAL_UL_FreeCadBlender_props,
    MESH_OT_FreeCadBlender_subd_to_nurbs,
    VIEW3D_PT_FreeCadBlender_tool
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.FreeCadBlender_props = PointerProperty(
        type = GLOBAL_UL_FreeCadBlender_props
    )

def unregister():
    del(bpy.types.Scene.FreeCadBlender_props)
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

if __name__ == "__main__":
    register()




def SUBD_TO_NURBS():
    import bpy,sys

    sys.path.append(bpy.path.abspath(bpy.context.scene.FreeCadBlender_props.fc_dir))

    ex_dir = bpy.path.abspath(bpy.context.scene.FreeCadBlender_props.ex_dir)
    
    fname = bpy.context.scene.FreeCadBlender_props.fname

    import FreeCAD as F
    from FreeCAD import Part

    F.newDocument("freecad_temp")
    F.setActiveDocument('freecad_temp')

    import bpy,bmesh
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()

    obj = bpy.context.edit_object
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    patches=[]

    stored=set()

    def get_verts(vert):
        verts=set()
        for e in vert.link_edges:
            for v in e.verts: verts.add(v)
        return verts

    count=0
    for f in bm.faces:
        
        bpy.ops.mesh.select_all(action='DESELECT')
        
        if f not in stored:
            print ('PATCH:',count); count+=1
            
            bsplines=[]
            f.select=True
            bpy.ops.mesh.select_linked(delimit={'SEAM'})
            Fgroup= set( [f for f in bm.faces if f.select] )
            Vgroup= set( [v for v in bm.verts if v.select] )
            corners= set()
            borders = set()
            centers = set()
            
            for v in Vgroup:
                linkedVerts= get_verts(v)
                links = len ( set(Vgroup)&linkedVerts )
                if links == 3 : corners.add(v)
                elif links == 4 : borders.add(v)
                else: centers.add(v) 

            for b in borders:
                linkedVerts= get_verts(b)
                op = [ v for v in linkedVerts if v in corners ]
                triad = [op[0],b,op[1]]
                bsplines.append(triad)
            
            for f in bm.faces:
                if f.select: stored.add(f)
                        
            s1=bsplines.pop() 
            c1=s1[0]
            c2,c3=None,None
            bspline_ord=[s1]
            print(s1)
            
            for s in bsplines:
                for v in s: 
                    if v == c1: 
                        bspline_ord.append(s)
                        print(s)
                        if s[0]==c1: c2=s[2]
                        elif s[2]==c1: c2=s[0]
                        break                         
                    
            for s in bsplines:
                if s not in bspline_ord:
                    for v in s: 
                        if v==c2 and s not in bspline_ord:
                            bspline_ord.append(s)
                            print(s)
                            break                       
                    break 
                
            for s in bsplines:
                if s not in bspline_ord:
                    print(s) 
                    bspline_ord.append(s)
            
            patches.append(bspline_ord)    
            #patches.append(bsplines)

    for p in patches:
        curves=[]
        item=0
        for b in p:
        
            Points=[]
            
            Points.append( F.Vector( b[0].co.x,b[0].co.y,b[0].co.z ) )
            Points.append( F.Vector( b[1].co.x,b[1].co.y,b[1].co.z ) )
            Points.append( F.Vector( b[2].co.x,b[2].co.y,b[2].co.z ) )
    
            curve=Part.BSplineCurve()
            curve.increaseDegree(1)
            curve.interpolate(Points)
            curves.append(curve)

        com = Part.makeCompound([x.toShape() for x in curves]) 
        com_obj = F.ActiveDocument.addObject('Part::Feature', 'boundary_edges%s'%item)
        com_obj.Shape = com
        F.ActiveDocument.recompute()
        edge_names  = ["Edge%d"%(n+1) for n in range(len(com.Edges))]
        #edge_names  = [n.name for n in com.Edges]
        patch = F.ActiveDocument.addObject("Surface::Filling","Surface%s"%item)
        patch.BoundaryEdges = (com_obj, edge_names) 

        F.ActiveDocument.recompute() 
        item+=1
        
        
    F.ActiveDocument.recompute()

    SURFS= []

    for obj in F.ActiveDocument.Objects:
        if 'Surface' in obj.Name: 
            SURFS.append(obj)
        if 'boundary' in obj.Name:
            F.ActiveDocument.removeObject(obj.Name)
                

    F.activeDocument().addObject("Part::Compound","Compound")
    F.activeDocument().Compound.Links = SURFS

    F.ActiveDocument.recompute()

    print (ex_dir+fname+'.step')
    ex_dir=ex_dir+fname+'.step'
    F.ActiveDocument.getObject("Compound").Shape.exportStep(ex_dir)
    
    F.closeDocument("freecad_temp")

