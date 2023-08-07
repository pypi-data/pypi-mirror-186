import{_ as t,a as s,w as e,n as a,y as i,H as o,v as r}from"./c.998383f4.js";import"./c.5b9dec44.js";let l=class extends a{async showDialog(t,s){this._params=t,this._resolve=s}render(){return this._params?i`
      <mwc-dialog
        .heading=${this._params.title||""}
        @closed=${this._handleClose}
        open
      >
        ${this._params.text?i`<div>${this._params.text}</div>`:""}
        <mwc-button
          slot="secondaryAction"
          no-attention
          .label=${this._params.dismissText||"Cancel"}
          dialogAction="dismiss"
        ></mwc-button>
        <mwc-button
          slot="primaryAction"
          .label=${this._params.confirmText||"Yes"}
          class=${o({destructive:this._params.destructive||!1})}
          dialogAction="confirm"
        ></mwc-button>
      </mwc-dialog>
    `:i``}_handleClose(t){this._resolve("confirm"===t.detail.action),this.parentNode.removeChild(this)}static get styles(){return r`
      .destructive {
        --mdc-theme-primary: var(--alert-error-color);
      }
    `}};t([s()],l.prototype,"_params",void 0),t([s()],l.prototype,"_resolve",void 0),l=t([e("esphome-confirmation-dialog")],l);
