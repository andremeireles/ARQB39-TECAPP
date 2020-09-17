import bpy,sys
from bpy.props import IntProperty, FloatProperty, StringProperty,BoolProperty
from sverchok.node_tree import SverchCustomTreeNode
from numpy import ndarray

class SvFCprojectNode(bpy.types.Node, SverchCustomTreeNode):
    ''' SvFCprojectNode '''
    bl_idname = 'SvFCprojectNode'
    bl_label = 'SvFCprojectNode'
    bl_icon = 'OUTLINER_OB_EMPTY'
    sv_icon = 'SV_FLOAT_TO_INT'

    fc_file : StringProperty(name="fc_file",subtype="FILE_PATH")
    fc_dir : StringProperty(name="fc_dir",subtype="DIR_PATH")
    detail : FloatProperty(name="detail", default=0.01)
    read_update : BoolProperty(name="read_update", default=True)
    write_update : BoolProperty(name="write_update", default=True)
    

    def draw_buttons(self, context, layout):
        #addon = context.preferences.addons.get(sverchok.__name__)
        #over_sized_buttons = addon.preferences.over_sized_buttons
        col = layout.column(align=True)
        col.prop(self, 'fc_dir')
        col.prop(self, 'fc_file')
        col.prop(self, 'detail')
        col.prop(self, 'read_update')
        col.prop(self, 'write_update')
        

    def sv_init(self, context):
        self.inputs.new('SvVerticesSocket', "Vers")
        self.inputs.new('SvStringsSocket', "Pols")
        
        self.outputs.new('SvVerticesSocket', "Vers")
        self.outputs.new('SvStringsSocket', "Pols")

    def process(self):
        #self.inputs['float'].sv_get()
        #self.inputs['WRITE'].sv_get(fc_file)
        if self.outputs['Vers'].is_linked and self.read_update:
            verts_out,pols_out = FC_LOAD_PARTS(self.fc_dir,self.fc_file,self.detail)
            if verts_out==None:
                verts_out,pols_out = [],[]
            #self.outputs['READ'].sv_set( (self.fc_file) )
            self.outputs['Vers'].sv_set(verts_out)
            self.outputs['Pols'].sv_set(pols_out)

        if self.inputs['Vers'].is_linked and self.inputs['Pols'].is_linked and self.write_update:
            verts=self.inputs['Vers'].sv_get()
            pols=self.inputs['Pols'].sv_get()
            FC_WRITE_PARTS(self.fc_dir,self.fc_file,verts,pols)

def FC_LOAD_PARTS(fc_dir,fc_file,detail):
    
    sys.path.append(bpy.path.abspath(fc_dir))
    #sys.path.append(fc_dir)
    import FreeCAD as F
    try:
        F.open(bpy.path.abspath(fc_file))
        #F.open(fc_file)        
    except: 
        return ([],[])

    Fname = bpy.path.display_name_from_filepath(fc_file)
    F.setActiveDocument(Fname)
    verts=[]
    faces=[]

    try:
        for obj in F.ActiveDocument.Objects:
            if obj.Module in ('Part','PartDesign'):    
                mesh_data=obj.Shape.tessellate(detail) # return-> [ [(x,y,z),(x,y,z)] [(1,2,3),(1,7,3),(1,2,3)]   ]
                verts.append( mesh_data[0] )
                faces.append( mesh_data[1] )

                F.ActiveDocument.recompute()
        F.closeDocument(Fname)
    except:
        F.closeDocument(Fname)
        return ([],[])

    return (verts,faces)

def FC_WRITE_PARTS(fc_dir,fc_file,verts,faces):
    sys.path.append(bpy.path.abspath(fc_dir))
    #sys.path.append(fc_dir)
    import FreeCAD as F
    try:
        F.open(bpy.path.abspath(fc_file))
        #F.open(fc_file)
    except: 
        return

    Fname = bpy.path.display_name_from_filepath(fc_file)

    import Mesh

    F.setActiveDocument(Fname)
    fc_root = F.getDocument(Fname)

    try:
        obj_names = set( [ i.Name for i in fc_root.Objects])

        if "Mesh" in obj_names:
            fc_root.removeObject("Mesh")
        
        meshdata=[]

        faces=faces[0]
        verts=verts[0]

        for f in faces:
            v1,v2,v3 = f[0],f[1],f[2]
            meshdata.append(verts[v1])
            meshdata.append(verts[v2])
            meshdata.append(verts[v3])
                
        MeshObject = Mesh.Mesh(meshdata)
        Mesh.show(MeshObject)

        to_solid=False
        if to_solid:
            obj_names = set( [ i.Name for i in fc_root.Objects])
            if "Mesh001" in obj_names: fc_root.removeObject("Mesh001")
            if "Mesh002" in obj_names: fc_root.removeObject("Mesh002")
            if "Mesh002 (Solid)" in obj_names: fc_root.removeObject("Mesh002 (Solid)")
            F.ActiveDocument.recompute()
            import Part
            fc_root.addObject("Part::Feature","Mesh001")
            __shape__=Part.Shape()
            __shape__.makeShapeFromMesh(fc_root.getObject("Mesh").Mesh.Topology,0.100000)
            fc_root.getObject("Mesh001").Shape=__shape__
            fc_root.getObject("Mesh001").purgeTouched()
            del __shape__
            #refine
            F.ActiveDocument.addObject('Part::Feature','Mesh001').Shape=F.ActiveDocument.Mesh001.Shape.removeSplitter()
            F.ActiveDocument.ActiveObject.Label=F.ActiveDocument.Mesh001.Label
            #to solid
            __s__=F.ActiveDocument.Mesh001001.Shape
            __s__=Part.Solid(__s__)
            __o__=F.ActiveDocument.addObject("Part::Feature","Mesh001001_solid")
            __o__.Label="Mesh002 (Solid)"
            __o__.Shape=__s__
            del __s__, __o__

        F.ActiveDocument.recompute()
        F.getDocument(Fname).save()
        F.closeDocument(Fname)


    except:
        F.closeDocument(Fname)




def register():
    bpy.utils.register_class(SvFCprojectNode)

def unregister():
    bpy.utils.unregister_class(SvFCprojectNode)
