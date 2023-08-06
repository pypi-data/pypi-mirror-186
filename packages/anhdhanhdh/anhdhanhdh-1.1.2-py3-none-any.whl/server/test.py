from anhdhanhdh import Convert

def obj_to_gltf(input_path: str, need_draco=False, is_bin=False):
    """
    Convert Warefront OBJ to GLTF (or GLB) with draco compress
    """

    output_path = _mkdtemp()
    filename = _extract_filename_without_ext_from_path(input_path)
    if is_bin:
        output_file = os.path.join(output_path, f"{filename}.glb")
    else:
        output_file = os.path.join(output_path, f"{filename}.gltf")

    out_convert_gltf_path = Convert.convert_by_type(
        input_path,
        os.path.abspath(output_file),
        is_bin,
        need_draco,
    )

    return out_convert_gltf_path

obj_to_gltf("/home/ha/Documents/odm_textured_model_geo.obj")