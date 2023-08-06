import{n as t,y as e,ad as i,a1 as r,a3 as s,v as o,_ as a,d as n,a as l,w as c}from"./c.998383f4.js";import"./c.5b9dec44.js";import"./c.e246cdf3.js";import{f as d,g as p}from"./c.bc777be6.js";import{o as h,a as g}from"./c.d6b2a450.js";import{c as _}from"./c.d3b09e82.js";import"./c.fa668126.js";import"./c.b3d7125b.js";let m=class extends t{constructor(){super(...arguments),this._state="connecting_webserial"}render(){let t,i=!1;return"connecting_webserial"===this._state?(t=this._renderProgress("Connecting"),i=!0):"prepare_installation"===this._state?(t=this._renderProgress("Preparing installation"),i=!0):"installing"===this._state?(t=void 0===this._writeProgress?this._renderProgress("Erasing"):this._renderProgress(e`
                Installing<br /><br />
                This will take
                ${"ESP8266"===this._platform?"a minute":"2 minutes"}.<br />
                Keep this page visible to prevent slow down
              `,this._writeProgress>3?this._writeProgress:void 0),i=!0):"done"===this._state&&(t=this._error?t=e`
          ${this._renderMessage("👀",this._error,!1)}
          <mwc-button
            slot="secondaryAction"
            dialogAction="ok"
            label="Close"
          ></mwc-button>
          <mwc-button
            slot="primaryAction"
            label="Retry"
            @click=${this._handleRetry}
          ></mwc-button>
        `:this._renderMessage("🎉","Configuration installed!",!0)),e`
      <mwc-dialog
        open
        heading=${undefined}
        scrimClickAction
        @closed=${this._handleClose}
        .hideActions=${i}
      >
        ${t}
      </mwc-dialog>
    `}_renderProgress(t,i){return e`
      <div class="center">
        <div>
          <mwc-circular-progress
            active
            ?indeterminate=${void 0===i}
            .progress=${void 0!==i?i/100:void 0}
            density="8"
          ></mwc-circular-progress>
          ${void 0!==i?e`<div class="progress-pct">${i}%</div>`:""}
        </div>
        ${t}
      </div>
    `}_renderMessage(t,i,r){return e`
      <div class="center">
        <div class="icon">${t}</div>
        ${i}
      </div>
      ${r?e`
            <mwc-button
              slot="primaryAction"
              dialogAction="ok"
              label="Close"
            ></mwc-button>
          `:""}
    `}firstUpdated(t){super.firstUpdated(t),this._handleInstall()}_openCompileDialog(){h(this.params.configuration,!1),this._close()}_handleRetry(){g(this.params,(()=>this._close()))}async _handleInstall(){const t=this.esploader;t.port.addEventListener("disconnect",(async()=>{this._state="done",this._error="Device disconnected",this.params.port||await t.port.close()}));try{try{await t.initialize()}catch(t){return console.error(t),this._state="done",void(this._error="Failed to initialize. Try resetting your device or holding the BOOT button while selecting your serial port until it starts preparing the installation.")}this._platform=_[t.chipFamily];const e=this.params.filesCallback||(t=>this._getFilesForConfiguration(this.params.configuration,t));let i=[];try{i=await e(this._platform)}catch(t){return this._state="done",void(this._error=String(t))}if(!i)return;this._state="installing";try{await d(t,i,!0===this.params.erase,(t=>{this._writeProgress=t}))}catch(t){return void("done"!==this._state&&(this._error=`Installation failed: ${t}`,this._state="done"))}await t.hardReset(),this._state="done"}finally{if(t.connected&&(console.log("Disconnecting esp"),await t.disconnect()),!this.params.port){console.log("Closing port");try{await t.port.close()}catch(t){}}}}async _getFilesForConfiguration(t,s){let o;try{o=await i(t)}catch(t){return this._state="done",void(this._error="Error fetching configuration information")}if(s!==o.esp_platform.toUpperCase())return this._state="done",void(this._error=`Configuration does not match the platform of the connected device. Expected an ${o.esp_platform.toUpperCase()} device.`);this._state="prepare_installation";try{await r(t)}catch(t){return this._error=e`
        Failed to prepare configuration<br /><br />
        <button class="link" @click=${this._openCompileDialog}>
          See what went wrong.
        </button>
      `,void(this._state="done")}return"done"!==this._state?await p(t):void 0}_close(){this.shadowRoot.querySelector("mwc-dialog").close()}async _handleClose(){this.params.onClose&&this.params.onClose("done"===this._state&&void 0===this._error),this.parentNode.removeChild(this)}};m.styles=[s,o`
      mwc-list-item {
        margin: 0 -20px;
      }
      svg {
        fill: currentColor;
      }
      .center {
        text-align: center;
      }
      mwc-circular-progress {
        margin-bottom: 16px;
      }
      .progress-pct {
        position: absolute;
        top: 50px;
        left: 0;
        right: 0;
      }
      .icon {
        font-size: 50px;
        line-height: 80px;
        color: black;
      }
      .show-ports {
        margin-top: 16px;
      }
      .error {
        padding: 8px 24px;
        background-color: #fff59d;
        margin: 0 -24px;
      }
    `],a([n()],m.prototype,"params",void 0),a([n()],m.prototype,"esploader",void 0),a([l()],m.prototype,"_writeProgress",void 0),a([l()],m.prototype,"_state",void 0),a([l()],m.prototype,"_error",void 0),m=a([c("esphome-install-web-dialog")],m);export{m as ESPHomeInstallWebDialog};
