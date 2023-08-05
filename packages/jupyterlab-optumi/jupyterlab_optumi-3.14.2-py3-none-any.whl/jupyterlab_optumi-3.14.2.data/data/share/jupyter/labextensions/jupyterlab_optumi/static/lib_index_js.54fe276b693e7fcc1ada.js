"use strict";
(self["webpackChunkjupyterlab_optumi"] = self["webpackChunkjupyterlab_optumi"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./widget */ "./lib/widget.js");
/*
 **  Copyright (C) Optumi Inc - All rights reserved.
 **
 **  You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
 **  To receive a copy of the licensing terms please write to contact@optumi.com or visit us at http://www.optumi.com.
 **/

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ([_widget__WEBPACK_IMPORTED_MODULE_0__["default"]]);


/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IOptumi": () => (/* binding */ IOptumi),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! common */ "webpack/sharing/consume/default/common/common");
/* harmony import */ var common__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(common__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/docmanager */ "webpack/sharing/consume/default/@jupyterlab/docmanager");
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_7__);
/*
 **  Copyright (C) Optumi Inc - All rights reserved.
 **
 **  You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
 **  To receive a copy of the licensing terms please write to contact@optumi.com or visit us at http://www.optumi.com.
 **/









// TODO:JJ Does this really need to be exported?
const IOptumi = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_7__.Token('optumi:IOptumi');
const id = 'optumi';
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ({
    activate,
    id,
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_2__.ILabShell, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_2__.ILayoutRestorer, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_6__.INotebookTracker, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_5__.IThemeManager, _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_4__.IDocumentManager],
    provides: IOptumi,
    autoStart: true,
});
async function activate(lab, labShell, restorer, tracker, manager, docManager) {
    let widget;
    async function loadPanel() {
        // add widget
        if (!widget.isAttached) {
            labShell.add(widget, 'left', { rank: 1000 });
        }
    }
    // Creates the left side bar widget once the app has fully started
    lab.started.then(() => {
        document.documentElement.style.setProperty('--jp-sidebar-min-width', '340px');
        // Set some well known globals
        common__WEBPACK_IMPORTED_MODULE_1__.Global.lab = lab;
        common__WEBPACK_IMPORTED_MODULE_1__.Global.labShell = labShell;
        common__WEBPACK_IMPORTED_MODULE_1__.Global.themeManager = manager;
        common__WEBPACK_IMPORTED_MODULE_1__.Global.docManager = docManager;
        common__WEBPACK_IMPORTED_MODULE_1__.Global.tracker = tracker;
        docManager.services.contents.getDownloadUrl('Agreement.html').then((url) => (common__WEBPACK_IMPORTED_MODULE_1__.Global.agreementURL = url));
        // Wait until we have a version to set metadata related globals
        const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_3__.ServerConnection.makeSettings();
        const url = settings.baseUrl + 'optumi/version';
        _jupyterlab_services__WEBPACK_IMPORTED_MODULE_3__.ServerConnection.makeRequest(url, {}, settings)
            .then((response) => {
            if (response.status !== 200)
                throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_3__.ServerConnection.ResponseError(response);
            return response.json();
        })
            .then((data) => {
            // Get the version from the server
            // We do not want to start the extension until we know the version, it might mess with metadata
            const version = data.version;
            const userHome = data.userHome;
            const jupyterHome = data.jupyterHome;
            console.log('JupyterLab extension jupyterlab-optumi version ' + version + ' is activated!');
            common__WEBPACK_IMPORTED_MODULE_1__.Global.version = version;
            common__WEBPACK_IMPORTED_MODULE_1__.Global.userHome = userHome;
            common__WEBPACK_IMPORTED_MODULE_1__.Global.jupyterHome = jupyterHome;
        });
        widget = _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_5__.ReactWidget.create(react__WEBPACK_IMPORTED_MODULE_0__.createElement(common__WEBPACK_IMPORTED_MODULE_1__.OptumiLeftPanel, null));
        widget.id = 'optumi/Optumi';
        widget.title.iconClass = 'jp-o-logo jp-SideBar-tabIcon';
        widget.title.caption = 'Optumi';
        restorer.add(widget, widget.id);
    });
    // Initialize once the application shell has been restored
    lab.restored.then(() => {
        loadPanel();
    });
    return { widget };
}


/***/ })

}]);
//# sourceMappingURL=lib_index_js.54fe276b693e7fcc1ada.js.map