(self["webpackChunkipylgbst"] = self["webpackChunkipylgbst"] || []).push([["lib_widget_js"],{

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

// Copyright (c) Thorsten Beier
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

"use strict";

// Copyright (c) Dr. Thorsten Beier
// Distributed under the terms of the Modified BSD License.
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.LegoBoostView = exports.LegoBoostModel = void 0;
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
// Import the CSS
__webpack_require__(/*! ../css/widget.css */ "./css/widget.css");
const lego_boost_browser_1 = __importDefault(__webpack_require__(/*! lego-boost-browser */ "webpack/sharing/consume/default/lego-boost-browser/lego-boost-browser"));
let boost = new lego_boost_browser_1.default();
class LegoBoostModel extends base_1.DOMWidgetModel {
    constructor() {
        super(...arguments);
        this.polling_is_running = false;
        this.stop_polling = false;
        this.currentProcessing = Promise.resolve();
    }
    defaults() {
        return Object.assign(Object.assign({}, super.defaults()), { _model_name: LegoBoostModel.model_name, _model_module: LegoBoostModel.model_module, _model_module_version: LegoBoostModel.model_module_version, _view_name: LegoBoostModel.view_name, _view_module: LegoBoostModel.view_module, _view_module_version: LegoBoostModel.view_module_version, polling_frame: 0, command_frame: 0, device_info: {} });
    }
    poll() {
        this.set('device_info', this.boost.deviceInfo);
        this.set('polling_frame', this.get('polling_frame') + 1);
        this.save_changes();
    }
    polling() {
        this.poll();
        if (!this.stop_polling) {
            this.polling_is_running = true;
            setTimeout(this.polling.bind(this), 200);
        }
        else {
            this.polling_is_running = false;
        }
    }
    initialize(attributes, options) {
        console.log("INITIALIZE");
        super.initialize(attributes, options);
        this.boost = boost; //new LegoBoost();
        this.on('msg:custom', (command, buffers) => {
            this.currentProcessing = this.currentProcessing.then(() => __awaiter(this, void 0, void 0, function* () {
                yield this.onCommand(command, buffers);
                this.set('command_frame', this.get('command_frame') + 1);
                this.save_changes();
            }));
        });
    }
    onCommand(command, buffers) {
        return __awaiter(this, void 0, void 0, function* () {
            console.log("onCommand", command);
            const cmd = command['command'];
            const args = command['args'];
            if (cmd === "connect") {
                yield this.connect();
            }
            else if (cmd === "disconnect") {
                this.disconnect();
            }
            else {
                if (this.boost.deviceInfo.connected) {
                    switch (cmd) {
                        case "poll":
                            this.poll();
                            break;
                        case "drive":
                            yield this.boost.drive.apply(this.boost, args);
                            break;
                        case "turn":
                            yield this.boost.turn.apply(this.boost, args);
                            break;
                        case "driveUntil":
                            yield this.boost.driveUntil.apply(this.boost, args);
                            break;
                        case "turnUntil":
                            yield this.boost.turnUntil.apply(this.boost, args);
                            break;
                        case "ledAsync":
                            yield this.boost.ledAsync.apply(this.boost, args);
                            break;
                        case "motorTime":
                            yield this.boost.motorTime.apply(this.boost, args);
                            break;
                        case "motorTimeMulti":
                            yield this.boost.motorTimeMulti.apply(this.boost, args);
                            break;
                        case "motorTimeAsync":
                            yield this.boost.motorTimeAsync.apply(this.boost, args);
                            break;
                        case "motorTimeMultiAsync":
                            yield this.boost.motorTimeMultiAsync.apply(this.boost, args);
                            break;
                        case "motorAngle":
                            yield this.boost.motorAngle.apply(this.boost, args);
                            break;
                        case "motorAngleMulti":
                            yield this.boost.motorAngleMulti.apply(this.boost, args);
                            break;
                        case "motorAngleAsync":
                            yield this.boost.motorAngleAsync.apply(this.boost, args);
                            break;
                        case "motorAngleMultiAsync":
                            yield this.boost.motorAngleMultiAsync.apply(this.boost, args);
                            break;
                        default:
                            console.log(`unknown command "${cmd}"`);
                            break;
                    }
                }
                else {
                    console.log(`cannot run command ${cmd} since we are not connected`);
                }
            }
        });
    }
    connect() {
        return __awaiter(this, void 0, void 0, function* () {
            const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
            if (!this.boost.deviceInfo.connected) {
                yield this.boost.connect();
                for (let i = 0; i < 30; i++) {
                    // console.log("pre sleep")
                    yield sleep(100);
                    // console.log("post sleep")
                    if (this.boost.deviceInfo.connected && this.boost.hub !== undefined && this.boost.hub.connected) {
                        console.log("early exit1");
                        break;
                    }
                }
                yield sleep(4000);
            }
            else {
                console.log("alreay connected");
            }
            if (!this.polling_is_running) {
                this.polling_is_running = true;
                this.polling();
            }
        });
    }
    disconnect() {
        console.log("disconnect");
        this.boost.disconnect();
    }
    dispose() {
        console.log('remove model');
    }
}
exports.LegoBoostModel = LegoBoostModel;
LegoBoostModel.serializers = Object.assign({}, base_1.DOMWidgetModel.serializers);
LegoBoostModel.model_name = 'LegoBoostModel';
LegoBoostModel.model_module = version_1.MODULE_NAME;
LegoBoostModel.model_module_version = version_1.MODULE_VERSION;
LegoBoostModel.view_name = 'LegoBoostView'; // Set to null if no view
LegoBoostModel.view_module = version_1.MODULE_NAME; // Set to null if no view
LegoBoostModel.view_module_version = version_1.MODULE_VERSION;
class LegoBoostView extends base_1.DOMWidgetView {
    render() {
        this.el.classList.add('custom-widget');
        this.txt_pitch = document.createElement("div");
        this.txt_pitch.textContent = "pitch:";
        this.el.appendChild(this.txt_pitch);
        this.meter_pitch = document.createElement('meter');
        this.el.appendChild(this.meter_pitch);
        this.meter_pitch.min = -90;
        this.meter_pitch.max = 90;
        this.el.appendChild(document.createElement("br"));
        this.txt_roll = document.createElement("div");
        this.txt_roll.textContent = "roll:";
        this.el.appendChild(this.txt_roll);
        this.meter_roll = document.createElement('meter');
        this.el.appendChild(this.meter_roll);
        this.meter_roll.min = -90;
        this.meter_roll.max = 90;
        this.el.appendChild(document.createElement("br"));
        this.txt_distance = document.createElement("div");
        this.txt_distance.textContent = "distance:";
        this.el.appendChild(this.txt_distance);
        this.meter_distance = document.createElement('meter');
        this.el.appendChild(this.meter_distance);
        this.meter_distance.min = 0;
        this.meter_distance.max = 255;
        this.changes();
        this.model.on('change:polling_frame', this.changes, this);
    }
    changes() {
        let b = (this.model);
        const di = b.boost.deviceInfo;
        if (di.connected !== undefined && di.connected) {
            this.meter_roll.value = di['tilt']['roll'];
            this.txt_roll.textContent = `roll: ${di['tilt']['roll']}`;
            this.meter_pitch.value = di['tilt']['pitch'];
            this.txt_pitch.textContent = `pitch: ${di['tilt']['pitch']}`;
            const d = di['distance'];
            if (d !== undefined && d !== null && isFinite(d)) {
                this.meter_distance.value = d;
                this.txt_distance.textContent = `distance: ${d}`;
            }
            else {
                this.meter_distance.value = 255;
                this.txt_distance.textContent = `distance: ∞`;
            }
        }
    }
    remove() {
        // this.stop_polling = true;
        let b = (this.model);
        b.stop_polling = true;
    }
}
exports.LegoBoostView = LegoBoostView;
//# sourceMappingURL=widget.js.map

/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js!./css/widget.css":
/*!**************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./css/widget.css ***!
  \**************************************************************/
/***/ ((module, exports, __webpack_require__) => {

// Imports
var ___CSS_LOADER_API_IMPORT___ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
exports = ___CSS_LOADER_API_IMPORT___(false);
// Module
exports.push([module.id, ".custom-widget {\n  background-color: lightseagreen;\n  padding: 0px 2px;\n}\n", ""]);
// Exports
module.exports = exports;


/***/ }),

/***/ "./node_modules/css-loader/dist/runtime/api.js":
/*!*****************************************************!*\
  !*** ./node_modules/css-loader/dist/runtime/api.js ***!
  \*****************************************************/
/***/ ((module) => {

"use strict";


/*
  MIT License http://www.opensource.org/licenses/mit-license.php
  Author Tobias Koppers @sokra
*/
// css base code, injected by the css-loader
// eslint-disable-next-line func-names
module.exports = function (useSourceMap) {
  var list = []; // return the list of modules as css string

  list.toString = function toString() {
    return this.map(function (item) {
      var content = cssWithMappingToString(item, useSourceMap);

      if (item[2]) {
        return "@media ".concat(item[2], " {").concat(content, "}");
      }

      return content;
    }).join('');
  }; // import a list of modules into the list
  // eslint-disable-next-line func-names


  list.i = function (modules, mediaQuery, dedupe) {
    if (typeof modules === 'string') {
      // eslint-disable-next-line no-param-reassign
      modules = [[null, modules, '']];
    }

    var alreadyImportedModules = {};

    if (dedupe) {
      for (var i = 0; i < this.length; i++) {
        // eslint-disable-next-line prefer-destructuring
        var id = this[i][0];

        if (id != null) {
          alreadyImportedModules[id] = true;
        }
      }
    }

    for (var _i = 0; _i < modules.length; _i++) {
      var item = [].concat(modules[_i]);

      if (dedupe && alreadyImportedModules[item[0]]) {
        // eslint-disable-next-line no-continue
        continue;
      }

      if (mediaQuery) {
        if (!item[2]) {
          item[2] = mediaQuery;
        } else {
          item[2] = "".concat(mediaQuery, " and ").concat(item[2]);
        }
      }

      list.push(item);
    }
  };

  return list;
};

function cssWithMappingToString(item, useSourceMap) {
  var content = item[1] || ''; // eslint-disable-next-line prefer-destructuring

  var cssMapping = item[3];

  if (!cssMapping) {
    return content;
  }

  if (useSourceMap && typeof btoa === 'function') {
    var sourceMapping = toComment(cssMapping);
    var sourceURLs = cssMapping.sources.map(function (source) {
      return "/*# sourceURL=".concat(cssMapping.sourceRoot || '').concat(source, " */");
    });
    return [content].concat(sourceURLs).concat([sourceMapping]).join('\n');
  }

  return [content].join('\n');
} // Adapted from convert-source-map (MIT)


function toComment(sourceMap) {
  // eslint-disable-next-line no-undef
  var base64 = btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap))));
  var data = "sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(base64);
  return "/*# ".concat(data, " */");
}

/***/ }),

/***/ "./css/widget.css":
/*!************************!*\
  !*** ./css/widget.css ***!
  \************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var api = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
            var content = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./widget.css */ "./node_modules/css-loader/dist/cjs.js!./css/widget.css");

            content = content.__esModule ? content.default : content;

            if (typeof content === 'string') {
              content = [[module.id, content, '']];
            }

var options = {};

options.insert = "head";
options.singleton = false;

var update = api(content, options);



module.exports = content.locals || {};

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js":
/*!****************************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js ***!
  \****************************************************************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

"use strict";


var isOldIE = function isOldIE() {
  var memo;
  return function memorize() {
    if (typeof memo === 'undefined') {
      // Test for IE <= 9 as proposed by Browserhacks
      // @see http://browserhacks.com/#hack-e71d8692f65334173fee715c222cb805
      // Tests for existence of standard globals is to allow style-loader
      // to operate correctly into non-standard environments
      // @see https://github.com/webpack-contrib/style-loader/issues/177
      memo = Boolean(window && document && document.all && !window.atob);
    }

    return memo;
  };
}();

var getTarget = function getTarget() {
  var memo = {};
  return function memorize(target) {
    if (typeof memo[target] === 'undefined') {
      var styleTarget = document.querySelector(target); // Special case to return head of iframe instead of iframe itself

      if (window.HTMLIFrameElement && styleTarget instanceof window.HTMLIFrameElement) {
        try {
          // This will throw an exception if access to iframe is blocked
          // due to cross-origin restrictions
          styleTarget = styleTarget.contentDocument.head;
        } catch (e) {
          // istanbul ignore next
          styleTarget = null;
        }
      }

      memo[target] = styleTarget;
    }

    return memo[target];
  };
}();

var stylesInDom = [];

function getIndexByIdentifier(identifier) {
  var result = -1;

  for (var i = 0; i < stylesInDom.length; i++) {
    if (stylesInDom[i].identifier === identifier) {
      result = i;
      break;
    }
  }

  return result;
}

function modulesToDom(list, options) {
  var idCountMap = {};
  var identifiers = [];

  for (var i = 0; i < list.length; i++) {
    var item = list[i];
    var id = options.base ? item[0] + options.base : item[0];
    var count = idCountMap[id] || 0;
    var identifier = "".concat(id, " ").concat(count);
    idCountMap[id] = count + 1;
    var index = getIndexByIdentifier(identifier);
    var obj = {
      css: item[1],
      media: item[2],
      sourceMap: item[3]
    };

    if (index !== -1) {
      stylesInDom[index].references++;
      stylesInDom[index].updater(obj);
    } else {
      stylesInDom.push({
        identifier: identifier,
        updater: addStyle(obj, options),
        references: 1
      });
    }

    identifiers.push(identifier);
  }

  return identifiers;
}

function insertStyleElement(options) {
  var style = document.createElement('style');
  var attributes = options.attributes || {};

  if (typeof attributes.nonce === 'undefined') {
    var nonce =  true ? __webpack_require__.nc : 0;

    if (nonce) {
      attributes.nonce = nonce;
    }
  }

  Object.keys(attributes).forEach(function (key) {
    style.setAttribute(key, attributes[key]);
  });

  if (typeof options.insert === 'function') {
    options.insert(style);
  } else {
    var target = getTarget(options.insert || 'head');

    if (!target) {
      throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");
    }

    target.appendChild(style);
  }

  return style;
}

function removeStyleElement(style) {
  // istanbul ignore if
  if (style.parentNode === null) {
    return false;
  }

  style.parentNode.removeChild(style);
}
/* istanbul ignore next  */


var replaceText = function replaceText() {
  var textStore = [];
  return function replace(index, replacement) {
    textStore[index] = replacement;
    return textStore.filter(Boolean).join('\n');
  };
}();

function applyToSingletonTag(style, index, remove, obj) {
  var css = remove ? '' : obj.media ? "@media ".concat(obj.media, " {").concat(obj.css, "}") : obj.css; // For old IE

  /* istanbul ignore if  */

  if (style.styleSheet) {
    style.styleSheet.cssText = replaceText(index, css);
  } else {
    var cssNode = document.createTextNode(css);
    var childNodes = style.childNodes;

    if (childNodes[index]) {
      style.removeChild(childNodes[index]);
    }

    if (childNodes.length) {
      style.insertBefore(cssNode, childNodes[index]);
    } else {
      style.appendChild(cssNode);
    }
  }
}

function applyToTag(style, options, obj) {
  var css = obj.css;
  var media = obj.media;
  var sourceMap = obj.sourceMap;

  if (media) {
    style.setAttribute('media', media);
  } else {
    style.removeAttribute('media');
  }

  if (sourceMap && typeof btoa !== 'undefined') {
    css += "\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap)))), " */");
  } // For old IE

  /* istanbul ignore if  */


  if (style.styleSheet) {
    style.styleSheet.cssText = css;
  } else {
    while (style.firstChild) {
      style.removeChild(style.firstChild);
    }

    style.appendChild(document.createTextNode(css));
  }
}

var singleton = null;
var singletonCounter = 0;

function addStyle(obj, options) {
  var style;
  var update;
  var remove;

  if (options.singleton) {
    var styleIndex = singletonCounter++;
    style = singleton || (singleton = insertStyleElement(options));
    update = applyToSingletonTag.bind(null, style, styleIndex, false);
    remove = applyToSingletonTag.bind(null, style, styleIndex, true);
  } else {
    style = insertStyleElement(options);
    update = applyToTag.bind(null, style, options);

    remove = function remove() {
      removeStyleElement(style);
    };
  }

  update(obj);
  return function updateStyle(newObj) {
    if (newObj) {
      if (newObj.css === obj.css && newObj.media === obj.media && newObj.sourceMap === obj.sourceMap) {
        return;
      }

      update(obj = newObj);
    } else {
      remove();
    }
  };
}

module.exports = function (list, options) {
  options = options || {}; // Force single-tag solution on IE6-9, which has a hard limit on the # of <style>
  // tags it will allow on a page

  if (!options.singleton && typeof options.singleton !== 'boolean') {
    options.singleton = isOldIE();
  }

  list = list || [];
  var lastIdentifiers = modulesToDom(list, options);
  return function update(newList) {
    newList = newList || [];

    if (Object.prototype.toString.call(newList) !== '[object Array]') {
      return;
    }

    for (var i = 0; i < lastIdentifiers.length; i++) {
      var identifier = lastIdentifiers[i];
      var index = getIndexByIdentifier(identifier);
      stylesInDom[index].references--;
    }

    var newLastIdentifiers = modulesToDom(newList, options);

    for (var _i = 0; _i < lastIdentifiers.length; _i++) {
      var _identifier = lastIdentifiers[_i];

      var _index = getIndexByIdentifier(_identifier);

      if (stylesInDom[_index].references === 0) {
        stylesInDom[_index].updater();

        stylesInDom.splice(_index, 1);
      }
    }

    lastIdentifiers = newLastIdentifiers;
  };
};

/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"name":"ipylgbst","version":"0.1.3","description":"A widget library for controlling LEGO® BOOST via web-bluetooth","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/DerThorsten/ipylgbst","bugs":{"url":"https://github.com/DerThorsten/ipylgbst/issues"},"license":"BSD-3-Clause","author":{"name":"Thorsten Beier","email":"derthorstenbeier@gmail.com"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/DerThorsten/ipylgbst"},"scripts":{"build":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension:dev","build:prod":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack","clean":"yarn run clean:lib && yarn run clean:nbextension && yarn run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf ipylgbst/labextension","clean:nbextension":"rimraf ipylgbst/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"yarn run build:lib","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode=development","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@jupyter-widgets/base":"^1.1.10 || ^2 || ^3 || ^4 || ^5 || ^6","add":"^2.0.6","ieee754":"^1.2.1","lego-boost-browser":"git+https://github.com/DerThorsten/lego-boost-browser.git"},"devDependencies":{"@babel/core":"^7.5.0","@babel/preset-env":"^7.5.0","@jupyter-widgets/base-manager":"^1.0.2","@jupyterlab/builder":"^3.0.0","@lumino/application":"^1.6.0","@lumino/widgets":"^1.6.0","@types/jest":"^26.0.0","@types/webpack-env":"^1.13.6","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-config-prettier":"^6.11.0","eslint-plugin-prettier":"^3.1.4","fs-extra":"^7.0.0","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webpack":"^5.61.0","webpack-cli":"^4.0.0"},"jupyterlab":{"extension":"lib/plugin","outputDir":"ipylgbst/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_widget_js.63b73ead37e2cffb243a.js.map