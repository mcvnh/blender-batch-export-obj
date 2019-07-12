# Blender Batch Export OBJ

A simple Blender extension used to export meshes of a model into separate files, each file is a mesh exact from the model and saved as OBJ file format.

## Installation

In Blender, open `Info` view, select `File` and `User Preferences...` or press its shortcut `Cmd + ,`.

Select `Add-ons` tab and click on `Install Add-on from File...` and point to `batchexport.py`

## Usage

Open `Info` view, select `File`, `Export` and select `OBJ Batch Export`.

The file modal will be shown, select a folder in which exported files will be stored.

## Advantage Usage

It is able to use this batch export obj on a remote server; however, Blender must be installed on the remote server first before running the script.

```bash
OBJ_EXPORT_PATH=EXPORT_PATH blender -b MODEL_FILE_PATH --python batchexport_cli.py
```

The only thing you have to do here is change variables `EXPORT_PATH` and `MODEL_FILE_PATH` by your own.

