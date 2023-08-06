import{a3 as t,v as e,_ as i,d as s,a as o,h as a,w as r,n,y as d}from"./c.998383f4.js";import"./c.5b9dec44.js";import"./c.a0dcba7a.js";import{f as l}from"./c.abbbe9de.js";import{i as c}from"./index-5f0ec3b8.js";import{c as h,s as p}from"./c.f5e9b64a.js";import{o as m}from"./c.b3d7125b.js";import"./c.bc0ca5c5.js";let u=class extends n{constructor(){super(...arguments),this._state="ask",this._busy=!1,this._cleanSSIDBlur=t=>{const e=t.target;e.value=e.value.trim()}}render(){let t,e;return"ask"===this._state?(t="Adopt device",e=d`
        <div>
          Adopting ${this.device.friendly_name||this.device.name} will create
          an ESPHome configuration for this device. This allows you to install
          updates and customize the original firmware.
        </div>

        ${this._error?d`<div class="error">${this._error}</div>`:""}
        ${this.device.friendly_name?d`
              <mwc-textfield
                label="New Name"
                name="name"
                required
                dialogInitialFocus
              ></mwc-textfield>
            `:""}
        ${this._needsWifiSecrets?!1!==this._hasWifiSecrets?d`
              <div>
                This device will be configured to connect to the Wi-Fi network
                stored in your secrets.
              </div>
            `:d`
              <div>
                Enter the credentials of the Wi-Fi network that you want your
                device to connect to.
              </div>
              <div>
                This information will be stored in your secrets and used for
                this and future devices. You can edit the information later by
                editing your secrets at the top of the page.
              </div>

              <mwc-textfield
                label="Network name"
                name="ssid"
                required
                @blur=${this._cleanSSIDBlur}
                .disabled=${this._busy}
              ></mwc-textfield>

              <mwc-textfield
                label="Password"
                name="password"
                type="password"
                helper="Leave blank if no password"
                .disabled=${this._busy}
              ></mwc-textfield>
            `:""}

        <mwc-button
          slot="primaryAction"
          .label=${this._busy?"Adopting…":"Adopt"}
          @click=${this._handleAdopt}
          .disabled=${this._needsWifiSecrets&&void 0===this._hasWifiSecrets}
        ></mwc-button>
        ${this._busy?"":d`
              <mwc-button
                no-attention
                slot="secondaryAction"
                label="Cancel"
                dialogAction="cancel"
              ></mwc-button>
            `}
      `):"adopted"===this._state?(t="Configuration created",e=d`
        <div>
          To finish adoption of ${this._nameOverride||this.device.name}, the
          new configuration needs to be installed on the device.
        </div>

        <mwc-button
          slot="primaryAction"
          label="Install"
          @click=${this._handleInstall}
        ></mwc-button>
        <mwc-button
          slot="secondaryAction"
          no-attention
          label="skip"
          @click=${()=>{this._state="skipped"}}
        ></mwc-button>
      `):"skipped"===this._state&&(t="Installation skipped",e=d`
        <div>
          You will be able to install the configuration at a later point from
          the three-dot menu on the device card.
        </div>
        <mwc-button
          slot="primaryAction"
          dialogAction="close"
          label="Close"
        ></mwc-button>
        <mwc-button
          slot="secondaryAction"
          no-attention
          label="back"
          @click=${()=>{this._state="adopted"}}
        ></mwc-button>
      `),d`
      <mwc-dialog .heading=${t} @closed=${this._handleClose} open>
        ${e}
      </mwc-dialog>
    `}firstUpdated(t){super.firstUpdated(t),this._needsWifiSecrets&&h().then((t=>{this._hasWifiSecrets=t}))}updated(t){if(super.updated(t),t.has("_state")&&"ask"===this._state&&this.device.friendly_name){const t=this._inputName;t.value=this.device.friendly_name,t.updateComplete.then((()=>t.focus()))}}get _needsWifiSecrets(){return"wifi"===this.device.network}_handleClose(){this.parentNode.removeChild(this)}async _handleAdopt(){this._error=void 0;const t=!!this.device.friendly_name,e=this._needsWifiSecrets&&!1===this._hasWifiSecrets,i=!t||this._inputName.reportValidity(),s=!e||this._inputSSID.reportValidity();if(i)if(s){if(e){this._busy=!0;try{await p(this._inputSSID.value,this._inputPassword.value)}catch(t){return console.error(t),this._busy=!1,void(this._error="Failed to store Wi-Fi credentials")}}this._busy=!0;try{let e=this.device;t&&(e={...e,friendly_name:this._inputName.value},this._nameOverride=e.friendly_name);const i=await c(e);this._configFilename=i.configuration,l(this,"adopted"),this._state="adopted"}catch(t){this._busy=!1,this._error="Failed to import device"}}else this._inputSSID.focus();else this._inputName.focus()}async _handleInstall(){m(this._configFilename,"OTA"),this.shadowRoot.querySelector("mwc-dialog").close()}};u.styles=[t,e`
      :host {
        --mdc-dialog-max-width: 390px;
      }
      .error {
        color: var(--alert-error-color);
        margin-bottom: 16px;
      }
    `],i([s()],u.prototype,"device",void 0),i([o()],u.prototype,"_hasWifiSecrets",void 0),i([o()],u.prototype,"_state",void 0),i([o()],u.prototype,"_busy",void 0),i([o()],u.prototype,"_error",void 0),i([a("mwc-textfield[name=ssid]")],u.prototype,"_inputSSID",void 0),i([a("mwc-textfield[name=password]")],u.prototype,"_inputPassword",void 0),i([a("mwc-textfield[name=name]")],u.prototype,"_inputName",void 0),u=i([r("esphome-adopt-dialog")],u);
