# Tools for Painkiller 2004 game Blender Lightmaps

> Made by dilettante. Supports Blender 4.2 LTS

These tools address issues with ase2mpk that breaks lightmaps during MPK creation.

1. io_mpk_blend_list creates a list of map objects linked to lightmaps.
It takes the lightmap names from the names of the collections that the objects belong to

2. The custom "blend" tool assigns one common light map to several mesh objects. Usage example:

    ```
    blend.exe dm_temp.mpk
    ```

3. PKBlend is the same as the custom "blend" tool but with GUI.
