import{a3 as e,v as t,_ as a,d as o,a as r,h as s,w as i,n,y as l}from"./c.998383f4.js";import"./c.a0dcba7a.js";import"./c.5b9dec44.js";const c=()=>import("./c.b43ad2de.js");let m=class extends n{constructor(){super(...arguments),this._cleanNameInput=e=>{this._error=void 0;const t=e.target;t.value=t.value.toLowerCase().replace(/[ \._]/g,"-").replace(/[^a-z0-9-]/g,"")},this._cleanNameBlur=e=>{const t=e.target;t.value=t.value.replace(/^-+/,"").replace(/-+$/,"")}}render(){return l`
      <mwc-dialog
        open
        heading=${`Rename ${this.configuration}`}
        scrimClickAction
        @closed=${this._handleClose}
      >
        ${this._error?l`<div class="error">${this._error}</div>`:""}

        <mwc-textfield
          label="New Name"
          name="name"
          required
          dialogInitialFocus
          spellcheck="false"
          pattern="^[a-z0-9-]+$"
          helper="Lowercase letters (a-z), numbers (0-9) or dash (-)"
          @input=${this._cleanNameInput}
          @blur=${this._cleanNameBlur}
        ></mwc-textfield>

        <mwc-button
          no-attention
          slot="secondaryAction"
          dialogAction="close"
          label="Close"
        ></mwc-button>
        <mwc-button
          slot="primaryAction"
          label="Rename"
          @click=${this._handleRename}
        ></mwc-button>
      </mwc-dialog>
    `}firstUpdated(e){super.firstUpdated(e);this._inputName.value=this.suggestedName}async _handleRename(e){c();const t=this._inputName;if(!t.reportValidity())return void t.focus();const a=t.value;a!==this.suggestedName&&((e,t)=>{c();const a=document.createElement("esphome-rename-process-dialog");a.configuration=e,a.newName=t,document.body.append(a)})(this.configuration,a),this.shadowRoot.querySelector("mwc-dialog").close()}_handleClose(){this.parentNode.removeChild(this)}};m.styles=[e,t`
      .error {
        color: var(--alert-error-color);
        margin-bottom: 16px;
      }
    `],a([o()],m.prototype,"configuration",void 0),a([r()],m.prototype,"_error",void 0),a([s("mwc-textfield[name=name]")],m.prototype,"_inputName",void 0),m=a([i("esphome-rename-dialog")],m);
