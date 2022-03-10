const fs = require("fs");
const { contextBridge, ipcRenderer } = require("electron");


const WINDOW_API = {
    GetVersion: () => ipcRenderer.invoke("get-version"),
    PowerOff: () => ipcRenderer.invoke("power-off"),
    Stream: (callback) => {
        // Waiting on bpm data from UI
        ipcRenderer.on("data", (evt, data) => {
            callback(evt, data);    // passing bpm data to UI
        })
    }
}


// window.api
contextBridge.exposeInMainWorld("api", WINDOW_API);