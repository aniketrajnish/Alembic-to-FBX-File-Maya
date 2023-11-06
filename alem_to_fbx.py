import maya.cmds as cmds
import maya.mel as mm
import os
from datetime import datetime

def export_frames_as_fbx(abc_node, export_dir, start_frame, end_frame):
    original_start_frame = cmds.playbackOptions(query=True, animationStartTime=True)
    original_end_frame = cmds.playbackOptions(query=True, animationEndTime=True)
    
    for frame in range(start_frame, end_frame + 1):
        cmds.currentTime(frame)
        cmds.playbackOptions(min=frame, max=frame)
        
        frame_export_path = os.path.join(export_dir, f"frame_{frame:04d}.fbx")
        cmds.FBXExport('-file', frame_export_path, '-s')
        
        print(f"Exported: {frame_export_path}")

    cmds.playbackOptions(min=original_start_frame, max=original_end_frame)

def create_animation_from_fbx(export_dir, start_frame, end_frame):
    imported_frame_nodes = []
    original_import_mode = mm.eval("FBXImportMode -q;")
    mm.eval("FBXImportMode -v add;")
    
    # Importing the exported FBX frames
    for frame in range(start_frame, end_frame + 1):
        fbx_path = os.path.join(export_dir, f"frame_{frame:04d}.fbx")
        nodes = cmds.file(fbx_path, i=True, type="FBX", returnNewNodes=True, options="v=0")
        imported_frame_nodes.append(nodes)
        for node in nodes:
            if cmds.nodeType(node) == "transform":
                cmds.setAttr(f"{node}.visibility", 0)
                
    # Animation hax - enabling disabling visibility
    for frame in range(start_frame, end_frame + 1):
        cmds.currentTime(frame)
        for i, nodes in enumerate(imported_frame_nodes):
            visibility = 1 if i == frame - start_frame else 0
            for node in nodes:
                if cmds.nodeType(node) == "transform":
                    cmds.setAttr(f"{node}.visibility", visibility)
                    cmds.setKeyframe(f"{node}.visibility")
            
    
    all_nodes = [node for frame_nodes in imported_frame_nodes for node in frame_nodes if cmds.nodeType(node) == "transform"]
    cmds.select(all_nodes)
    
    animation_export_path = cmds.fileDialog2(fileMode=0, caption="Save Final Animation", startingDirectory=export_dir, fileFilter="FBX Files (*.fbx)")
    if not animation_export_path:
        cmds.warning("Operation canceled. Final animation not saved.")
        return
    
    animation_export_path = animation_export_path[0]
    if not animation_export_path.lower().endswith('.fbx'):
        animation_export_path += '.fbx'
    
    cmds.FBXExport('-file', animation_export_path, '-s')
    print(f"Final Animation Exported: {animation_export_path}")
    
    # Cleanup
    for frame_nodes in imported_frame_nodes:
        cmds.delete(frame_nodes)
    for frame in range(start_frame, end_frame + 1):
        frame_file_path = os.path.join(export_dir, f"frame_{frame:04d}.fbx")
        if os.path.exists(frame_file_path):
            os.remove(frame_file_path)
    mm.eval(f"FBXImportMode -v {original_import_mode};")
    
    print("Individual frame nodes and files removed. Import settings reverted.")

def convert_alembic_to_fbx():
    # init()
    
    # Step 1- Asking user to select an alembic file
    alembic_file = cmds.ls(selection=True)
    if not alembic_file:
        cmds.warning("Please select an Alembic node")
        return
    alembic_node = alembic_file[0]    

    # Step 2- Asking user to select a directory to export to
    export_dir = cmds.fileDialog2(fileMode=3, caption="Select Export Directory")
    if not export_dir:
        cmds.warning("Please select a directory")
        return
    
    export_dir = export_dir[0]
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_dir = os.path.join(export_dir, f"alembic_to_fbx_{timestamp}")
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    start_frame = int(cmds.playbackOptions(query=True, animationStartTime=True))
    end_frame = int(cmds.playbackOptions(query=True, animationEndTime=True))
    
    # Step 3- Exporting each frame of the alembic file as FBX individually
    export_frames_as_fbx(alembic_node, export_dir, start_frame, end_frame)    
    
    cmds.setAttr(f"{alembic_node}.visibility", 0)    
    
    # Step 4- Importing all the exported FBX files and combining and exporting them as a single animated FBX file
    create_animation_from_fbx(export_dir, start_frame, end_frame)
    
    cmds.setAttr(f"{alembic_node}.visibility", 1)
    
convert_alembic_to_fbx()