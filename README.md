# Alembic to FBX File Maya
 A python script that converts an Alembic file to animated FBX files using Maya.

 ## Usage
 * Clone the repository
    ```
       git clone https://github.com/aniketrajnish/Alembic-to-FBX-File-Maya.git
    ```  
 * Import the `alem_to_fbx.py` script into Maya.
 * Import the alembic file into Maya.
 * Make sure that your import preset for the File content for a fbx file is set to  `Add`.
 * Select the alembic node and run the python script.

## Contribution
Contributions to the project are welcome. 
Currently working on:
* Changing the FBX import preset through the script itself. 
* Exporting blend shapes with a single mesh file for the alembic files with same topology across the animation cycle.
* Supporting bigger files.
* Exporting texture information.

## License
MIT License