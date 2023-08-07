import{_ as o,d as e,w as s,n as i,y as t}from"./c.998383f4.js";import"./c.79283163.js";import"./c.5b9dec44.js";import"./c.abbbe9de.js";let a=class extends i{render(){return t`
      <esphome-process-dialog
        .heading=${`Clean MQTT discovery topics for ${this.configuration}`}
        .type=${"clean-mqtt"}
        .spawnParams=${{configuration:this.configuration}}
        @closed=${this._handleClose}
      >
      </esphome-process-dialog>
    `}_handleClose(){this.parentNode.removeChild(this)}};o([e()],a.prototype,"configuration",void 0),a=o([s("esphome-clean-mqtt-dialog")],a);
