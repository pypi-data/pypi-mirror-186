from enum import Enum, auto
from .engine_pipe_abstract import EnginePlatform

GRPC_INTERFACE_METHOD_HEADER = 'method'
GRPC_INTERFACE_PROPERTY_HEADER = 'property'


class GRPCInterface(Enum):

    # declare method interface
    method_system_get_projectinfo = auto()
    method_scene_clone = auto()

    # UnityEditor built-in static method
    method_unity_editor_import_asset = auto()
    method_unity_editor_move_asset = auto()
    method_unity_editor_assetdatabase_refresh = auto()
    method_unity_editor_assetdatabase_copy_asset = auto()

    method_unity_editor_scenemanager_open = auto()

    # prefab utilities
    method_unity_prefab_create = auto()
    method_unity_prefab_merge = auto()
    method_unity_prefab_add_component = auto()
    method_unity_prefab_set_value = auto()
    method_unity_prefab_set_reference_value = auto()
    method_unity_prefab_create_mesh_collider_object = auto()

    # material utilities
    method_unity_material_update_textures = auto()
    method_unity_material_update_alpha_and_color = auto()

    # syngar integration
    method_syngar_integ_create_mesh_group = auto()
    method_syngar_integ_integrate_models = auto()
    method_syngar_integ_initialize_model_view_buttons = auto()  # add dicom viewer buttons to the bottom mainMenu
    method_syngar_integ_initialize_dicom_view_buttons = auto()  # add dicom viewer buttons to the bottom mainMenu
    method_syngar_integ_integrate_bottom_menu = auto()
    method_syngar_integ_initialize_dicom_viewer = auto()
    method_syngar_integ_integrate_dicom_viewer = auto()
    method_syngar_integ_initialize_dicom_widget = auto()
    method_syngar_integ_integrate_dicom_widget = auto()


INTERFACE_MAPPINGS = {
    GRPCInterface.method_system_get_projectinfo: {
        EnginePlatform.unity: "UGrpc.SystemUtils.GetProjectInfo"
    },
    GRPCInterface.method_scene_clone: {
        EnginePlatform.unity: "UGrpc.SceneUtils.SceneClone"
    },

    # AssetDatabase
    GRPCInterface.method_unity_editor_move_asset: {
        EnginePlatform.unity: "UnityEditor.AssetDatabase.MoveAsset"
    },
    GRPCInterface.method_unity_editor_import_asset: {
        EnginePlatform.unity: "UnityEditor.AssetDatabase.ImportAsset"
    },
    GRPCInterface.method_unity_editor_assetdatabase_refresh: {
        EnginePlatform.unity: "UnityEditor.AssetDatabase.Refresh"
    },
    GRPCInterface.method_unity_editor_assetdatabase_copy_asset: {
        EnginePlatform.unity: "UnityEditor.AssetDatabase.CopyAsset"
    },

    # Prefab utilities
    GRPCInterface.method_unity_prefab_create: {
        EnginePlatform.unity: "UGrpc.PrefabUtils.CreateModelAsset"
    },
    GRPCInterface.method_unity_prefab_merge: {
        EnginePlatform.unity: "UGrpc.PrefabUtils.Merge"
    },
    GRPCInterface.method_unity_prefab_add_component: {
        EnginePlatform.unity: "UGrpc.PrefabUtils.AddComponent"
    },
    GRPCInterface.method_unity_prefab_set_value: {
        EnginePlatform.unity: "UGrpc.PrefabUtils.SetValue"
    },
    GRPCInterface.method_unity_prefab_set_reference_value: {
        EnginePlatform.unity: "UGrpc.PrefabUtils.SetReferenceValue"
    },
    GRPCInterface.method_unity_prefab_create_mesh_collider_object: {
        EnginePlatform.unity: "UGrpc.PrefabUtils.CreateMeshColliderObject"
    },

    # Scene manager
    GRPCInterface.method_unity_editor_scenemanager_open: {
        EnginePlatform.unity: "UnityEditor.SceneManagement.EditorSceneManager.OpenScene"
    },


    # Material utilities
    GRPCInterface.method_unity_material_update_textures: {
        EnginePlatform.unity: "UGrpc.MaterialUtils.UpdateTextures"
    },
    GRPCInterface.method_unity_material_update_alpha_and_color: {
        EnginePlatform.unity: "UGrpc.MaterialUtils.UpdateAlphaAndColor"
    }
}
