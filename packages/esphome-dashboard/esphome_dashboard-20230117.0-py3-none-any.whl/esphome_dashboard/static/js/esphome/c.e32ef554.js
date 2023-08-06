import{v as o,_ as t,d as e,a as i,w as s,n as r,y as a,a6 as n}from"./c.998383f4.js";import"./c.79283163.js";import{o as c}from"./c.d6b2a450.js";import"./c.5b9dec44.js";import"./c.abbbe9de.js";import"./c.fa668126.js";import"./c.e246cdf3.js";import"./c.d3b09e82.js";import"./c.b3d7125b.js";let d=class extends r{constructor(){super(...arguments),this.downloadFactoryFirmware=!0}render(){return a`
      <esphome-process-dialog
        .heading=${`Download ${this.configuration}`}
        .type=${"compile"}
        .spawnParams=${{configuration:this.configuration}}
        @closed=${this._handleClose}
        @process-done=${this._handleProcessDone}
      >
        ${void 0===this._result?"":0===this._result?a`
              <a
                slot="secondaryAction"
                href="${n(this.configuration,this.downloadFactoryFirmware)}"
              >
                <mwc-button label="Download"></mwc-button>
              </a>
            `:a`
              <mwc-button
                slot="secondaryAction"
                dialogAction="close"
                label="Retry"
                @click=${this._handleRetry}
              ></mwc-button>
            `}
      </esphome-process-dialog>
    `}_handleProcessDone(o){if(this._result=o.detail,0!==o.detail)return;const t=document.createElement("a");t.download=this.configuration+".bin",t.href=n(this.configuration,this.downloadFactoryFirmware),document.body.appendChild(t),t.click(),t.remove()}_handleRetry(){c(this.configuration,this.downloadFactoryFirmware)}_handleClose(){this.parentNode.removeChild(this)}};d.styles=o`
    a {
      text-decoration: none;
    }
  `,t([e()],d.prototype,"configuration",void 0),t([e()],d.prototype,"downloadFactoryFirmware",void 0),t([i()],d.prototype,"_result",void 0),d=t([s("esphome-compile-dialog")],d);
