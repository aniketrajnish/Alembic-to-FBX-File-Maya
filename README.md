# Alembic to FBX File Maya
 A python script that converts an Alembic file to animated FBX files using Maya while retaining the texture information.

https://github.com/aniketrajnish/Alembic-to-FBX-File-Maya/assets/58925008/33739de4-6689-4843-8e8b-727c9e7dee0b

 ## Usage
 * Clone the repository
    ```
    git clone https://github.com/aniketrajnish/Alembic-to-FBX-File-Maya.git
    ```  
 * Import the `alem_to_fbx.py` script into Maya.
 * Import the alembic file into Maya.   
 * Select the alembic node and run the python script.
 * To export the texture information along with the mesh, change to blinn/lambert materials.

## Contribution
Contributions to the project are welcome. 
Currently working on:
* ~~Changing the FBX import preset through the script itself.~~ [Done!] 
* Exporting blend shapes with a single mesh file for the alembic files with same topology across the animation cycle.
* Supporting bigger files.
* ~~Exporting texture information.~~ [Done!]
* ~~Ability to work with multiple Alembic nodes at once.~~ [Done!]

## License
MIT License
