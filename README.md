# Alembic to FBX File Maya
 A python script that converts an Alembic file to animated FBX files using Maya. 

https://github.com/aniketrajnish/Alembic-to-FBX-File-Maya/assets/58925008/33739de4-6689-4843-8e8b-727c9e7dee0b

 ## Usage
 * Clone the repository
    ```
    git clone https://github.com/aniketrajnish/Alembic-to-FBX-File-Maya.git
    ```  
 * Import the `alem_to_fbx.py` script into Maya.
 * Import the alembic file into Maya.
 * Make sure that your import preset for the File content for a fbx file is set to  `Add`.   
   
    <p align="center">
   <img src="https://github.com/aniketrajnish/Alembic-to-FBX-File-Maya/assets/58925008/963328a6-8fca-42a9-944b-80aced85507c" alt="File Content" width="75%"/>
    </p>
   
 * Select the alembic node and run the python script.

## Contribution
Contributions to the project are welcome. Currently working on changing the FBX import preset through the script itself as well as exporting blend shapes with a single mesh file for the alembic files with same topology across the animation cycle.

## License
MIT License
