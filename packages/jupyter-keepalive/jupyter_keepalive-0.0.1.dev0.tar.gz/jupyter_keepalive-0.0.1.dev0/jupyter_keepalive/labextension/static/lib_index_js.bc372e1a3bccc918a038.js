"use strict";
(self["webpackChunk_minrk_jupyter_keepalive"] = self["webpackChunk_minrk_jupyter_keepalive"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_2__);



/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function keepAliveRequest(endPoint = "", init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_2__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.URLExt.join(settings.baseUrl, "ext-keepalive", endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_2__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_2__.ServerConnection.NetworkError(error);
    }
    const data = await response.json();
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_2__.ServerConnection.ResponseError(response, data.message);
    }
    return data;
}
async function keepAliveStart() {
    return await keepAliveRequest("", { method: "POST" });
}
async function keepAliveStop() {
    return await keepAliveRequest("", { method: "DELETE" });
}
async function keepAliveRemaining() {
    return await keepAliveRequest("");
}
/**
 * Initialization data for the server-extension-example extension.
 */
const extension = {
    id: "jupyter-keepalive",
    autoStart: true,
    optional: [],
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette],
    activate: async (app, palette) => {
        console.log("JupyterLab extension keepalive is activated!");
        // GET request
        try {
            const data = await keepAliveRemaining();
            console.log(data);
        }
        catch (reason) {
            console.error(`Error on GET /api/.\n${reason}`);
        }
        // POST request
        const dataToSend = { name: "George" };
        try {
            const reply = await keepAliveStart();
            console.log(reply);
        }
        catch (reason) {
            console.error(`Error on POST /jlab-ext-example/hello ${dataToSend}.\n${reason}`);
        }
        const { commands } = app;
        const category = "Keepalive";
        commands.addCommand("keepalive:start", {
            label: "Keep server alive while idle",
            caption: "Registers activity so idle cullers don't shut this server down.",
            execute: () => {
                // todo: prompt for interval
                // send as JSON.stringify({seconds: n})
                // maybe that should be minutes? who keeps alive for seconds...?
                keepAliveStart();
            },
        });
        commands.addCommand("keepalive:stop", {
            label: "Stop keeping server alive",
            caption: "Stop the keepalive spinner",
            execute: () => {
                keepAliveStop();
            },
        });
        commands.addCommand("keepalive:check", {
            label: "Check keepalive status",
            caption: "Check the remaining time on the ",
            execute: () => {
                keepAliveRemaining();
                // todo: display it somehow
            },
        });
        for (var command of [
            "keepalive:start",
            "keepalive:stop",
            "keepalive:check",
        ]) {
            palette.addItem({ command: command, category: category });
        }
    },
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.bc372e1a3bccc918a038.js.map