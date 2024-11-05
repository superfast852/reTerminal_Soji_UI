# DEV LOG:
## Progress:
- 12/11/2022: Made this file, fixed switch bug, fixed double cleanup bug, added frame_switch, added plotting
- 14/11/2022: Added Terminal Window. Found some bugs
- 19/11/2022: Added Fullscreen


## TODO:
***
- #### Make Async Communication Pipline
- Add more comments
- Create Settings File
- Find out data to collect
***
- Make Tab 1: Home
    - Make a Connection Interface: `socket.connect(socket.gethostbyname("soji.local"), 9160)`
    - Make a Disconnect Interface: `socket.close()`
***
- Refine Tab 2: Data
    - Make a Data Interface: `socket.send("data")`
    - Make a Data Plotting Interface: `plt.plot(data)`
    - Make a Data Saving Interface: `np.save(data)`
***
- Make Tab 3: Terminal
    - Make a Terminal Interface: `socket.send("echo hello")`, `command = socket.recv(1024)`, `res = os.system(command)`
***
- Make Tab 5: Settings
    - Add Robot Settings
    - Add Communication Settings
    - Add App Settings
***
- Add Async receiving Process
    - Use threading to offload data transmissions, and update the GUI when data packets are received.

## File Structure:
***
- `main.py`: Main file, contains the GUI
- `assets/`: Image folderContains all the assets
- `main_experimental.py`: Experimental file, contains the GUI with ongoing modifications
- `main_no_plot.py`: Contains the base GUI without plotting, only camera feed. Used for testing new frames.
- [TODO] `settings.py | settings.json | settings.yaml | settings.txt`: Contains the settings for the app

## Bug Bounty
***
* Done!