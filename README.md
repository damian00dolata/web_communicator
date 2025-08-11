# Web Communicator by Damian Dolata

## Project description
This is a project of a simple Messanger, built with Python, SvelteKit and Sqlite3. It contains Socket connection, dependency injection, objective programming, simple database interface and more.

## Dockerizing the project
The project is dockerized. To launch it, you need to use ``` docker compose up -d --build``` in the main folder.

On dev, use Docker profile ``` docker compose --profile dev up -d --build ``` for dynamic code updates.

## IntelliSense access through Remote Containers
You can run Remote Container to access IntelliSense, through installing Dev Containers and Docker extensions, then ``` F1 ``` > ``` Dev Containers: Attack to Running Container... ``` and use both API and frontend containers to open new windows.

Last step is ``` File ``` > ``` Open Folder... ``` and picking ``` app ``` catalog in root directory of the container.