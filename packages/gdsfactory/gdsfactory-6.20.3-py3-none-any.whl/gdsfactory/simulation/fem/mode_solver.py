import pathlib
import pickle
from typing import Optional

import numpy as np
from femwell import mode_solver
from skfem import Basis, ElementTriN2, ElementTriP0, ElementTriP2, Mesh

import gdsfactory as gf
from gdsfactory.config import logger
from gdsfactory.pdk import _ACTIVE_PDK, get_layer_stack
from gdsfactory.simulation.get_modes_path import get_modes_path_femwell
from gdsfactory.technology import LayerStack
from gdsfactory.types import CrossSectionSpec, PathType


def compute_cross_section_modes(
    cross_section: CrossSectionSpec,
    layerstack: LayerStack,
    wl: float = 1.55,
    num_modes: int = 4,
    order: int = 1,
    radius: float = np.inf,
    mesh_filename: str = "mesh.msh",
    dirpath: Optional[PathType] = None,
    filepath: Optional[PathType] = None,
    overwrite: bool = False,
    with_cache: bool = True,
    **kwargs,
):
    """Calculate effective index of a straight cross-section.

    Args:
        cross_section: gdsfactory cross-section.
        layerstack: gdsfactory layerstack.
        wl: wavelength (um).
        num_modes: number of modes to return.
        order: order of the mesh elements.
        radius: bend radius of the cross-section.
        mesh_filename (str, path): where to save the .msh file.
        dirpath: Optional directory to store modes.
        filepath: Optional path to store modes.
        overwrite: Overwrite mode filepath if it exists.
        with_cache: write modes to filepath cache.

    Keyword Args:
        resolutions (Dict): Pairs {"layername": {"resolution": float, "distance": "float}}
            to roughly control mesh refinement within and away from entity, respectively.
        mesh_scaling_factor (float): factor multiply mesh geometry by.
        default_resolution_min (float): gmsh minimal edge length.
        default_resolution_max (float): gmsh maximal edge length.
        background_tag (str): name of the background layer to add (default: no background added).
        background_padding (Tuple): [xleft, ydown, xright, yup] distances to add to the components and to fill with background_tag.
        global_meshsize_array: np array [x,y,z,lc] to parametrize the mesh.
        global_meshsize_interpolant_func: interpolating function for global_meshsize_array.
        extra_shapes_dict: Optional[OrderedDict] = OrderedDict of {key: geo} with key a label and geo a shapely (Multi)Polygon or (Multi)LineString of extra shapes to override component.
        merge_by_material: boolean, if True will merge polygons from layers with the same layer.material. Physical keys will be material in this case.
    """
    sim_settings = dict(
        wl=wl, num_modes=num_modes, radius=radius, order=order, **kwargs
    )
    filepath = filepath or get_modes_path_femwell(
        cross_section=cross_section,
        dirpath=dirpath,
        layerstack=layerstack,
        **sim_settings,
    )
    filepath = pathlib.Path(filepath)

    if with_cache and filepath.exists():
        if overwrite:
            filepath.unlink()

        else:
            logger.info(f"Simulation loaded from {filepath!r}")

            with open(filepath, "rb") as handle:
                modes_dict = pickle.load(handle)

            lams, basis, xs = modes_dict["lams"], modes_dict["basis"], modes_dict["xs"]
            return lams, basis, xs

    # Get meshable component from cross-section
    c = gf.components.straight(length=10, cross_section=cross_section)
    c.show()
    bounds = c.bbox
    dx = np.diff(bounds[:, 0])[0]

    # Mesh
    mesh = c.to_gmsh(
        type="uz",
        xsection_bounds=[[dx / 2, bounds[0, 1]], [dx / 2, bounds[1, 1]]],
        layer_stack=layerstack,
        filename=mesh_filename,
        **kwargs,
    )

    # Assign materials to mesh elements
    mesh = Mesh.load(mesh_filename)
    basis = Basis(mesh, ElementTriN2() * ElementTriP2())
    basis0 = basis.with_element(ElementTriP0())
    epsilon = basis0.zeros(dtype=complex)
    for layername, layer in layerstack.layers.items():
        if layername in mesh.subdomains.keys():
            epsilon[basis0.get_dofs(elements=layername)] = (
                _ACTIVE_PDK.materials_index[layer.material](wl) ** 2
            )
        if "background_tag" in kwargs:
            epsilon[basis0.get_dofs(elements=kwargs["background_tag"])] = (
                _ACTIVE_PDK.materials_index[kwargs["background_tag"]](wl) ** 2
            )

    # Mode solve
    lams, basis, xs = mode_solver.compute_modes(
        basis0,
        epsilon,
        wavelength=wl,
        mu_r=1,
        num_modes=num_modes,
        order=order,
        radius=radius,
    )

    if with_cache:
        modes_dict = {"lams": lams, "basis": basis, "xs": xs}

        with open(filepath, "wb") as handle:
            pickle.dump(modes_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

        logger.info(f"Write simulation results to {filepath!r}")
    return lams, basis, xs


if __name__ == "__main__":
    filtered_layerstack = LayerStack(
        layers={
            k: get_layer_stack().layers[k]
            for k in (
                "core",
                "clad",
                "slab90",
                "box",
            )
        }
    )

    filtered_layerstack.layers["core"].thickness = 0.2

    resolutions = {
        "core": {"resolution": 0.02, "distance": 2},
        "clad": {"resolution": 0.2, "distance": 1},
        "box": {"resolution": 0.2, "distance": 1},
        "slab90": {"resolution": 0.05, "distance": 1},
    }
    lams, basis, xs = compute_cross_section_modes(
        cross_section="rib",
        layerstack=filtered_layerstack,
        wl=1.55,
        num_modes=4,
        order=1,
        radius=np.inf,
        mesh_filename="mesh.msh",
        resolutions=resolutions,
        overwrite=False,
        with_cache=True,
    )
    mode_solver.plot_mode(
        basis=basis,
        mode=np.real(xs[0]),
        plot_vectors=False,
        colorbar=True,
        title="E",
        direction="y",
    )
