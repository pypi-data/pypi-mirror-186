"use strict";(self.webpackChunkinsteon_panel_frontend=self.webpackChunkinsteon_panel_frontend||[]).push([[3925],{2996:(e,t,r)=>{r.d(t,{p:()=>i});const i=(e,t)=>e&&e.config.components.includes(t)},1007:(e,t,r)=>{var i=r(3239),o=r(7500),a=r(3550),n=r(8636),l=r(1346),s=r(483),c=r(4516),d=r(7715),h=r(8394);r(2678),r(7662),r(1520);function f(){f=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var a="static"===o?e:r;this.defineClassElement(a,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!m(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var a=this.decorateConstructor(r,t);return i.push.apply(i,a.finishers),a.finishers=i,a},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,a=o.length-1;a>=0;a--){var n=t[e.placement];n.splice(n.indexOf(e.key),1);var l=this.fromElementDescriptor(e),s=this.toElementFinisherExtras((0,o[a])(l)||l);e=s.element,this.addElementPlacement(e,t),s.finisher&&i.push(s.finisher);var c=s.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),a=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==a.finisher&&r.push(a.finisher),void 0!==a.elements){e=a.elements;for(var n=0;n<e.length-1;n++)for(var l=n+1;l<e.length;l++)if(e[n].key===e[l].key&&e[n].placement===e[l].placement)throw new TypeError("Duplicated element ("+e[n].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return k(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?k(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=y(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var a={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),a.initializer=e.initializer),a},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:v(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=v(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function u(e){var t,r=y(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function p(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function m(e){return e.decorators&&e.decorators.length}function b(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function v(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function y(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function k(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var o=f();if(i)for(var a=0;a<i.length;a++)o=i[a](o);var n=t((function(e){o.initializeInstanceElements(e,l.elements)}),r),l=o.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===a.key&&e.placement===a.placement},i=0;i<e.length;i++){var o,a=e[i];if("method"===a.kind&&(o=t.find(r)))if(b(a.descriptor)||b(o.descriptor)){if(m(a)||m(o))throw new ReferenceError("Duplicated methods ("+a.key+") can't be decorated.");o.descriptor=a.descriptor}else{if(m(a)){if(m(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+a.key+").");o.decorators=a.decorators}p(a,o)}else t.push(a)}return t}(n.d.map(u)),e);o.initializeClassElements(n.F,l.elements),o.runClassFinishers(n.F,l.finishers)}([(0,a.Mo)("search-input")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,a.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.Cb)()],key:"filter",value:void 0},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"suffix",value:()=>!1},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"autofocus",value:()=>!1},{kind:"field",decorators:[(0,a.Cb)({type:String})],key:"label",value:void 0},{kind:"method",key:"focus",value:function(){var e;null===(e=this._input)||void 0===e||e.focus()}},{kind:"field",decorators:[(0,a.IO)("ha-textfield",!0)],key:"_input",value:void 0},{kind:"method",key:"render",value:function(){return o.dy`
      <ha-textfield
        .autofocus=${this.autofocus}
        .label=${this.label||"Search"}
        .value=${this.filter||""}
        icon
        .iconTrailing=${this.filter||this.suffix}
        @input=${this._filterInputChanged}
      >
        <slot name="prefix" slot="leadingIcon">
          <ha-svg-icon
            tabindex="-1"
            class="prefix"
            .path=${"M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"}
          ></ha-svg-icon>
        </slot>
        <div class="trailing" slot="trailingIcon">
          ${this.filter&&o.dy`
            <ha-icon-button
              @click=${this._clearSearch}
              .label=${this.hass.localize("ui.common.clear")}
              .path=${"M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z"}
              class="clear-button"
            ></ha-icon-button>
          `}
          <slot name="suffix"></slot>
        </div>
      </ha-textfield>
    `}},{kind:"method",key:"_filterChanged",value:async function(e){(0,h.B)(this,"value-changed",{value:String(e)})}},{kind:"method",key:"_filterInputChanged",value:async function(e){this._filterChanged(e.target.value)}},{kind:"method",key:"_clearSearch",value:async function(){this._filterChanged("")}},{kind:"get",static:!0,key:"styles",value:function(){return o.iv`
      :host {
        display: inline-flex;
      }
      ha-svg-icon,
      ha-icon-button {
        color: var(--primary-text-color);
      }
      ha-svg-icon {
        outline: none;
      }
      .clear-button {
        --mdc-icon-size: 20px;
      }
      ha-textfield {
        display: inherit;
      }
      .trailing {
        display: flex;
        align-items: center;
      }
    `}}]}}),o.oi);var g=r(2218),w=r(2537),_=r(9950),x=(r(4376),r(3217));let E;r(9874);function C(){C=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var a="static"===o?e:r;this.defineClassElement(a,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!$(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var a=this.decorateConstructor(r,t);return i.push.apply(i,a.finishers),a.finishers=i,a},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,a=o.length-1;a>=0;a--){var n=t[e.placement];n.splice(n.indexOf(e.key),1);var l=this.fromElementDescriptor(e),s=this.toElementFinisherExtras((0,o[a])(l)||l);e=s.element,this.addElementPlacement(e,t),s.finisher&&i.push(s.finisher);var c=s.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),a=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==a.finisher&&r.push(a.finisher),void 0!==a.elements){e=a.elements;for(var n=0;n<e.length-1;n++)for(var l=n+1;l<e.length;l++)if(e[n].key===e[l].key&&e[n].placement===e[l].placement)throw new TypeError("Duplicated element ("+e[n].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return R(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?R(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=T(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var a={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),a.initializer=e.initializer),a},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:A(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=A(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function D(e){var t,r=T(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function P(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function $(e){return e.decorators&&e.decorators.length}function S(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function A(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function T(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function R(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}function z(){return z="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,r){var i=O(e,t);if(i){var o=Object.getOwnPropertyDescriptor(i,t);return o.get?o.get.call(arguments.length<3?e:r):o.value}},z.apply(this,arguments)}function O(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=j(e)););return e}function j(e){return j=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},j(e)}!function(e,t,r,i){var o=C();if(i)for(var a=0;a<i.length;a++)o=i[a](o);var n=t((function(e){o.initializeInstanceElements(e,l.elements)}),r),l=o.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===a.key&&e.placement===a.placement},i=0;i<e.length;i++){var o,a=e[i];if("method"===a.kind&&(o=t.find(r)))if(S(a.descriptor)||S(o.descriptor)){if($(a)||$(o))throw new ReferenceError("Duplicated methods ("+a.key+") can't be decorated.");o.descriptor=a.descriptor}else{if($(a)){if($(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+a.key+").");o.decorators=a.decorators}P(a,o)}else t.push(a)}return t}(n.d.map(D)),e);o.initializeClassElements(n.F,l.elements),o.runClassFinishers(n.F,l.finishers)}([(0,a.Mo)("ha-data-table")],(function(e,t){class f extends t{constructor(...t){super(...t),e(this)}}return{F:f,d:[{kind:"field",decorators:[(0,a.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.Cb)({type:Object})],key:"columns",value:()=>({})},{kind:"field",decorators:[(0,a.Cb)({type:Array})],key:"data",value:()=>[]},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"selectable",value:()=>!1},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"clickable",value:()=>!1},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"hasFab",value:()=>!1},{kind:"field",decorators:[(0,a.Cb)({attribute:!1})],key:"appendRow",value:void 0},{kind:"field",decorators:[(0,a.Cb)({type:Boolean,attribute:"auto-height"})],key:"autoHeight",value:()=>!1},{kind:"field",decorators:[(0,a.Cb)({type:String})],key:"id",value:()=>"id"},{kind:"field",decorators:[(0,a.Cb)({type:String})],key:"noDataText",value:void 0},{kind:"field",decorators:[(0,a.Cb)({type:String})],key:"searchLabel",value:void 0},{kind:"field",decorators:[(0,a.Cb)({type:Boolean,attribute:"no-label-float"})],key:"noLabelFloat",value:()=>!1},{kind:"field",decorators:[(0,a.Cb)({type:String})],key:"filter",value:()=>""},{kind:"field",decorators:[(0,a.SB)()],key:"_filterable",value:()=>!1},{kind:"field",decorators:[(0,a.SB)()],key:"_filter",value:()=>""},{kind:"field",decorators:[(0,a.SB)()],key:"_sortColumn",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_sortDirection",value:()=>null},{kind:"field",decorators:[(0,a.SB)()],key:"_filteredData",value:()=>[]},{kind:"field",decorators:[(0,a.SB)()],key:"_headerHeight",value:()=>0},{kind:"field",decorators:[(0,a.IO)("slot[name='header']")],key:"_header",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_items",value:()=>[]},{kind:"field",key:"_checkableRowsCount",value:void 0},{kind:"field",key:"_checkedRows",value:()=>[]},{kind:"field",key:"_sortColumns",value:()=>({})},{kind:"field",key:"curRequest",value:()=>0},{kind:"field",decorators:[(0,d.i)(".scroller")],key:"_savedScrollPos",value:void 0},{kind:"field",key:"_debounceSearch",value(){return(0,g.D)((e=>{this._filter=e}),100,!1)}},{kind:"method",key:"clearSelection",value:function(){this._checkedRows=[],this._checkedRowsChanged()}},{kind:"method",key:"connectedCallback",value:function(){z(j(f.prototype),"connectedCallback",this).call(this),this._items.length&&(this._items=[...this._items])}},{kind:"method",key:"firstUpdated",value:function(){this.updateComplete.then((()=>this._calcTableHeight()))}},{kind:"method",key:"willUpdate",value:function(e){if(z(j(f.prototype),"willUpdate",this).call(this,e),e.has("columns")){this._filterable=Object.values(this.columns).some((e=>e.filterable));for(const e in this.columns)if(this.columns[e].direction){this._sortDirection=this.columns[e].direction,this._sortColumn=e;break}const e=(0,i.Z)(this.columns);Object.values(e).forEach((e=>{delete e.title,delete e.type,delete e.template})),this._sortColumns=e}e.has("filter")&&this._debounceSearch(this.filter),e.has("data")&&(this._checkableRowsCount=this.data.filter((e=>!1!==e.selectable)).length),(e.has("data")||e.has("columns")||e.has("_filter")||e.has("_sortColumn")||e.has("_sortDirection"))&&this._sortFilterData()}},{kind:"method",key:"render",value:function(){return o.dy`
      <div class="mdc-data-table">
        <slot name="header" @slotchange=${this._calcTableHeight}>
          ${this._filterable?o.dy`
                <div class="table-header">
                  <search-input
                    .hass=${this.hass}
                    @value-changed=${this._handleSearchChange}
                    .label=${this.searchLabel}
                    .noLabelFloat=${this.noLabelFloat}
                  ></search-input>
                </div>
              `:""}
        </slot>
        <div
          class="mdc-data-table__table ${(0,n.$)({"auto-height":this.autoHeight})}"
          role="table"
          aria-rowcount=${this._filteredData.length+1}
          style=${(0,s.V)({height:this.autoHeight?53*(this._filteredData.length||1)+53+"px":`calc(100% - ${this._headerHeight}px)`})}
        >
          <div class="mdc-data-table__header-row" role="row" aria-rowindex="1">
            ${this.selectable?o.dy`
                  <div
                    class="mdc-data-table__header-cell mdc-data-table__header-cell--checkbox"
                    role="columnheader"
                  >
                    <ha-checkbox
                      class="mdc-data-table__row-checkbox"
                      @change=${this._handleHeaderRowCheckboxClick}
                      .indeterminate=${this._checkedRows.length&&this._checkedRows.length!==this._checkableRowsCount}
                      .checked=${this._checkedRows.length&&this._checkedRows.length===this._checkableRowsCount}
                    >
                    </ha-checkbox>
                  </div>
                `:""}
            ${Object.entries(this.columns).map((([e,t])=>{if(t.hidden)return"";const r=e===this._sortColumn,i={"mdc-data-table__header-cell--numeric":"numeric"===t.type,"mdc-data-table__header-cell--icon":"icon"===t.type,"mdc-data-table__header-cell--icon-button":"icon-button"===t.type,"mdc-data-table__header-cell--overflow-menu":"overflow-menu"===t.type,sortable:Boolean(t.sortable),"not-sorted":Boolean(t.sortable&&!r),grows:Boolean(t.grows)};return o.dy`
                <div
                  aria-label=${t.label}
                  class="mdc-data-table__header-cell ${(0,n.$)(i)}"
                  style=${t.width?(0,s.V)({[t.grows?"minWidth":"width"]:t.width,maxWidth:t.maxWidth||""}):""}
                  role="columnheader"
                  aria-sort=${(0,l.o)(r?"desc"===this._sortDirection?"descending":"ascending":void 0)}
                  @click=${this._handleHeaderClick}
                  .columnId=${e}
                >
                  ${t.sortable?o.dy`
                        <ha-svg-icon
                          .path=${r&&"desc"===this._sortDirection?"M11,4H13V16L18.5,10.5L19.92,11.92L12,19.84L4.08,11.92L5.5,10.5L11,16V4Z":"M13,20H11V8L5.5,13.5L4.08,12.08L12,4.16L19.92,12.08L18.5,13.5L13,8V20Z"}
                        ></ha-svg-icon>
                      `:""}
                  <span>${t.title}</span>
                </div>
              `}))}
          </div>
          ${this._filteredData.length?o.dy`
                <lit-virtualizer
                  scroller
                  class="mdc-data-table__content scroller ha-scrollbar"
                  @scroll=${this._saveScrollPos}
                  .items=${this._items}
                  .renderItem=${this._renderRow}
                ></lit-virtualizer>
              `:o.dy`
                <div class="mdc-data-table__content">
                  <div class="mdc-data-table__row" role="row">
                    <div class="mdc-data-table__cell grows center" role="cell">
                      ${this.noDataText||"No data"}
                    </div>
                  </div>
                </div>
              `}
        </div>
      </div>
    `}},{kind:"field",key:"_renderRow",value(){return(e,t)=>e?e.append?o.dy` <div class="mdc-data-table__row">${e.content}</div> `:e.empty?o.dy` <div class="mdc-data-table__row"></div> `:o.dy`
      <div
        aria-rowindex=${t+2}
        role="row"
        .rowId=${e[this.id]}
        @click=${this._handleRowClick}
        class="mdc-data-table__row ${(0,n.$)({"mdc-data-table__row--selected":this._checkedRows.includes(String(e[this.id])),clickable:this.clickable})}"
        aria-selected=${(0,l.o)(!!this._checkedRows.includes(String(e[this.id]))||void 0)}
        .selectable=${!1!==e.selectable}
      >
        ${this.selectable?o.dy`
              <div
                class="mdc-data-table__cell mdc-data-table__cell--checkbox"
                role="cell"
              >
                <ha-checkbox
                  class="mdc-data-table__row-checkbox"
                  @change=${this._handleRowCheckboxClick}
                  .rowId=${e[this.id]}
                  .disabled=${!1===e.selectable}
                  .checked=${this._checkedRows.includes(String(e[this.id]))}
                >
                </ha-checkbox>
              </div>
            `:""}
        ${Object.entries(this.columns).map((([t,r])=>r.hidden?"":o.dy`
            <div
              role=${r.main?"rowheader":"cell"}
              class="mdc-data-table__cell ${(0,n.$)({"mdc-data-table__cell--numeric":"numeric"===r.type,"mdc-data-table__cell--icon":"icon"===r.type,"mdc-data-table__cell--icon-button":"icon-button"===r.type,"mdc-data-table__cell--overflow-menu":"overflow-menu"===r.type,grows:Boolean(r.grows),forceLTR:Boolean(r.forceLTR)})}"
              style=${r.width?(0,s.V)({[r.grows?"minWidth":"width"]:r.width,maxWidth:r.maxWidth?r.maxWidth:""}):""}
            >
              ${r.template?r.template(e[t],e):e[t]}
            </div>
          `))}
      </div>
    `:o.dy``}},{kind:"method",key:"_sortFilterData",value:async function(){const e=(new Date).getTime();this.curRequest++;const t=this.curRequest;let i=this.data;this._filter&&(i=await this._memFilterData(this.data,this._sortColumns,this._filter));const o=this._sortColumn?(async(e,t,i,o)=>(E||(E=(0,x.Ud)(new Worker(new URL(r.p+r.u(7686),r.b)))),E.sortData(e,t,i,o)))(i,this._sortColumns[this._sortColumn],this._sortDirection,this._sortColumn):i,[a]=await Promise.all([o,w.y]),n=(new Date).getTime()-e;if(n<100&&await new Promise((e=>setTimeout(e,100-n))),this.curRequest===t){if(this.appendRow||this.hasFab){const e=[...a];this.appendRow&&e.push({append:!0,content:this.appendRow}),this.hasFab&&e.push({empty:!0}),this._items=e}else this._items=a;this._filteredData=a}}},{kind:"field",key:"_memFilterData",value:()=>(0,c.Z)((async(e,t,i)=>(async(e,t,i)=>(E||(E=(0,x.Ud)(new Worker(new URL(r.p+r.u(503),r.b)))),E.filterData(e,t,i)))(e,t,i)))},{kind:"method",key:"_handleHeaderClick",value:function(e){const t=e.currentTarget.columnId;this.columns[t].sortable&&(this._sortDirection&&this._sortColumn===t?"asc"===this._sortDirection?this._sortDirection="desc":this._sortDirection=null:this._sortDirection="asc",this._sortColumn=null===this._sortDirection?void 0:t,(0,h.B)(this,"sorting-changed",{column:t,direction:this._sortDirection}))}},{kind:"method",key:"_handleHeaderRowCheckboxClick",value:function(e){e.target.checked?(this._checkedRows=this._filteredData.filter((e=>!1!==e.selectable)).map((e=>e[this.id])),this._checkedRowsChanged()):(this._checkedRows=[],this._checkedRowsChanged())}},{kind:"field",key:"_handleRowCheckboxClick",value(){return e=>{const t=e.currentTarget,r=t.rowId;if(t.checked){if(this._checkedRows.includes(r))return;this._checkedRows=[...this._checkedRows,r]}else this._checkedRows=this._checkedRows.filter((e=>e!==r));this._checkedRowsChanged()}}},{kind:"field",key:"_handleRowClick",value(){return e=>{const t=e.target;if(["HA-CHECKBOX","MWC-BUTTON"].includes(t.tagName))return;const r=e.currentTarget.rowId;(0,h.B)(this,"row-click",{id:r},{bubbles:!1})}}},{kind:"method",key:"_checkedRowsChanged",value:function(){this._items.length&&(this._items=[...this._items]),(0,h.B)(this,"selection-changed",{value:this._checkedRows})}},{kind:"method",key:"_handleSearchChange",value:function(e){this.filter||this._debounceSearch(e.detail.value)}},{kind:"method",key:"_calcTableHeight",value:async function(){this.autoHeight||(await this.updateComplete,this._headerHeight=this._header.clientHeight)}},{kind:"method",decorators:[(0,a.hO)({passive:!0})],key:"_saveScrollPos",value:function(e){this._savedScrollPos=e.target.scrollTop}},{kind:"get",static:!0,key:"styles",value:function(){return[_.$c,o.iv`
        /* default mdc styles, colors changed, without checkbox styles */
        :host {
          height: 100%;
        }
        .mdc-data-table__content {
          font-family: Roboto, sans-serif;
          -moz-osx-font-smoothing: grayscale;
          -webkit-font-smoothing: antialiased;
          font-size: 0.875rem;
          line-height: 1.25rem;
          font-weight: 400;
          letter-spacing: 0.0178571429em;
          text-decoration: inherit;
          text-transform: inherit;
        }

        .mdc-data-table {
          background-color: var(--data-table-background-color);
          border-radius: 4px;
          border-width: 1px;
          border-style: solid;
          border-color: var(--divider-color);
          display: inline-flex;
          flex-direction: column;
          box-sizing: border-box;
          overflow: hidden;
        }

        .mdc-data-table__row--selected {
          background-color: rgba(var(--rgb-primary-color), 0.04);
        }

        .mdc-data-table__row {
          display: flex;
          width: 100%;
          height: 52px;
        }

        .mdc-data-table__row ~ .mdc-data-table__row {
          border-top: 1px solid var(--divider-color);
        }

        .mdc-data-table__row:not(.mdc-data-table__row--selected):hover {
          background-color: rgba(var(--rgb-primary-text-color), 0.04);
        }

        .mdc-data-table__header-cell {
          color: var(--primary-text-color);
        }

        .mdc-data-table__cell {
          color: var(--primary-text-color);
        }

        .mdc-data-table__header-row {
          height: 56px;
          display: flex;
          width: 100%;
          border-bottom: 1px solid var(--divider-color);
          overflow-x: auto;
        }

        .mdc-data-table__header-row::-webkit-scrollbar {
          display: none;
        }

        .mdc-data-table__cell,
        .mdc-data-table__header-cell {
          padding-right: 16px;
          padding-left: 16px;
          align-self: center;
          overflow: hidden;
          text-overflow: ellipsis;
          flex-shrink: 0;
          box-sizing: border-box;
        }

        .mdc-data-table__cell.mdc-data-table__cell--icon {
          overflow: initial;
        }

        .mdc-data-table__header-cell--checkbox,
        .mdc-data-table__cell--checkbox {
          /* @noflip */
          padding-left: 16px;
          /* @noflip */
          padding-right: 0;
          width: 60px;
        }
        :host([dir="rtl"]) .mdc-data-table__header-cell--checkbox,
        :host([dir="rtl"]) .mdc-data-table__cell--checkbox {
          /* @noflip */
          padding-left: 0;
          /* @noflip */
          padding-right: 16px;
        }

        .mdc-data-table__table {
          height: 100%;
          width: 100%;
          border: 0;
          white-space: nowrap;
        }

        .mdc-data-table__cell {
          font-family: Roboto, sans-serif;
          -moz-osx-font-smoothing: grayscale;
          -webkit-font-smoothing: antialiased;
          font-size: 0.875rem;
          line-height: 1.25rem;
          font-weight: 400;
          letter-spacing: 0.0178571429em;
          text-decoration: inherit;
          text-transform: inherit;
        }

        .mdc-data-table__cell a {
          color: inherit;
          text-decoration: none;
        }

        .mdc-data-table__cell--numeric {
          text-align: right;
        }
        :host([dir="rtl"]) .mdc-data-table__cell--numeric {
          /* @noflip */
          text-align: left;
        }

        .mdc-data-table__cell--icon {
          color: var(--secondary-text-color);
          text-align: center;
        }

        .mdc-data-table__header-cell--icon,
        .mdc-data-table__cell--icon {
          width: 54px;
        }

        .mdc-data-table__header-cell.mdc-data-table__header-cell--icon {
          text-align: center;
        }

        .mdc-data-table__header-cell.sortable.mdc-data-table__header-cell--icon:hover,
        .mdc-data-table__header-cell.sortable.mdc-data-table__header-cell--icon:not(.not-sorted) {
          text-align: left;
        }
        :host([dir="rtl"])
          .mdc-data-table__header-cell.sortable.mdc-data-table__header-cell--icon:hover,
        :host([dir="rtl"])
          .mdc-data-table__header-cell.sortable.mdc-data-table__header-cell--icon:not(.not-sorted) {
          text-align: right;
        }

        .mdc-data-table__cell--icon:first-child ha-icon,
        .mdc-data-table__cell--icon:first-child ha-state-icon,
        .mdc-data-table__cell--icon:first-child ha-svg-icon {
          margin-left: 8px;
        }
        :host([dir="rtl"]) .mdc-data-table__cell--icon:first-child ha-icon,
        :host([dir="rtl"])
          .mdc-data-table__cell--icon:first-child
          ha-state-icon,
        :host([dir="rtl"]) .mdc-data-table__cell--icon:first-child ha-svg-icon {
          margin-left: auto;
          margin-right: 8px;
        }

        .mdc-data-table__cell--icon:first-child state-badge {
          margin-right: -8px;
        }
        :host([dir="rtl"]) .mdc-data-table__cell--icon:first-child state-badge {
          margin-right: auto;
          margin-left: -8px;
        }

        .mdc-data-table__cell--overflow-menu,
        .mdc-data-table__header-cell--overflow-menu,
        .mdc-data-table__header-cell--icon-button,
        .mdc-data-table__cell--icon-button {
          padding: 8px;
        }

        .mdc-data-table__header-cell--icon-button,
        .mdc-data-table__cell--icon-button {
          width: 56px;
        }

        .mdc-data-table__cell--overflow-menu,
        .mdc-data-table__cell--icon-button {
          color: var(--secondary-text-color);
          text-overflow: clip;
        }

        .mdc-data-table__header-cell--icon-button:first-child,
        .mdc-data-table__cell--icon-button:first-child,
        .mdc-data-table__header-cell--icon-button:last-child,
        .mdc-data-table__cell--icon-button:last-child {
          width: 64px;
        }

        .mdc-data-table__cell--overflow-menu:first-child,
        .mdc-data-table__header-cell--overflow-menu:first-child,
        .mdc-data-table__header-cell--icon-button:first-child,
        .mdc-data-table__cell--icon-button:first-child {
          padding-left: 16px;
        }
        :host([dir="rtl"])
          .mdc-data-table__header-cell--overflow-menu:first-child,
        :host([dir="rtl"]) .mdc-data-table__cell--overflow-menu:first-child,
        :host([dir="rtl"])
          .mdc-data-table__header-cell--overflow-menu:first-child,
        :host([dir="rtl"]) .mdc-data-table__cell--overflow-menu:first-child {
          padding-left: 8px;
          padding-right: 16px;
        }

        .mdc-data-table__cell--overflow-menu:last-child,
        .mdc-data-table__header-cell--overflow-menu:last-child,
        .mdc-data-table__header-cell--icon-button:last-child,
        .mdc-data-table__cell--icon-button:last-child {
          padding-right: 16px;
        }
        :host([dir="rtl"])
          .mdc-data-table__header-cell--overflow-menu:last-child,
        :host([dir="rtl"]) .mdc-data-table__cell--overflow-menu:last-child,
        :host([dir="rtl"]) .mdc-data-table__header-cell--icon-button:last-child,
        :host([dir="rtl"]) .mdc-data-table__cell--icon-button:last-child {
          padding-right: 8px;
          padding-left: 16px;
        }
        .mdc-data-table__cell--overflow-menu,
        .mdc-data-table__header-cell--overflow-menu {
          overflow: initial;
        }
        .mdc-data-table__cell--icon-button a {
          color: var(--secondary-text-color);
        }

        .mdc-data-table__header-cell {
          font-family: Roboto, sans-serif;
          -moz-osx-font-smoothing: grayscale;
          -webkit-font-smoothing: antialiased;
          font-size: 0.875rem;
          line-height: 1.375rem;
          font-weight: 500;
          letter-spacing: 0.0071428571em;
          text-decoration: inherit;
          text-transform: inherit;
          text-align: left;
        }
        :host([dir="rtl"]) .mdc-data-table__header-cell {
          /* @noflip */
          text-align: right;
        }

        .mdc-data-table__header-cell--numeric {
          text-align: right;
        }
        .mdc-data-table__header-cell--numeric.sortable:hover,
        .mdc-data-table__header-cell--numeric.sortable:not(.not-sorted) {
          text-align: left;
        }
        :host([dir="rtl"]) .mdc-data-table__header-cell--numeric {
          /* @noflip */
          text-align: left;
        }
        :host([dir="rtl"]) .mdc-data-table__header-cell--numeric.sortable:hover,
        :host([dir="rtl"])
          .mdc-data-table__header-cell--numeric.sortable:not(.not-sorted) {
          text-align: right;
        }

        /* custom from here */

        :host {
          display: block;
        }

        .mdc-data-table {
          display: block;
          border-width: var(--data-table-border-width, 1px);
          height: 100%;
        }
        .mdc-data-table__header-cell {
          overflow: hidden;
          position: relative;
        }
        .mdc-data-table__header-cell span {
          position: relative;
          left: 0px;
        }
        :host([dir="rtl"]) .mdc-data-table__header-cell span {
          left: auto;
          right: 0px;
        }

        .mdc-data-table__header-cell.sortable {
          cursor: pointer;
        }
        .mdc-data-table__header-cell > * {
          transition: left 0.2s ease;
        }
        :host([dir="rtl"]) .mdc-data-table__header-cell > * {
          transition: right 0.2s ease;
        }
        .mdc-data-table__header-cell ha-svg-icon {
          top: -3px;
          position: absolute;
        }
        .mdc-data-table__header-cell.not-sorted ha-svg-icon {
          left: -20px;
        }
        :host([dir="rtl"]) .mdc-data-table__header-cell.not-sorted ha-svg-icon {
          right: -20px;
        }
        .mdc-data-table__header-cell.sortable:not(.not-sorted) span,
        .mdc-data-table__header-cell.sortable.not-sorted:hover span {
          left: 24px;
        }
        :host([dir="rtl"])
          .mdc-data-table__header-cell.sortable:not(.not-sorted)
          span,
        :host([dir="rtl"])
          .mdc-data-table__header-cell.sortable.not-sorted:hover
          span {
          left: auto;
          right: 24px;
        }
        .mdc-data-table__header-cell.sortable:not(.not-sorted) ha-svg-icon,
        .mdc-data-table__header-cell.sortable:hover.not-sorted ha-svg-icon {
          left: 12px;
        }
        :host([dir="rtl"])
          .mdc-data-table__header-cell.sortable:not(.not-sorted)
          ha-svg-icon,
        :host([dir="rtl"])
          .mdc-data-table__header-cell.sortable:hover.not-sorted
          ha-svg-icon {
          left: auto;
          right: 12px;
        }
        .table-header {
          border-bottom: 1px solid var(--divider-color);
        }
        search-input {
          display: block;
          flex: 1;
        }
        slot[name="header"] {
          display: block;
        }
        .center {
          text-align: center;
        }
        .secondary {
          color: var(--secondary-text-color);
        }
        .scroller {
          height: calc(100% - 57px);
          overflow: overlay !important;
        }

        .mdc-data-table__table.auto-height .scroller {
          overflow-y: hidden !important;
        }
        .grows {
          flex-grow: 1;
          flex-shrink: 1;
        }
        .forceLTR {
          direction: ltr;
        }
        .clickable {
          cursor: pointer;
        }
        lit-virtualizer {
          contain: size layout !important;
        }
      `]}}]}}),o.oi)},841:(e,t,r)=>{r(1156);var i=r(7500),o=r(3550),a=r(8636),n=r(4516),l=r(2996),s=r(7715),c=r(1750),d=(r(3358),r(7565),r(7662),r(8734)),h=r(1346);function f(){f=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var a="static"===o?e:r;this.defineClassElement(a,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!m(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var a=this.decorateConstructor(r,t);return i.push.apply(i,a.finishers),a.finishers=i,a},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,a=o.length-1;a>=0;a--){var n=t[e.placement];n.splice(n.indexOf(e.key),1);var l=this.fromElementDescriptor(e),s=this.toElementFinisherExtras((0,o[a])(l)||l);e=s.element,this.addElementPlacement(e,t),s.finisher&&i.push(s.finisher);var c=s.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),a=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==a.finisher&&r.push(a.finisher),void 0!==a.elements){e=a.elements;for(var n=0;n<e.length-1;n++)for(var l=n+1;l<e.length;l++)if(e[n].key===e[l].key&&e[n].placement===e[l].placement)throw new TypeError("Duplicated element ("+e[n].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return k(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?k(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=y(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var a={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),a.initializer=e.initializer),a},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:v(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=v(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function u(e){var t,r=y(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function p(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function m(e){return e.decorators&&e.decorators.length}function b(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function v(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function y(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function k(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}!function(e,t,r,i){var o=f();if(i)for(var a=0;a<i.length;a++)o=i[a](o);var n=t((function(e){o.initializeInstanceElements(e,l.elements)}),r),l=o.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===a.key&&e.placement===a.placement},i=0;i<e.length;i++){var o,a=e[i];if("method"===a.kind&&(o=t.find(r)))if(b(a.descriptor)||b(o.descriptor)){if(m(a)||m(o))throw new ReferenceError("Duplicated methods ("+a.key+") can't be decorated.");o.descriptor=a.descriptor}else{if(m(a)){if(m(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+a.key+").");o.decorators=a.decorators}p(a,o)}else t.push(a)}return t}(n.d.map(u)),e);o.initializeClassElements(n.F,l.elements),o.runClassFinishers(n.F,l.finishers)}([(0,o.Mo)("ha-tab")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({type:Boolean,reflect:!0})],key:"active",value:()=>!1},{kind:"field",decorators:[(0,o.Cb)({type:Boolean,reflect:!0})],key:"narrow",value:()=>!1},{kind:"field",decorators:[(0,o.Cb)()],key:"name",value:void 0},{kind:"field",decorators:[(0,o.GC)("mwc-ripple")],key:"_ripple",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_shouldRenderRipple",value:()=>!1},{kind:"method",key:"render",value:function(){return i.dy`
      <div
        tabindex="0"
        role="tab"
        aria-selected=${this.active}
        aria-label=${(0,h.o)(this.name)}
        @focus=${this.handleRippleFocus}
        @blur=${this.handleRippleBlur}
        @mousedown=${this.handleRippleActivate}
        @mouseup=${this.handleRippleDeactivate}
        @mouseenter=${this.handleRippleMouseEnter}
        @mouseleave=${this.handleRippleMouseLeave}
        @touchstart=${this.handleRippleActivate}
        @touchend=${this.handleRippleDeactivate}
        @touchcancel=${this.handleRippleDeactivate}
        @keydown=${this._handleKeyDown}
      >
        ${this.narrow?i.dy`<slot name="icon"></slot>`:""}
        <span class="name">${this.name}</span>
        ${this._shouldRenderRipple?i.dy`<mwc-ripple></mwc-ripple>`:""}
      </div>
    `}},{kind:"field",key:"_rippleHandlers",value(){return new d.A((()=>(this._shouldRenderRipple=!0,this._ripple)))}},{kind:"method",key:"_handleKeyDown",value:function(e){13===e.keyCode&&e.target.click()}},{kind:"method",decorators:[(0,o.hO)({passive:!0})],key:"handleRippleActivate",value:function(e){this._rippleHandlers.startPress(e)}},{kind:"method",key:"handleRippleDeactivate",value:function(){this._rippleHandlers.endPress()}},{kind:"method",key:"handleRippleMouseEnter",value:function(){this._rippleHandlers.startHover()}},{kind:"method",key:"handleRippleMouseLeave",value:function(){this._rippleHandlers.endHover()}},{kind:"method",key:"handleRippleFocus",value:function(){this._rippleHandlers.startFocus()}},{kind:"method",key:"handleRippleBlur",value:function(){this._rippleHandlers.endFocus()}},{kind:"get",static:!0,key:"styles",value:function(){return i.iv`
      div {
        padding: 0 32px;
        display: flex;
        flex-direction: column;
        text-align: center;
        box-sizing: border-box;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: var(--header-height);
        cursor: pointer;
        position: relative;
        outline: none;
      }

      .name {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 100%;
      }

      :host([active]) {
        color: var(--primary-color);
      }

      :host(:not([narrow])[active]) div {
        border-bottom: 2px solid var(--primary-color);
      }

      :host([narrow]) {
        min-width: 0;
        display: flex;
        justify-content: center;
        overflow: hidden;
      }

      :host([narrow]) div {
        padding: 0 4px;
      }
    `}}]}}),i.oi);function g(){g=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var a="static"===o?e:r;this.defineClassElement(a,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!x(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var a=this.decorateConstructor(r,t);return i.push.apply(i,a.finishers),a.finishers=i,a},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,a=o.length-1;a>=0;a--){var n=t[e.placement];n.splice(n.indexOf(e.key),1);var l=this.fromElementDescriptor(e),s=this.toElementFinisherExtras((0,o[a])(l)||l);e=s.element,this.addElementPlacement(e,t),s.finisher&&i.push(s.finisher);var c=s.extras;if(c){for(var d=0;d<c.length;d++)this.addElementPlacement(c[d],t);r.push.apply(r,c)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),a=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==a.finisher&&r.push(a.finisher),void 0!==a.elements){e=a.elements;for(var n=0;n<e.length-1;n++)for(var l=n+1;l<e.length;l++)if(e[n].key===e[l].key&&e[n].placement===e[l].placement)throw new TypeError("Duplicated element ("+e[n].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return P(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?P(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=D(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var a={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),a.initializer=e.initializer),a},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:C(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=C(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function w(e){var t,r=D(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function _(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function x(e){return e.decorators&&e.decorators.length}function E(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function C(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function D(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function P(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}function $(){return $="undefined"!=typeof Reflect&&Reflect.get?Reflect.get.bind():function(e,t,r){var i=S(e,t);if(i){var o=Object.getOwnPropertyDescriptor(i,t);return o.get?o.get.call(arguments.length<3?e:r):o.value}},$.apply(this,arguments)}function S(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=A(e)););return e}function A(e){return A=Object.setPrototypeOf?Object.getPrototypeOf.bind():function(e){return e.__proto__||Object.getPrototypeOf(e)},A(e)}!function(e,t,r,i){var o=g();if(i)for(var a=0;a<i.length;a++)o=i[a](o);var n=t((function(e){o.initializeInstanceElements(e,l.elements)}),r),l=o.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===a.key&&e.placement===a.placement},i=0;i<e.length;i++){var o,a=e[i];if("method"===a.kind&&(o=t.find(r)))if(E(a.descriptor)||E(o.descriptor)){if(x(a)||x(o))throw new ReferenceError("Duplicated methods ("+a.key+") can't be decorated.");o.descriptor=a.descriptor}else{if(x(a)){if(x(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+a.key+").");o.decorators=a.decorators}_(a,o)}else t.push(a)}return t}(n.d.map(w)),e);o.initializeClassElements(n.F,l.elements),o.runClassFinishers(n.F,l.finishers)}([(0,o.Mo)("hass-tabs-subpage")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"supervisor",value:()=>!1},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"localizeFunc",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:String,attribute:"back-path"})],key:"backPath",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"backCallback",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean,attribute:"main-page"})],key:"mainPage",value:()=>!1},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"route",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"tabs",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean,reflect:!0})],key:"narrow",value:()=>!1},{kind:"field",decorators:[(0,o.Cb)({type:Boolean,reflect:!0,attribute:"is-wide"})],key:"isWide",value:()=>!1},{kind:"field",decorators:[(0,o.Cb)({type:Boolean,reflect:!0})],key:"rtl",value:()=>!1},{kind:"field",decorators:[(0,o.SB)()],key:"_activeTab",value:void 0},{kind:"field",decorators:[(0,s.i)(".content")],key:"_savedScrollPos",value:void 0},{kind:"field",key:"_getTabs",value(){return(0,n.Z)(((e,t,r,o,a,n,s)=>{const c=e.filter((e=>(!e.component||e.core||(0,l.p)(this.hass,e.component))&&(!e.advancedOnly||r)));if(c.length<2){if(1===c.length){const e=c[0];return[e.translationKey?s(e.translationKey):e.name]}return[""]}return c.map((e=>i.dy`
            <a href=${e.path}>
              <ha-tab
                .hass=${this.hass}
                .active=${e.path===(null==t?void 0:t.path)}
                .narrow=${this.narrow}
                .name=${e.translationKey?s(e.translationKey):e.name}
              >
                ${e.iconPath?i.dy`<ha-svg-icon
                      slot="icon"
                      .path=${e.iconPath}
                    ></ha-svg-icon>`:""}
              </ha-tab>
            </a>
          `))}))}},{kind:"method",key:"willUpdate",value:function(e){if(e.has("route")&&(this._activeTab=this.tabs.find((e=>`${this.route.prefix}${this.route.path}`.includes(e.path)))),e.has("hass")){const t=e.get("hass");t&&t.language===this.hass.language||(this.rtl=(0,c.HE)(this.hass))}$(A(r.prototype),"willUpdate",this).call(this,e)}},{kind:"method",key:"render",value:function(){var e,t;const r=this._getTabs(this.tabs,this._activeTab,null===(e=this.hass.userData)||void 0===e?void 0:e.showAdvanced,this.hass.config.components,this.hass.language,this.narrow,this.localizeFunc||this.hass.localize),o=r.length>1;return i.dy`
      <div class="toolbar">
        ${this.mainPage||!this.backPath&&null!==(t=history.state)&&void 0!==t&&t.root?i.dy`
              <ha-menu-button
                .hassio=${this.supervisor}
                .hass=${this.hass}
                .narrow=${this.narrow}
              ></ha-menu-button>
            `:this.backPath?i.dy`
              <a href=${this.backPath}>
                <ha-icon-button-arrow-prev
                  .hass=${this.hass}
                ></ha-icon-button-arrow-prev>
              </a>
            `:i.dy`
              <ha-icon-button-arrow-prev
                .hass=${this.hass}
                @click=${this._backTapped}
              ></ha-icon-button-arrow-prev>
            `}
        ${this.narrow||!o?i.dy`<div class="main-title">
              <slot name="header">${o?"":r[0]}</slot>
            </div>`:""}
        ${o?i.dy`
              <div id="tabbar" class=${(0,a.$)({"bottom-bar":this.narrow})}>
                ${r}
              </div>
            `:""}
        <div id="toolbar-icon">
          <slot name="toolbar-icon"></slot>
        </div>
      </div>
      <div
        class="content ${(0,a.$)({tabs:o})}"
        @scroll=${this._saveScrollPos}
      >
        <slot></slot>
      </div>
      <div id="fab" class=${(0,a.$)({tabs:o})}>
        <slot name="fab"></slot>
      </div>
    `}},{kind:"method",decorators:[(0,o.hO)({passive:!0})],key:"_saveScrollPos",value:function(e){this._savedScrollPos=e.target.scrollTop}},{kind:"method",key:"_backTapped",value:function(){this.backCallback?this.backCallback():history.back()}},{kind:"get",static:!0,key:"styles",value:function(){return i.iv`
      :host {
        display: block;
        height: 100%;
        background-color: var(--primary-background-color);
      }

      :host([narrow]) {
        width: 100%;
        position: fixed;
      }

      ha-menu-button {
        margin-right: 24px;
      }

      .toolbar {
        display: flex;
        align-items: center;
        font-size: 20px;
        height: var(--header-height);
        background-color: var(--sidebar-background-color);
        font-weight: 400;
        border-bottom: 1px solid var(--divider-color);
        padding: 0 16px;
        box-sizing: border-box;
      }
      .toolbar a {
        color: var(--sidebar-text-color);
        text-decoration: none;
      }
      .bottom-bar a {
        width: 25%;
      }

      #tabbar {
        display: flex;
        font-size: 14px;
        overflow: hidden;
      }

      #tabbar > a {
        overflow: hidden;
        max-width: 45%;
      }

      #tabbar.bottom-bar {
        position: absolute;
        bottom: 0;
        left: 0;
        padding: 0 16px;
        box-sizing: border-box;
        background-color: var(--sidebar-background-color);
        border-top: 1px solid var(--divider-color);
        justify-content: space-around;
        z-index: 2;
        font-size: 12px;
        width: 100%;
        padding-bottom: env(safe-area-inset-bottom);
      }

      #tabbar:not(.bottom-bar) {
        flex: 1;
        justify-content: center;
      }

      :host(:not([narrow])) #toolbar-icon {
        min-width: 40px;
      }

      ha-menu-button,
      ha-icon-button-arrow-prev,
      ::slotted([slot="toolbar-icon"]) {
        display: flex;
        flex-shrink: 0;
        pointer-events: auto;
        color: var(--sidebar-icon-color);
      }

      .main-title {
        flex: 1;
        max-height: var(--header-height);
        line-height: 20px;
        color: var(--sidebar-text-color);
        margin: var(--main-title-margin, 0 0 0 24px);
      }

      .content {
        position: relative;
        width: calc(
          100% - env(safe-area-inset-left) - env(safe-area-inset-right)
        );
        margin-left: env(safe-area-inset-left);
        margin-right: env(safe-area-inset-right);
        height: calc(100% - 1px - var(--header-height));
        height: calc(
          100% - 1px - var(--header-height) - env(safe-area-inset-bottom)
        );
        overflow: auto;
        -webkit-overflow-scrolling: touch;
      }

      :host([narrow]) .content.tabs {
        height: calc(100% - 2 * var(--header-height));
        height: calc(
          100% - 2 * var(--header-height) - env(safe-area-inset-bottom)
        );
      }

      #fab {
        position: fixed;
        right: calc(16px + env(safe-area-inset-right));
        bottom: calc(16px + env(safe-area-inset-bottom));
        z-index: 1;
      }
      :host([narrow]) #fab.tabs {
        bottom: calc(84px + env(safe-area-inset-bottom));
      }
      #fab[is-wide] {
        bottom: 24px;
        right: 24px;
      }
      :host([rtl]) #fab {
        right: auto;
        left: calc(16px + env(safe-area-inset-left));
      }
      :host([rtl][is-wide]) #fab {
        bottom: 24px;
        left: 24px;
        right: auto;
      }
    `}}]}}),i.oi)}}]);
//# sourceMappingURL=2b6ee92b.js.map