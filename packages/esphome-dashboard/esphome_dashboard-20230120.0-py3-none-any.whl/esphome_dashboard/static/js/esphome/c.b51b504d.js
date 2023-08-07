import{_ as e,d as t,w as o,n as a,y as i,a2 as n,v as l}from"./c.998383f4.js";import"./c.5b9dec44.js";import{f as s}from"./c.abbbe9de.js";let r=class extends a{render(){return i`
      <mwc-dialog
        .heading=${`Delete ${this.name}`}
        @closed=${this._handleClose}
        open
      >
        <div>Are you sure you want to delete ${this.name}?</div>
        <mwc-button
          slot="primaryAction"
          class="warning"
          label="Delete"
          dialogAction="close"
          @click=${this._handleDelete}
        ></mwc-button>
        <mwc-button
          slot="secondaryAction"
          no-attention
          label="Cancel"
          dialogAction="cancel"
        ></mwc-button>
      </mwc-dialog>
    `}_handleClose(){this.parentNode.removeChild(this)}async _handleDelete(){await n(this.configuration),s(this,"deleted")}static get styles(){return l`
      .warning {
        --mdc-theme-primary: var(--alert-error-color);
      }
    `}};e([t()],r.prototype,"name",void 0),e([t()],r.prototype,"configuration",void 0),r=e([o("esphome-delete-device-dialog")],r);
