/*! For license information please see 22011c56.js.LICENSE.txt */
"use strict";(self.webpackChunkinsteon_panel_frontend=self.webpackChunkinsteon_panel_frontend||[]).push([[3725],{3725:(e,t,a)=>{const i=Intl&&Intl.DateTimeFormat,r=[38,33,36],n=[40,34,35],o=new Set([37,...r]),s=new Set([39,...n]),l=new Set([39,...r]),d=new Set([37,...n]),c=new Set([37,39,...r,...n]);var h=a(7480),u=a(7500),p=a(3550),y=a(5304),_=a(8941),m=a(1563);const f=(0,_.XM)(class extends _.Xe{constructor(e){super(e),this.tt=new WeakMap}render(e){return[e]}update(e,[t]){if((0,m.hN)(this.it)&&(!(0,m.hN)(t)||this.it.strings!==t.strings)){const t=(0,m.i9)(e).pop();let a=this.tt.get(this.it.strings);if(void 0===a){const e=document.createDocumentFragment();a=(0,y.sY)(y.Ld,e),a.setConnected(!1),this.tt.set(this.it.strings,a)}(0,m.hl)(a,[t]),(0,m._Y)(a,void 0,t)}if((0,m.hN)(t)){if(!(0,m.hN)(this.it)||this.it.strings!==t.strings){const a=this.tt.get(t.strings);if(void 0!==a){const t=(0,m.i9)(a).pop();(0,m.E_)(e),(0,m._Y)(e,void 0,t),(0,m.hl)(e,[t])}}this.it=t}else this.it=void 0;return this.render(t)}});var b=a(8636),w=a(6230);function v(e,t,a){return new Date(Date.UTC(e,t,a))}const g=u.dy`<svg height="24" viewBox="0 0 24 24" width="24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"></path></svg>`,k=u.dy`<svg height="24" viewBox="0 0 24 24" width="24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg>`,D=u.iv`
button {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;

  position: relative;
  display: block;
  margin: 0;
  padding: 0;
  background: none; /** NOTE: IE11 fix */
  color: inherit;
  border: none;
  font: inherit;
  text-align: left;
  text-transform: inherit;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
`,x=(u.iv`
a {
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);

  position: relative;
  display: inline-block;
  background: initial;
  color: inherit;
  font: inherit;
  text-transform: inherit;
  text-decoration: none;
  outline: none;
}
a:focus,
a:focus.page-selected {
  text-decoration: underline;
}
`,u.iv`
svg {
  display: block;
  min-width: var(--svg-icon-min-width, 24px);
  min-height: var(--svg-icon-min-height, 24px);
  fill: var(--svg-icon-fill, currentColor);
  pointer-events: none;
}
`,u.iv`[hidden] { display: none !important; }`,u.iv`
:host {
  display: block;

  /* --app-datepicker-width: 300px; */
  /* --app-datepicker-primary-color: #4285f4; */
  /* --app-datepicker-header-height: 80px; */
}

* {
  box-sizing: border-box;
}
`);function C(e,t){return+t-+e}function T({hasAltKey:e,keyCode:t,focusedDate:a,selectedDate:i,disabledDaysSet:r,disabledDatesSet:n,minTime:c,maxTime:h}){const u=a.getUTCFullYear(),p=a.getUTCMonth(),y=a.getUTCDate(),_=+a,m=i.getUTCFullYear(),f=i.getUTCMonth();let b=u,w=p,g=y,k=!0;switch((f!==p||m!==u)&&(b=m,w=f,g=1,k=34===t||33===t||35===t),k){case _===c&&o.has(t):case _===h&&s.has(t):break;case 38===t:g-=7;break;case 40===t:g+=7;break;case 37===t:g-=1;break;case 39===t:g+=1;break;case 34===t:e?b+=1:w+=1;break;case 33===t:e?b-=1:w-=1;break;case 35===t:w+=1,g=0;break;default:g=1}if(34===t||33===t){const e=v(b,w+1,0).getUTCDate();g>e&&(g=e)}const D=function({keyCode:e,disabledDaysSet:t,disabledDatesSet:a,focusedDate:i,maxTime:r,minTime:n}){const o=+i;let s=o<n,c=o>r;if(C(n,r)<864e5)return i;let h=s||c||t.has(i.getUTCDay())||a.has(o);if(!h)return i;let u=0,p=s===c?i:new Date(s?n-864e5:864e5+r);const y=p.getUTCFullYear(),_=p.getUTCMonth();let m=p.getUTCDate();for(;h;)(s||!c&&l.has(e))&&(m+=1),(c||!s&&d.has(e))&&(m-=1),p=v(y,_,m),u=+p,s||(s=u<n,s&&(p=new Date(n),u=+p,m=p.getUTCDate())),c||(c=u>r,c&&(p=new Date(r),u=+p,m=p.getUTCDate())),h=t.has(p.getUTCDay())||a.has(u);return p}({keyCode:t,maxTime:h,minTime:c,disabledDaysSet:r,disabledDatesSet:n,focusedDate:v(b,w,g)});return D}function S(e,t,a){return e.dispatchEvent(new CustomEvent(t,{detail:a,bubbles:!0,composed:!0}))}function $(e,t){return e.composedPath().find((e=>e instanceof HTMLElement&&t(e)))}function F(e){return t=>e.format(t).replace(/\u200e/gi,"")}function U(e){const t=i(e,{timeZone:"UTC",weekday:"short",month:"short",day:"numeric"}),a=i(e,{timeZone:"UTC",day:"numeric"}),r=i(e,{timeZone:"UTC",year:"numeric",month:"short",day:"numeric"}),n=i(e,{timeZone:"UTC",year:"numeric",month:"long"}),o=i(e,{timeZone:"UTC",weekday:"long"}),s=i(e,{timeZone:"UTC",weekday:"narrow"}),l=i(e,{timeZone:"UTC",year:"numeric"});return{locale:e,dateFormat:F(t),dayFormat:F(a),fullDateFormat:F(r),longMonthYearFormat:F(n),longWeekdayFormat:F(o),narrowWeekdayFormat:F(s),yearFormat:F(l)}}function N(e,t){const a=function(e,t){const a=t.getUTCFullYear(),i=t.getUTCMonth(),r=t.getUTCDate(),n=t.getUTCDay();let o=n;return"first-4-day-week"===e&&(o=3),"first-day-of-year"===e&&(o=6),"first-full-week"===e&&(o=0),v(a,i,r-n+o)}(e,t),i=v(a.getUTCFullYear(),0,1),r=1+(+a-+i)/864e5;return Math.ceil(r/7)}function M(e){if(e>=0&&e<7)return Math.abs(e);return((e<0?7*Math.ceil(Math.abs(e)):0)+e)%7}function E(e,t,a){const i=M(e-t);return a?1+i:i}function L(e){const{dayFormat:t,fullDateFormat:a,locale:i,longWeekdayFormat:r,narrowWeekdayFormat:n,selectedDate:o,disabledDates:s,disabledDays:l,firstDayOfWeek:d,max:c,min:h,showWeekNumber:u,weekLabel:p,weekNumberType:y}=e,_=null==h?Number.MIN_SAFE_INTEGER:+h,m=null==c?Number.MAX_SAFE_INTEGER:+c,f=function(e){const{firstDayOfWeek:t=0,showWeekNumber:a=!1,weekLabel:i,longWeekdayFormat:r,narrowWeekdayFormat:n}=e||{},o=1+(t+(t<0?7:0))%7,s=i||"Wk",l=a?[{label:"Wk"===s?"Week":s,value:s}]:[],d=Array.from(Array(7)).reduce(((e,t,a)=>{const i=v(2017,0,o+a);return e.push({label:r(i),value:n(i)}),e}),l);return d}({longWeekdayFormat:r,narrowWeekdayFormat:n,firstDayOfWeek:d,showWeekNumber:u,weekLabel:p}),b=e=>[i,e.toJSON(),null==s?void 0:s.join("_"),null==l?void 0:l.join("_"),d,null==c?void 0:c.toJSON(),null==h?void 0:h.toJSON(),u,p,y].filter(Boolean).join(":"),w=o.getUTCFullYear(),g=o.getUTCMonth(),k=[-1,0,1].map((e=>{const r=v(w,g+e,1),n=+v(w,g+e+1,0),o=b(r);if(n<_||+r>m)return{key:o,calendar:[],disabledDatesSet:new Set,disabledDaysSet:new Set};const f=function(e){const{date:t,dayFormat:a,disabledDates:i=[],disabledDays:r=[],firstDayOfWeek:n=0,fullDateFormat:o,locale:s="en-US",max:l,min:d,showWeekNumber:c=!1,weekLabel:h="Week",weekNumberType:u="first-4-day-week"}=e||{},p=M(n),y=t.getUTCFullYear(),_=t.getUTCMonth(),m=v(y,_,1),f=new Set(r.map((e=>E(e,p,c)))),b=new Set(i.map((e=>+e))),w=[m.toJSON(),p,s,null==l?"":l.toJSON(),null==d?"":d.toJSON(),Array.from(f).join(","),Array.from(b).join(","),u].filter(Boolean).join(":"),g=E(m.getUTCDay(),p,c),k=null==d?+new Date("2000-01-01"):+d,D=null==l?+new Date("2100-12-31"):+l,x=c?8:7,C=v(y,1+_,0).getUTCDate(),T=[];let S=[],$=!1,F=1;for(const e of[0,1,2,3,4,5]){for(const t of[0,1,2,3,4,5,6].concat(7===x?[]:[7])){const i=t+e*x;if(!$&&c&&0===t){const t=N(u,v(y,_,F-(e<1?p:0))),a=`${h} ${t}`;S.push({fullDate:null,label:a,value:`${t}`,key:`${w}:${a}`,disabled:!0});continue}if($||i<g){S.push({fullDate:null,label:"",value:"",key:`${w}:${i}`,disabled:!0});continue}const r=v(y,_,F),n=+r,s=f.has(t)||b.has(n)||n<k||n>D;s&&b.add(n),S.push({fullDate:r,label:o(r),value:a(r),key:`${w}:${r.toJSON()}`,disabled:s}),F+=1,F>C&&($=!0)}T.push(S),S=[]}return{disabledDatesSet:b,calendar:T,disabledDaysSet:new Set(r.map((e=>M(e)))),key:w}}({dayFormat:t,fullDateFormat:a,locale:i,disabledDates:s,disabledDays:l,firstDayOfWeek:d,max:c,min:h,showWeekNumber:u,weekLabel:p,weekNumberType:y,date:r});return{...f,key:o}})),D=[],x=new Set,C=new Set;for(const e of k){const{disabledDatesSet:t,disabledDaysSet:a,...i}=e;if(i.calendar.length>0){if(a.size>0)for(const e of a)C.add(e);if(t.size>0)for(const e of t)x.add(e)}D.push(i)}return{calendars:D,weekdays:f,disabledDatesSet:x,disabledDaysSet:C,key:b(o)}}function W(e){const t=null==e?new Date:new Date(e),a="string"==typeof e&&(/^\d{4}-\d{2}-\d{2}$/i.test(e)||/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}(Z|\+00:00|-00:00)$/i.test(e)),i="number"==typeof e&&e>0&&isFinite(e);let r=t.getFullYear(),n=t.getMonth(),o=t.getDate();return(a||i)&&(r=t.getUTCFullYear(),n=t.getUTCMonth(),o=t.getUTCDate()),v(r,n,o)}function Y(e,t){return e.classList.contains(t)}function O(e,t){return!(null==e||!(t instanceof Date)||isNaN(+t))}function V(e){return e-Math.floor(e)>0?+e.toFixed(3):e}function A(e){return{passive:!0,handleEvent:e}}function P(e,t){const a="string"==typeof e&&e.length>0?e.split(/,\s*/i):[];return a.length?"function"==typeof t?a.map(t):a:[]}function I(e){if(e instanceof Date&&!isNaN(+e)){const t=e.toJSON();return null==t?"":t.replace(/^(.+)T.+/i,"$1")}return""}function z(e,t){if(C(e,t)<864e5)return[];const a=e.getUTCFullYear();return Array.from(Array(t.getUTCFullYear()-a+1),((e,t)=>t+a))}function K(e,t,a){const i="number"==typeof e?e:+e,r=+t,n=+a;return i<r?r:i>n?n:e}var q,R,Z=a(2612);function j(e){const{clientX:t,clientY:a,pageX:i,pageY:r}=e,n=Math.max(i,t),o=Math.max(r,a),s=e.identifier||e.pointerId;return{x:n,y:o,id:null==s?0:s}}function B(e,t){const a=t.changedTouches;if(null==a)return{newPointer:j(t),oldPointer:e};const i=Array.from(a,(e=>j(e)));return{newPointer:null==e?i[0]:i.find((t=>t.id===e.id)),oldPointer:e}}function J(e,t,a){e.addEventListener(t,a,!!Z.Vq&&{passive:!0})}class X{constructor(e,t){this._element=e,this._startPointer=null;const{down:a,move:i,up:r}=t;this._down=this._onDown(a),this._move=this._onMove(i),this._up=this._onUp(r),e&&e.addEventListener&&(e.addEventListener("mousedown",this._down),J(e,"touchstart",this._down),J(e,"touchmove",this._move),J(e,"touchend",this._up))}disconnect(){const e=this._element;e&&e.removeEventListener&&(e.removeEventListener("mousedown",this._down),e.removeEventListener("touchstart",this._down),e.removeEventListener("touchmove",this._move),e.removeEventListener("touchend",this._up))}_onDown(e){return t=>{t instanceof MouseEvent&&(this._element.addEventListener("mousemove",this._move),this._element.addEventListener("mouseup",this._up),this._element.addEventListener("mouseleave",this._up));const{newPointer:a}=B(this._startPointer,t);e(a,t),this._startPointer=a}}_onMove(e){return t=>{this._updatePointers(e,t)}}_onUp(e){return t=>{this._updatePointers(e,t,!0)}}_updatePointers(e,t,a){a&&t instanceof MouseEvent&&(this._element.removeEventListener("mousemove",this._move),this._element.removeEventListener("mouseup",this._up),this._element.removeEventListener("mouseleave",this._up));const{newPointer:i,oldPointer:r}=B(this._startPointer,t);e(i,r,t),this._startPointer=a?null:i}}class H extends u.oi{constructor(){super(),this.firstDayOfWeek=0,this.showWeekNumber=!1,this.weekNumberType="first-4-day-week",this.landscape=!1,this.locale=i&&i().resolvedOptions&&i().resolvedOptions().locale||"en-US",this.disabledDays="",this.disabledDates="",this.weekLabel="Wk",this.inline=!1,this.dragRatio=.15,this._hasMin=!1,this._hasMax=!1,this._disabledDaysSet=new Set,this._disabledDatesSet=new Set,this._dx=-1/0,this._hasNativeWebAnimation="animate"in HTMLElement.prototype,this._updatingDateWithKey=!1;const e=W(),t=U(this.locale),a=I(e),r=W("2100-12-31");this.value=a,this.startView="calendar",this._min=new Date(e),this._max=new Date(r),this._todayDate=e,this._maxDate=r,this._yearList=z(e,r),this._selectedDate=new Date(e),this._focusedDate=new Date(e),this._formatters=t}get startView(){return this._startView}set startView(e){const t=e||"calendar";if("calendar"!==t&&"yearList"!==t)return;const a=this._startView;this._startView=t,this.requestUpdate("startView",a)}get min(){return this._hasMin?I(this._min):""}set min(e){const t=W(e),a=O(e,t);this._min=a?t:this._todayDate,this._hasMin=a,this.requestUpdate("min")}get max(){return this._hasMax?I(this._max):""}set max(e){const t=W(e),a=O(e,t);this._max=a?t:this._maxDate,this._hasMax=a,this.requestUpdate("max")}get value(){return I(this._focusedDate)}set value(e){const t=W(e),a=O(e,t)?t:this._todayDate;this._focusedDate=new Date(a),this._selectedDate=this._lastSelectedDate=new Date(a)}disconnectedCallback(){super.disconnectedCallback(),this._tracker&&(this._tracker.disconnect(),this._tracker=void 0)}render(){this._formatters.locale!==this.locale&&(this._formatters=U(this.locale));const e="yearList"===this._startView?this._renderDatepickerYearList():this._renderDatepickerCalendar(),t=this.inline?null:u.dy`<div class="datepicker-header" part="header">${this._renderHeaderSelectorButton()}</div>`;return u.dy`
    ${t}
    <div class="datepicker-body" part="body">${f(e)}</div>
    `}firstUpdated(){let e;e="calendar"===this._startView?this.inline?this.shadowRoot.querySelector(".btn__month-selector"):this._buttonSelectorYear:this._yearViewListItem,S(this,"datepicker-first-updated",{firstFocusableElement:e,value:this.value})}async updated(e){const t=this._startView;if(e.has("min")||e.has("max")){this._yearList=z(this._min,this._max),"yearList"===t&&this.requestUpdate();const e=+this._min,a=+this._max;if(C(e,a)>864e5){const t=+this._focusedDate;let i=t;t<e&&(i=e),t>a&&(i=a),this.value=I(new Date(i))}}if(e.has("_startView")||e.has("startView")){if("yearList"===t){const e=48*(this._selectedDate.getUTCFullYear()-this._min.getUTCFullYear()-2);!function(e,t){if(null==e.scrollTo){const{top:a,left:i}=t||{};e.scrollTop=a||0,e.scrollLeft=i||0}else e.scrollTo(t)}(this._yearViewFullList,{top:e,left:0})}if("calendar"===t&&null==this._tracker){const e=this.calendarsContainer;let t=!1,a=!1,i=!1;if(e){const r={down:()=>{i||(t=!0,this._dx=0)},move:(r,n)=>{if(i||!t)return;const o=this._dx,s=o<0&&Y(e,"has-max-date")||o>0&&Y(e,"has-min-date");!s&&Math.abs(o)>0&&t&&(a=!0,e.style.transform=`translateX(${V(o)}px)`),this._dx=s?0:o+(r.x-n.x)},up:async(r,n,o)=>{if(t&&a){const r=this._dx,n=e.getBoundingClientRect().width/3,o=Math.abs(r)>Number(this.dragRatio)*n,s=350,l="cubic-bezier(0, 0, .4, 1)",d=o?V(n*(r<0?-1:1)):0;i=!0,await async function(e,t){const{hasNativeWebAnimation:a=!1,keyframes:i=[],options:r={duration:100}}=t||{};if(Array.isArray(i)&&i.length)return new Promise((t=>{if(a)e.animate(i,r).onfinish=()=>t();else{const[,a]=i||[],n=()=>{e.removeEventListener("transitionend",n),t()};e.addEventListener("transitionend",n),e.style.transitionDuration=`${r.duration}ms`,r.easing&&(e.style.transitionTimingFunction=r.easing),Object.keys(a).forEach((t=>{t&&(e.style[t]=a[t])}))}}))}(e,{hasNativeWebAnimation:this._hasNativeWebAnimation,keyframes:[{transform:`translateX(${r}px)`},{transform:`translateX(${d}px)`}],options:{duration:s,easing:l}}),o&&this._updateMonth(r<0?"next":"previous").handleEvent(),t=a=i=!1,this._dx=-1/0,e.removeAttribute("style"),S(this,"datepicker-animation-finished")}else t&&(this._updateFocusedDate(o),t=a=!1,this._dx=-1/0)}};this._tracker=new X(e,r)}}e.get("_startView")&&"calendar"===t&&this._focusElement('[part="year-selector"]')}this._updatingDateWithKey&&(this._focusElement('[part="calendars"]:nth-of-type(2) .day--focused'),this._updatingDateWithKey=!1)}_focusElement(e){const t=this.shadowRoot.querySelector(e);t&&t.focus()}_renderHeaderSelectorButton(){const{yearFormat:e,dateFormat:t}=this._formatters,a="calendar"===this.startView,i=this._focusedDate,r=t(i),n=e(i);return u.dy`
    <button
      class="${(0,b.$)({"btn__year-selector":!0,selected:!a})}"
      type="button"
      part="year-selector"
      data-view="${"yearList"}"
      @click="${this._updateView("yearList")}">${n}</button>

    <div class="datepicker-toolbar" part="toolbar">
      <button
        class="${(0,b.$)({"btn__calendar-selector":!0,selected:a})}"
        type="button"
        part="calendar-selector"
        data-view="${"calendar"}"
        @click="${this._updateView("calendar")}">${r}</button>
    </div>
    `}_renderDatepickerYearList(){const{yearFormat:e}=this._formatters,t=this._focusedDate.getUTCFullYear();return u.dy`
    <div class="datepicker-body__year-list-view" part="year-list-view">
      <div class="year-list-view__full-list" part="year-list" @click="${this._updateYear}">
      ${this._yearList.map((a=>u.dy`<button
        class="${(0,b.$)({"year-list-view__list-item":!0,"year--selected":t===a})}"
        type="button"
        part="year"
        .year="${a}">${e(v(a,0,1))}</button>`))}</div>
    </div>
    `}_renderDatepickerCalendar(){const{longMonthYearFormat:e,dayFormat:t,fullDateFormat:a,longWeekdayFormat:i,narrowWeekdayFormat:r}=this._formatters,n=P(this.disabledDays,Number),o=P(this.disabledDates,W),s=this.showWeekNumber,l=this._focusedDate,d=this.firstDayOfWeek,c=W(),h=this._selectedDate,p=this._max,y=this._min,{calendars:_,disabledDaysSet:m,disabledDatesSet:f,weekdays:v}=L({dayFormat:t,fullDateFormat:a,longWeekdayFormat:i,narrowWeekdayFormat:r,firstDayOfWeek:d,disabledDays:n,disabledDates:o,locale:this.locale,selectedDate:h,showWeekNumber:this.showWeekNumber,weekNumberType:this.weekNumberType,max:p,min:y,weekLabel:this.weekLabel}),D=!_[0].calendar.length,x=!_[2].calendar.length,C=v.map((e=>u.dy`<th
        class="calendar-weekday"
        part="calendar-weekday"
        role="columnheader"
        aria-label="${e.label}"
      >
        <div class="weekday" part="weekday">${e.value}</div>
      </th>`)),S=(0,w.r)(_,(e=>e.key),(({calendar:t},a)=>{if(!t.length)return u.dy`<div class="calendar-container" part="calendar"></div>`;const i=`calendarcaption${a}`,r=t[1][1].fullDate,n=1===a,o=n&&!this._isInVisibleMonth(l,h)?T({disabledDaysSet:m,disabledDatesSet:f,hasAltKey:!1,keyCode:36,focusedDate:l,selectedDate:h,minTime:+y,maxTime:+p}):l;return u.dy`
      <div class="calendar-container" part="calendar">
        <table class="calendar-table" part="table" role="grid" aria-labelledby="${i}">
          <caption id="${i}">
            <div class="calendar-label" part="label">${r?e(r):""}</div>
          </caption>

          <thead role="rowgroup">
            <tr class="calendar-weekdays" part="weekdays" role="row">${C}</tr>
          </thead>

          <tbody role="rowgroup">${t.map((e=>u.dy`<tr role="row">${e.map(((e,t)=>{const{disabled:a,fullDate:i,label:r,value:d}=e;if(!i&&d&&s&&t<1)return u.dy`<th
                      class="full-calendar__day weekday-label"
                      part="calendar-day"
                      scope="row"
                      role="rowheader"
                      abbr="${r}"
                      aria-label="${r}"
                    >${d}</th>`;if(!d||!i)return u.dy`<td class="full-calendar__day day--empty" part="calendar-day"></td>`;const h=+new Date(i),p=+l===h,y=n&&o.getUTCDate()===Number(d);return u.dy`
                  <td
                    tabindex="${y?"0":"-1"}"
                    class="${(0,b.$)({"full-calendar__day":!0,"day--disabled":a,"day--today":+c===h,"day--focused":!a&&p})}"
                    part="calendar-day${+c===h?" calendar-today":""}"
                    role="gridcell"
                    aria-disabled="${a?"true":"false"}"
                    aria-label="${r}"
                    aria-selected="${p?"true":"false"}"
                    .fullDate="${i}"
                    .day="${d}"
                  >
                    <div
                      class="calendar-day"
                      part="day${+c===h?" today":""}"
                    >${d}</div>
                  </td>
                  `}))}</tr>`))}</tbody>
        </table>
      </div>
      `}));return this._disabledDatesSet=f,this._disabledDaysSet=m,u.dy`
    <div class="datepicker-body__calendar-view" part="calendar-view">
      <div class="calendar-view__month-selector" part="month-selectors">
        <div class="month-selector-container">${D?null:u.dy`
          <button
            class="btn__month-selector"
            type="button"
            part="month-selector"
            aria-label="Previous month"
            @click="${this._updateMonth("previous")}"
          >${g}</button>
        `}</div>

        <div class="month-selector-container">${x?null:u.dy`
          <button
            class="btn__month-selector"
            type="button"
            part="month-selector"
            aria-label="Next month"
            @click="${this._updateMonth("next")}"
          >${k}</button>
        `}</div>
      </div>

      <div
        class="${(0,b.$)({"calendars-container":!0,"has-min-date":D,"has-max-date":x})}"
        part="calendars"
        @keyup="${this._updateFocusedDateWithKeyboard}"
      >${S}</div>
    </div>
    `}_updateView(e){return A((()=>{"calendar"===e&&(this._selectedDate=this._lastSelectedDate=new Date(K(this._focusedDate,this._min,this._max))),this._startView=e}))}_updateMonth(e){return A((()=>{if(null==this.calendarsContainer)return this.updateComplete;const t=this._lastSelectedDate||this._selectedDate,a=this._min,i=this._max,r="previous"===e,n=v(t.getUTCFullYear(),t.getUTCMonth()+(r?-1:1),1),o=n.getUTCFullYear(),s=n.getUTCMonth(),l=a.getUTCFullYear(),d=a.getUTCMonth(),c=i.getUTCFullYear(),h=i.getUTCMonth();return o<l||o<=l&&s<d||(o>c||o>=c&&s>h)||(this._lastSelectedDate=n,this._selectedDate=this._lastSelectedDate),this.updateComplete}))}_updateYear(e){const t=$(e,(e=>Y(e,"year-list-view__list-item")));if(null==t)return;const a=K(new Date(this._focusedDate).setUTCFullYear(+t.year),this._min,this._max);this._selectedDate=this._lastSelectedDate=new Date(a),this._focusedDate=new Date(a),this._startView="calendar"}_updateFocusedDate(e){const t=$(e,(e=>Y(e,"full-calendar__day")));null==t||["day--empty","day--disabled","day--focused","weekday-label"].some((e=>Y(t,e)))||(this._focusedDate=new Date(t.fullDate),S(this,"datepicker-value-updated",{isKeypress:!1,value:this.value}))}_updateFocusedDateWithKeyboard(e){const t=e.keyCode;if(13===t||32===t)return S(this,"datepicker-value-updated",{keyCode:t,isKeypress:!0,value:this.value}),void(this._focusedDate=new Date(this._selectedDate));if(9===t||!c.has(t))return;const a=this._selectedDate,i=T({keyCode:t,selectedDate:a,disabledDatesSet:this._disabledDatesSet,disabledDaysSet:this._disabledDaysSet,focusedDate:this._focusedDate,hasAltKey:e.altKey,maxTime:+this._max,minTime:+this._min});this._isInVisibleMonth(i,a)||(this._selectedDate=this._lastSelectedDate=i),this._focusedDate=i,this._updatingDateWithKey=!0,S(this,"datepicker-value-updated",{keyCode:t,isKeypress:!0,value:this.value})}_isInVisibleMonth(e,t){const a=e.getUTCFullYear(),i=e.getUTCMonth(),r=t.getUTCFullYear(),n=t.getUTCMonth();return a===r&&i===n}get calendarsContainer(){return this.shadowRoot.querySelector(".calendars-container")}}H.styles=[x,D,u.iv`
    :host {
      width: 312px;
      /** NOTE: Magic number as 16:9 aspect ratio does not look good */
      /* height: calc((var(--app-datepicker-width) / .66) - var(--app-datepicker-footer-height, 56px)); */
      background-color: var(--app-datepicker-bg-color, #fff);
      color: var(--app-datepicker-color, #000);
      border-radius:
        var(--app-datepicker-border-top-left-radius, 0)
        var(--app-datepicker-border-top-right-radius, 0)
        var(--app-datepicker-border-bottom-right-radius, 0)
        var(--app-datepicker-border-bottom-left-radius, 0);
      contain: content;
      overflow: hidden;
    }
    :host([landscape]) {
      display: flex;

      /** <iphone-5-landscape-width> - <standard-side-margin-width> */
      min-width: calc(568px - 16px * 2);
      width: calc(568px - 16px * 2);
    }

    .datepicker-header + .datepicker-body {
      border-top: 1px solid var(--app-datepicker-separator-color, #ddd);
    }
    :host([landscape]) > .datepicker-header + .datepicker-body {
      border-top: none;
      border-left: 1px solid var(--app-datepicker-separator-color, #ddd);
    }

    .datepicker-header {
      display: flex;
      flex-direction: column;
      align-items: flex-start;

      position: relative;
      padding: 16px 24px;
    }
    :host([landscape]) > .datepicker-header {
      /** :this.<one-liner-month-day-width> + :this.<side-padding-width> */
      min-width: calc(14ch + 24px * 2);
    }

    .btn__year-selector,
    .btn__calendar-selector {
      color: var(--app-datepicker-selector-color, rgba(0, 0, 0, .55));
      cursor: pointer;
      /* outline: none; */
    }
    .btn__year-selector.selected,
    .btn__calendar-selector.selected {
      color: currentColor;
    }

    /**
      * NOTE: IE11-only fix. This prevents formatted focused date from overflowing the container.
      */
    .datepicker-toolbar {
      width: 100%;
    }

    .btn__year-selector {
      font-size: 16px;
      font-weight: 700;
    }
    .btn__calendar-selector {
      font-size: 36px;
      font-weight: 700;
      line-height: 1;
    }

    .datepicker-body {
      position: relative;
      width: 100%;
      overflow: hidden;
    }

    .datepicker-body__calendar-view {
      min-height: 56px;
    }

    .calendar-view__month-selector {
      display: flex;
      align-items: center;

      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      padding: 0 8px;
      z-index: 1;
    }

    .month-selector-container {
      max-height: 56px;
      height: 100%;
    }
    .month-selector-container + .month-selector-container {
      margin: 0 0 0 auto;
    }

    .btn__month-selector {
      padding: calc((56px - 24px) / 2);
      /**
        * NOTE: button element contains no text, only SVG.
        * No extra height will incur with such setting.
        */
      line-height: 0;
    }
    .btn__month-selector > svg {
      fill: currentColor;
    }

    .calendars-container {
      display: flex;
      justify-content: center;

      position: relative;
      top: 0;
      left: calc(-100%);
      width: calc(100% * 3);
      transform: translateZ(0);
      will-change: transform;
      /**
        * NOTE: Required for Pointer Events API to work on touch devices.
        * Native \`pan-y\` action will be fired by the browsers since we only care about the
        * horizontal direction. This is great as vertical scrolling still works even when touch
        * event happens on a datepicker's calendar.
        */
      touch-action: pan-y;
      /* outline: none; */
    }

    .year-list-view__full-list {
      max-height: calc(48px * 7);
      overflow-y: auto;

      scrollbar-color: var(--app-datepicker-scrollbar-thumb-bg-color, rgba(0, 0, 0, .35)) rgba(0, 0, 0, 0);
      scrollbar-width: thin;
    }
    .year-list-view__full-list::-webkit-scrollbar {
      width: 8px;
      background-color: rgba(0, 0, 0, 0);
    }
    .year-list-view__full-list::-webkit-scrollbar-thumb {
      background-color: var(--app-datepicker-scrollbar-thumb-bg-color, rgba(0, 0, 0, .35));
      border-radius: 50px;
    }
    .year-list-view__full-list::-webkit-scrollbar-thumb:hover {
      background-color: var(--app-datepicker-scrollbar-thumb-hover-bg-color, rgba(0, 0, 0, .5));
    }

    .calendar-weekdays > th,
    .weekday-label {
      color: var(--app-datepicker-weekday-color, rgba(0, 0, 0, .55));
      font-weight: 400;
      transform: translateZ(0);
      will-change: transform;
    }

    .calendar-container,
    .calendar-label,
    .calendar-table {
      width: 100%;
    }

    .calendar-container {
      position: relative;
      padding: 0 16px 16px;
    }

    .calendar-table {
      -moz-user-select: none;
      -webkit-user-select: none;
      user-select: none;

      border-collapse: collapse;
      border-spacing: 0;
      text-align: center;
    }

    .calendar-label {
      display: flex;
      align-items: center;
      justify-content: center;

      height: 56px;
      font-weight: 500;
      text-align: center;
    }

    .calendar-weekday,
    .full-calendar__day {
      position: relative;
      width: calc(100% / 7);
      height: 0;
      padding: calc(100% / 7 / 2) 0;
      outline: none;
      text-align: center;
    }
    .full-calendar__day:not(.day--disabled):focus {
      outline: #000 dotted 1px;
      outline: -webkit-focus-ring-color auto 1px;
    }
    :host([showweeknumber]) .calendar-weekday,
    :host([showweeknumber]) .full-calendar__day {
      width: calc(100% / 8);
      padding-top: calc(100% / 8);
      padding-bottom: 0;
    }
    :host([showweeknumber]) th.weekday-label {
      padding: 0;
    }

    /**
      * NOTE: Interesting fact! That is ::after will trigger paint when dragging. This will trigger
      * layout and paint on **ONLY** affected nodes. This is much cheaper as compared to rendering
      * all :::after of all calendar day elements. When dragging the entire calendar container,
      * because of all layout and paint trigger on each and every ::after, this becomes a expensive
      * task for the browsers especially on low-end devices. Even though animating opacity is much
      * cheaper, the technique does not work here. Adding 'will-change' will further reduce overall
      * painting at the expense of memory consumption as many cells in a table has been promoted
      * a its own layer.
      */
    .full-calendar__day:not(.day--empty):not(.day--disabled):not(.weekday-label) {
      transform: translateZ(0);
      will-change: transform;
    }
    .full-calendar__day:not(.day--empty):not(.day--disabled):not(.weekday-label).day--focused::after,
    .full-calendar__day:not(.day--empty):not(.day--disabled):not(.day--focused):not(.weekday-label):hover::after {
      content: '';
      display: block;
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: var(--app-datepicker-accent-color, #1a73e8);
      border-radius: 50%;
      opacity: 0;
      pointer-events: none;
    }
    .full-calendar__day:not(.day--empty):not(.day--disabled):not(.weekday-label) {
      cursor: pointer;
      pointer-events: auto;
      -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    }
    .full-calendar__day.day--focused:not(.day--empty):not(.day--disabled):not(.weekday-label)::after,
    .full-calendar__day.day--today.day--focused:not(.day--empty):not(.day--disabled):not(.weekday-label)::after {
      opacity: 1;
    }

    .calendar-weekday > .weekday,
    .full-calendar__day > .calendar-day {
      display: flex;
      align-items: center;
      justify-content: center;

      position: absolute;
      top: 5%;
      left: 5%;
      width: 90%;
      height: 90%;
      color: currentColor;
      font-size: 14px;
      pointer-events: none;
      z-index: 1;
    }
    .full-calendar__day.day--today {
      color: var(--app-datepicker-accent-color, #1a73e8);
    }
    .full-calendar__day.day--focused,
    .full-calendar__day.day--today.day--focused {
      color: var(--app-datepicker-focused-day-color, #fff);
    }
    .full-calendar__day.day--empty,
    .full-calendar__day.weekday-label,
    .full-calendar__day.day--disabled > .calendar-day {
      pointer-events: none;
    }
    .full-calendar__day.day--disabled:not(.day--today) {
      color: var(--app-datepicker-disabled-day-color, rgba(0, 0, 0, .55));
    }

    .year-list-view__list-item {
      position: relative;
      width: 100%;
      padding: 12px 16px;
      text-align: center;
      /** NOTE: Reduce paint when hovering and scrolling, but this increases memory usage */
      /* will-change: opacity; */
      /* outline: none; */
    }
    .year-list-view__list-item::after {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: var(--app-datepicker-focused-year-bg-color, #000);
      opacity: 0;
      pointer-events: none;
    }
    .year-list-view__list-item:focus::after {
      opacity: .05;
    }
    .year-list-view__list-item.year--selected {
      color: var(--app-datepicker-accent-color, #1a73e8);
      font-size: 24px;
      font-weight: 500;
    }

    @media (any-hover: hover) {
      .btn__month-selector:hover,
      .year-list-view__list-item:hover {
        cursor: pointer;
      }
      .full-calendar__day:not(.day--empty):not(.day--disabled):not(.day--focused):not(.weekday-label):hover::after {
        opacity: .15;
      }
      .year-list-view__list-item:hover::after {
        opacity: .05;
      }
    }

    @supports (background: -webkit-canvas(squares)) {
      .calendar-container {
        padding: 56px 16px 16px;
      }

      table > caption {
        position: absolute;
        top: 0;
        left: 50%;
        transform: translate3d(-50%, 0, 0);
        will-change: transform;
      }
    }
    `],(0,h.__decorate)([(0,p.Cb)({type:Number,reflect:!0})],H.prototype,"firstDayOfWeek",void 0),(0,h.__decorate)([(0,p.Cb)({type:Boolean,reflect:!0})],H.prototype,"showWeekNumber",void 0),(0,h.__decorate)([(0,p.Cb)({type:String,reflect:!0})],H.prototype,"weekNumberType",void 0),(0,h.__decorate)([(0,p.Cb)({type:Boolean,reflect:!0})],H.prototype,"landscape",void 0),(0,h.__decorate)([(0,p.Cb)({type:String,reflect:!0})],H.prototype,"startView",null),(0,h.__decorate)([(0,p.Cb)({type:String,reflect:!0})],H.prototype,"min",null),(0,h.__decorate)([(0,p.Cb)({type:String,reflect:!0})],H.prototype,"max",null),(0,h.__decorate)([(0,p.Cb)({type:String})],H.prototype,"value",null),(0,h.__decorate)([(0,p.Cb)({type:String})],H.prototype,"locale",void 0),(0,h.__decorate)([(0,p.Cb)({type:String})],H.prototype,"disabledDays",void 0),(0,h.__decorate)([(0,p.Cb)({type:String})],H.prototype,"disabledDates",void 0),(0,h.__decorate)([(0,p.Cb)({type:String})],H.prototype,"weekLabel",void 0),(0,h.__decorate)([(0,p.Cb)({type:Boolean})],H.prototype,"inline",void 0),(0,h.__decorate)([(0,p.Cb)({type:Number})],H.prototype,"dragRatio",void 0),(0,h.__decorate)([(0,p.Cb)({type:Date,attribute:!1})],H.prototype,"_selectedDate",void 0),(0,h.__decorate)([(0,p.Cb)({type:Date,attribute:!1})],H.prototype,"_focusedDate",void 0),(0,h.__decorate)([(0,p.Cb)({type:String,attribute:!1})],H.prototype,"_startView",void 0),(0,h.__decorate)([(0,p.IO)(".year-list-view__full-list")],H.prototype,"_yearViewFullList",void 0),(0,h.__decorate)([(0,p.IO)(".btn__year-selector")],H.prototype,"_buttonSelectorYear",void 0),(0,h.__decorate)([(0,p.IO)(".year-list-view__list-item")],H.prototype,"_yearViewListItem",void 0),(0,h.__decorate)([(0,p.hO)({passive:!0})],H.prototype,"_updateYear",null),(0,h.__decorate)([(0,p.hO)({passive:!0})],H.prototype,"_updateFocusedDateWithKeyboard",null),q="app-datepicker",R=H,window.customElements&&!window.customElements.get(q)&&window.customElements.define(q,R)}}]);
//# sourceMappingURL=22011c56.js.map