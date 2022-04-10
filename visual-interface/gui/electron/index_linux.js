const { app, BrowserWindow, ipcMain, dialog } = require("electron");
const { join } = require("path");
const fs = require("fs");
const process = require("process");

// Disable error dialogs by overriding
dialog.showErrorBox = function(title, content) {
    console.log(`${title}\n${content}`);
};

app.whenReady().then(main).catch((err) => console.log(err));

const isDev = !app.isPackaged;

function main() {
    const window = new BrowserWindow({
        height: 480,
        width: 800,
        autoHideMenuBar: true,
        show: false,
        useContentSize: true,
        resizable: false,
        kiosk: true,
        webPreferences: {
            nodeIntegration: true,
            enableRemoteModules: true,
            preload: join(__dirname, "./preload.js")
        }
    })

    window.loadFile(join(__dirname, "../public/index.html"));
    window.on("ready-to-show", window.show);
    
    window.webContents.on('dom-ready', (event)=> {
        let css = '* { cursor: none !important; }';
        window.webContents.insertCSS(css);
    });
    
    if (isDev) {
        //window.webContents.openDevTools();   // uncomment to show devTools on startup
    }    
    
    
    // Sending bpm data to UI
    const filename = "shared_file";
    const path = process.cwd() + "/electron/" + filename;

    fs.watch(path, (evt, file) => {
        if (evt === "change") {
            if (file === filename) {
                fs.readFile(path, "utf-8", (err, data) => { // IMPORTANT: when using with C++, use "utf-8" parameter [NOTE]
                    if (err) {
                        console.error("Error: ", err);
                    }
                    
                    // stream = [...data];
                    // window.webContents.send("data", stream);
                    window.webContents.send("data", JSON.parse(data)); //[resp_ave, heart_ave, resp_detection]
                })
            } else {
                console.log(`Error: Different file changed - ${file}`);
            }
        } else {
            console.log(`Attention: ${file} experienced ${evt}`);
        }
    });
}


ipcMain.handleOnce("calibrate", () => {
    // const filename = "dsp.py";
    // const path = process.cwd() + "/electron/" + filename;
    // // pyshell.run(path, null, (err, results)  => {
    // //     if (err) {
    // //         console.log(err);
    // //     };
    // //     console.log('dsp.py finished.');
    // //     console.log('results', results);
    // // });
    // var python = require('child_process').spawn('python3', [path]);
    // python.stdout.on('data',function(data){
	//     console.log("data: ",data.toString('utf8'));
    // });
});
ipcMain.handleOnce("get-version", () => app.getVersion());
ipcMain.handleOnce("power-off", () => app.quit());