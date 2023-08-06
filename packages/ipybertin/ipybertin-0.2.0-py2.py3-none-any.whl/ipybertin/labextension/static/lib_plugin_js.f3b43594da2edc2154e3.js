"use strict";
(self["webpackChunkipybertin"] = self["webpackChunkipybertin"] || []).push([["lib_plugin_js"],{

/***/ "./lib/plugin.js":
/*!***********************!*\
  !*** ./lib/plugin.js ***!
  \***********************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


// Copyright (c) David Brochart
// Distributed under the terms of the Modified BSD License.
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const widgetExports = __importStar(__webpack_require__(/*! ./widget */ "./lib/widget.js"));
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
const EXTENSION_ID = 'ipybertin:plugin';
/**
 * The example plugin.
 */
const examplePlugin = {
    id: EXTENSION_ID,
    requires: [base_1.IJupyterWidgetRegistry],
    activate: activateWidgetExtension,
    autoStart: true,
};
// the "as unknown as ..." typecast above is solely to support JupyterLab 1
// and 2 in the same codebase and should be removed when we migrate to Lumino.
exports["default"] = examplePlugin;
/**
 * Activate the widget extension.
 */
function activateWidgetExtension(app, registry) {
    registry.registerWidget({
        name: version_1.MODULE_NAME,
        version: version_1.MODULE_VERSION,
        exports: widgetExports,
    });
}
//# sourceMappingURL=plugin.js.map

/***/ }),

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


// Copyright (c) David Brochart
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MODULE_NAME = exports.MODULE_VERSION = void 0;
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
// eslint-disable-next-line @typescript-eslint/no-var-requires
const data = __webpack_require__(/*! ../package.json */ "./package.json");
/**
 * The _model_module_version/_view_module_version this package implements.
 *
 * The html widget manager assumes that this is the same as the npm package
 * version number.
 */
exports.MODULE_VERSION = data.version;
/*
 * The current package name.
 */
exports.MODULE_NAME = data.name;
//# sourceMappingURL=version.js.map

/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


// Copyright (c) David Brochart
// Distributed under the terms of the Modified BSD License.
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MapView = exports.MapModel = void 0;
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const bertin = __importStar(__webpack_require__(/*! bertin */ "webpack/sharing/consume/default/bertin/bertin"));
const d3_geo = __importStar(__webpack_require__(/*! d3-geo */ "./node_modules/d3-geo/src/index.js"));
const d3_geo_projection = __importStar(__webpack_require__(/*! d3-geo-projection */ "webpack/sharing/consume/default/d3-geo-projection/d3-geo-projection"));
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
class MapModel extends base_1.DOMWidgetModel {
    defaults() {
        return Object.assign(Object.assign({}, super.defaults()), { _model_name: MapModel.model_name, _model_module: MapModel.model_module, _model_module_version: MapModel.model_module_version, _view_name: MapModel.view_name, _view_module: MapModel.view_module, _view_module_version: MapModel.view_module_version, options: {} });
    }
}
exports.MapModel = MapModel;
MapModel.serializers = Object.assign({}, base_1.DOMWidgetModel.serializers);
MapModel.model_name = 'MapModel';
MapModel.model_module = version_1.MODULE_NAME;
MapModel.model_module_version = version_1.MODULE_VERSION;
MapModel.view_name = 'MapView'; // Set to null if no view
MapModel.view_module = version_1.MODULE_NAME; // Set to null if no view
MapModel.view_module_version = version_1.MODULE_VERSION;
class MapView extends base_1.DOMWidgetView {
    render() {
        d3_geo;
        d3_geo_projection;
        this.map = null;
        this.options_changed();
        this.model.on('change:options', this.options_changed, this);
    }
    options_changed() {
        const options = this.model.get('options');
        const pyParams = options.params;
        let params = {};
        for (const p in pyParams) {
            if (p === 'projection') {
                let code = pyParams[p];
                let i = code.indexOf('.');
                let lib = code.slice(0, i);
                lib = lib.replaceAll('-', '_');
                code = lib.concat(code.slice(i));
                params[p] = eval(code);
            }
            else if (p === 'extent') {
                params[p] = JSON.parse(pyParams[p]);
            }
            else {
                params[p] = pyParams[p];
            }
        }
        const pyLayers = options.layers;
        let layers = [];
        for (const l of pyLayers) {
            let layer = {};
            for (const p in l) {
                if (p === 'geojson') {
                    const s = l[p].trim();
                    if (s.startsWith('{')) {
                        layer[p] = JSON.parse(l[p]);
                    }
                    else {
                        layer[p] = eval(s);
                    }
                }
                else {
                    layer[p] = l[p];
                }
            }
            layers.push(layer);
        }
        if (this.map !== null) {
            this.el.removeChild(this.map);
        }
        this.map = this.el.appendChild(bertin.draw({
            params,
            layers,
        }));
    }
}
exports.MapView = MapView;
//# sourceMappingURL=widget.js.map

/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

module.exports = JSON.parse('{"name":"ipybertin","version":"0.1.0","description":"A Jupyter - Bertin.js bridge","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/davidbrochart/ipybertin","bugs":{"url":"https://github.com/davidbrochart/ipybertin/issues"},"license":"BSD-3-Clause","author":{"name":"David Brochart","email":"david.brochart@gmail.com"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/davidbrochart/ipybertin"},"scripts":{"build":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension:dev","build:prod":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack","clean":"yarn run clean:lib && yarn run clean:nbextension && yarn run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf ipybertin/labextension","clean:nbextension":"rimraf ipybertin/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"yarn run build:lib","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode=development","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@jupyter-widgets/base":"^1.1.10 || ^2.0.0 || ^3.0.0 || ^4.0.0","bertin":"^0.12.0","d3":"^7.4.4","d3-geo-projection":"^4.0.0"},"devDependencies":{"@babel/core":"^7.5.0","@babel/preset-env":"^7.5.0","@jupyterlab/builder":"^3.0.0","@phosphor/application":"^1.6.0","@phosphor/widgets":"^1.6.0","@types/d3":"^7.4.0","@types/jest":"^26.0.0","@types/webpack-env":"^1.13.6","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-config-prettier":"^6.11.0","eslint-plugin-prettier":"^3.1.4","fs-extra":"^7.0.0","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webpack":"^5.61.0","webpack-cli":"^4.0.0"},"jupyterlab":{"extension":"lib/plugin","outputDir":"ipybertin/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_plugin_js.f3b43594da2edc2154e3.js.map