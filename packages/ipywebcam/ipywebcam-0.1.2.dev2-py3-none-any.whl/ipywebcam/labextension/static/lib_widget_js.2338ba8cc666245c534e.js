(self["webpackChunkipywebcam"] = self["webpackChunkipywebcam"] || []).push([["lib_widget_js"],{

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

// Copyright (c) Xiaojing Chen
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

/***/ "./lib/webrtc.js":
/*!***********************!*\
  !*** ./lib/webrtc.js ***!
  \***********************/
/***/ (function(__unused_webpack_module, exports) {

"use strict";

/* eslint-disable @typescript-eslint/no-non-null-assertion */
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.negotiate = exports.waitForConnectionState = exports.createPeerConnection = void 0;
const DEFAULT_ICE_SERVERS = [
    { urls: ['stun:stun.l.google.com:19302'] },
    { urls: ['stun:23.21.150.121'] },
    { urls: ['stun:stun01.sipphone.com'] },
    { urls: ['stun:stun.ekiga.net'] },
    { urls: ['stun:stun.fwdnet.net'] },
    { urls: ['stun:stun.ideasip.com'] },
    { urls: ['stun:stun.iptel.org'] },
    { urls: ['stun:stun.rixtelecom.se'] },
    { urls: ['stun:stun.schlund.de'] },
    { urls: ['stun:stunserver.org'] },
    { urls: ['stun:stun.softjoys.com'] },
    { urls: ['stun:stun.voiparound.com'] },
    { urls: ['stun:stun.voipbuster.com'] },
    { urls: ['stun:stun.voipstunt.com'] },
    { urls: ['stun:stun.voxgratia.org'] },
    { urls: ['stun:stun.xten.com'] },
];
function createPeerConnection(config) {
    const pc = new RTCPeerConnection(Object.assign({}, { iceServers: DEFAULT_ICE_SERVERS }, config || {}));
    // register some listeners to help debugging
    pc.addEventListener('icegatheringstatechange', () => {
        console.log(`iceGathering -> ${pc.iceGatheringState}`);
    }, false);
    pc.addEventListener('iceconnectionstatechange', () => {
        console.log(`iceConnection -> ${pc.iceConnectionState}`);
    }, false);
    pc.addEventListener('signalingstatechange', () => {
        console.log(`signaling -> ${pc.signalingState}`);
    }, false);
    return pc;
}
exports.createPeerConnection = createPeerConnection;
function waitForConnectionState(pc, checker) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => {
            if (checker(pc.connectionState)) {
                resolve(pc.connectionState);
            }
            else {
                const checkState = () => {
                    if (checker(pc.connectionState)) {
                        pc.removeEventListener('connectionstatechange', checkState);
                        resolve(pc.connectionState);
                    }
                };
                pc.addEventListener('connectionstatechange', checkState);
            }
        });
    });
}
exports.waitForConnectionState = waitForConnectionState;
function waitIceGathering(pc) {
    return __awaiter(this, void 0, void 0, function* () {
        return new Promise((resolve) => {
            if (pc.iceGatheringState === 'complete') {
                resolve();
            }
            else {
                const checkState = () => {
                    if (pc.iceGatheringState === 'complete') {
                        pc.removeEventListener('icegatheringstatechange', checkState);
                        resolve();
                    }
                };
                pc.addEventListener('icegatheringstatechange', checkState);
            }
        });
    });
}
function negotiate(pc, offerFunc, codec) {
    return __awaiter(this, void 0, void 0, function* () {
        let offer = yield pc.createOffer();
        yield pc.setLocalDescription(offer);
        yield waitIceGathering(pc);
        offer = pc.localDescription;
        if (codec) {
            if (codec.audio && codec.audio !== 'default') {
                offer.sdp = sdpFilterCodec('audio', codec.audio, offer.sdp);
            }
            if (codec.video && codec.video !== 'default') {
                offer.sdp = sdpFilterCodec('video', codec.video, offer.sdp);
            }
        }
        const remoteOffer = yield offerFunc(offer);
        yield pc.setRemoteDescription(remoteOffer);
    });
}
exports.negotiate = negotiate;
function arrayInclude(arr, target) {
    return !!~arr.indexOf(target);
}
function sdpFilterCodec(kind, codec, realSdp) {
    const allowed = [];
    const rtxRegex = new RegExp('a=fmtp:(\\d+) apt=(\\d+)\\r$');
    const codecRegex = new RegExp('a=rtpmap:([0-9]+) ' + escapeRegExp(codec));
    const videoRegex = new RegExp('(m=' + kind + ' .*?)( ([0-9]+))*\\s*$');
    const lines = realSdp.split('\n');
    let isKind = false;
    for (let i = 0; i < lines.length; i++) {
        if (lines[i].startsWith('m=' + kind + ' ')) {
            isKind = true;
        }
        else if (lines[i].startsWith('m=')) {
            isKind = false;
        }
        if (isKind) {
            let match = lines[i].match(codecRegex);
            if (match) {
                allowed.push(parseInt(match[1]));
            }
            match = lines[i].match(rtxRegex);
            if (match && arrayInclude(allowed, parseInt(match[2]))) {
                allowed.push(parseInt(match[1]));
            }
        }
    }
    const skipRegex = 'a=(fmtp|rtcp-fb|rtpmap):([0-9]+)';
    let sdp = '';
    isKind = false;
    for (let i = 0; i < lines.length; i++) {
        if (lines[i].startsWith('m=' + kind + ' ')) {
            isKind = true;
        }
        else if (lines[i].startsWith('m=')) {
            isKind = false;
        }
        if (isKind) {
            const skipMatch = lines[i].match(skipRegex);
            if (skipMatch && !arrayInclude(allowed, parseInt(skipMatch[2]))) {
                continue;
            }
            else if (lines[i].match(videoRegex)) {
                sdp += lines[i].replace(videoRegex, '$1 ' + allowed.join(' ')) + '\n';
            }
            else {
                sdp += lines[i] + '\n';
            }
        }
        else {
            sdp += lines[i] + '\n';
        }
    }
    return sdp;
}
function escapeRegExp(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); // $& means the whole matched string
}
//# sourceMappingURL=webrtc.js.map

/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

// Copyright (c) Xiaojing Chen
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.WebCamView = exports.WebCamModel = void 0;
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const webrtc_1 = __webpack_require__(/*! ./webrtc */ "./lib/webrtc.js");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
// Import the CSS
__webpack_require__(/*! ../css/widget.css */ "./css/widget.css");
class WebCamModel extends base_1.DOMWidgetModel {
    // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
    constructor(...args) {
        super(...args);
        this.resetPeer = () => {
            this.pc = undefined;
            this.client_stream = undefined;
            this.server_stream = undefined;
        };
        this.waitForStateWhen = (checker) => __awaiter(this, void 0, void 0, function* () {
            return new Promise((resolve) => {
                const state = this.get('state');
                if (checker(state)) {
                    resolve(state);
                }
                else {
                    const checkState = () => {
                        const state = this.get('state');
                        if (checker(state)) {
                            this.off('change:state', checkState);
                            resolve(state);
                        }
                    };
                    this.on('change:state', checkState);
                }
            });
        });
        this.waitForStateIn = (...states) => __awaiter(this, void 0, void 0, function* () {
            return this.waitForStateWhen((state) => states.indexOf(state) !== -1);
        });
        this.getState = () => this.get('state');
        this.setState = (state) => {
            this.set('state', state);
        };
        this.closePeer = () => __awaiter(this, void 0, void 0, function* () {
            const state = yield this.waitForStateIn('closed', 'connected', 'error');
            const pc = this.pc;
            if (!pc || state === 'closed' || state === 'error') {
                return;
            }
            this.setState('closing');
            try {
                this.resetPeer();
                pc.close();
                if (pc.connectionState !== 'closed') {
                    yield new Promise((resolve) => {
                        pc.addEventListener('connectionstatechange', () => {
                            if (pc.connectionState === 'closed') {
                                resolve();
                            }
                        });
                    });
                }
                this.setState('closed');
            }
            catch (err) {
                this.setState('error');
            }
        });
        this.fetchDevices = () => __awaiter(this, void 0, void 0, function* () {
            console.log('fetchDevices');
            let devices = yield navigator.mediaDevices.enumerateDevices();
            devices = devices.filter((device) => device.kind === 'videoinput');
            console.log(devices);
            this.set('devices', devices);
            this.save_changes();
        });
        this.getPeerConfig = () => {
            const config = {};
            const iceServers = this.get('iceServers');
            if (iceServers && iceServers.length > 0) {
                config.iceServers = iceServers.map((server) => {
                    if (typeof server === 'string') {
                        return { urls: server };
                    }
                    else {
                        return server;
                    }
                });
            }
            return config;
        };
        this.connect = (video, force_new_pc = false) => __awaiter(this, void 0, void 0, function* () {
            const state = yield this.waitForStateIn('closed', 'connected', 'error');
            if (state === 'closed' || state === 'error') {
                try {
                    this.setState('connecting');
                    const pc = webrtc_1.createPeerConnection(this.getPeerConfig());
                    this.pc = pc;
                    this.bindVideo(video);
                    pc.addEventListener('connectionstatechange', () => {
                        const state = pc.connectionState;
                        if (state === 'failed' ||
                            state === 'disconnected' ||
                            state === 'closed') {
                            pc.close();
                            if (this.pc === pc) {
                                this.resetPeer();
                            }
                        }
                    });
                    pc.addEventListener('track', (evt) => {
                        if (evt.track.kind === 'video') {
                            console.log('track gotten');
                            this.server_stream = evt.streams[0];
                        }
                    });
                    const device = this.get('device');
                    const constraints = {
                        audio: false,
                        video: device ? { deviceId: device.deviceId } : true,
                    };
                    const stream = yield navigator.mediaDevices.getUserMedia(constraints);
                    this.client_stream = stream;
                    stream.getTracks().forEach((track) => {
                        pc.addTrack(track, stream);
                    });
                    yield webrtc_1.negotiate(pc, (offer) => {
                        console.log(offer);
                        return new Promise((resolve) => {
                            this.set('client_desc', offer);
                            this.save_changes();
                            this.on('change:server_desc', () => {
                                resolve(this.get('server_desc'));
                            });
                        });
                    });
                    const pcState = yield webrtc_1.waitForConnectionState(pc, (state) => state !== 'connecting');
                    if (pcState === 'connected') {
                        this.setState('connected');
                    }
                    else {
                        yield this.closePeer();
                    }
                }
                catch (err) {
                    this.setState('error');
                    console.error(err);
                }
            }
            else if (force_new_pc) {
                yield this.closePeer();
                yield this.connect(video, force_new_pc);
            }
            else {
                this.bindVideo(video);
            }
        });
        this.bindVideo = (video) => {
            const pc = this.pc;
            if (!pc || !video) {
                return;
            }
            if (pc.connectionState === 'connected' && this.server_stream) {
                video.srcObject = this.server_stream;
            }
            else {
                const handler = (evt) => {
                    if (evt.track.kind === 'video') {
                        console.log('track gotten');
                        this.server_stream = evt.streams[0];
                        video.srcObject = this.server_stream;
                        pc.removeEventListener('track', handler);
                    }
                };
                pc.addEventListener('track', handler);
            }
        };
        this.fetchDevices();
        this.on('change:device', () => {
            this.connect(undefined, true);
        });
        this.on('change:iceServers', () => {
            this.connect(undefined, true);
        });
    }
    defaults() {
        return Object.assign(Object.assign({}, super.defaults()), { _model_name: WebCamModel.model_name, _model_module: WebCamModel.model_module, _model_module_version: WebCamModel.model_module_version, _view_name: WebCamModel.view_name, _view_module: WebCamModel.view_module, _view_module_version: WebCamModel.view_module_version, server_desc: null, client_desc: null, iceServers: [], devices: [], device: null, state: 'closed', autoplay: true, controls: true, crossOrigin: 'not-support', width: null, height: null, playsInline: true, muted: false });
    }
}
exports.WebCamModel = WebCamModel;
WebCamModel.serializers = Object.assign({}, base_1.DOMWidgetModel.serializers);
WebCamModel.model_name = 'WebCamModel';
WebCamModel.model_module = version_1.MODULE_NAME;
WebCamModel.model_module_version = version_1.MODULE_VERSION;
WebCamModel.view_name = 'WebCamView'; // Set to null if no view
WebCamModel.view_module = version_1.MODULE_NAME; // Set to null if no view
WebCamModel.view_module_version = version_1.MODULE_VERSION;
class WebCamView extends base_1.DOMWidgetView {
    render() {
        const video = document.createElement('video');
        video.playsInline = true;
        this.el.appendChild(video);
        this.model.connect(video);
        this.model.on('change:state', () => {
            const model = this.model;
            if (model.getState() === 'connected') {
                model.connect(video);
            }
        });
        video.autoplay = this.model.get('autoplay');
        this.model.on('change:autoplay', () => {
            video.autoplay = this.model.get('autoplay');
        });
        video.controls = this.model.get('controls');
        this.model.on('change:controls', () => {
            video.controls = this.model.get('controls');
        });
        const width = this.model.get('width');
        if (width) {
            video.width = width;
        }
        this.model.on('change:width', () => {
            const width = this.model.get('width');
            if (width) {
                video.width = width;
            }
        });
        const height = this.model.get('height');
        if (height) {
            video.height = height;
        }
        this.model.on('change:height', () => {
            const height = this.model.get('height');
            if (height) {
                video.height = height;
            }
        });
        video.playsInline = this.model.get('playsInline');
        this.model.on('change:playsInline', () => {
            video.playsInline = this.model.get('playsInline');
        });
        video.muted = this.model.get('muted');
        this.model.on('change:muted', () => {
            video.muted = this.model.get('muted');
        });
        const crossOrigin = this.model.get('crossOrigin');
        if (crossOrigin === 'not-support') {
            video.crossOrigin = null;
        }
        else {
            video.crossOrigin = crossOrigin;
        }
        this.model.on('change:crossOrigin', () => {
            const crossOrigin = this.model.get('crossOrigin');
            if (crossOrigin === 'not-support') {
                video.crossOrigin = null;
            }
            else {
                video.crossOrigin = crossOrigin;
            }
        });
    }
}
exports.WebCamView = WebCamView;
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
module.exports = JSON.parse('{"name":"ipywebcam","version":"0.1.0","description":"A Custom Jupyter Widget Library for Web Camera using WebRTC","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/vipcxj/ipywebcam","bugs":{"url":"https://github.com/vipcxj/ipywebcam/issues"},"license":"BSD-3-Clause","author":{"name":"Xiaojing Chen","email":"vipcxj@126.com"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/vipcxj/ipywebcam"},"scripts":{"build":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension:dev","build:prod":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack","clean":"yarn run clean:lib && yarn run clean:nbextension && yarn run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf ipywebcam/labextension","clean:nbextension":"rimraf ipywebcam/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"yarn run build:lib","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode=development","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@jupyter-widgets/base":"^1.1.10 || ^2 || ^3 || ^4 || ^5 || ^6"},"devDependencies":{"@babel/core":"^7.5.0","@babel/preset-env":"^7.5.0","@jupyter-widgets/base-manager":"^1.0.2","@jupyterlab/builder":"^3.0.0","@lumino/application":"^1.6.0","@lumino/widgets":"^1.6.0","@types/jest":"^26.0.0","@types/webpack-env":"^1.13.6","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-config-prettier":"^6.11.0","eslint-plugin-prettier":"^3.1.4","fs-extra":"^7.0.0","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webpack":"^5.61.0","webpack-cli":"^4.0.0"},"jupyterlab":{"extension":"lib/plugin","outputDir":"ipywebcam/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_widget_js.2338ba8cc666245c534e.js.map