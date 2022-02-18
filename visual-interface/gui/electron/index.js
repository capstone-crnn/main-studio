const { app, BrowserWindow, icpMain } = require("electron");
const { ipcMain } = require("electron/main");
const { join } = require("path");




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
        webPreferences: {
            preload: join(__dirname, "./preload.js")
        }
    })

    window.loadFile(join(__dirname, "../public/index.html"));
    window.on("ready-to-show", window.show);

    if (isDev) {
        // window.webContents.openDevTools();   // uncomment to show devTools on startup
    }
}

ipcMain.handleOnce("get/version", () => app.getVersion());