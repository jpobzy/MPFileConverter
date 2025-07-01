# MPFileConverter
For Ray, converts MP4 to MP3

# Creating an exe file:
### server
- cd to server folder
- run `pyinstaller --onefile server.py`
- move server.exe from `Server\dist\server` to `Client\dist`

### client
- cd to client folder
- uncomment `startFlaskServer();` in `Client\src\main\index.js`
- run `npm install`
- run `npm run build`
- run `npm run build:win`

### Running the exe file
- You can either run the exe file in `Client/dist/win-unpacked/mpfileconverter.exe` 
- Or install the executable by running `Client/dist/mpfileconverter 1.0.0.exe`


# Running locally (non exe file)
**LANGUAGES REQUIRED TO RUN**  
- Node.js: [https://nodejs.org/en/download](https://nodejs.org/en/download)
- Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Running the app
- Clone the repo and open a terminal 
- CD into the repo
- Run `start cmd /k cd "%cd%"` to open a duplicate terminal`
- In one of the terminals run `cd Client` and `cd Server` in the other
- In the client terminal run `npm run install` and then `npm run dev`
- In the server termnial run `pip install -r requirements.txt` and `python server.py` 