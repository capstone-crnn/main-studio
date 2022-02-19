# gui

### Steps to create the GUI executable on the RPI:

1. Copy the 'gui' file (without /dist and /node_module directories) onto the raspberry pi.
2. Use the terminal on the pi to navigate to the pasted 'gui' folder.
3. Make sure you export the necessary variables: `export USE_SYSTEM_FPM="true"`
4. Run the `npm run pack:deb` command to create the executable file.
5. Once that is complete, you should find the executable file (with extension .deb) in the /dist directory of the 'gui' folder. Click on the executable and install the application.
6. Navigate to the Raspberry menu icon on the taskbar, and click on Accessories. You should find the 'gui' application under the directory.