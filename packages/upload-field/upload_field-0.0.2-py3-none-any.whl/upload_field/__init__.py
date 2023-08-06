import os
import io
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "upload_field",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("upload_field", path=build_dir)

def upload_field(
    title: str, socket_uri: str, identification: str, upload_suffix: str, chunk_size: int = 1024, key=None
):
    component_value = _component_func(
        title=title, 
        key=key, 
        socket_uri=socket_uri, 
        chunk_size=chunk_size,
        identification=identification,
        upload_suffix=upload_suffix,
        default=0
    )
    return component_value

if not _RELEASE:
    import streamlit as st
    uploaded_files = upload_field(
        "Scan Upload", 
        "ws://localhost:8030",
        "test_identification_2",
        "scan",
        chunk_size=100000,
    )
    uploaded_files
    #if type(uploaded_files)==list:
    #    with open(uploaded_files[0], "rb") as file:
    #        file_bytes = io.BytesIO(file)
    #        file.read(2)
