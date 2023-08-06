/******/ var __webpack_modules__ = ({

/***/ "./node_modules/js-cookie/dist/js.cookie.js":
/*!**************************************************!*\
  !*** ./node_modules/js-cookie/dist/js.cookie.js ***!
  \**************************************************/
/***/ (function(module) {

/*! js-cookie v3.0.1 | MIT */
;
(function (global, factory) {
   true ? module.exports = factory() :
  0;
}(this, (function () { 'use strict';

  /* eslint-disable no-var */
  function assign (target) {
    for (var i = 1; i < arguments.length; i++) {
      var source = arguments[i];
      for (var key in source) {
        target[key] = source[key];
      }
    }
    return target
  }
  /* eslint-enable no-var */

  /* eslint-disable no-var */
  var defaultConverter = {
    read: function (value) {
      if (value[0] === '"') {
        value = value.slice(1, -1);
      }
      return value.replace(/(%[\dA-F]{2})+/gi, decodeURIComponent)
    },
    write: function (value) {
      return encodeURIComponent(value).replace(
        /%(2[346BF]|3[AC-F]|40|5[BDE]|60|7[BCD])/g,
        decodeURIComponent
      )
    }
  };
  /* eslint-enable no-var */

  /* eslint-disable no-var */

  function init (converter, defaultAttributes) {
    function set (key, value, attributes) {
      if (typeof document === 'undefined') {
        return
      }

      attributes = assign({}, defaultAttributes, attributes);

      if (typeof attributes.expires === 'number') {
        attributes.expires = new Date(Date.now() + attributes.expires * 864e5);
      }
      if (attributes.expires) {
        attributes.expires = attributes.expires.toUTCString();
      }

      key = encodeURIComponent(key)
        .replace(/%(2[346B]|5E|60|7C)/g, decodeURIComponent)
        .replace(/[()]/g, escape);

      var stringifiedAttributes = '';
      for (var attributeName in attributes) {
        if (!attributes[attributeName]) {
          continue
        }

        stringifiedAttributes += '; ' + attributeName;

        if (attributes[attributeName] === true) {
          continue
        }

        // Considers RFC 6265 section 5.2:
        // ...
        // 3.  If the remaining unparsed-attributes contains a %x3B (";")
        //     character:
        // Consume the characters of the unparsed-attributes up to,
        // not including, the first %x3B (";") character.
        // ...
        stringifiedAttributes += '=' + attributes[attributeName].split(';')[0];
      }

      return (document.cookie =
        key + '=' + converter.write(value, key) + stringifiedAttributes)
    }

    function get (key) {
      if (typeof document === 'undefined' || (arguments.length && !key)) {
        return
      }

      // To prevent the for loop in the first place assign an empty array
      // in case there are no cookies at all.
      var cookies = document.cookie ? document.cookie.split('; ') : [];
      var jar = {};
      for (var i = 0; i < cookies.length; i++) {
        var parts = cookies[i].split('=');
        var value = parts.slice(1).join('=');

        try {
          var foundKey = decodeURIComponent(parts[0]);
          jar[foundKey] = converter.read(value, foundKey);

          if (key === foundKey) {
            break
          }
        } catch (e) {}
      }

      return key ? jar[key] : jar
    }

    return Object.create(
      {
        set: set,
        get: get,
        remove: function (key, attributes) {
          set(
            key,
            '',
            assign({}, attributes, {
              expires: -1
            })
          );
        },
        withAttributes: function (attributes) {
          return init(this.converter, assign({}, this.attributes, attributes))
        },
        withConverter: function (converter) {
          return init(assign({}, this.converter, converter), this.attributes)
        }
      },
      {
        attributes: { value: Object.freeze(defaultAttributes) },
        converter: { value: Object.freeze(converter) }
      }
    )
  }

  var api = init(defaultConverter, { path: '/' });
  /* eslint-enable no-var */

  return api;

})));


/***/ })

/******/ });
/************************************************************************/
/******/ // The module cache
/******/ var __webpack_module_cache__ = {};
/******/ 
/******/ // The require function
/******/ function __webpack_require__(moduleId) {
/******/ 	// Check if module is in cache
/******/ 	var cachedModule = __webpack_module_cache__[moduleId];
/******/ 	if (cachedModule !== undefined) {
/******/ 		return cachedModule.exports;
/******/ 	}
/******/ 	// Create a new module (and put it into the cache)
/******/ 	var module = __webpack_module_cache__[moduleId] = {
/******/ 		// no module.id needed
/******/ 		// no module.loaded needed
/******/ 		exports: {}
/******/ 	};
/******/ 
/******/ 	// Execute the module function
/******/ 	__webpack_modules__[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/ 
/******/ 	// Return the exports of the module
/******/ 	return module.exports;
/******/ }
/******/ 
/************************************************************************/
/******/ /* webpack/runtime/define property getters */
/******/ (() => {
/******/ 	// define getter functions for harmony exports
/******/ 	__webpack_require__.d = (exports, definition) => {
/******/ 		for(var key in definition) {
/******/ 			if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 				Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 			}
/******/ 		}
/******/ 	};
/******/ })();
/******/ 
/******/ /* webpack/runtime/hasOwnProperty shorthand */
/******/ (() => {
/******/ 	__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ })();
/******/ 
/******/ /* webpack/runtime/make namespace object */
/******/ (() => {
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = (exports) => {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/ })();
/******/ 
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
(() => {
/*!*************************!*\
  !*** ./web.ts/index.ts ***!
  \*************************/
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "MicropubClient": () => (/* binding */ MicropubClient),
/* harmony export */   "cookies": () => (/* binding */ cookies),
/* harmony export */   "createEl": () => (/* binding */ createEl),
/* harmony export */   "createEls": () => (/* binding */ createEls),
/* harmony export */   "error": () => (/* binding */ error),
/* harmony export */   "getBrowser": () => (/* binding */ getBrowser),
/* harmony export */   "load": () => (/* binding */ load),
/* harmony export */   "mouseup": () => (/* binding */ mouseup),
/* harmony export */   "offline": () => (/* binding */ offline),
/* harmony export */   "online": () => (/* binding */ online),
/* harmony export */   "popstate": () => (/* binding */ popstate),
/* harmony export */   "unload": () => (/* binding */ unload),
/* harmony export */   "upgradeTimestamps": () => (/* binding */ upgradeTimestamps)
/* harmony export */ });
// function bindWebActions() {
//     $$("indie-action").each(function() {
//         this.onclick = function(e) {
//             var action_link = this.querySelector("a");
//             // TODO action_link.attr("class", "fa fa-spinner fa-spin");
//
//             var action_do = this.getAttribute("do");
//             var action_with = this.getAttribute("with");
//
//             // protocolCheck("web+action://" + action_do + "?url=" + action_with,
//             // setTimeout(function() {
//             //     var url = "//canopy.garden/?origin=" + window.location.href +
//             //               "do=" + action_do + "&with=" + action_with;
//             //     var html = `<!--p>Your device does not support web
//             //                 actions<br><em><strong>or</strong></em><br>
//             //                 You have not yet paired your website with
//             //                 your browser</p>
//             //                 <hr-->
//             //                 <p>If you have a website that supports web
//             //                 actions enter it here:</p>
//             //                 <form id=action-handler action=/actions-finder>
//             //                 <label>Your Website
//             //                 <div class=bounding><input type=text
//             //                 name=url></div></label>
//             //                 <input type=hidden name=do value="${action_do}">
//             //                 <input type=hidden name=with value="${action_with}">
//             //                 <p><small>Target:
//             //                 <code>${action_with}</code></small></p>
//             //                 <button>${action_do}</button>
//             //                 </form>
//             //                 <p>If you do not you can create one <a
//             //                 href="${url}">here</a>.</p>`;
//             //     switch (action_do) {
//             //         case "sign-in":
//             //             html = html + `<p>If you are the owner of this site,
//             //                            <a href=/security/identification>sign
//             //                            in here</a>.</p>`;
//             //     }
//             //     html = html + `<p><small><a href=/help#web-actions>Learn
//             //                    more about web actions</a></small></p>`;
//             //     $("#webaction_help").innerHTML = html;
//             //     $("#webaction_help").style.display = "block";
//             //     $("#blackout").style.display = "block";
//             //     $("#blackout").onclick = function() {
//             //         $("#webaction_help").style.display = "none";
//             //         $("#blackout").style.display = "none";
//             //     };
//             // }, 200);
//
//             window.location = action_link.getAttribute("href");
//
//             e.preventDefault ? e.preventDefault() : e.returnValue = false;
//         }
//     });
// }
// $.load(function () {
//   bindWebActions()
//
//   /*
//     $$(".pubkey").each(function() {
//         var armored_pubkey = $(this).text();
//         if (armored_pubkey) {
//             var pubkey = get_pubkey(armored_pubkey);
//             var fingerprint = pubkey.fingerprint.substring(0, 2);
//             for (i = 2; i < 40; i = i + 2)
//                 fingerprint = fingerprint + ":" +
//                               pubkey.fingerprint.substring(i, i + 2);
//             $(this).after("<code class=fingerprint><span>" +
//                           fingerprint.substr(0, 30) + "</span><span>" +
//                           fingerprint.substr(30, 60) + "</span></code>");
//         }
//     });
//     */
//
//   // var mySVG = document.getElementById("action_like");
//   // var svgDoc;
//   // mySVG.addEventListener("load",function() {
//   //     svgDoc = mySVG.contentDocument;
//   //     path = svgDoc.querySelector("path");
//   //     setTimeout(function() {
//   //         path.setAttribute("fill", "red");
//   //         mySVG.setAttribute("class", "icon animated pulse");
//   //     }, 2000);
//   // }, false);
//
//   // $$(".icon").each(function() {
//   //     var svgDoc;
//   //     var mySVG = this;
//   //     mySVG.addEventListener("load", function() {
//   //         svgDoc = mySVG.contentDocument;
//   //         // function z() {
//   //             svgDoc.querySelector("path").setAttribute("fill", "#2aa198");
//   //             // mySVG.setAttribute("class", "icon animated pulse");
//   //         // }
//   //         // setTimeout(z, 2000);
//   //     }, false);
//   // });
//
//   // $("a.quote").click(function() {
//   //     window.location = "web+action://quote=?url=" + window.location +
//   //                       "&quote=" + window.getSelection().toString();
//   //     return false
//   // });
//
//   // $$("#search").submit(function() {
//   //     $.ajax({method: "GET",
//   //              url: "/search?query=" +
//   //                   $(this).find("input[name=query]").val()})
//   //         .done(function(msg) { $("#resource_preview").html(msg); });
//   //     return false
//   // });
// })
// function get_pubkey (armored_pubkey) {
//   /*
//     handle displaying of fingerprints
//
//     */
//   let foundKeys = openpgp.key.readArmored(armored_pubkey).keys
//   if (!foundKeys || foundKeys.length !== 1) {
//     throw new Error('No key found or more than one key')
//   }
//   const pubKey = foundKeys[0]
//   foundKeys = null
//   return pubKey.primaryKey
// }
// activate fast AES-GCM mode (not yet OpenPGP standard)
// openpgp.config.aead_protect = true;  // TODO move to after openpgp load
// function sign (payload, handler) {
//   // XXX var pubkey = localStorage["pubkey"];
//   // XXX var privkey = localStorage["privkey"];
//   // XXX var passphrase = "";  // window.prompt("please enter the pass phrase");
//
//   // XXX // console.log(openpgp.key.readArmored(privkey));
//   // XXX // var privKeyObj = openpgp.key.readArmored(privkey).keys[0];
//   // XXX // privKeyObj.decrypt(passphrase);
//
//   // XXX // options = {
//   // XXX //     message: openpgp.cleartext.fromText('Hello, World!'),
//   // XXX //     privateKeys: [privKeyObj]
//   // XXX // };
//
//   // XXX // openpgp.sign(options).then(function(signed) {
//   // XXX //     cleartext = signed.data;
//   // XXX //     console.log(cleartext);
//   // XXX // });
//
//   // XXX openpgp.key.readArmored(privkey).then(function(privKeyObj) {
//   // XXX     // XXX var privKeyObj = z.keys[0];
//   // XXX     // XXX privKeyObj.decrypt(passphrase);
//   // XXX     // XXX var options = {data: payload, privateKeys: privKeyObj};
//   // XXX     var options = {message: openpgp.cleartext.fromText("helloworld"),
//   // XXX                    privateKeys: [privKeyObj]}
//   // XXX     openpgp.sign(options).then(handler);
//   // XXX });
// }
// function sign_form (form, data, submission_handler) {
//   const button = form.find('button')
//   button.prop('disabled', true)
//   const timestamp = Date.now()
//   form.append("<input type=hidden name=published value='" +
//                 timestamp + "'>")
//   data.published = timestamp
//   const payload = JSON.stringify(data, Object.keys(data).sort(), '  ')
//   sign(payload, function (signed) {
//     form.append('<input id=signature type=hidden name=signature>')
//     $('#signature').val(signed.data)
//     // XXX form.submit();
//     submission_handler()
//     button.prop('disabled', false)
//   })
// }
// function getTimeSlug (when) {
//   const centiseconds = (((when.hours() * 3600) +
//                          (when.minutes() * 60) +
//                          when.seconds()) * 100) +
//                        Math.round(when.milliseconds() / 10)
//   return when.format('Y/MM/DD/') + num_to_sxgf(centiseconds, 4)
// }
// function getTextSlug (words) {
//   let padding = ''
//   if (words.slice(-1) == ' ') { padding = '_' }
//   return words.toLowerCase().split(punct_re).join('_')
//     .replace(/_$$/gm, '') + padding
// }
// function previewImage(file, preview_container) {
//     return false
//     var reader = new FileReader();
//     reader.onload = function (e) {
//         preview_container.attr("src", e.target.result);
//     }
//     reader.readAsDataURL(file);
//
//     // var data = new FormData();
//     // data.append("file-0", file);
//     // $.ajax({method: "POST",
//     //         url: "/editor/media",
//     //         contentType: "multipart/form-data",
//     //         data: data
//     //        }).done(function(msg) {
//     //                    console.log("repsonse");
//     //                    console.log(msg);
//     //                    var body = msg["content"];
//     //                    preview_container.html(body);
//     //                });
// }
// function previewResource (url, handler) {
//   if (url == '') {
//     // preview_container.innerHTML = "";
//     return
//   }
//
//   const xhr = new XMLHttpRequest()
//   xhr.open('GET', '/editor/preview/microformats?url=' +
//                     encodeURIComponent(url))
//   xhr.onload = function () {
//     if (xhr.status === 200) {
//       const response = JSON.parse(xhr.responseText)
//       // var entry = response["entry"];
//       // XXX console.log(response);
//       handler(response)
//       // var body = "";
//       // if ("profile" in response) {
//       //     // asd
//       // } else if (entry) {
//       //     if ("name" in entry)
//       //         body = "unknown type";
//       //     else if ("photo" in entry)
//       //         body = "Photo:<br><img src=" + entry["photo"] + ">";
//       //     else
//       //         body = "Note:<br>" + entry["content"];
//       // }
//       // preview_container.innerHTML = body;
//     } else { console.log('request failed: ' + xhr.status) }
//   }
//   xhr.send()
// }
// $(function() {
//     var current_body = "";
//     function setTimer() {
//         setTimeout(function() {
//             var new_body = $("#body").val();
//             if (new_body != current_body) {
//                 $.ajax({method: "POST",
//                          url: "/content/editor/preview",
//                          data: {content: new_body}
//                         }).done(function(msg) {
//                                     $("#body_readability").html(msg["readability"]);
//                                     $("#body_preview").html(msg["content"]);
//                                 });
//                 current_body = new_body;
//             }
//             setTimer();
//         }, 5000);
//     };
//     setTimer();
// });
// const socket_origin = (window.location.protocol == 'http:' ? 'ws' : 'wss') +
//                       '://' + window.location.host + '/'
//   followers (...channel) {
//     let requestUrl = this.endpoint + 'action=follow'
//     if (channel.length) {
//       requestUrl += `&channel=${channel[0]}`
//     }
//     return fetch(requestUrl).then(response => {
//       if (response.status === 200 || response.status === 201) {
//         return response.json().then(data => {
//           return data
//         })
//       }
//     })
//   }
//
//   follow (url, ...channel) {
//     let body = `action=follow&url=${url}`
//     if (channel.length) {
//       body += `&channel=${channel[0]}`
//     }
//     fetch(this.endpoint, {
//       method: 'POST',
//       headers: { 'content-type': 'application/x-www-form-urlencoded' },
//       body: body
//     }).then(response => {
//       if (response.status === 200 || response.status === 201) {
//         return response.json().then(data => {
//           return data
//         })
//       }
//     })
//   }
//
//   search (query, ...channel) {
//     let body = `action=search&query=${query}`
//     if (channel.length) {
//       body += `&channel=${channel[0]}`
//     }
//     return fetch(this.endpoint, {
//       method: 'POST',
//       headers: { 'content-type': 'application/x-www-form-urlencoded' },
//       body: body
//     }).then(response => {
//       if (response.status === 200 || response.status === 201) {
//         return response.json().then(data => {
//           return data
//         })
//       }
//     })
//   }
// --- WORKING ---
// import * as monaco from 'monaco-editor'
// import { initVimMode } from 'monaco-vim'
// import * as solarizedDark from './themes/solarized-dark'
// // import { subscribeDT } from './dt/client'
//
// export const diamondMonaco = (url, editorEl, statusEl, connectionEl, versionEl, options, userID, vim) => {
//   monaco.editor.defineTheme('solarized-dark', {
//     base: solarizedDark.base,
//     colors: solarizedDark.colors,
//     inherit: solarizedDark.inherit,
//     rules: solarizedDark.rules
//   })
//   options.theme = 'solarized-dark'
//   options.automaticLayout = true
//   const editor = monaco.editor.create(editorEl, options)
//   if (vim === true) {
//     initVimMode(editor, statusEl)
//   }
//   editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.KeyS, () => {
//     alert('saved')
//   })
//   editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, () => {
//     alert('publish')
//   })
//   editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyMod.Shift | monaco.KeyCode.Enter, () => {
//     alert('publish and go live')
//   })
//   // subscribeDT(url + '.dt', editor, userID, {
//   //   setStatus: m => {
//   //     connectionEl.innerHTML = m
//   //   },
//   //   setInfo: m => {
//   //     versionEl.innerHTML = m
//   //   }
//   // })
//   return editor
// }
//
// --- /WORKING ---
/**
 * JavaScript Client Detection
 * (C) viazenetti GmbH (Christian Ludwig)
 */
const getBrowser = () => {
    const unknown = '-';
    // screen
    let screenSize = '';
    if (screen.width) {
        const width = (screen.width) ? screen.width : '';
        const height = (screen.height) ? screen.height : '';
        screenSize += '' + width + ' x ' + height;
    }
    // browser
    const nVer = navigator.appVersion;
    const nAgt = navigator.userAgent;
    let browser = navigator.appName;
    let version = '' + parseFloat(navigator.appVersion);
    let majorVersion = parseInt(navigator.appVersion, 10);
    let nameOffset, verOffset, ix;
    // Opera
    if ((verOffset = nAgt.indexOf('Opera')) !== -1) {
        browser = 'Opera';
        version = nAgt.substring(verOffset + 6);
        if ((verOffset = nAgt.indexOf('Version')) !== -1) {
            version = nAgt.substring(verOffset + 8);
        }
    }
    // Opera Next
    if ((verOffset = nAgt.indexOf('OPR')) !== -1) {
        browser = 'Opera';
        version = nAgt.substring(verOffset + 4);
    }
    else if ((verOffset = nAgt.indexOf('Edge')) !== -1) { // Legacy Edge
        browser = 'Microsoft Legacy Edge';
        version = nAgt.substring(verOffset + 5);
    }
    else if ((verOffset = nAgt.indexOf('Edg')) !== -1) { // Edge (Chromium)
        browser = 'Microsoft Edge';
        version = nAgt.substring(verOffset + 4);
    }
    else if ((verOffset = nAgt.indexOf('MSIE')) !== -1) { // MSIE
        browser = 'Microsoft Internet Explorer';
        version = nAgt.substring(verOffset + 5);
    }
    else if ((verOffset = nAgt.indexOf('Chrome')) !== -1) { // Chrome
        browser = 'Chrome';
        version = nAgt.substring(verOffset + 7);
    }
    else if ((verOffset = nAgt.indexOf('Safari')) !== -1) { // Safari
        browser = 'Safari';
        version = nAgt.substring(verOffset + 7);
        if ((verOffset = nAgt.indexOf('Version')) !== -1) {
            version = nAgt.substring(verOffset + 8);
        }
    }
    else if ((verOffset = nAgt.indexOf('Firefox')) !== -1) { // Firefox
        browser = 'Firefox';
        version = nAgt.substring(verOffset + 8);
    }
    else if (nAgt.indexOf('Trident/') !== -1) { // MSIE 11+
        browser = 'Microsoft Internet Explorer';
        version = nAgt.substring(nAgt.indexOf('rv:') + 3);
    }
    else if ((nameOffset = nAgt.lastIndexOf(' ') + 1) <
        (verOffset = nAgt.lastIndexOf('/'))) { // Other browsers
        browser = nAgt.substring(nameOffset, verOffset);
        version = nAgt.substring(verOffset + 1);
        if (browser.toLowerCase() === browser.toUpperCase()) {
            browser = navigator.appName;
        }
    }
    // trim the version string
    if ((ix = version.indexOf(';')) !== -1)
        version = version.substring(0, ix);
    if ((ix = version.indexOf(' ')) !== -1)
        version = version.substring(0, ix);
    if ((ix = version.indexOf(')')) !== -1)
        version = version.substring(0, ix);
    majorVersion = parseInt('' + version, 10);
    if (isNaN(majorVersion)) {
        version = '' + parseFloat(navigator.appVersion);
        majorVersion = parseInt(navigator.appVersion, 10);
    }
    // mobile version
    const mobile = /Mobile|mini|Fennec|Android|iP(ad|od|hone)/.test(nVer);
    // cookie
    let cookieEnabled = !!(navigator.cookieEnabled);
    if (typeof navigator.cookieEnabled === 'undefined' && !cookieEnabled) {
        document.cookie = 'testcookie';
        cookieEnabled = (document.cookie.indexOf('testcookie') !== -1);
    }
    // test
    // system
    let os = unknown;
    const clientStrings = [
        { s: 'Windows 10', r: /(Windows 10.0|Windows NT 10.0)/ },
        { s: 'Windows 8.1', r: /(Windows 8.1|Windows NT 6.3)/ },
        { s: 'Windows 8', r: /(Windows 8|Windows NT 6.2)/ },
        { s: 'Windows 7', r: /(Windows 7|Windows NT 6.1)/ },
        { s: 'Windows Vista', r: /Windows NT 6.0/ },
        { s: 'Windows Server 2003', r: /Windows NT 5.2/ },
        { s: 'Windows XP', r: /(Windows NT 5.1|Windows XP)/ },
        { s: 'Windows 2000', r: /(Windows NT 5.0|Windows 2000)/ },
        { s: 'Windows ME', r: /(Win 9x 4.90|Windows ME)/ },
        { s: 'Windows 98', r: /(Windows 98|Win98)/ },
        { s: 'Windows 95', r: /(Windows 95|Win95|Windows_95)/ },
        { s: 'Windows NT 4.0', r: /(Windows NT 4.0|WinNT4.0|WinNT|Windows NT)/ },
        { s: 'Windows CE', r: /Windows CE/ },
        { s: 'Windows 3.11', r: /Win16/ },
        { s: 'Android', r: /Android/ },
        { s: 'Open BSD', r: /OpenBSD/ },
        { s: 'Sun OS', r: /SunOS/ },
        { s: 'Chrome OS', r: /CrOS/ },
        { s: 'Linux', r: /(Linux|X11(?!.*CrOS))/ },
        { s: 'iOS', r: /(iPhone|iPad|iPod)/ },
        { s: 'Mac OS X', r: /Mac OS X/ },
        { s: 'Mac OS', r: /(Mac OS|MacPPC|MacIntel|Mac_PowerPC|Macintosh)/ },
        { s: 'QNX', r: /QNX/ },
        { s: 'UNIX', r: /UNIX/ },
        { s: 'BeOS', r: /BeOS/ },
        { s: 'OS/2', r: /OS\/2/ },
        { s: 'Search Bot', r: /(nuhk|Googlebot|Yammybot|Openbot|Slurp|MSNBot|Ask Jeeves\/Teoma|ia_archiver)/ }
    ];
    for (const id in clientStrings) {
        const cs = clientStrings[id];
        if (cs.r.test(nAgt)) {
            os = cs.s;
            break;
        }
    }
    let osVersion = unknown;
    if (/Windows/.test(os)) {
        osVersion = /Windows (.*)/.exec(os)[1];
        os = 'Windows';
    }
    switch (os) {
        case 'Mac OS':
        case 'Mac OS X':
        case 'Android':
            osVersion = /(?:Android|Mac OS|Mac OS X|MacPPC|MacIntel|Mac_PowerPC|Macintosh) ([._d]+)/.exec(nAgt)[1];
            break;
        // TODO case 'iOS':
        // TODO   osVersion = /OS (\d+)_(\d+)_?(\d+)?/.exec(nVer)
        // TODO   osVersion = osVersion[1] + '.' + osVersion[2] + '.' + (osVersion[3] | 0)
        // TODO   break
    }
    // flash (you'll need to include swfobject)
    /* script src="//ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js" */
    // TODO var flashVersion = 'no check'
    // TODO if (typeof swfobject !== 'undefined') {
    // TODO   const fv = swfobject.getFlashPlayerVersion()
    // TODO   if (fv.major > 0) {
    // TODO     flashVersion = fv.major + '.' + fv.minor + ' r' + fv.release
    // TODO   } else {
    // TODO     flashVersion = unknown
    // TODO   }
    // TODO }
    return {
        screen: screenSize,
        browser: browser,
        browserVersion: version,
        browserMajorVersion: majorVersion,
        mobile: mobile,
        os: os,
        osVersion: osVersion,
        cookies: cookieEnabled
        // TODO flashVersion: flashVersion
    };
};
// TODO alert(
// TODO   'OS: ' + jscd.os + ' ' + jscd.osVersion + '\n' +
// TODO     'Browser: ' + jscd.browser + ' ' + jscd.browserMajorVersion +
// TODO       ' (' + jscd.browserVersion + ')\n' +
// TODO     'Mobile: ' + jscd.mobile + '\n' +
// TODO     'Flash: ' + jscd.flashVersion + '\n' +
// TODO     'Cookies: ' + jscd.cookies + '\n' +
// TODO     'Screen Size: ' + jscd.screen + '\n\n' +
// TODO     'Full User Agent: ' + navigator.userAgent
// TODO )
const Cookies = __webpack_require__(/*! js-cookie */ "./node_modules/js-cookie/dist/js.cookie.js");
// TODO const { DateTime } = require('luxon')
// const { nb60encode, nb60decode } = require('NewMath')
const cookies = Cookies;
// TODO export const dt = DateTime
// _.nb60encode = nb60encode
// _.nb60decode = nb60decode
// export const _ = (selector) => {
//   const results = typeof selector === 'string'
//     ? document.querySelectorAll(selector)
//     : [selector]
//   // const results = Array.prototype.slice.call(nodes)
//   const items = {}
//   for (let i = 0; i < results.length; i++) {
//     items[i] = results[i]
//   }
//   items._ = _
//   items.el = items[0]
//   items.n = results.length
//   // items.splice = [].splice() // simulates an array FIXME
//   // items.each = callback => { nodes.forEach(callback, ) }
//   items.each = callback => {
//     for (let i = 0; i < results.length; i++) {
//       callback(results[i])
//     }
//   }
//   // for (let i = 0; i < results.length; i++) {
//   //   console.log(results[i])
//   //   results[i].addEventListener('click', () => { console.log('er') })
//   // }
//   // items.click = callback => {
//   //   for (let i = 0; i < results.length; i++) {
//   //     console.log(this.results[i], this)
//   //     this.results[i].addEventListener('click', () => { console.log('er') })
//   //     // callback.bind(nodes[i])
//   //     // callback(nodes[i])
//   //   }
//   // }
//   items.append = html => {
//     items.each(item => item.appendChild(createEl(html)))
//   }
//   items.move = (left, top) => {
//     items.el.style.left = left
//     items.el.style.top = top
//   }
//   items.click = callback => {
//     items.each(item => {
//       item.addEventListener('click', callback)
//     })
//   }
//   return items
// }
const createEl = html => {
    const template = document.createElement('template');
    template.innerHTML = html.trim();
    return template.content.firstChild;
};
const createEls = html => {
    const template = document.createElement('template');
    template.innerHTML = html;
    return template.content.childNodes;
};
const loadScripts = [];
const unloadScripts = [];
const executeLoadScripts = () => {
    loadScripts.forEach(handler => handler());
    loadScripts.length = 0;
};
const executeUnloadScripts = () => {
    unloadScripts.forEach(handler => handler());
    unloadScripts.length = 0;
};
document.addEventListener('DOMContentLoaded', () => executeLoadScripts());
window.addEventListener('beforeunload', () => {
    executeUnloadScripts();
});
const load = handler => loadScripts.push(handler);
const unload = handler => unloadScripts.push(handler);
const mouseup = handler => document.addEventListener('mouseup', handler);
const popstate = handler => window.addEventListener('popstate', handler);
const online = handler => window.addEventListener('online', handler);
const offline = handler => window.addEventListener('offline', handler);
const error = handler => window.addEventListener('error', handler);
const upgradeTimestamps = () => {
    // TODO const pageLoad = DateTime.now()
    // TODO _('time').each(item => {
    // TODO   item.setAttribute('title', item.innerHTML)
    // TODO   item.innerHTML = DateTime.fromISO(item.attributes.datetime.value)
    // TODO     .toRelative({ base: pageLoad })
    // TODO })
};
class MicropubClient {
    endpoint;
    token;
    headers;
    config;
    constructor(endpoint, token) {
        this.endpoint = endpoint;
        this.token = token;
        this.headers = {
            accept: 'application/json'
        };
        if (typeof token !== 'undefined') {
            this.headers.authorization = `Bearer ${token}`;
        }
        this.getConfig = this.getConfig.bind(this);
        this.create = this.create.bind(this);
        this.read = this.read.bind(this);
        this.update = this.update.bind(this);
        this.delete = this.delete.bind(this);
        this.query = this.query.bind(this);
        this.upload = this.upload.bind(this);
    }
    getConfig() {
        return fetch(this.endpoint + '?q=config', {
            headers: this.headers
        }).then(response => {
            if (response.status === 200 || response.status === 201) {
                return response.json().then(data => {
                    return data;
                });
            }
        });
    }
    getCategories() {
        return fetch(this.endpoint + '?q=category', {
            headers: this.headers
        }).then(response => {
            if (response.status === 200 || response.status === 201) {
                return response.json().then(data => {
                    return data;
                });
            }
        });
    }
    create(type, properties, visibility) {
        const headers = this.headers;
        headers['content-type'] = 'application/json';
        if (typeof visibility === 'undefined') {
            visibility = 'private';
        }
        // TODO properties.visibility = visibility
        return fetch(this.endpoint, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify({
                type: [`h-${type}`],
                properties: properties
            })
        }).then(response => {
            if (response.status === 200 || response.status === 201) {
                return response.headers.get('location'); // permalink
            }
        });
    }
    read(url) {
        const headers = this.headers;
        headers['content-type'] = 'application/json';
        return fetch(this.endpoint, {
            method: 'GET',
            headers: headers
        }).then(response => {
            if (response.status === 200 || response.status === 201) {
                return response.json().then(data => {
                    return data;
                });
            }
        });
    }
    update(url, operation, properties) {
        const payload = { action: 'update', url: url };
        payload[operation] = properties;
        // payload[operation][property] = values
        return fetch(this.endpoint, {
            method: 'POST',
            headers: {
                accept: 'application/json',
                authorization: `Bearer ${this.token}`,
                'content-type': 'application/json'
            },
            body: JSON.stringify(payload)
        }).then(response => {
            if (response.status === 200 || response.status === 201) {
                console.log('UPDATED!');
            }
        });
    }
    delete(url) {
    }
    query(q, args) {
        return fetch(this.endpoint + `?q=${q}&search=${args}`, {
            headers: this.headers
        }).then(response => {
            if (response.status === 200 || response.status === 201) {
                return response.json().then(data => {
                    return data;
                });
            }
        });
    }
    upload() {
    }
}

})();

var __webpack_exports__MicropubClient = __webpack_exports__.MicropubClient;
var __webpack_exports__cookies = __webpack_exports__.cookies;
var __webpack_exports__createEl = __webpack_exports__.createEl;
var __webpack_exports__createEls = __webpack_exports__.createEls;
var __webpack_exports__error = __webpack_exports__.error;
var __webpack_exports__getBrowser = __webpack_exports__.getBrowser;
var __webpack_exports__load = __webpack_exports__.load;
var __webpack_exports__mouseup = __webpack_exports__.mouseup;
var __webpack_exports__offline = __webpack_exports__.offline;
var __webpack_exports__online = __webpack_exports__.online;
var __webpack_exports__popstate = __webpack_exports__.popstate;
var __webpack_exports__unload = __webpack_exports__.unload;
var __webpack_exports__upgradeTimestamps = __webpack_exports__.upgradeTimestamps;
export { __webpack_exports__MicropubClient as MicropubClient, __webpack_exports__cookies as cookies, __webpack_exports__createEl as createEl, __webpack_exports__createEls as createEls, __webpack_exports__error as error, __webpack_exports__getBrowser as getBrowser, __webpack_exports__load as load, __webpack_exports__mouseup as mouseup, __webpack_exports__offline as offline, __webpack_exports__online as online, __webpack_exports__popstate as popstate, __webpack_exports__unload as unload, __webpack_exports__upgradeTimestamps as upgradeTimestamps };

//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoid2ViLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7O0FBQUE7QUFDQTtBQUNBO0FBQ0EsRUFBRSxLQUE0RDtBQUM5RCxFQUFFLENBS0s7QUFDUCxDQUFDLHNCQUFzQjs7QUFFdkI7QUFDQTtBQUNBLG9CQUFvQixzQkFBc0I7QUFDMUM7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxzQ0FBc0MsRUFBRTtBQUN4QyxLQUFLO0FBQ0w7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7QUFFQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBLDRCQUE0Qjs7QUFFNUI7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOztBQUVBLG9DQUFvQzs7QUFFcEM7QUFDQTtBQUNBOztBQUVBO0FBQ0E7QUFDQSx1RUFBdUU7QUFDdkU7QUFDQTtBQUNBLDRDQUE0QztBQUM1QztBQUNBLHlFQUF5RTtBQUN6RTs7QUFFQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBLCtEQUErRDtBQUMvRDtBQUNBLHNCQUFzQixvQkFBb0I7QUFDMUM7QUFDQTs7QUFFQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0EsVUFBVTtBQUNWOztBQUVBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLHFCQUFxQjtBQUNyQjtBQUNBLGFBQWE7QUFDYjtBQUNBLFNBQVM7QUFDVDtBQUNBLCtDQUErQztBQUMvQyxTQUFTO0FBQ1Q7QUFDQSwrQkFBK0I7QUFDL0I7QUFDQSxPQUFPO0FBQ1A7QUFDQSxzQkFBc0IseUNBQXlDO0FBQy9ELHFCQUFxQjtBQUNyQjtBQUNBO0FBQ0E7O0FBRUEscUNBQXFDLFdBQVc7QUFDaEQ7O0FBRUE7O0FBRUEsQ0FBQzs7Ozs7OztTQ2xKRDtTQUNBOztTQUVBO1NBQ0E7U0FDQTtTQUNBO1NBQ0E7U0FDQTtTQUNBO1NBQ0E7U0FDQTtTQUNBO1NBQ0E7U0FDQTtTQUNBOztTQUVBO1NBQ0E7O1NBRUE7U0FDQTtTQUNBOzs7OztVQ3RCQTtVQUNBO1VBQ0E7VUFDQTtVQUNBLHlDQUF5Qyx3Q0FBd0M7VUFDakY7VUFDQTtVQUNBOzs7OztVQ1BBOzs7OztVQ0FBO1VBQ0E7VUFDQTtVQUNBLHVEQUF1RCxpQkFBaUI7VUFDeEU7VUFDQSxnREFBZ0QsYUFBYTtVQUM3RDs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUNOQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxzRUFBc0UsVUFBVTtBQUNoRix3RUFBd0UsWUFBWTtBQUNwRjtBQUNBLDBDQUEwQyxZQUFZO0FBQ3RELDRDQUE0QyxVQUFVO0FBQ3REO0FBQ0E7QUFDQSwwQ0FBMEMsSUFBSTtBQUM5QztBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxtQkFBbUI7QUFDbkI7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFFBQVE7QUFDUjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLDJCQUEyQixRQUFRO0FBQ25DO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFFBQVE7QUFDUjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLGFBQWE7QUFDYixTQUFTO0FBQ1Q7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLGFBQWE7QUFDYixTQUFTO0FBQ1Q7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFNBQVM7QUFDVDtBQUNBO0FBQ0Esb0JBQW9CO0FBQ3BCO0FBQ0Esa0VBQWtFO0FBQ2xFLHNDQUFzQyxtQ0FBbUM7QUFDekU7QUFDQSxTQUFTO0FBQ1QsSUFBSTtBQUNKO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSx3Q0FBd0M7QUFDeEM7QUFDQTtBQUNBO0FBQ0Esa0NBQWtDO0FBQ2xDO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsZ0JBQWdCO0FBQ2hCO0FBQ0E7QUFDQTtBQUNBO0FBQ0Esc0NBQXNDO0FBQ3RDLCtCQUErQjtBQUMvQjtBQUNBO0FBQ0EsYUFBYTtBQUNiO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLE1BQU07QUFDTjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLG1DQUFtQztBQUNuQztBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLGtCQUFrQjtBQUNsQjtBQUNBO0FBQ0E7QUFDQSxrQkFBa0I7QUFDbEI7QUFDQTtBQUNBO0FBQ0E7QUFDQSwwQkFBMEI7QUFDMUI7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxjQUFjO0FBQ2Q7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFNBQVMsT0FBTztBQUNoQjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSwyQkFBMkI7QUFDM0I7QUFDQSxtQ0FBbUM7QUFDbkMsNEJBQTRCO0FBQzVCO0FBQ0E7QUFDQSxvQ0FBb0M7QUFDcEM7QUFDQTtBQUNBO0FBQ0EsWUFBWTtBQUNaO0FBQ0E7QUFDQSxJQUFJO0FBQ0o7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLG1DQUFtQyxXQUFXO0FBQzlDO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxZQUFZO0FBQ1o7QUFDQSxRQUFRO0FBQ1I7QUFDQTtBQUNBO0FBQ0EsdUNBQXVDLElBQUk7QUFDM0M7QUFDQSw2QkFBNkIsV0FBVztBQUN4QztBQUNBO0FBQ0E7QUFDQSxvQkFBb0IscURBQXFEO0FBQ3pFO0FBQ0EsUUFBUTtBQUNSO0FBQ0E7QUFDQTtBQUNBLFlBQVk7QUFDWjtBQUNBLFFBQVE7QUFDUjtBQUNBO0FBQ0E7QUFDQSx5Q0FBeUMsTUFBTTtBQUMvQztBQUNBLDZCQUE2QixXQUFXO0FBQ3hDO0FBQ0E7QUFDQTtBQUNBLG9CQUFvQixxREFBcUQ7QUFDekU7QUFDQSxRQUFRO0FBQ1I7QUFDQTtBQUNBO0FBQ0EsWUFBWTtBQUNaO0FBQ0EsUUFBUTtBQUNSO0FBQ0E7QUFDQTtBQUNBLFlBQVksY0FBYztBQUMxQjtBQUNBLGVBQWUsY0FBYztBQUM3QjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLE1BQU07QUFDTjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsTUFBTTtBQUNOO0FBQ0E7QUFDQSxNQUFNO0FBQ047QUFDQTtBQUNBLE1BQU07QUFDTjtBQUNBO0FBQ0E7QUFDQSxXQUFXO0FBQ1g7QUFDQTtBQUNBO0FBQ0EsU0FBUztBQUNUO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDTztBQUNQO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsMERBQTBEO0FBQzFEO0FBQ0E7QUFDQTtBQUNBLHlEQUF5RDtBQUN6RDtBQUNBO0FBQ0E7QUFDQSwwREFBMEQ7QUFDMUQ7QUFDQTtBQUNBO0FBQ0EsNERBQTREO0FBQzVEO0FBQ0E7QUFDQTtBQUNBLDREQUE0RDtBQUM1RDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSw2REFBNkQ7QUFDN0Q7QUFDQTtBQUNBO0FBQ0EsZ0RBQWdEO0FBQ2hEO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsK0NBQStDO0FBQy9DO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsZ0NBQWdDO0FBQ2hDO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsVUFBVSxzREFBc0Q7QUFDaEUsVUFBVSxxREFBcUQ7QUFDL0QsVUFBVSxpREFBaUQ7QUFDM0QsVUFBVSxpREFBaUQ7QUFDM0QsVUFBVSx5Q0FBeUM7QUFDbkQsVUFBVSwrQ0FBK0M7QUFDekQsVUFBVSxtREFBbUQ7QUFDN0QsVUFBVSx1REFBdUQ7QUFDakUsVUFBVSxnREFBZ0Q7QUFDMUQsVUFBVSwwQ0FBMEM7QUFDcEQsVUFBVSxxREFBcUQ7QUFDL0QsVUFBVSxzRUFBc0U7QUFDaEYsVUFBVSxrQ0FBa0M7QUFDNUMsVUFBVSwrQkFBK0I7QUFDekMsVUFBVSw0QkFBNEI7QUFDdEMsVUFBVSw2QkFBNkI7QUFDdkMsVUFBVSx5QkFBeUI7QUFDbkMsVUFBVSwyQkFBMkI7QUFDckMsVUFBVSx3Q0FBd0M7QUFDbEQsVUFBVSxtQ0FBbUM7QUFDN0MsVUFBVSw4QkFBOEI7QUFDeEMsVUFBVSxrRUFBa0U7QUFDNUUsVUFBVSxvQkFBb0I7QUFDOUIsVUFBVSxzQkFBc0I7QUFDaEMsVUFBVSxzQkFBc0I7QUFDaEMsVUFBVSx1QkFBdUI7QUFDakMsVUFBVTtBQUNWO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsZ0JBQWdCO0FBQ2hCO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EsZ0JBQWdCLG1CQUFPLENBQUMsNkRBQVc7QUFDbkMsZ0JBQWdCLFdBQVc7QUFDM0IsV0FBVyx5QkFBeUI7QUFDN0I7QUFDUDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxxQkFBcUIsb0JBQW9CO0FBQ3pDO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLG1DQUFtQztBQUNuQztBQUNBLHVCQUF1QixvQkFBb0I7QUFDM0M7QUFDQTtBQUNBO0FBQ0Esd0JBQXdCLG9CQUFvQjtBQUM1QztBQUNBLHVEQUF1RCxtQkFBbUI7QUFDMUU7QUFDQTtBQUNBLDBCQUEwQixvQkFBb0I7QUFDOUM7QUFDQSw4REFBOEQsbUJBQW1CO0FBQ2pGO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSxRQUFRO0FBQ1I7QUFDQTtBQUNBO0FBQ087QUFDUDtBQUNBO0FBQ0E7QUFDQTtBQUNPO0FBQ1A7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLENBQUM7QUFDTTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ1A7QUFDQTtBQUNBO0FBQ0E7QUFDQSw4QkFBOEIsZ0JBQWdCO0FBQzlDLGFBQWE7QUFDYjtBQUNPO0FBQ1A7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLG1EQUFtRCxNQUFNO0FBQ3pEO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFNBQVM7QUFDVDtBQUNBO0FBQ0E7QUFDQSxpQkFBaUI7QUFDakI7QUFDQSxTQUFTO0FBQ1Q7QUFDQTtBQUNBO0FBQ0E7QUFDQSxTQUFTO0FBQ1Q7QUFDQTtBQUNBO0FBQ0EsaUJBQWlCO0FBQ2pCO0FBQ0EsU0FBUztBQUNUO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLDRCQUE0QixLQUFLO0FBQ2pDO0FBQ0EsYUFBYTtBQUNiLFNBQVM7QUFDVDtBQUNBLHlEQUF5RDtBQUN6RDtBQUNBLFNBQVM7QUFDVDtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBLFNBQVM7QUFDVDtBQUNBO0FBQ0E7QUFDQSxpQkFBaUI7QUFDakI7QUFDQSxTQUFTO0FBQ1Q7QUFDQTtBQUNBLDBCQUEwQjtBQUMxQjtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQSx5Q0FBeUMsV0FBVztBQUNwRDtBQUNBLGFBQWE7QUFDYjtBQUNBLFNBQVM7QUFDVDtBQUNBO0FBQ0E7QUFDQSxTQUFTO0FBQ1Q7QUFDQTtBQUNBO0FBQ0E7QUFDQSwyQ0FBMkMsRUFBRSxVQUFVLEtBQUs7QUFDNUQ7QUFDQSxTQUFTO0FBQ1Q7QUFDQTtBQUNBO0FBQ0EsaUJBQWlCO0FBQ2pCO0FBQ0EsU0FBUztBQUNUO0FBQ0E7QUFDQTtBQUNBIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vd2ViLmpzLy4vbm9kZV9tb2R1bGVzL2pzLWNvb2tpZS9kaXN0L2pzLmNvb2tpZS5qcyIsIndlYnBhY2s6Ly93ZWIuanMvd2VicGFjay9ib290c3RyYXAiLCJ3ZWJwYWNrOi8vd2ViLmpzL3dlYnBhY2svcnVudGltZS9kZWZpbmUgcHJvcGVydHkgZ2V0dGVycyIsIndlYnBhY2s6Ly93ZWIuanMvd2VicGFjay9ydW50aW1lL2hhc093blByb3BlcnR5IHNob3J0aGFuZCIsIndlYnBhY2s6Ly93ZWIuanMvd2VicGFjay9ydW50aW1lL21ha2UgbmFtZXNwYWNlIG9iamVjdCIsIndlYnBhY2s6Ly93ZWIuanMvLi93ZWIudHMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLyohIGpzLWNvb2tpZSB2My4wLjEgfCBNSVQgKi9cbjtcbihmdW5jdGlvbiAoZ2xvYmFsLCBmYWN0b3J5KSB7XG4gIHR5cGVvZiBleHBvcnRzID09PSAnb2JqZWN0JyAmJiB0eXBlb2YgbW9kdWxlICE9PSAndW5kZWZpbmVkJyA/IG1vZHVsZS5leHBvcnRzID0gZmFjdG9yeSgpIDpcbiAgdHlwZW9mIGRlZmluZSA9PT0gJ2Z1bmN0aW9uJyAmJiBkZWZpbmUuYW1kID8gZGVmaW5lKGZhY3RvcnkpIDpcbiAgKGdsb2JhbCA9IGdsb2JhbCB8fCBzZWxmLCAoZnVuY3Rpb24gKCkge1xuICAgIHZhciBjdXJyZW50ID0gZ2xvYmFsLkNvb2tpZXM7XG4gICAgdmFyIGV4cG9ydHMgPSBnbG9iYWwuQ29va2llcyA9IGZhY3RvcnkoKTtcbiAgICBleHBvcnRzLm5vQ29uZmxpY3QgPSBmdW5jdGlvbiAoKSB7IGdsb2JhbC5Db29raWVzID0gY3VycmVudDsgcmV0dXJuIGV4cG9ydHM7IH07XG4gIH0oKSkpO1xufSh0aGlzLCAoZnVuY3Rpb24gKCkgeyAndXNlIHN0cmljdCc7XG5cbiAgLyogZXNsaW50LWRpc2FibGUgbm8tdmFyICovXG4gIGZ1bmN0aW9uIGFzc2lnbiAodGFyZ2V0KSB7XG4gICAgZm9yICh2YXIgaSA9IDE7IGkgPCBhcmd1bWVudHMubGVuZ3RoOyBpKyspIHtcbiAgICAgIHZhciBzb3VyY2UgPSBhcmd1bWVudHNbaV07XG4gICAgICBmb3IgKHZhciBrZXkgaW4gc291cmNlKSB7XG4gICAgICAgIHRhcmdldFtrZXldID0gc291cmNlW2tleV07XG4gICAgICB9XG4gICAgfVxuICAgIHJldHVybiB0YXJnZXRcbiAgfVxuICAvKiBlc2xpbnQtZW5hYmxlIG5vLXZhciAqL1xuXG4gIC8qIGVzbGludC1kaXNhYmxlIG5vLXZhciAqL1xuICB2YXIgZGVmYXVsdENvbnZlcnRlciA9IHtcbiAgICByZWFkOiBmdW5jdGlvbiAodmFsdWUpIHtcbiAgICAgIGlmICh2YWx1ZVswXSA9PT0gJ1wiJykge1xuICAgICAgICB2YWx1ZSA9IHZhbHVlLnNsaWNlKDEsIC0xKTtcbiAgICAgIH1cbiAgICAgIHJldHVybiB2YWx1ZS5yZXBsYWNlKC8oJVtcXGRBLUZdezJ9KSsvZ2ksIGRlY29kZVVSSUNvbXBvbmVudClcbiAgICB9LFxuICAgIHdyaXRlOiBmdW5jdGlvbiAodmFsdWUpIHtcbiAgICAgIHJldHVybiBlbmNvZGVVUklDb21wb25lbnQodmFsdWUpLnJlcGxhY2UoXG4gICAgICAgIC8lKDJbMzQ2QkZdfDNbQUMtRl18NDB8NVtCREVdfDYwfDdbQkNEXSkvZyxcbiAgICAgICAgZGVjb2RlVVJJQ29tcG9uZW50XG4gICAgICApXG4gICAgfVxuICB9O1xuICAvKiBlc2xpbnQtZW5hYmxlIG5vLXZhciAqL1xuXG4gIC8qIGVzbGludC1kaXNhYmxlIG5vLXZhciAqL1xuXG4gIGZ1bmN0aW9uIGluaXQgKGNvbnZlcnRlciwgZGVmYXVsdEF0dHJpYnV0ZXMpIHtcbiAgICBmdW5jdGlvbiBzZXQgKGtleSwgdmFsdWUsIGF0dHJpYnV0ZXMpIHtcbiAgICAgIGlmICh0eXBlb2YgZG9jdW1lbnQgPT09ICd1bmRlZmluZWQnKSB7XG4gICAgICAgIHJldHVyblxuICAgICAgfVxuXG4gICAgICBhdHRyaWJ1dGVzID0gYXNzaWduKHt9LCBkZWZhdWx0QXR0cmlidXRlcywgYXR0cmlidXRlcyk7XG5cbiAgICAgIGlmICh0eXBlb2YgYXR0cmlidXRlcy5leHBpcmVzID09PSAnbnVtYmVyJykge1xuICAgICAgICBhdHRyaWJ1dGVzLmV4cGlyZXMgPSBuZXcgRGF0ZShEYXRlLm5vdygpICsgYXR0cmlidXRlcy5leHBpcmVzICogODY0ZTUpO1xuICAgICAgfVxuICAgICAgaWYgKGF0dHJpYnV0ZXMuZXhwaXJlcykge1xuICAgICAgICBhdHRyaWJ1dGVzLmV4cGlyZXMgPSBhdHRyaWJ1dGVzLmV4cGlyZXMudG9VVENTdHJpbmcoKTtcbiAgICAgIH1cblxuICAgICAga2V5ID0gZW5jb2RlVVJJQ29tcG9uZW50KGtleSlcbiAgICAgICAgLnJlcGxhY2UoLyUoMlszNDZCXXw1RXw2MHw3QykvZywgZGVjb2RlVVJJQ29tcG9uZW50KVxuICAgICAgICAucmVwbGFjZSgvWygpXS9nLCBlc2NhcGUpO1xuXG4gICAgICB2YXIgc3RyaW5naWZpZWRBdHRyaWJ1dGVzID0gJyc7XG4gICAgICBmb3IgKHZhciBhdHRyaWJ1dGVOYW1lIGluIGF0dHJpYnV0ZXMpIHtcbiAgICAgICAgaWYgKCFhdHRyaWJ1dGVzW2F0dHJpYnV0ZU5hbWVdKSB7XG4gICAgICAgICAgY29udGludWVcbiAgICAgICAgfVxuXG4gICAgICAgIHN0cmluZ2lmaWVkQXR0cmlidXRlcyArPSAnOyAnICsgYXR0cmlidXRlTmFtZTtcblxuICAgICAgICBpZiAoYXR0cmlidXRlc1thdHRyaWJ1dGVOYW1lXSA9PT0gdHJ1ZSkge1xuICAgICAgICAgIGNvbnRpbnVlXG4gICAgICAgIH1cblxuICAgICAgICAvLyBDb25zaWRlcnMgUkZDIDYyNjUgc2VjdGlvbiA1LjI6XG4gICAgICAgIC8vIC4uLlxuICAgICAgICAvLyAzLiAgSWYgdGhlIHJlbWFpbmluZyB1bnBhcnNlZC1hdHRyaWJ1dGVzIGNvbnRhaW5zIGEgJXgzQiAoXCI7XCIpXG4gICAgICAgIC8vICAgICBjaGFyYWN0ZXI6XG4gICAgICAgIC8vIENvbnN1bWUgdGhlIGNoYXJhY3RlcnMgb2YgdGhlIHVucGFyc2VkLWF0dHJpYnV0ZXMgdXAgdG8sXG4gICAgICAgIC8vIG5vdCBpbmNsdWRpbmcsIHRoZSBmaXJzdCAleDNCIChcIjtcIikgY2hhcmFjdGVyLlxuICAgICAgICAvLyAuLi5cbiAgICAgICAgc3RyaW5naWZpZWRBdHRyaWJ1dGVzICs9ICc9JyArIGF0dHJpYnV0ZXNbYXR0cmlidXRlTmFtZV0uc3BsaXQoJzsnKVswXTtcbiAgICAgIH1cblxuICAgICAgcmV0dXJuIChkb2N1bWVudC5jb29raWUgPVxuICAgICAgICBrZXkgKyAnPScgKyBjb252ZXJ0ZXIud3JpdGUodmFsdWUsIGtleSkgKyBzdHJpbmdpZmllZEF0dHJpYnV0ZXMpXG4gICAgfVxuXG4gICAgZnVuY3Rpb24gZ2V0IChrZXkpIHtcbiAgICAgIGlmICh0eXBlb2YgZG9jdW1lbnQgPT09ICd1bmRlZmluZWQnIHx8IChhcmd1bWVudHMubGVuZ3RoICYmICFrZXkpKSB7XG4gICAgICAgIHJldHVyblxuICAgICAgfVxuXG4gICAgICAvLyBUbyBwcmV2ZW50IHRoZSBmb3IgbG9vcCBpbiB0aGUgZmlyc3QgcGxhY2UgYXNzaWduIGFuIGVtcHR5IGFycmF5XG4gICAgICAvLyBpbiBjYXNlIHRoZXJlIGFyZSBubyBjb29raWVzIGF0IGFsbC5cbiAgICAgIHZhciBjb29raWVzID0gZG9jdW1lbnQuY29va2llID8gZG9jdW1lbnQuY29va2llLnNwbGl0KCc7ICcpIDogW107XG4gICAgICB2YXIgamFyID0ge307XG4gICAgICBmb3IgKHZhciBpID0gMDsgaSA8IGNvb2tpZXMubGVuZ3RoOyBpKyspIHtcbiAgICAgICAgdmFyIHBhcnRzID0gY29va2llc1tpXS5zcGxpdCgnPScpO1xuICAgICAgICB2YXIgdmFsdWUgPSBwYXJ0cy5zbGljZSgxKS5qb2luKCc9Jyk7XG5cbiAgICAgICAgdHJ5IHtcbiAgICAgICAgICB2YXIgZm91bmRLZXkgPSBkZWNvZGVVUklDb21wb25lbnQocGFydHNbMF0pO1xuICAgICAgICAgIGphcltmb3VuZEtleV0gPSBjb252ZXJ0ZXIucmVhZCh2YWx1ZSwgZm91bmRLZXkpO1xuXG4gICAgICAgICAgaWYgKGtleSA9PT0gZm91bmRLZXkpIHtcbiAgICAgICAgICAgIGJyZWFrXG4gICAgICAgICAgfVxuICAgICAgICB9IGNhdGNoIChlKSB7fVxuICAgICAgfVxuXG4gICAgICByZXR1cm4ga2V5ID8gamFyW2tleV0gOiBqYXJcbiAgICB9XG5cbiAgICByZXR1cm4gT2JqZWN0LmNyZWF0ZShcbiAgICAgIHtcbiAgICAgICAgc2V0OiBzZXQsXG4gICAgICAgIGdldDogZ2V0LFxuICAgICAgICByZW1vdmU6IGZ1bmN0aW9uIChrZXksIGF0dHJpYnV0ZXMpIHtcbiAgICAgICAgICBzZXQoXG4gICAgICAgICAgICBrZXksXG4gICAgICAgICAgICAnJyxcbiAgICAgICAgICAgIGFzc2lnbih7fSwgYXR0cmlidXRlcywge1xuICAgICAgICAgICAgICBleHBpcmVzOiAtMVxuICAgICAgICAgICAgfSlcbiAgICAgICAgICApO1xuICAgICAgICB9LFxuICAgICAgICB3aXRoQXR0cmlidXRlczogZnVuY3Rpb24gKGF0dHJpYnV0ZXMpIHtcbiAgICAgICAgICByZXR1cm4gaW5pdCh0aGlzLmNvbnZlcnRlciwgYXNzaWduKHt9LCB0aGlzLmF0dHJpYnV0ZXMsIGF0dHJpYnV0ZXMpKVxuICAgICAgICB9LFxuICAgICAgICB3aXRoQ29udmVydGVyOiBmdW5jdGlvbiAoY29udmVydGVyKSB7XG4gICAgICAgICAgcmV0dXJuIGluaXQoYXNzaWduKHt9LCB0aGlzLmNvbnZlcnRlciwgY29udmVydGVyKSwgdGhpcy5hdHRyaWJ1dGVzKVxuICAgICAgICB9XG4gICAgICB9LFxuICAgICAge1xuICAgICAgICBhdHRyaWJ1dGVzOiB7IHZhbHVlOiBPYmplY3QuZnJlZXplKGRlZmF1bHRBdHRyaWJ1dGVzKSB9LFxuICAgICAgICBjb252ZXJ0ZXI6IHsgdmFsdWU6IE9iamVjdC5mcmVlemUoY29udmVydGVyKSB9XG4gICAgICB9XG4gICAgKVxuICB9XG5cbiAgdmFyIGFwaSA9IGluaXQoZGVmYXVsdENvbnZlcnRlciwgeyBwYXRoOiAnLycgfSk7XG4gIC8qIGVzbGludC1lbmFibGUgbm8tdmFyICovXG5cbiAgcmV0dXJuIGFwaTtcblxufSkpKTtcbiIsIi8vIFRoZSBtb2R1bGUgY2FjaGVcbnZhciBfX3dlYnBhY2tfbW9kdWxlX2NhY2hlX18gPSB7fTtcblxuLy8gVGhlIHJlcXVpcmUgZnVuY3Rpb25cbmZ1bmN0aW9uIF9fd2VicGFja19yZXF1aXJlX18obW9kdWxlSWQpIHtcblx0Ly8gQ2hlY2sgaWYgbW9kdWxlIGlzIGluIGNhY2hlXG5cdHZhciBjYWNoZWRNb2R1bGUgPSBfX3dlYnBhY2tfbW9kdWxlX2NhY2hlX19bbW9kdWxlSWRdO1xuXHRpZiAoY2FjaGVkTW9kdWxlICE9PSB1bmRlZmluZWQpIHtcblx0XHRyZXR1cm4gY2FjaGVkTW9kdWxlLmV4cG9ydHM7XG5cdH1cblx0Ly8gQ3JlYXRlIGEgbmV3IG1vZHVsZSAoYW5kIHB1dCBpdCBpbnRvIHRoZSBjYWNoZSlcblx0dmFyIG1vZHVsZSA9IF9fd2VicGFja19tb2R1bGVfY2FjaGVfX1ttb2R1bGVJZF0gPSB7XG5cdFx0Ly8gbm8gbW9kdWxlLmlkIG5lZWRlZFxuXHRcdC8vIG5vIG1vZHVsZS5sb2FkZWQgbmVlZGVkXG5cdFx0ZXhwb3J0czoge31cblx0fTtcblxuXHQvLyBFeGVjdXRlIHRoZSBtb2R1bGUgZnVuY3Rpb25cblx0X193ZWJwYWNrX21vZHVsZXNfX1ttb2R1bGVJZF0uY2FsbChtb2R1bGUuZXhwb3J0cywgbW9kdWxlLCBtb2R1bGUuZXhwb3J0cywgX193ZWJwYWNrX3JlcXVpcmVfXyk7XG5cblx0Ly8gUmV0dXJuIHRoZSBleHBvcnRzIG9mIHRoZSBtb2R1bGVcblx0cmV0dXJuIG1vZHVsZS5leHBvcnRzO1xufVxuXG4iLCIvLyBkZWZpbmUgZ2V0dGVyIGZ1bmN0aW9ucyBmb3IgaGFybW9ueSBleHBvcnRzXG5fX3dlYnBhY2tfcmVxdWlyZV9fLmQgPSAoZXhwb3J0cywgZGVmaW5pdGlvbikgPT4ge1xuXHRmb3IodmFyIGtleSBpbiBkZWZpbml0aW9uKSB7XG5cdFx0aWYoX193ZWJwYWNrX3JlcXVpcmVfXy5vKGRlZmluaXRpb24sIGtleSkgJiYgIV9fd2VicGFja19yZXF1aXJlX18ubyhleHBvcnRzLCBrZXkpKSB7XG5cdFx0XHRPYmplY3QuZGVmaW5lUHJvcGVydHkoZXhwb3J0cywga2V5LCB7IGVudW1lcmFibGU6IHRydWUsIGdldDogZGVmaW5pdGlvbltrZXldIH0pO1xuXHRcdH1cblx0fVxufTsiLCJfX3dlYnBhY2tfcmVxdWlyZV9fLm8gPSAob2JqLCBwcm9wKSA9PiAoT2JqZWN0LnByb3RvdHlwZS5oYXNPd25Qcm9wZXJ0eS5jYWxsKG9iaiwgcHJvcCkpIiwiLy8gZGVmaW5lIF9fZXNNb2R1bGUgb24gZXhwb3J0c1xuX193ZWJwYWNrX3JlcXVpcmVfXy5yID0gKGV4cG9ydHMpID0+IHtcblx0aWYodHlwZW9mIFN5bWJvbCAhPT0gJ3VuZGVmaW5lZCcgJiYgU3ltYm9sLnRvU3RyaW5nVGFnKSB7XG5cdFx0T2JqZWN0LmRlZmluZVByb3BlcnR5KGV4cG9ydHMsIFN5bWJvbC50b1N0cmluZ1RhZywgeyB2YWx1ZTogJ01vZHVsZScgfSk7XG5cdH1cblx0T2JqZWN0LmRlZmluZVByb3BlcnR5KGV4cG9ydHMsICdfX2VzTW9kdWxlJywgeyB2YWx1ZTogdHJ1ZSB9KTtcbn07IiwiLy8gZnVuY3Rpb24gYmluZFdlYkFjdGlvbnMoKSB7XG4vLyAgICAgJCQoXCJpbmRpZS1hY3Rpb25cIikuZWFjaChmdW5jdGlvbigpIHtcbi8vICAgICAgICAgdGhpcy5vbmNsaWNrID0gZnVuY3Rpb24oZSkge1xuLy8gICAgICAgICAgICAgdmFyIGFjdGlvbl9saW5rID0gdGhpcy5xdWVyeVNlbGVjdG9yKFwiYVwiKTtcbi8vICAgICAgICAgICAgIC8vIFRPRE8gYWN0aW9uX2xpbmsuYXR0cihcImNsYXNzXCIsIFwiZmEgZmEtc3Bpbm5lciBmYS1zcGluXCIpO1xuLy9cbi8vICAgICAgICAgICAgIHZhciBhY3Rpb25fZG8gPSB0aGlzLmdldEF0dHJpYnV0ZShcImRvXCIpO1xuLy8gICAgICAgICAgICAgdmFyIGFjdGlvbl93aXRoID0gdGhpcy5nZXRBdHRyaWJ1dGUoXCJ3aXRoXCIpO1xuLy9cbi8vICAgICAgICAgICAgIC8vIHByb3RvY29sQ2hlY2soXCJ3ZWIrYWN0aW9uOi8vXCIgKyBhY3Rpb25fZG8gKyBcIj91cmw9XCIgKyBhY3Rpb25fd2l0aCxcbi8vICAgICAgICAgICAgIC8vIHNldFRpbWVvdXQoZnVuY3Rpb24oKSB7XG4vLyAgICAgICAgICAgICAvLyAgICAgdmFyIHVybCA9IFwiLy9jYW5vcHkuZ2FyZGVuLz9vcmlnaW49XCIgKyB3aW5kb3cubG9jYXRpb24uaHJlZiArXG4vLyAgICAgICAgICAgICAvLyAgICAgICAgICAgICAgIFwiZG89XCIgKyBhY3Rpb25fZG8gKyBcIiZ3aXRoPVwiICsgYWN0aW9uX3dpdGg7XG4vLyAgICAgICAgICAgICAvLyAgICAgdmFyIGh0bWwgPSBgPCEtLXA+WW91ciBkZXZpY2UgZG9lcyBub3Qgc3VwcG9ydCB3ZWJcbi8vICAgICAgICAgICAgIC8vICAgICAgICAgICAgICAgICBhY3Rpb25zPGJyPjxlbT48c3Ryb25nPm9yPC9zdHJvbmc+PC9lbT48YnI+XG4vLyAgICAgICAgICAgICAvLyAgICAgICAgICAgICAgICAgWW91IGhhdmUgbm90IHlldCBwYWlyZWQgeW91ciB3ZWJzaXRlIHdpdGhcbi8vICAgICAgICAgICAgIC8vICAgICAgICAgICAgICAgICB5b3VyIGJyb3dzZXI8L3A+XG4vLyAgICAgICAgICAgICAvLyAgICAgICAgICAgICAgICAgPGhyLS0+XG4vLyAgICAgICAgICAgICAvLyAgICAgICAgICAgICAgICAgPHA+SWYgeW91IGhhdmUgYSB3ZWJzaXRlIHRoYXQgc3VwcG9ydHMgd2ViXG4vLyAgICAgICAgICAgICAvLyAgICAgICAgICAgICAgICAgYWN0aW9ucyBlbnRlciBpdCBoZXJlOjwvcD5cbi8vICAgICAgICAgICAgIC8vICAgICAgICAgICAgICAgICA8Zm9ybSBpZD1hY3Rpb24taGFuZGxlciBhY3Rpb249L2FjdGlvbnMtZmluZGVyPlxuLy8gICAgICAgICAgICAgLy8gICAgICAgICAgICAgICAgIDxsYWJlbD5Zb3VyIFdlYnNpdGVcbi8vICAgICAgICAgICAgIC8vICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPWJvdW5kaW5nPjxpbnB1dCB0eXBlPXRleHRcbi8vICAgICAgICAgICAgIC8vICAgICAgICAgICAgICAgICBuYW1lPXVybD48L2Rpdj48L2xhYmVsPlxuLy8gICAgICAgICAgICAgLy8gICAgICAgICAgICAgICAgIDxpbnB1dCB0eXBlPWhpZGRlbiBuYW1lPWRvIHZhbHVlPVwiJHthY3Rpb25fZG99XCI+XG4vLyAgICAgICAgICAgICAvLyAgICAgICAgICAgICAgICAgPGlucHV0IHR5cGU9aGlkZGVuIG5hbWU9d2l0aCB2YWx1ZT1cIiR7YWN0aW9uX3dpdGh9XCI+XG4vLyAgICAgICAgICAgICAvLyAgICAgICAgICAgICAgICAgPHA+PHNtYWxsPlRhcmdldDpcbi8vICAgICAgICAgICAgIC8vICAgICAgICAgICAgICAgICA8Y29kZT4ke2FjdGlvbl93aXRofTwvY29kZT48L3NtYWxsPjwvcD5cbi8vICAgICAgICAgICAgIC8vICAgICAgICAgICAgICAgICA8YnV0dG9uPiR7YWN0aW9uX2RvfTwvYnV0dG9uPlxuLy8gICAgICAgICAgICAgLy8gICAgICAgICAgICAgICAgIDwvZm9ybT5cbi8vICAgICAgICAgICAgIC8vICAgICAgICAgICAgICAgICA8cD5JZiB5b3UgZG8gbm90IHlvdSBjYW4gY3JlYXRlIG9uZSA8YVxuLy8gICAgICAgICAgICAgLy8gICAgICAgICAgICAgICAgIGhyZWY9XCIke3VybH1cIj5oZXJlPC9hPi48L3A+YDtcbi8vICAgICAgICAgICAgIC8vICAgICBzd2l0Y2ggKGFjdGlvbl9kbykge1xuLy8gICAgICAgICAgICAgLy8gICAgICAgICBjYXNlIFwic2lnbi1pblwiOlxuLy8gICAgICAgICAgICAgLy8gICAgICAgICAgICAgaHRtbCA9IGh0bWwgKyBgPHA+SWYgeW91IGFyZSB0aGUgb3duZXIgb2YgdGhpcyBzaXRlLFxuLy8gICAgICAgICAgICAgLy8gICAgICAgICAgICAgICAgICAgICAgICAgICAgPGEgaHJlZj0vc2VjdXJpdHkvaWRlbnRpZmljYXRpb24+c2lnblxuLy8gICAgICAgICAgICAgLy8gICAgICAgICAgICAgICAgICAgICAgICAgICAgaW4gaGVyZTwvYT4uPC9wPmA7XG4vLyAgICAgICAgICAgICAvLyAgICAgfVxuLy8gICAgICAgICAgICAgLy8gICAgIGh0bWwgPSBodG1sICsgYDxwPjxzbWFsbD48YSBocmVmPS9oZWxwI3dlYi1hY3Rpb25zPkxlYXJuXG4vLyAgICAgICAgICAgICAvLyAgICAgICAgICAgICAgICAgICAgbW9yZSBhYm91dCB3ZWIgYWN0aW9uczwvYT48L3NtYWxsPjwvcD5gO1xuLy8gICAgICAgICAgICAgLy8gICAgICQoXCIjd2ViYWN0aW9uX2hlbHBcIikuaW5uZXJIVE1MID0gaHRtbDtcbi8vICAgICAgICAgICAgIC8vICAgICAkKFwiI3dlYmFjdGlvbl9oZWxwXCIpLnN0eWxlLmRpc3BsYXkgPSBcImJsb2NrXCI7XG4vLyAgICAgICAgICAgICAvLyAgICAgJChcIiNibGFja291dFwiKS5zdHlsZS5kaXNwbGF5ID0gXCJibG9ja1wiO1xuLy8gICAgICAgICAgICAgLy8gICAgICQoXCIjYmxhY2tvdXRcIikub25jbGljayA9IGZ1bmN0aW9uKCkge1xuLy8gICAgICAgICAgICAgLy8gICAgICAgICAkKFwiI3dlYmFjdGlvbl9oZWxwXCIpLnN0eWxlLmRpc3BsYXkgPSBcIm5vbmVcIjtcbi8vICAgICAgICAgICAgIC8vICAgICAgICAgJChcIiNibGFja291dFwiKS5zdHlsZS5kaXNwbGF5ID0gXCJub25lXCI7XG4vLyAgICAgICAgICAgICAvLyAgICAgfTtcbi8vICAgICAgICAgICAgIC8vIH0sIDIwMCk7XG4vL1xuLy8gICAgICAgICAgICAgd2luZG93LmxvY2F0aW9uID0gYWN0aW9uX2xpbmsuZ2V0QXR0cmlidXRlKFwiaHJlZlwiKTtcbi8vXG4vLyAgICAgICAgICAgICBlLnByZXZlbnREZWZhdWx0ID8gZS5wcmV2ZW50RGVmYXVsdCgpIDogZS5yZXR1cm5WYWx1ZSA9IGZhbHNlO1xuLy8gICAgICAgICB9XG4vLyAgICAgfSk7XG4vLyB9XG4vLyAkLmxvYWQoZnVuY3Rpb24gKCkge1xuLy8gICBiaW5kV2ViQWN0aW9ucygpXG4vL1xuLy8gICAvKlxuLy8gICAgICQkKFwiLnB1YmtleVwiKS5lYWNoKGZ1bmN0aW9uKCkge1xuLy8gICAgICAgICB2YXIgYXJtb3JlZF9wdWJrZXkgPSAkKHRoaXMpLnRleHQoKTtcbi8vICAgICAgICAgaWYgKGFybW9yZWRfcHVia2V5KSB7XG4vLyAgICAgICAgICAgICB2YXIgcHVia2V5ID0gZ2V0X3B1YmtleShhcm1vcmVkX3B1YmtleSk7XG4vLyAgICAgICAgICAgICB2YXIgZmluZ2VycHJpbnQgPSBwdWJrZXkuZmluZ2VycHJpbnQuc3Vic3RyaW5nKDAsIDIpO1xuLy8gICAgICAgICAgICAgZm9yIChpID0gMjsgaSA8IDQwOyBpID0gaSArIDIpXG4vLyAgICAgICAgICAgICAgICAgZmluZ2VycHJpbnQgPSBmaW5nZXJwcmludCArIFwiOlwiICtcbi8vICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHB1YmtleS5maW5nZXJwcmludC5zdWJzdHJpbmcoaSwgaSArIDIpO1xuLy8gICAgICAgICAgICAgJCh0aGlzKS5hZnRlcihcIjxjb2RlIGNsYXNzPWZpbmdlcnByaW50PjxzcGFuPlwiICtcbi8vICAgICAgICAgICAgICAgICAgICAgICAgICAgZmluZ2VycHJpbnQuc3Vic3RyKDAsIDMwKSArIFwiPC9zcGFuPjxzcGFuPlwiICtcbi8vICAgICAgICAgICAgICAgICAgICAgICAgICAgZmluZ2VycHJpbnQuc3Vic3RyKDMwLCA2MCkgKyBcIjwvc3Bhbj48L2NvZGU+XCIpO1xuLy8gICAgICAgICB9XG4vLyAgICAgfSk7XG4vLyAgICAgKi9cbi8vXG4vLyAgIC8vIHZhciBteVNWRyA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFwiYWN0aW9uX2xpa2VcIik7XG4vLyAgIC8vIHZhciBzdmdEb2M7XG4vLyAgIC8vIG15U1ZHLmFkZEV2ZW50TGlzdGVuZXIoXCJsb2FkXCIsZnVuY3Rpb24oKSB7XG4vLyAgIC8vICAgICBzdmdEb2MgPSBteVNWRy5jb250ZW50RG9jdW1lbnQ7XG4vLyAgIC8vICAgICBwYXRoID0gc3ZnRG9jLnF1ZXJ5U2VsZWN0b3IoXCJwYXRoXCIpO1xuLy8gICAvLyAgICAgc2V0VGltZW91dChmdW5jdGlvbigpIHtcbi8vICAgLy8gICAgICAgICBwYXRoLnNldEF0dHJpYnV0ZShcImZpbGxcIiwgXCJyZWRcIik7XG4vLyAgIC8vICAgICAgICAgbXlTVkcuc2V0QXR0cmlidXRlKFwiY2xhc3NcIiwgXCJpY29uIGFuaW1hdGVkIHB1bHNlXCIpO1xuLy8gICAvLyAgICAgfSwgMjAwMCk7XG4vLyAgIC8vIH0sIGZhbHNlKTtcbi8vXG4vLyAgIC8vICQkKFwiLmljb25cIikuZWFjaChmdW5jdGlvbigpIHtcbi8vICAgLy8gICAgIHZhciBzdmdEb2M7XG4vLyAgIC8vICAgICB2YXIgbXlTVkcgPSB0aGlzO1xuLy8gICAvLyAgICAgbXlTVkcuYWRkRXZlbnRMaXN0ZW5lcihcImxvYWRcIiwgZnVuY3Rpb24oKSB7XG4vLyAgIC8vICAgICAgICAgc3ZnRG9jID0gbXlTVkcuY29udGVudERvY3VtZW50O1xuLy8gICAvLyAgICAgICAgIC8vIGZ1bmN0aW9uIHooKSB7XG4vLyAgIC8vICAgICAgICAgICAgIHN2Z0RvYy5xdWVyeVNlbGVjdG9yKFwicGF0aFwiKS5zZXRBdHRyaWJ1dGUoXCJmaWxsXCIsIFwiIzJhYTE5OFwiKTtcbi8vICAgLy8gICAgICAgICAgICAgLy8gbXlTVkcuc2V0QXR0cmlidXRlKFwiY2xhc3NcIiwgXCJpY29uIGFuaW1hdGVkIHB1bHNlXCIpO1xuLy8gICAvLyAgICAgICAgIC8vIH1cbi8vICAgLy8gICAgICAgICAvLyBzZXRUaW1lb3V0KHosIDIwMDApO1xuLy8gICAvLyAgICAgfSwgZmFsc2UpO1xuLy8gICAvLyB9KTtcbi8vXG4vLyAgIC8vICQoXCJhLnF1b3RlXCIpLmNsaWNrKGZ1bmN0aW9uKCkge1xuLy8gICAvLyAgICAgd2luZG93LmxvY2F0aW9uID0gXCJ3ZWIrYWN0aW9uOi8vcXVvdGU9P3VybD1cIiArIHdpbmRvdy5sb2NhdGlvbiArXG4vLyAgIC8vICAgICAgICAgICAgICAgICAgICAgICBcIiZxdW90ZT1cIiArIHdpbmRvdy5nZXRTZWxlY3Rpb24oKS50b1N0cmluZygpO1xuLy8gICAvLyAgICAgcmV0dXJuIGZhbHNlXG4vLyAgIC8vIH0pO1xuLy9cbi8vICAgLy8gJCQoXCIjc2VhcmNoXCIpLnN1Ym1pdChmdW5jdGlvbigpIHtcbi8vICAgLy8gICAgICQuYWpheCh7bWV0aG9kOiBcIkdFVFwiLFxuLy8gICAvLyAgICAgICAgICAgICAgdXJsOiBcIi9zZWFyY2g/cXVlcnk9XCIgK1xuLy8gICAvLyAgICAgICAgICAgICAgICAgICAkKHRoaXMpLmZpbmQoXCJpbnB1dFtuYW1lPXF1ZXJ5XVwiKS52YWwoKX0pXG4vLyAgIC8vICAgICAgICAgLmRvbmUoZnVuY3Rpb24obXNnKSB7ICQoXCIjcmVzb3VyY2VfcHJldmlld1wiKS5odG1sKG1zZyk7IH0pO1xuLy8gICAvLyAgICAgcmV0dXJuIGZhbHNlXG4vLyAgIC8vIH0pO1xuLy8gfSlcbi8vIGZ1bmN0aW9uIGdldF9wdWJrZXkgKGFybW9yZWRfcHVia2V5KSB7XG4vLyAgIC8qXG4vLyAgICAgaGFuZGxlIGRpc3BsYXlpbmcgb2YgZmluZ2VycHJpbnRzXG4vL1xuLy8gICAgICovXG4vLyAgIGxldCBmb3VuZEtleXMgPSBvcGVucGdwLmtleS5yZWFkQXJtb3JlZChhcm1vcmVkX3B1YmtleSkua2V5c1xuLy8gICBpZiAoIWZvdW5kS2V5cyB8fCBmb3VuZEtleXMubGVuZ3RoICE9PSAxKSB7XG4vLyAgICAgdGhyb3cgbmV3IEVycm9yKCdObyBrZXkgZm91bmQgb3IgbW9yZSB0aGFuIG9uZSBrZXknKVxuLy8gICB9XG4vLyAgIGNvbnN0IHB1YktleSA9IGZvdW5kS2V5c1swXVxuLy8gICBmb3VuZEtleXMgPSBudWxsXG4vLyAgIHJldHVybiBwdWJLZXkucHJpbWFyeUtleVxuLy8gfVxuLy8gYWN0aXZhdGUgZmFzdCBBRVMtR0NNIG1vZGUgKG5vdCB5ZXQgT3BlblBHUCBzdGFuZGFyZClcbi8vIG9wZW5wZ3AuY29uZmlnLmFlYWRfcHJvdGVjdCA9IHRydWU7ICAvLyBUT0RPIG1vdmUgdG8gYWZ0ZXIgb3BlbnBncCBsb2FkXG4vLyBmdW5jdGlvbiBzaWduIChwYXlsb2FkLCBoYW5kbGVyKSB7XG4vLyAgIC8vIFhYWCB2YXIgcHVia2V5ID0gbG9jYWxTdG9yYWdlW1wicHVia2V5XCJdO1xuLy8gICAvLyBYWFggdmFyIHByaXZrZXkgPSBsb2NhbFN0b3JhZ2VbXCJwcml2a2V5XCJdO1xuLy8gICAvLyBYWFggdmFyIHBhc3NwaHJhc2UgPSBcIlwiOyAgLy8gd2luZG93LnByb21wdChcInBsZWFzZSBlbnRlciB0aGUgcGFzcyBwaHJhc2VcIik7XG4vL1xuLy8gICAvLyBYWFggLy8gY29uc29sZS5sb2cob3BlbnBncC5rZXkucmVhZEFybW9yZWQocHJpdmtleSkpO1xuLy8gICAvLyBYWFggLy8gdmFyIHByaXZLZXlPYmogPSBvcGVucGdwLmtleS5yZWFkQXJtb3JlZChwcml2a2V5KS5rZXlzWzBdO1xuLy8gICAvLyBYWFggLy8gcHJpdktleU9iai5kZWNyeXB0KHBhc3NwaHJhc2UpO1xuLy9cbi8vICAgLy8gWFhYIC8vIG9wdGlvbnMgPSB7XG4vLyAgIC8vIFhYWCAvLyAgICAgbWVzc2FnZTogb3BlbnBncC5jbGVhcnRleHQuZnJvbVRleHQoJ0hlbGxvLCBXb3JsZCEnKSxcbi8vICAgLy8gWFhYIC8vICAgICBwcml2YXRlS2V5czogW3ByaXZLZXlPYmpdXG4vLyAgIC8vIFhYWCAvLyB9O1xuLy9cbi8vICAgLy8gWFhYIC8vIG9wZW5wZ3Auc2lnbihvcHRpb25zKS50aGVuKGZ1bmN0aW9uKHNpZ25lZCkge1xuLy8gICAvLyBYWFggLy8gICAgIGNsZWFydGV4dCA9IHNpZ25lZC5kYXRhO1xuLy8gICAvLyBYWFggLy8gICAgIGNvbnNvbGUubG9nKGNsZWFydGV4dCk7XG4vLyAgIC8vIFhYWCAvLyB9KTtcbi8vXG4vLyAgIC8vIFhYWCBvcGVucGdwLmtleS5yZWFkQXJtb3JlZChwcml2a2V5KS50aGVuKGZ1bmN0aW9uKHByaXZLZXlPYmopIHtcbi8vICAgLy8gWFhYICAgICAvLyBYWFggdmFyIHByaXZLZXlPYmogPSB6LmtleXNbMF07XG4vLyAgIC8vIFhYWCAgICAgLy8gWFhYIHByaXZLZXlPYmouZGVjcnlwdChwYXNzcGhyYXNlKTtcbi8vICAgLy8gWFhYICAgICAvLyBYWFggdmFyIG9wdGlvbnMgPSB7ZGF0YTogcGF5bG9hZCwgcHJpdmF0ZUtleXM6IHByaXZLZXlPYmp9O1xuLy8gICAvLyBYWFggICAgIHZhciBvcHRpb25zID0ge21lc3NhZ2U6IG9wZW5wZ3AuY2xlYXJ0ZXh0LmZyb21UZXh0KFwiaGVsbG93b3JsZFwiKSxcbi8vICAgLy8gWFhYICAgICAgICAgICAgICAgICAgICBwcml2YXRlS2V5czogW3ByaXZLZXlPYmpdfVxuLy8gICAvLyBYWFggICAgIG9wZW5wZ3Auc2lnbihvcHRpb25zKS50aGVuKGhhbmRsZXIpO1xuLy8gICAvLyBYWFggfSk7XG4vLyB9XG4vLyBmdW5jdGlvbiBzaWduX2Zvcm0gKGZvcm0sIGRhdGEsIHN1Ym1pc3Npb25faGFuZGxlcikge1xuLy8gICBjb25zdCBidXR0b24gPSBmb3JtLmZpbmQoJ2J1dHRvbicpXG4vLyAgIGJ1dHRvbi5wcm9wKCdkaXNhYmxlZCcsIHRydWUpXG4vLyAgIGNvbnN0IHRpbWVzdGFtcCA9IERhdGUubm93KClcbi8vICAgZm9ybS5hcHBlbmQoXCI8aW5wdXQgdHlwZT1oaWRkZW4gbmFtZT1wdWJsaXNoZWQgdmFsdWU9J1wiICtcbi8vICAgICAgICAgICAgICAgICB0aW1lc3RhbXAgKyBcIic+XCIpXG4vLyAgIGRhdGEucHVibGlzaGVkID0gdGltZXN0YW1wXG4vLyAgIGNvbnN0IHBheWxvYWQgPSBKU09OLnN0cmluZ2lmeShkYXRhLCBPYmplY3Qua2V5cyhkYXRhKS5zb3J0KCksICcgICcpXG4vLyAgIHNpZ24ocGF5bG9hZCwgZnVuY3Rpb24gKHNpZ25lZCkge1xuLy8gICAgIGZvcm0uYXBwZW5kKCc8aW5wdXQgaWQ9c2lnbmF0dXJlIHR5cGU9aGlkZGVuIG5hbWU9c2lnbmF0dXJlPicpXG4vLyAgICAgJCgnI3NpZ25hdHVyZScpLnZhbChzaWduZWQuZGF0YSlcbi8vICAgICAvLyBYWFggZm9ybS5zdWJtaXQoKTtcbi8vICAgICBzdWJtaXNzaW9uX2hhbmRsZXIoKVxuLy8gICAgIGJ1dHRvbi5wcm9wKCdkaXNhYmxlZCcsIGZhbHNlKVxuLy8gICB9KVxuLy8gfVxuLy8gZnVuY3Rpb24gZ2V0VGltZVNsdWcgKHdoZW4pIHtcbi8vICAgY29uc3QgY2VudGlzZWNvbmRzID0gKCgod2hlbi5ob3VycygpICogMzYwMCkgK1xuLy8gICAgICAgICAgICAgICAgICAgICAgICAgICh3aGVuLm1pbnV0ZXMoKSAqIDYwKSArXG4vLyAgICAgICAgICAgICAgICAgICAgICAgICAgd2hlbi5zZWNvbmRzKCkpICogMTAwKSArXG4vLyAgICAgICAgICAgICAgICAgICAgICAgIE1hdGgucm91bmQod2hlbi5taWxsaXNlY29uZHMoKSAvIDEwKVxuLy8gICByZXR1cm4gd2hlbi5mb3JtYXQoJ1kvTU0vREQvJykgKyBudW1fdG9fc3hnZihjZW50aXNlY29uZHMsIDQpXG4vLyB9XG4vLyBmdW5jdGlvbiBnZXRUZXh0U2x1ZyAod29yZHMpIHtcbi8vICAgbGV0IHBhZGRpbmcgPSAnJ1xuLy8gICBpZiAod29yZHMuc2xpY2UoLTEpID09ICcgJykgeyBwYWRkaW5nID0gJ18nIH1cbi8vICAgcmV0dXJuIHdvcmRzLnRvTG93ZXJDYXNlKCkuc3BsaXQocHVuY3RfcmUpLmpvaW4oJ18nKVxuLy8gICAgIC5yZXBsYWNlKC9fJCQvZ20sICcnKSArIHBhZGRpbmdcbi8vIH1cbi8vIGZ1bmN0aW9uIHByZXZpZXdJbWFnZShmaWxlLCBwcmV2aWV3X2NvbnRhaW5lcikge1xuLy8gICAgIHJldHVybiBmYWxzZVxuLy8gICAgIHZhciByZWFkZXIgPSBuZXcgRmlsZVJlYWRlcigpO1xuLy8gICAgIHJlYWRlci5vbmxvYWQgPSBmdW5jdGlvbiAoZSkge1xuLy8gICAgICAgICBwcmV2aWV3X2NvbnRhaW5lci5hdHRyKFwic3JjXCIsIGUudGFyZ2V0LnJlc3VsdCk7XG4vLyAgICAgfVxuLy8gICAgIHJlYWRlci5yZWFkQXNEYXRhVVJMKGZpbGUpO1xuLy9cbi8vICAgICAvLyB2YXIgZGF0YSA9IG5ldyBGb3JtRGF0YSgpO1xuLy8gICAgIC8vIGRhdGEuYXBwZW5kKFwiZmlsZS0wXCIsIGZpbGUpO1xuLy8gICAgIC8vICQuYWpheCh7bWV0aG9kOiBcIlBPU1RcIixcbi8vICAgICAvLyAgICAgICAgIHVybDogXCIvZWRpdG9yL21lZGlhXCIsXG4vLyAgICAgLy8gICAgICAgICBjb250ZW50VHlwZTogXCJtdWx0aXBhcnQvZm9ybS1kYXRhXCIsXG4vLyAgICAgLy8gICAgICAgICBkYXRhOiBkYXRhXG4vLyAgICAgLy8gICAgICAgIH0pLmRvbmUoZnVuY3Rpb24obXNnKSB7XG4vLyAgICAgLy8gICAgICAgICAgICAgICAgICAgIGNvbnNvbGUubG9nKFwicmVwc29uc2VcIik7XG4vLyAgICAgLy8gICAgICAgICAgICAgICAgICAgIGNvbnNvbGUubG9nKG1zZyk7XG4vLyAgICAgLy8gICAgICAgICAgICAgICAgICAgIHZhciBib2R5ID0gbXNnW1wiY29udGVudFwiXTtcbi8vICAgICAvLyAgICAgICAgICAgICAgICAgICAgcHJldmlld19jb250YWluZXIuaHRtbChib2R5KTtcbi8vICAgICAvLyAgICAgICAgICAgICAgICB9KTtcbi8vIH1cbi8vIGZ1bmN0aW9uIHByZXZpZXdSZXNvdXJjZSAodXJsLCBoYW5kbGVyKSB7XG4vLyAgIGlmICh1cmwgPT0gJycpIHtcbi8vICAgICAvLyBwcmV2aWV3X2NvbnRhaW5lci5pbm5lckhUTUwgPSBcIlwiO1xuLy8gICAgIHJldHVyblxuLy8gICB9XG4vL1xuLy8gICBjb25zdCB4aHIgPSBuZXcgWE1MSHR0cFJlcXVlc3QoKVxuLy8gICB4aHIub3BlbignR0VUJywgJy9lZGl0b3IvcHJldmlldy9taWNyb2Zvcm1hdHM/dXJsPScgK1xuLy8gICAgICAgICAgICAgICAgICAgICBlbmNvZGVVUklDb21wb25lbnQodXJsKSlcbi8vICAgeGhyLm9ubG9hZCA9IGZ1bmN0aW9uICgpIHtcbi8vICAgICBpZiAoeGhyLnN0YXR1cyA9PT0gMjAwKSB7XG4vLyAgICAgICBjb25zdCByZXNwb25zZSA9IEpTT04ucGFyc2UoeGhyLnJlc3BvbnNlVGV4dClcbi8vICAgICAgIC8vIHZhciBlbnRyeSA9IHJlc3BvbnNlW1wiZW50cnlcIl07XG4vLyAgICAgICAvLyBYWFggY29uc29sZS5sb2cocmVzcG9uc2UpO1xuLy8gICAgICAgaGFuZGxlcihyZXNwb25zZSlcbi8vICAgICAgIC8vIHZhciBib2R5ID0gXCJcIjtcbi8vICAgICAgIC8vIGlmIChcInByb2ZpbGVcIiBpbiByZXNwb25zZSkge1xuLy8gICAgICAgLy8gICAgIC8vIGFzZFxuLy8gICAgICAgLy8gfSBlbHNlIGlmIChlbnRyeSkge1xuLy8gICAgICAgLy8gICAgIGlmIChcIm5hbWVcIiBpbiBlbnRyeSlcbi8vICAgICAgIC8vICAgICAgICAgYm9keSA9IFwidW5rbm93biB0eXBlXCI7XG4vLyAgICAgICAvLyAgICAgZWxzZSBpZiAoXCJwaG90b1wiIGluIGVudHJ5KVxuLy8gICAgICAgLy8gICAgICAgICBib2R5ID0gXCJQaG90bzo8YnI+PGltZyBzcmM9XCIgKyBlbnRyeVtcInBob3RvXCJdICsgXCI+XCI7XG4vLyAgICAgICAvLyAgICAgZWxzZVxuLy8gICAgICAgLy8gICAgICAgICBib2R5ID0gXCJOb3RlOjxicj5cIiArIGVudHJ5W1wiY29udGVudFwiXTtcbi8vICAgICAgIC8vIH1cbi8vICAgICAgIC8vIHByZXZpZXdfY29udGFpbmVyLmlubmVySFRNTCA9IGJvZHk7XG4vLyAgICAgfSBlbHNlIHsgY29uc29sZS5sb2coJ3JlcXVlc3QgZmFpbGVkOiAnICsgeGhyLnN0YXR1cykgfVxuLy8gICB9XG4vLyAgIHhoci5zZW5kKClcbi8vIH1cbi8vICQoZnVuY3Rpb24oKSB7XG4vLyAgICAgdmFyIGN1cnJlbnRfYm9keSA9IFwiXCI7XG4vLyAgICAgZnVuY3Rpb24gc2V0VGltZXIoKSB7XG4vLyAgICAgICAgIHNldFRpbWVvdXQoZnVuY3Rpb24oKSB7XG4vLyAgICAgICAgICAgICB2YXIgbmV3X2JvZHkgPSAkKFwiI2JvZHlcIikudmFsKCk7XG4vLyAgICAgICAgICAgICBpZiAobmV3X2JvZHkgIT0gY3VycmVudF9ib2R5KSB7XG4vLyAgICAgICAgICAgICAgICAgJC5hamF4KHttZXRob2Q6IFwiUE9TVFwiLFxuLy8gICAgICAgICAgICAgICAgICAgICAgICAgIHVybDogXCIvY29udGVudC9lZGl0b3IvcHJldmlld1wiLFxuLy8gICAgICAgICAgICAgICAgICAgICAgICAgIGRhdGE6IHtjb250ZW50OiBuZXdfYm9keX1cbi8vICAgICAgICAgICAgICAgICAgICAgICAgIH0pLmRvbmUoZnVuY3Rpb24obXNnKSB7XG4vLyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAkKFwiI2JvZHlfcmVhZGFiaWxpdHlcIikuaHRtbChtc2dbXCJyZWFkYWJpbGl0eVwiXSk7XG4vLyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAkKFwiI2JvZHlfcHJldmlld1wiKS5odG1sKG1zZ1tcImNvbnRlbnRcIl0pO1xuLy8gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTtcbi8vICAgICAgICAgICAgICAgICBjdXJyZW50X2JvZHkgPSBuZXdfYm9keTtcbi8vICAgICAgICAgICAgIH1cbi8vICAgICAgICAgICAgIHNldFRpbWVyKCk7XG4vLyAgICAgICAgIH0sIDUwMDApO1xuLy8gICAgIH07XG4vLyAgICAgc2V0VGltZXIoKTtcbi8vIH0pO1xuLy8gY29uc3Qgc29ja2V0X29yaWdpbiA9ICh3aW5kb3cubG9jYXRpb24ucHJvdG9jb2wgPT0gJ2h0dHA6JyA/ICd3cycgOiAnd3NzJykgK1xuLy8gICAgICAgICAgICAgICAgICAgICAgICc6Ly8nICsgd2luZG93LmxvY2F0aW9uLmhvc3QgKyAnLydcbi8vICAgZm9sbG93ZXJzICguLi5jaGFubmVsKSB7XG4vLyAgICAgbGV0IHJlcXVlc3RVcmwgPSB0aGlzLmVuZHBvaW50ICsgJ2FjdGlvbj1mb2xsb3cnXG4vLyAgICAgaWYgKGNoYW5uZWwubGVuZ3RoKSB7XG4vLyAgICAgICByZXF1ZXN0VXJsICs9IGAmY2hhbm5lbD0ke2NoYW5uZWxbMF19YFxuLy8gICAgIH1cbi8vICAgICByZXR1cm4gZmV0Y2gocmVxdWVzdFVybCkudGhlbihyZXNwb25zZSA9PiB7XG4vLyAgICAgICBpZiAocmVzcG9uc2Uuc3RhdHVzID09PSAyMDAgfHwgcmVzcG9uc2Uuc3RhdHVzID09PSAyMDEpIHtcbi8vICAgICAgICAgcmV0dXJuIHJlc3BvbnNlLmpzb24oKS50aGVuKGRhdGEgPT4ge1xuLy8gICAgICAgICAgIHJldHVybiBkYXRhXG4vLyAgICAgICAgIH0pXG4vLyAgICAgICB9XG4vLyAgICAgfSlcbi8vICAgfVxuLy9cbi8vICAgZm9sbG93ICh1cmwsIC4uLmNoYW5uZWwpIHtcbi8vICAgICBsZXQgYm9keSA9IGBhY3Rpb249Zm9sbG93JnVybD0ke3VybH1gXG4vLyAgICAgaWYgKGNoYW5uZWwubGVuZ3RoKSB7XG4vLyAgICAgICBib2R5ICs9IGAmY2hhbm5lbD0ke2NoYW5uZWxbMF19YFxuLy8gICAgIH1cbi8vICAgICBmZXRjaCh0aGlzLmVuZHBvaW50LCB7XG4vLyAgICAgICBtZXRob2Q6ICdQT1NUJyxcbi8vICAgICAgIGhlYWRlcnM6IHsgJ2NvbnRlbnQtdHlwZSc6ICdhcHBsaWNhdGlvbi94LXd3dy1mb3JtLXVybGVuY29kZWQnIH0sXG4vLyAgICAgICBib2R5OiBib2R5XG4vLyAgICAgfSkudGhlbihyZXNwb25zZSA9PiB7XG4vLyAgICAgICBpZiAocmVzcG9uc2Uuc3RhdHVzID09PSAyMDAgfHwgcmVzcG9uc2Uuc3RhdHVzID09PSAyMDEpIHtcbi8vICAgICAgICAgcmV0dXJuIHJlc3BvbnNlLmpzb24oKS50aGVuKGRhdGEgPT4ge1xuLy8gICAgICAgICAgIHJldHVybiBkYXRhXG4vLyAgICAgICAgIH0pXG4vLyAgICAgICB9XG4vLyAgICAgfSlcbi8vICAgfVxuLy9cbi8vICAgc2VhcmNoIChxdWVyeSwgLi4uY2hhbm5lbCkge1xuLy8gICAgIGxldCBib2R5ID0gYGFjdGlvbj1zZWFyY2gmcXVlcnk9JHtxdWVyeX1gXG4vLyAgICAgaWYgKGNoYW5uZWwubGVuZ3RoKSB7XG4vLyAgICAgICBib2R5ICs9IGAmY2hhbm5lbD0ke2NoYW5uZWxbMF19YFxuLy8gICAgIH1cbi8vICAgICByZXR1cm4gZmV0Y2godGhpcy5lbmRwb2ludCwge1xuLy8gICAgICAgbWV0aG9kOiAnUE9TVCcsXG4vLyAgICAgICBoZWFkZXJzOiB7ICdjb250ZW50LXR5cGUnOiAnYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkJyB9LFxuLy8gICAgICAgYm9keTogYm9keVxuLy8gICAgIH0pLnRoZW4ocmVzcG9uc2UgPT4ge1xuLy8gICAgICAgaWYgKHJlc3BvbnNlLnN0YXR1cyA9PT0gMjAwIHx8IHJlc3BvbnNlLnN0YXR1cyA9PT0gMjAxKSB7XG4vLyAgICAgICAgIHJldHVybiByZXNwb25zZS5qc29uKCkudGhlbihkYXRhID0+IHtcbi8vICAgICAgICAgICByZXR1cm4gZGF0YVxuLy8gICAgICAgICB9KVxuLy8gICAgICAgfVxuLy8gICAgIH0pXG4vLyAgIH1cbi8vIC0tLSBXT1JLSU5HIC0tLVxuLy8gaW1wb3J0ICogYXMgbW9uYWNvIGZyb20gJ21vbmFjby1lZGl0b3InXG4vLyBpbXBvcnQgeyBpbml0VmltTW9kZSB9IGZyb20gJ21vbmFjby12aW0nXG4vLyBpbXBvcnQgKiBhcyBzb2xhcml6ZWREYXJrIGZyb20gJy4vdGhlbWVzL3NvbGFyaXplZC1kYXJrJ1xuLy8gLy8gaW1wb3J0IHsgc3Vic2NyaWJlRFQgfSBmcm9tICcuL2R0L2NsaWVudCdcbi8vXG4vLyBleHBvcnQgY29uc3QgZGlhbW9uZE1vbmFjbyA9ICh1cmwsIGVkaXRvckVsLCBzdGF0dXNFbCwgY29ubmVjdGlvbkVsLCB2ZXJzaW9uRWwsIG9wdGlvbnMsIHVzZXJJRCwgdmltKSA9PiB7XG4vLyAgIG1vbmFjby5lZGl0b3IuZGVmaW5lVGhlbWUoJ3NvbGFyaXplZC1kYXJrJywge1xuLy8gICAgIGJhc2U6IHNvbGFyaXplZERhcmsuYmFzZSxcbi8vICAgICBjb2xvcnM6IHNvbGFyaXplZERhcmsuY29sb3JzLFxuLy8gICAgIGluaGVyaXQ6IHNvbGFyaXplZERhcmsuaW5oZXJpdCxcbi8vICAgICBydWxlczogc29sYXJpemVkRGFyay5ydWxlc1xuLy8gICB9KVxuLy8gICBvcHRpb25zLnRoZW1lID0gJ3NvbGFyaXplZC1kYXJrJ1xuLy8gICBvcHRpb25zLmF1dG9tYXRpY0xheW91dCA9IHRydWVcbi8vICAgY29uc3QgZWRpdG9yID0gbW9uYWNvLmVkaXRvci5jcmVhdGUoZWRpdG9yRWwsIG9wdGlvbnMpXG4vLyAgIGlmICh2aW0gPT09IHRydWUpIHtcbi8vICAgICBpbml0VmltTW9kZShlZGl0b3IsIHN0YXR1c0VsKVxuLy8gICB9XG4vLyAgIGVkaXRvci5hZGRDb21tYW5kKG1vbmFjby5LZXlNb2QuQ3RybENtZCB8IG1vbmFjby5LZXlDb2RlLktleVMsICgpID0+IHtcbi8vICAgICBhbGVydCgnc2F2ZWQnKVxuLy8gICB9KVxuLy8gICBlZGl0b3IuYWRkQ29tbWFuZChtb25hY28uS2V5TW9kLkN0cmxDbWQgfCBtb25hY28uS2V5Q29kZS5FbnRlciwgKCkgPT4ge1xuLy8gICAgIGFsZXJ0KCdwdWJsaXNoJylcbi8vICAgfSlcbi8vICAgZWRpdG9yLmFkZENvbW1hbmQobW9uYWNvLktleU1vZC5DdHJsQ21kIHwgbW9uYWNvLktleU1vZC5TaGlmdCB8IG1vbmFjby5LZXlDb2RlLkVudGVyLCAoKSA9PiB7XG4vLyAgICAgYWxlcnQoJ3B1Ymxpc2ggYW5kIGdvIGxpdmUnKVxuLy8gICB9KVxuLy8gICAvLyBzdWJzY3JpYmVEVCh1cmwgKyAnLmR0JywgZWRpdG9yLCB1c2VySUQsIHtcbi8vICAgLy8gICBzZXRTdGF0dXM6IG0gPT4ge1xuLy8gICAvLyAgICAgY29ubmVjdGlvbkVsLmlubmVySFRNTCA9IG1cbi8vICAgLy8gICB9LFxuLy8gICAvLyAgIHNldEluZm86IG0gPT4ge1xuLy8gICAvLyAgICAgdmVyc2lvbkVsLmlubmVySFRNTCA9IG1cbi8vICAgLy8gICB9XG4vLyAgIC8vIH0pXG4vLyAgIHJldHVybiBlZGl0b3Jcbi8vIH1cbi8vXG4vLyAtLS0gL1dPUktJTkcgLS0tXG4vKipcbiAqIEphdmFTY3JpcHQgQ2xpZW50IERldGVjdGlvblxuICogKEMpIHZpYXplbmV0dGkgR21iSCAoQ2hyaXN0aWFuIEx1ZHdpZylcbiAqL1xuZXhwb3J0IGNvbnN0IGdldEJyb3dzZXIgPSAoKSA9PiB7XG4gICAgY29uc3QgdW5rbm93biA9ICctJztcbiAgICAvLyBzY3JlZW5cbiAgICBsZXQgc2NyZWVuU2l6ZSA9ICcnO1xuICAgIGlmIChzY3JlZW4ud2lkdGgpIHtcbiAgICAgICAgY29uc3Qgd2lkdGggPSAoc2NyZWVuLndpZHRoKSA/IHNjcmVlbi53aWR0aCA6ICcnO1xuICAgICAgICBjb25zdCBoZWlnaHQgPSAoc2NyZWVuLmhlaWdodCkgPyBzY3JlZW4uaGVpZ2h0IDogJyc7XG4gICAgICAgIHNjcmVlblNpemUgKz0gJycgKyB3aWR0aCArICcgeCAnICsgaGVpZ2h0O1xuICAgIH1cbiAgICAvLyBicm93c2VyXG4gICAgY29uc3QgblZlciA9IG5hdmlnYXRvci5hcHBWZXJzaW9uO1xuICAgIGNvbnN0IG5BZ3QgPSBuYXZpZ2F0b3IudXNlckFnZW50O1xuICAgIGxldCBicm93c2VyID0gbmF2aWdhdG9yLmFwcE5hbWU7XG4gICAgbGV0IHZlcnNpb24gPSAnJyArIHBhcnNlRmxvYXQobmF2aWdhdG9yLmFwcFZlcnNpb24pO1xuICAgIGxldCBtYWpvclZlcnNpb24gPSBwYXJzZUludChuYXZpZ2F0b3IuYXBwVmVyc2lvbiwgMTApO1xuICAgIGxldCBuYW1lT2Zmc2V0LCB2ZXJPZmZzZXQsIGl4O1xuICAgIC8vIE9wZXJhXG4gICAgaWYgKCh2ZXJPZmZzZXQgPSBuQWd0LmluZGV4T2YoJ09wZXJhJykpICE9PSAtMSkge1xuICAgICAgICBicm93c2VyID0gJ09wZXJhJztcbiAgICAgICAgdmVyc2lvbiA9IG5BZ3Quc3Vic3RyaW5nKHZlck9mZnNldCArIDYpO1xuICAgICAgICBpZiAoKHZlck9mZnNldCA9IG5BZ3QuaW5kZXhPZignVmVyc2lvbicpKSAhPT0gLTEpIHtcbiAgICAgICAgICAgIHZlcnNpb24gPSBuQWd0LnN1YnN0cmluZyh2ZXJPZmZzZXQgKyA4KTtcbiAgICAgICAgfVxuICAgIH1cbiAgICAvLyBPcGVyYSBOZXh0XG4gICAgaWYgKCh2ZXJPZmZzZXQgPSBuQWd0LmluZGV4T2YoJ09QUicpKSAhPT0gLTEpIHtcbiAgICAgICAgYnJvd3NlciA9ICdPcGVyYSc7XG4gICAgICAgIHZlcnNpb24gPSBuQWd0LnN1YnN0cmluZyh2ZXJPZmZzZXQgKyA0KTtcbiAgICB9XG4gICAgZWxzZSBpZiAoKHZlck9mZnNldCA9IG5BZ3QuaW5kZXhPZignRWRnZScpKSAhPT0gLTEpIHsgLy8gTGVnYWN5IEVkZ2VcbiAgICAgICAgYnJvd3NlciA9ICdNaWNyb3NvZnQgTGVnYWN5IEVkZ2UnO1xuICAgICAgICB2ZXJzaW9uID0gbkFndC5zdWJzdHJpbmcodmVyT2Zmc2V0ICsgNSk7XG4gICAgfVxuICAgIGVsc2UgaWYgKCh2ZXJPZmZzZXQgPSBuQWd0LmluZGV4T2YoJ0VkZycpKSAhPT0gLTEpIHsgLy8gRWRnZSAoQ2hyb21pdW0pXG4gICAgICAgIGJyb3dzZXIgPSAnTWljcm9zb2Z0IEVkZ2UnO1xuICAgICAgICB2ZXJzaW9uID0gbkFndC5zdWJzdHJpbmcodmVyT2Zmc2V0ICsgNCk7XG4gICAgfVxuICAgIGVsc2UgaWYgKCh2ZXJPZmZzZXQgPSBuQWd0LmluZGV4T2YoJ01TSUUnKSkgIT09IC0xKSB7IC8vIE1TSUVcbiAgICAgICAgYnJvd3NlciA9ICdNaWNyb3NvZnQgSW50ZXJuZXQgRXhwbG9yZXInO1xuICAgICAgICB2ZXJzaW9uID0gbkFndC5zdWJzdHJpbmcodmVyT2Zmc2V0ICsgNSk7XG4gICAgfVxuICAgIGVsc2UgaWYgKCh2ZXJPZmZzZXQgPSBuQWd0LmluZGV4T2YoJ0Nocm9tZScpKSAhPT0gLTEpIHsgLy8gQ2hyb21lXG4gICAgICAgIGJyb3dzZXIgPSAnQ2hyb21lJztcbiAgICAgICAgdmVyc2lvbiA9IG5BZ3Quc3Vic3RyaW5nKHZlck9mZnNldCArIDcpO1xuICAgIH1cbiAgICBlbHNlIGlmICgodmVyT2Zmc2V0ID0gbkFndC5pbmRleE9mKCdTYWZhcmknKSkgIT09IC0xKSB7IC8vIFNhZmFyaVxuICAgICAgICBicm93c2VyID0gJ1NhZmFyaSc7XG4gICAgICAgIHZlcnNpb24gPSBuQWd0LnN1YnN0cmluZyh2ZXJPZmZzZXQgKyA3KTtcbiAgICAgICAgaWYgKCh2ZXJPZmZzZXQgPSBuQWd0LmluZGV4T2YoJ1ZlcnNpb24nKSkgIT09IC0xKSB7XG4gICAgICAgICAgICB2ZXJzaW9uID0gbkFndC5zdWJzdHJpbmcodmVyT2Zmc2V0ICsgOCk7XG4gICAgICAgIH1cbiAgICB9XG4gICAgZWxzZSBpZiAoKHZlck9mZnNldCA9IG5BZ3QuaW5kZXhPZignRmlyZWZveCcpKSAhPT0gLTEpIHsgLy8gRmlyZWZveFxuICAgICAgICBicm93c2VyID0gJ0ZpcmVmb3gnO1xuICAgICAgICB2ZXJzaW9uID0gbkFndC5zdWJzdHJpbmcodmVyT2Zmc2V0ICsgOCk7XG4gICAgfVxuICAgIGVsc2UgaWYgKG5BZ3QuaW5kZXhPZignVHJpZGVudC8nKSAhPT0gLTEpIHsgLy8gTVNJRSAxMStcbiAgICAgICAgYnJvd3NlciA9ICdNaWNyb3NvZnQgSW50ZXJuZXQgRXhwbG9yZXInO1xuICAgICAgICB2ZXJzaW9uID0gbkFndC5zdWJzdHJpbmcobkFndC5pbmRleE9mKCdydjonKSArIDMpO1xuICAgIH1cbiAgICBlbHNlIGlmICgobmFtZU9mZnNldCA9IG5BZ3QubGFzdEluZGV4T2YoJyAnKSArIDEpIDxcbiAgICAgICAgKHZlck9mZnNldCA9IG5BZ3QubGFzdEluZGV4T2YoJy8nKSkpIHsgLy8gT3RoZXIgYnJvd3NlcnNcbiAgICAgICAgYnJvd3NlciA9IG5BZ3Quc3Vic3RyaW5nKG5hbWVPZmZzZXQsIHZlck9mZnNldCk7XG4gICAgICAgIHZlcnNpb24gPSBuQWd0LnN1YnN0cmluZyh2ZXJPZmZzZXQgKyAxKTtcbiAgICAgICAgaWYgKGJyb3dzZXIudG9Mb3dlckNhc2UoKSA9PT0gYnJvd3Nlci50b1VwcGVyQ2FzZSgpKSB7XG4gICAgICAgICAgICBicm93c2VyID0gbmF2aWdhdG9yLmFwcE5hbWU7XG4gICAgICAgIH1cbiAgICB9XG4gICAgLy8gdHJpbSB0aGUgdmVyc2lvbiBzdHJpbmdcbiAgICBpZiAoKGl4ID0gdmVyc2lvbi5pbmRleE9mKCc7JykpICE9PSAtMSlcbiAgICAgICAgdmVyc2lvbiA9IHZlcnNpb24uc3Vic3RyaW5nKDAsIGl4KTtcbiAgICBpZiAoKGl4ID0gdmVyc2lvbi5pbmRleE9mKCcgJykpICE9PSAtMSlcbiAgICAgICAgdmVyc2lvbiA9IHZlcnNpb24uc3Vic3RyaW5nKDAsIGl4KTtcbiAgICBpZiAoKGl4ID0gdmVyc2lvbi5pbmRleE9mKCcpJykpICE9PSAtMSlcbiAgICAgICAgdmVyc2lvbiA9IHZlcnNpb24uc3Vic3RyaW5nKDAsIGl4KTtcbiAgICBtYWpvclZlcnNpb24gPSBwYXJzZUludCgnJyArIHZlcnNpb24sIDEwKTtcbiAgICBpZiAoaXNOYU4obWFqb3JWZXJzaW9uKSkge1xuICAgICAgICB2ZXJzaW9uID0gJycgKyBwYXJzZUZsb2F0KG5hdmlnYXRvci5hcHBWZXJzaW9uKTtcbiAgICAgICAgbWFqb3JWZXJzaW9uID0gcGFyc2VJbnQobmF2aWdhdG9yLmFwcFZlcnNpb24sIDEwKTtcbiAgICB9XG4gICAgLy8gbW9iaWxlIHZlcnNpb25cbiAgICBjb25zdCBtb2JpbGUgPSAvTW9iaWxlfG1pbml8RmVubmVjfEFuZHJvaWR8aVAoYWR8b2R8aG9uZSkvLnRlc3QoblZlcik7XG4gICAgLy8gY29va2llXG4gICAgbGV0IGNvb2tpZUVuYWJsZWQgPSAhIShuYXZpZ2F0b3IuY29va2llRW5hYmxlZCk7XG4gICAgaWYgKHR5cGVvZiBuYXZpZ2F0b3IuY29va2llRW5hYmxlZCA9PT0gJ3VuZGVmaW5lZCcgJiYgIWNvb2tpZUVuYWJsZWQpIHtcbiAgICAgICAgZG9jdW1lbnQuY29va2llID0gJ3Rlc3Rjb29raWUnO1xuICAgICAgICBjb29raWVFbmFibGVkID0gKGRvY3VtZW50LmNvb2tpZS5pbmRleE9mKCd0ZXN0Y29va2llJykgIT09IC0xKTtcbiAgICB9XG4gICAgLy8gdGVzdFxuICAgIC8vIHN5c3RlbVxuICAgIGxldCBvcyA9IHVua25vd247XG4gICAgY29uc3QgY2xpZW50U3RyaW5ncyA9IFtcbiAgICAgICAgeyBzOiAnV2luZG93cyAxMCcsIHI6IC8oV2luZG93cyAxMC4wfFdpbmRvd3MgTlQgMTAuMCkvIH0sXG4gICAgICAgIHsgczogJ1dpbmRvd3MgOC4xJywgcjogLyhXaW5kb3dzIDguMXxXaW5kb3dzIE5UIDYuMykvIH0sXG4gICAgICAgIHsgczogJ1dpbmRvd3MgOCcsIHI6IC8oV2luZG93cyA4fFdpbmRvd3MgTlQgNi4yKS8gfSxcbiAgICAgICAgeyBzOiAnV2luZG93cyA3JywgcjogLyhXaW5kb3dzIDd8V2luZG93cyBOVCA2LjEpLyB9LFxuICAgICAgICB7IHM6ICdXaW5kb3dzIFZpc3RhJywgcjogL1dpbmRvd3MgTlQgNi4wLyB9LFxuICAgICAgICB7IHM6ICdXaW5kb3dzIFNlcnZlciAyMDAzJywgcjogL1dpbmRvd3MgTlQgNS4yLyB9LFxuICAgICAgICB7IHM6ICdXaW5kb3dzIFhQJywgcjogLyhXaW5kb3dzIE5UIDUuMXxXaW5kb3dzIFhQKS8gfSxcbiAgICAgICAgeyBzOiAnV2luZG93cyAyMDAwJywgcjogLyhXaW5kb3dzIE5UIDUuMHxXaW5kb3dzIDIwMDApLyB9LFxuICAgICAgICB7IHM6ICdXaW5kb3dzIE1FJywgcjogLyhXaW4gOXggNC45MHxXaW5kb3dzIE1FKS8gfSxcbiAgICAgICAgeyBzOiAnV2luZG93cyA5OCcsIHI6IC8oV2luZG93cyA5OHxXaW45OCkvIH0sXG4gICAgICAgIHsgczogJ1dpbmRvd3MgOTUnLCByOiAvKFdpbmRvd3MgOTV8V2luOTV8V2luZG93c185NSkvIH0sXG4gICAgICAgIHsgczogJ1dpbmRvd3MgTlQgNC4wJywgcjogLyhXaW5kb3dzIE5UIDQuMHxXaW5OVDQuMHxXaW5OVHxXaW5kb3dzIE5UKS8gfSxcbiAgICAgICAgeyBzOiAnV2luZG93cyBDRScsIHI6IC9XaW5kb3dzIENFLyB9LFxuICAgICAgICB7IHM6ICdXaW5kb3dzIDMuMTEnLCByOiAvV2luMTYvIH0sXG4gICAgICAgIHsgczogJ0FuZHJvaWQnLCByOiAvQW5kcm9pZC8gfSxcbiAgICAgICAgeyBzOiAnT3BlbiBCU0QnLCByOiAvT3BlbkJTRC8gfSxcbiAgICAgICAgeyBzOiAnU3VuIE9TJywgcjogL1N1bk9TLyB9LFxuICAgICAgICB7IHM6ICdDaHJvbWUgT1MnLCByOiAvQ3JPUy8gfSxcbiAgICAgICAgeyBzOiAnTGludXgnLCByOiAvKExpbnV4fFgxMSg/IS4qQ3JPUykpLyB9LFxuICAgICAgICB7IHM6ICdpT1MnLCByOiAvKGlQaG9uZXxpUGFkfGlQb2QpLyB9LFxuICAgICAgICB7IHM6ICdNYWMgT1MgWCcsIHI6IC9NYWMgT1MgWC8gfSxcbiAgICAgICAgeyBzOiAnTWFjIE9TJywgcjogLyhNYWMgT1N8TWFjUFBDfE1hY0ludGVsfE1hY19Qb3dlclBDfE1hY2ludG9zaCkvIH0sXG4gICAgICAgIHsgczogJ1FOWCcsIHI6IC9RTlgvIH0sXG4gICAgICAgIHsgczogJ1VOSVgnLCByOiAvVU5JWC8gfSxcbiAgICAgICAgeyBzOiAnQmVPUycsIHI6IC9CZU9TLyB9LFxuICAgICAgICB7IHM6ICdPUy8yJywgcjogL09TXFwvMi8gfSxcbiAgICAgICAgeyBzOiAnU2VhcmNoIEJvdCcsIHI6IC8obnVoa3xHb29nbGVib3R8WWFtbXlib3R8T3BlbmJvdHxTbHVycHxNU05Cb3R8QXNrIEplZXZlc1xcL1Rlb21hfGlhX2FyY2hpdmVyKS8gfVxuICAgIF07XG4gICAgZm9yIChjb25zdCBpZCBpbiBjbGllbnRTdHJpbmdzKSB7XG4gICAgICAgIGNvbnN0IGNzID0gY2xpZW50U3RyaW5nc1tpZF07XG4gICAgICAgIGlmIChjcy5yLnRlc3QobkFndCkpIHtcbiAgICAgICAgICAgIG9zID0gY3MucztcbiAgICAgICAgICAgIGJyZWFrO1xuICAgICAgICB9XG4gICAgfVxuICAgIGxldCBvc1ZlcnNpb24gPSB1bmtub3duO1xuICAgIGlmICgvV2luZG93cy8udGVzdChvcykpIHtcbiAgICAgICAgb3NWZXJzaW9uID0gL1dpbmRvd3MgKC4qKS8uZXhlYyhvcylbMV07XG4gICAgICAgIG9zID0gJ1dpbmRvd3MnO1xuICAgIH1cbiAgICBzd2l0Y2ggKG9zKSB7XG4gICAgICAgIGNhc2UgJ01hYyBPUyc6XG4gICAgICAgIGNhc2UgJ01hYyBPUyBYJzpcbiAgICAgICAgY2FzZSAnQW5kcm9pZCc6XG4gICAgICAgICAgICBvc1ZlcnNpb24gPSAvKD86QW5kcm9pZHxNYWMgT1N8TWFjIE9TIFh8TWFjUFBDfE1hY0ludGVsfE1hY19Qb3dlclBDfE1hY2ludG9zaCkgKFsuX2RdKykvLmV4ZWMobkFndClbMV07XG4gICAgICAgICAgICBicmVhaztcbiAgICAgICAgLy8gVE9ETyBjYXNlICdpT1MnOlxuICAgICAgICAvLyBUT0RPICAgb3NWZXJzaW9uID0gL09TIChcXGQrKV8oXFxkKylfPyhcXGQrKT8vLmV4ZWMoblZlcilcbiAgICAgICAgLy8gVE9ETyAgIG9zVmVyc2lvbiA9IG9zVmVyc2lvblsxXSArICcuJyArIG9zVmVyc2lvblsyXSArICcuJyArIChvc1ZlcnNpb25bM10gfCAwKVxuICAgICAgICAvLyBUT0RPICAgYnJlYWtcbiAgICB9XG4gICAgLy8gZmxhc2ggKHlvdSdsbCBuZWVkIHRvIGluY2x1ZGUgc3dmb2JqZWN0KVxuICAgIC8qIHNjcmlwdCBzcmM9XCIvL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL3N3Zm9iamVjdC8yLjIvc3dmb2JqZWN0LmpzXCIgKi9cbiAgICAvLyBUT0RPIHZhciBmbGFzaFZlcnNpb24gPSAnbm8gY2hlY2snXG4gICAgLy8gVE9ETyBpZiAodHlwZW9mIHN3Zm9iamVjdCAhPT0gJ3VuZGVmaW5lZCcpIHtcbiAgICAvLyBUT0RPICAgY29uc3QgZnYgPSBzd2ZvYmplY3QuZ2V0Rmxhc2hQbGF5ZXJWZXJzaW9uKClcbiAgICAvLyBUT0RPICAgaWYgKGZ2Lm1ham9yID4gMCkge1xuICAgIC8vIFRPRE8gICAgIGZsYXNoVmVyc2lvbiA9IGZ2Lm1ham9yICsgJy4nICsgZnYubWlub3IgKyAnIHInICsgZnYucmVsZWFzZVxuICAgIC8vIFRPRE8gICB9IGVsc2Uge1xuICAgIC8vIFRPRE8gICAgIGZsYXNoVmVyc2lvbiA9IHVua25vd25cbiAgICAvLyBUT0RPICAgfVxuICAgIC8vIFRPRE8gfVxuICAgIHJldHVybiB7XG4gICAgICAgIHNjcmVlbjogc2NyZWVuU2l6ZSxcbiAgICAgICAgYnJvd3NlcjogYnJvd3NlcixcbiAgICAgICAgYnJvd3NlclZlcnNpb246IHZlcnNpb24sXG4gICAgICAgIGJyb3dzZXJNYWpvclZlcnNpb246IG1ham9yVmVyc2lvbixcbiAgICAgICAgbW9iaWxlOiBtb2JpbGUsXG4gICAgICAgIG9zOiBvcyxcbiAgICAgICAgb3NWZXJzaW9uOiBvc1ZlcnNpb24sXG4gICAgICAgIGNvb2tpZXM6IGNvb2tpZUVuYWJsZWRcbiAgICAgICAgLy8gVE9ETyBmbGFzaFZlcnNpb246IGZsYXNoVmVyc2lvblxuICAgIH07XG59O1xuLy8gVE9ETyBhbGVydChcbi8vIFRPRE8gICAnT1M6ICcgKyBqc2NkLm9zICsgJyAnICsganNjZC5vc1ZlcnNpb24gKyAnXFxuJyArXG4vLyBUT0RPICAgICAnQnJvd3NlcjogJyArIGpzY2QuYnJvd3NlciArICcgJyArIGpzY2QuYnJvd3Nlck1ham9yVmVyc2lvbiArXG4vLyBUT0RPICAgICAgICcgKCcgKyBqc2NkLmJyb3dzZXJWZXJzaW9uICsgJylcXG4nICtcbi8vIFRPRE8gICAgICdNb2JpbGU6ICcgKyBqc2NkLm1vYmlsZSArICdcXG4nICtcbi8vIFRPRE8gICAgICdGbGFzaDogJyArIGpzY2QuZmxhc2hWZXJzaW9uICsgJ1xcbicgK1xuLy8gVE9ETyAgICAgJ0Nvb2tpZXM6ICcgKyBqc2NkLmNvb2tpZXMgKyAnXFxuJyArXG4vLyBUT0RPICAgICAnU2NyZWVuIFNpemU6ICcgKyBqc2NkLnNjcmVlbiArICdcXG5cXG4nICtcbi8vIFRPRE8gICAgICdGdWxsIFVzZXIgQWdlbnQ6ICcgKyBuYXZpZ2F0b3IudXNlckFnZW50XG4vLyBUT0RPIClcbmNvbnN0IENvb2tpZXMgPSByZXF1aXJlKCdqcy1jb29raWUnKTtcbi8vIFRPRE8gY29uc3QgeyBEYXRlVGltZSB9ID0gcmVxdWlyZSgnbHV4b24nKVxuLy8gY29uc3QgeyBuYjYwZW5jb2RlLCBuYjYwZGVjb2RlIH0gPSByZXF1aXJlKCdOZXdNYXRoJylcbmV4cG9ydCBjb25zdCBjb29raWVzID0gQ29va2llcztcbi8vIFRPRE8gZXhwb3J0IGNvbnN0IGR0ID0gRGF0ZVRpbWVcbi8vIF8ubmI2MGVuY29kZSA9IG5iNjBlbmNvZGVcbi8vIF8ubmI2MGRlY29kZSA9IG5iNjBkZWNvZGVcbi8vIGV4cG9ydCBjb25zdCBfID0gKHNlbGVjdG9yKSA9PiB7XG4vLyAgIGNvbnN0IHJlc3VsdHMgPSB0eXBlb2Ygc2VsZWN0b3IgPT09ICdzdHJpbmcnXG4vLyAgICAgPyBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKHNlbGVjdG9yKVxuLy8gICAgIDogW3NlbGVjdG9yXVxuLy8gICAvLyBjb25zdCByZXN1bHRzID0gQXJyYXkucHJvdG90eXBlLnNsaWNlLmNhbGwobm9kZXMpXG4vLyAgIGNvbnN0IGl0ZW1zID0ge31cbi8vICAgZm9yIChsZXQgaSA9IDA7IGkgPCByZXN1bHRzLmxlbmd0aDsgaSsrKSB7XG4vLyAgICAgaXRlbXNbaV0gPSByZXN1bHRzW2ldXG4vLyAgIH1cbi8vICAgaXRlbXMuXyA9IF9cbi8vICAgaXRlbXMuZWwgPSBpdGVtc1swXVxuLy8gICBpdGVtcy5uID0gcmVzdWx0cy5sZW5ndGhcbi8vICAgLy8gaXRlbXMuc3BsaWNlID0gW10uc3BsaWNlKCkgLy8gc2ltdWxhdGVzIGFuIGFycmF5IEZJWE1FXG4vLyAgIC8vIGl0ZW1zLmVhY2ggPSBjYWxsYmFjayA9PiB7IG5vZGVzLmZvckVhY2goY2FsbGJhY2ssICkgfVxuLy8gICBpdGVtcy5lYWNoID0gY2FsbGJhY2sgPT4ge1xuLy8gICAgIGZvciAobGV0IGkgPSAwOyBpIDwgcmVzdWx0cy5sZW5ndGg7IGkrKykge1xuLy8gICAgICAgY2FsbGJhY2socmVzdWx0c1tpXSlcbi8vICAgICB9XG4vLyAgIH1cbi8vICAgLy8gZm9yIChsZXQgaSA9IDA7IGkgPCByZXN1bHRzLmxlbmd0aDsgaSsrKSB7XG4vLyAgIC8vICAgY29uc29sZS5sb2cocmVzdWx0c1tpXSlcbi8vICAgLy8gICByZXN1bHRzW2ldLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgKCkgPT4geyBjb25zb2xlLmxvZygnZXInKSB9KVxuLy8gICAvLyB9XG4vLyAgIC8vIGl0ZW1zLmNsaWNrID0gY2FsbGJhY2sgPT4ge1xuLy8gICAvLyAgIGZvciAobGV0IGkgPSAwOyBpIDwgcmVzdWx0cy5sZW5ndGg7IGkrKykge1xuLy8gICAvLyAgICAgY29uc29sZS5sb2codGhpcy5yZXN1bHRzW2ldLCB0aGlzKVxuLy8gICAvLyAgICAgdGhpcy5yZXN1bHRzW2ldLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgKCkgPT4geyBjb25zb2xlLmxvZygnZXInKSB9KVxuLy8gICAvLyAgICAgLy8gY2FsbGJhY2suYmluZChub2Rlc1tpXSlcbi8vICAgLy8gICAgIC8vIGNhbGxiYWNrKG5vZGVzW2ldKVxuLy8gICAvLyAgIH1cbi8vICAgLy8gfVxuLy8gICBpdGVtcy5hcHBlbmQgPSBodG1sID0+IHtcbi8vICAgICBpdGVtcy5lYWNoKGl0ZW0gPT4gaXRlbS5hcHBlbmRDaGlsZChjcmVhdGVFbChodG1sKSkpXG4vLyAgIH1cbi8vICAgaXRlbXMubW92ZSA9IChsZWZ0LCB0b3ApID0+IHtcbi8vICAgICBpdGVtcy5lbC5zdHlsZS5sZWZ0ID0gbGVmdFxuLy8gICAgIGl0ZW1zLmVsLnN0eWxlLnRvcCA9IHRvcFxuLy8gICB9XG4vLyAgIGl0ZW1zLmNsaWNrID0gY2FsbGJhY2sgPT4ge1xuLy8gICAgIGl0ZW1zLmVhY2goaXRlbSA9PiB7XG4vLyAgICAgICBpdGVtLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgY2FsbGJhY2spXG4vLyAgICAgfSlcbi8vICAgfVxuLy8gICByZXR1cm4gaXRlbXNcbi8vIH1cbmV4cG9ydCBjb25zdCBjcmVhdGVFbCA9IGh0bWwgPT4ge1xuICAgIGNvbnN0IHRlbXBsYXRlID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgndGVtcGxhdGUnKTtcbiAgICB0ZW1wbGF0ZS5pbm5lckhUTUwgPSBodG1sLnRyaW0oKTtcbiAgICByZXR1cm4gdGVtcGxhdGUuY29udGVudC5maXJzdENoaWxkO1xufTtcbmV4cG9ydCBjb25zdCBjcmVhdGVFbHMgPSBodG1sID0+IHtcbiAgICBjb25zdCB0ZW1wbGF0ZSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3RlbXBsYXRlJyk7XG4gICAgdGVtcGxhdGUuaW5uZXJIVE1MID0gaHRtbDtcbiAgICByZXR1cm4gdGVtcGxhdGUuY29udGVudC5jaGlsZE5vZGVzO1xufTtcbmNvbnN0IGxvYWRTY3JpcHRzID0gW107XG5jb25zdCB1bmxvYWRTY3JpcHRzID0gW107XG5jb25zdCBleGVjdXRlTG9hZFNjcmlwdHMgPSAoKSA9PiB7XG4gICAgbG9hZFNjcmlwdHMuZm9yRWFjaChoYW5kbGVyID0+IGhhbmRsZXIoKSk7XG4gICAgbG9hZFNjcmlwdHMubGVuZ3RoID0gMDtcbn07XG5jb25zdCBleGVjdXRlVW5sb2FkU2NyaXB0cyA9ICgpID0+IHtcbiAgICB1bmxvYWRTY3JpcHRzLmZvckVhY2goaGFuZGxlciA9PiBoYW5kbGVyKCkpO1xuICAgIHVubG9hZFNjcmlwdHMubGVuZ3RoID0gMDtcbn07XG5kb2N1bWVudC5hZGRFdmVudExpc3RlbmVyKCdET01Db250ZW50TG9hZGVkJywgKCkgPT4gZXhlY3V0ZUxvYWRTY3JpcHRzKCkpO1xud2luZG93LmFkZEV2ZW50TGlzdGVuZXIoJ2JlZm9yZXVubG9hZCcsICgpID0+IHtcbiAgICBleGVjdXRlVW5sb2FkU2NyaXB0cygpO1xufSk7XG5leHBvcnQgY29uc3QgbG9hZCA9IGhhbmRsZXIgPT4gbG9hZFNjcmlwdHMucHVzaChoYW5kbGVyKTtcbmV4cG9ydCBjb25zdCB1bmxvYWQgPSBoYW5kbGVyID0+IHVubG9hZFNjcmlwdHMucHVzaChoYW5kbGVyKTtcbmV4cG9ydCBjb25zdCBtb3VzZXVwID0gaGFuZGxlciA9PiBkb2N1bWVudC5hZGRFdmVudExpc3RlbmVyKCdtb3VzZXVwJywgaGFuZGxlcik7XG5leHBvcnQgY29uc3QgcG9wc3RhdGUgPSBoYW5kbGVyID0+IHdpbmRvdy5hZGRFdmVudExpc3RlbmVyKCdwb3BzdGF0ZScsIGhhbmRsZXIpO1xuZXhwb3J0IGNvbnN0IG9ubGluZSA9IGhhbmRsZXIgPT4gd2luZG93LmFkZEV2ZW50TGlzdGVuZXIoJ29ubGluZScsIGhhbmRsZXIpO1xuZXhwb3J0IGNvbnN0IG9mZmxpbmUgPSBoYW5kbGVyID0+IHdpbmRvdy5hZGRFdmVudExpc3RlbmVyKCdvZmZsaW5lJywgaGFuZGxlcik7XG5leHBvcnQgY29uc3QgZXJyb3IgPSBoYW5kbGVyID0+IHdpbmRvdy5hZGRFdmVudExpc3RlbmVyKCdlcnJvcicsIGhhbmRsZXIpO1xuZXhwb3J0IGNvbnN0IHVwZ3JhZGVUaW1lc3RhbXBzID0gKCkgPT4ge1xuICAgIC8vIFRPRE8gY29uc3QgcGFnZUxvYWQgPSBEYXRlVGltZS5ub3coKVxuICAgIC8vIFRPRE8gXygndGltZScpLmVhY2goaXRlbSA9PiB7XG4gICAgLy8gVE9ETyAgIGl0ZW0uc2V0QXR0cmlidXRlKCd0aXRsZScsIGl0ZW0uaW5uZXJIVE1MKVxuICAgIC8vIFRPRE8gICBpdGVtLmlubmVySFRNTCA9IERhdGVUaW1lLmZyb21JU08oaXRlbS5hdHRyaWJ1dGVzLmRhdGV0aW1lLnZhbHVlKVxuICAgIC8vIFRPRE8gICAgIC50b1JlbGF0aXZlKHsgYmFzZTogcGFnZUxvYWQgfSlcbiAgICAvLyBUT0RPIH0pXG59O1xuZXhwb3J0IGNsYXNzIE1pY3JvcHViQ2xpZW50IHtcbiAgICBlbmRwb2ludDtcbiAgICB0b2tlbjtcbiAgICBoZWFkZXJzO1xuICAgIGNvbmZpZztcbiAgICBjb25zdHJ1Y3RvcihlbmRwb2ludCwgdG9rZW4pIHtcbiAgICAgICAgdGhpcy5lbmRwb2ludCA9IGVuZHBvaW50O1xuICAgICAgICB0aGlzLnRva2VuID0gdG9rZW47XG4gICAgICAgIHRoaXMuaGVhZGVycyA9IHtcbiAgICAgICAgICAgIGFjY2VwdDogJ2FwcGxpY2F0aW9uL2pzb24nXG4gICAgICAgIH07XG4gICAgICAgIGlmICh0eXBlb2YgdG9rZW4gIT09ICd1bmRlZmluZWQnKSB7XG4gICAgICAgICAgICB0aGlzLmhlYWRlcnMuYXV0aG9yaXphdGlvbiA9IGBCZWFyZXIgJHt0b2tlbn1gO1xuICAgICAgICB9XG4gICAgICAgIHRoaXMuZ2V0Q29uZmlnID0gdGhpcy5nZXRDb25maWcuYmluZCh0aGlzKTtcbiAgICAgICAgdGhpcy5jcmVhdGUgPSB0aGlzLmNyZWF0ZS5iaW5kKHRoaXMpO1xuICAgICAgICB0aGlzLnJlYWQgPSB0aGlzLnJlYWQuYmluZCh0aGlzKTtcbiAgICAgICAgdGhpcy51cGRhdGUgPSB0aGlzLnVwZGF0ZS5iaW5kKHRoaXMpO1xuICAgICAgICB0aGlzLmRlbGV0ZSA9IHRoaXMuZGVsZXRlLmJpbmQodGhpcyk7XG4gICAgICAgIHRoaXMucXVlcnkgPSB0aGlzLnF1ZXJ5LmJpbmQodGhpcyk7XG4gICAgICAgIHRoaXMudXBsb2FkID0gdGhpcy51cGxvYWQuYmluZCh0aGlzKTtcbiAgICB9XG4gICAgZ2V0Q29uZmlnKCkge1xuICAgICAgICByZXR1cm4gZmV0Y2godGhpcy5lbmRwb2ludCArICc/cT1jb25maWcnLCB7XG4gICAgICAgICAgICBoZWFkZXJzOiB0aGlzLmhlYWRlcnNcbiAgICAgICAgfSkudGhlbihyZXNwb25zZSA9PiB7XG4gICAgICAgICAgICBpZiAocmVzcG9uc2Uuc3RhdHVzID09PSAyMDAgfHwgcmVzcG9uc2Uuc3RhdHVzID09PSAyMDEpIHtcbiAgICAgICAgICAgICAgICByZXR1cm4gcmVzcG9uc2UuanNvbigpLnRoZW4oZGF0YSA9PiB7XG4gICAgICAgICAgICAgICAgICAgIHJldHVybiBkYXRhO1xuICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgfVxuICAgICAgICB9KTtcbiAgICB9XG4gICAgZ2V0Q2F0ZWdvcmllcygpIHtcbiAgICAgICAgcmV0dXJuIGZldGNoKHRoaXMuZW5kcG9pbnQgKyAnP3E9Y2F0ZWdvcnknLCB7XG4gICAgICAgICAgICBoZWFkZXJzOiB0aGlzLmhlYWRlcnNcbiAgICAgICAgfSkudGhlbihyZXNwb25zZSA9PiB7XG4gICAgICAgICAgICBpZiAocmVzcG9uc2Uuc3RhdHVzID09PSAyMDAgfHwgcmVzcG9uc2Uuc3RhdHVzID09PSAyMDEpIHtcbiAgICAgICAgICAgICAgICByZXR1cm4gcmVzcG9uc2UuanNvbigpLnRoZW4oZGF0YSA9PiB7XG4gICAgICAgICAgICAgICAgICAgIHJldHVybiBkYXRhO1xuICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgfVxuICAgICAgICB9KTtcbiAgICB9XG4gICAgY3JlYXRlKHR5cGUsIHByb3BlcnRpZXMsIHZpc2liaWxpdHkpIHtcbiAgICAgICAgY29uc3QgaGVhZGVycyA9IHRoaXMuaGVhZGVycztcbiAgICAgICAgaGVhZGVyc1snY29udGVudC10eXBlJ10gPSAnYXBwbGljYXRpb24vanNvbic7XG4gICAgICAgIGlmICh0eXBlb2YgdmlzaWJpbGl0eSA9PT0gJ3VuZGVmaW5lZCcpIHtcbiAgICAgICAgICAgIHZpc2liaWxpdHkgPSAncHJpdmF0ZSc7XG4gICAgICAgIH1cbiAgICAgICAgLy8gVE9ETyBwcm9wZXJ0aWVzLnZpc2liaWxpdHkgPSB2aXNpYmlsaXR5XG4gICAgICAgIHJldHVybiBmZXRjaCh0aGlzLmVuZHBvaW50LCB7XG4gICAgICAgICAgICBtZXRob2Q6ICdQT1NUJyxcbiAgICAgICAgICAgIGhlYWRlcnM6IGhlYWRlcnMsXG4gICAgICAgICAgICBib2R5OiBKU09OLnN0cmluZ2lmeSh7XG4gICAgICAgICAgICAgICAgdHlwZTogW2BoLSR7dHlwZX1gXSxcbiAgICAgICAgICAgICAgICBwcm9wZXJ0aWVzOiBwcm9wZXJ0aWVzXG4gICAgICAgICAgICB9KVxuICAgICAgICB9KS50aGVuKHJlc3BvbnNlID0+IHtcbiAgICAgICAgICAgIGlmIChyZXNwb25zZS5zdGF0dXMgPT09IDIwMCB8fCByZXNwb25zZS5zdGF0dXMgPT09IDIwMSkge1xuICAgICAgICAgICAgICAgIHJldHVybiByZXNwb25zZS5oZWFkZXJzLmdldCgnbG9jYXRpb24nKTsgLy8gcGVybWFsaW5rXG4gICAgICAgICAgICB9XG4gICAgICAgIH0pO1xuICAgIH1cbiAgICByZWFkKHVybCkge1xuICAgICAgICBjb25zdCBoZWFkZXJzID0gdGhpcy5oZWFkZXJzO1xuICAgICAgICBoZWFkZXJzWydjb250ZW50LXR5cGUnXSA9ICdhcHBsaWNhdGlvbi9qc29uJztcbiAgICAgICAgcmV0dXJuIGZldGNoKHRoaXMuZW5kcG9pbnQsIHtcbiAgICAgICAgICAgIG1ldGhvZDogJ0dFVCcsXG4gICAgICAgICAgICBoZWFkZXJzOiBoZWFkZXJzXG4gICAgICAgIH0pLnRoZW4ocmVzcG9uc2UgPT4ge1xuICAgICAgICAgICAgaWYgKHJlc3BvbnNlLnN0YXR1cyA9PT0gMjAwIHx8IHJlc3BvbnNlLnN0YXR1cyA9PT0gMjAxKSB7XG4gICAgICAgICAgICAgICAgcmV0dXJuIHJlc3BvbnNlLmpzb24oKS50aGVuKGRhdGEgPT4ge1xuICAgICAgICAgICAgICAgICAgICByZXR1cm4gZGF0YTtcbiAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfSk7XG4gICAgfVxuICAgIHVwZGF0ZSh1cmwsIG9wZXJhdGlvbiwgcHJvcGVydGllcykge1xuICAgICAgICBjb25zdCBwYXlsb2FkID0geyBhY3Rpb246ICd1cGRhdGUnLCB1cmw6IHVybCB9O1xuICAgICAgICBwYXlsb2FkW29wZXJhdGlvbl0gPSBwcm9wZXJ0aWVzO1xuICAgICAgICAvLyBwYXlsb2FkW29wZXJhdGlvbl1bcHJvcGVydHldID0gdmFsdWVzXG4gICAgICAgIHJldHVybiBmZXRjaCh0aGlzLmVuZHBvaW50LCB7XG4gICAgICAgICAgICBtZXRob2Q6ICdQT1NUJyxcbiAgICAgICAgICAgIGhlYWRlcnM6IHtcbiAgICAgICAgICAgICAgICBhY2NlcHQ6ICdhcHBsaWNhdGlvbi9qc29uJyxcbiAgICAgICAgICAgICAgICBhdXRob3JpemF0aW9uOiBgQmVhcmVyICR7dGhpcy50b2tlbn1gLFxuICAgICAgICAgICAgICAgICdjb250ZW50LXR5cGUnOiAnYXBwbGljYXRpb24vanNvbidcbiAgICAgICAgICAgIH0sXG4gICAgICAgICAgICBib2R5OiBKU09OLnN0cmluZ2lmeShwYXlsb2FkKVxuICAgICAgICB9KS50aGVuKHJlc3BvbnNlID0+IHtcbiAgICAgICAgICAgIGlmIChyZXNwb25zZS5zdGF0dXMgPT09IDIwMCB8fCByZXNwb25zZS5zdGF0dXMgPT09IDIwMSkge1xuICAgICAgICAgICAgICAgIGNvbnNvbGUubG9nKCdVUERBVEVEIScpO1xuICAgICAgICAgICAgfVxuICAgICAgICB9KTtcbiAgICB9XG4gICAgZGVsZXRlKHVybCkge1xuICAgIH1cbiAgICBxdWVyeShxLCBhcmdzKSB7XG4gICAgICAgIHJldHVybiBmZXRjaCh0aGlzLmVuZHBvaW50ICsgYD9xPSR7cX0mc2VhcmNoPSR7YXJnc31gLCB7XG4gICAgICAgICAgICBoZWFkZXJzOiB0aGlzLmhlYWRlcnNcbiAgICAgICAgfSkudGhlbihyZXNwb25zZSA9PiB7XG4gICAgICAgICAgICBpZiAocmVzcG9uc2Uuc3RhdHVzID09PSAyMDAgfHwgcmVzcG9uc2Uuc3RhdHVzID09PSAyMDEpIHtcbiAgICAgICAgICAgICAgICByZXR1cm4gcmVzcG9uc2UuanNvbigpLnRoZW4oZGF0YSA9PiB7XG4gICAgICAgICAgICAgICAgICAgIHJldHVybiBkYXRhO1xuICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgfVxuICAgICAgICB9KTtcbiAgICB9XG4gICAgdXBsb2FkKCkge1xuICAgIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==