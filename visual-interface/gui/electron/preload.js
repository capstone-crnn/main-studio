const { ipcRenderer, contextBridge } = require("electron");

const WINDOW_API = {
    GetVersion: () => ipcRenderer.invoke("get/version")
}

// window.api
contextBridge.exposeInMainWorld("api", WINDOW_API);