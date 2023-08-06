import{v as o,_ as t,d as e,h as n,a as s,w as i,n as c,y as a,ad as r}from"./c.998383f4.js";import"./c.5b9dec44.js";import{c as l,C as d,b as h}from"./c.79283163.js";import{s as p}from"./c.a6e96e5a.js";import{t as u}from"./c.abbbe9de.js";import{o as g}from"./c.bc0ca5c5.js";class m{constructor(){this.chunks=""}transform(o,t){this.chunks+=o;const e=this.chunks.split("\r\n");this.chunks=e.pop(),e.forEach((o=>t.enqueue(o+"\r\n")))}flush(o){o.enqueue(this.chunks)}}class w extends HTMLElement{constructor(){super(...arguments),this.allowInput=!0}logs(){var o;return(null===(o=this._console)||void 0===o?void 0:o.logs())||""}connectedCallback(){if(this._console)return;if(this.attachShadow({mode:"open"}).innerHTML=`\n      <style>\n        :host, input {\n          background-color: #1c1c1c;\n          color: #ddd;\n          font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier,\n            monospace;\n          line-height: 1.45;\n          display: flex;\n          flex-direction: column;\n        }\n        form {\n          display: flex;\n          align-items: center;\n          padding: 0 8px 0 16px;\n        }\n        input {\n          flex: 1;\n          padding: 4px;\n          margin: 0 8px;\n          border: 0;\n          outline: none;\n        }\n        ${l}\n      </style>\n      <div class="log"></div>\n      ${this.allowInput?"<form>\n                >\n                <input autofocus>\n              </form>\n            ":""}\n    `,this._console=new d(this.shadowRoot.querySelector("div")),this.allowInput){const o=this.shadowRoot.querySelector("input");this.addEventListener("click",(()=>{var t;""===(null===(t=getSelection())||void 0===t?void 0:t.toString())&&o.focus()})),o.addEventListener("keydown",(o=>{"Enter"===o.key&&(o.preventDefault(),o.stopPropagation(),this._sendCommand())}))}const o=new AbortController,t=this._connect(o.signal);this._cancelConnection=()=>(o.abort(),t)}async _connect(o){this.logger.debug("Starting console read loop");try{await this.port.readable.pipeThrough(new TextDecoderStream,{signal:o}).pipeThrough(new TransformStream(new m)).pipeTo(new WritableStream({write:o=>{this._console.addLine(o.replace("\r",""))}})),o.aborted||(this._console.addLine(""),this._console.addLine(""),this._console.addLine("Terminal disconnected"))}catch(o){this._console.addLine(""),this._console.addLine(""),this._console.addLine(`Terminal disconnected: ${o}`)}finally{await p(100),this.logger.debug("Finished console read loop")}}async _sendCommand(){const o=this.shadowRoot.querySelector("input"),t=o.value,e=new TextEncoder,n=this.port.writable.getWriter();await n.write(e.encode(t+"\r\n")),this._console.addLine(`> ${t}\r\n`),o.value="",o.focus();try{n.releaseLock()}catch(o){console.error("Ignoring release lock error",o)}}async disconnect(){this._cancelConnection&&(await this._cancelConnection(),this._cancelConnection=void 0)}async reset(){this.logger.debug("Triggering reset."),await this.port.setSignals({dataTerminalReady:!1,requestToSend:!0}),await this.port.setSignals({dataTerminalReady:!1,requestToSend:!1}),await new Promise((o=>setTimeout(o,1e3)))}}customElements.define("ewt-console",w);let f=class extends c{constructor(){super(...arguments),this._isPico=!1}render(){return a`
      <mwc-dialog
        open
        .heading=${this.configuration?`Logs ${this.configuration}`:"Logs"}
        scrimClickAction
        @closed=${this._handleClose}
      >
        <ewt-console
          .port=${this.port}
          .logger=${console}
          .allowInput=${!1}
        ></ewt-console>
        <mwc-button
          slot="secondaryAction"
          label="Download Logs"
          @click=${this._downloadLogs}
        ></mwc-button>
        ${this.configuration?a`
              <mwc-button
                slot="secondaryAction"
                dialogAction="close"
                label="Edit"
                @click=${this._openEdit}
              ></mwc-button>
            `:""}
        ${this._isPico?"":a`
              <mwc-button
                slot="secondaryAction"
                label="Reset Device"
                @click=${this._resetDevice}
              ></mwc-button>
            `}
        <mwc-button
          slot="primaryAction"
          dialogAction="close"
          label="Close"
        ></mwc-button>
      </mwc-dialog>
    `}firstUpdated(o){super.firstUpdated(o),this.configuration&&r(this.configuration).then((o=>{this._isPico="RP2040"===o.esp_platform}))}async _openEdit(){this.configuration&&g(this.configuration)}async _handleClose(){await this._console.disconnect(),this.closePortOnClose&&await this.port.close(),this.parentNode.removeChild(this)}async _resetDevice(){await this._console.reset()}_downloadLogs(){u(this._console.logs(),(this.configuration?`${h(this.configuration)}_logs`:"logs")+".txt")}};f.styles=o`
    mwc-dialog {
      --mdc-dialog-max-width: 90vw;
    }
    ewt-console {
      width: calc(80vw - 48px);
      height: calc(90vh - 128px);
    }
  `,t([e()],f.prototype,"configuration",void 0),t([e()],f.prototype,"port",void 0),t([e()],f.prototype,"closePortOnClose",void 0),t([n("ewt-console")],f.prototype,"_console",void 0),t([s()],f.prototype,"_isPico",void 0),f=t([i("esphome-logs-webserial-dialog")],f);
