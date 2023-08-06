import*as Q from"../../../__snowpack__/env.js";import s,{useCallback as T,useEffect as n,useImperativeHandle as X,useMemo as Y,useRef as Z,useState as $}from"../../../__snowpack__/pkg/react.js";import{contentHeight as M,position as O,primaryColor as W,rem as i,size as x,transitionProps as A}from"../../utils/style.js";import D from"../ChartToolbox.js";import G from"../../../__snowpack__/pkg/react-spinners/HashLoader.js";import N from"../../assets/images/netron.png.proxy.js";import B from"../../../__snowpack__/link/packages/netron2/dist/index.html.proxy.js";import l from"../../../__snowpack__/pkg/styled-components.js";import{toast as S}from"../../../__snowpack__/pkg/react-toastify.js";import ee from"../../hooks/useTheme.js";import{useTranslation as te}from"../../../__snowpack__/pkg/react-i18next.js";console.log("netron2",B);const h=Q.SNOWPACK_PUBLIC_PATH;let I=`${window.location.protocol}//${window.location.host}`;if(h.startsWith("http")){const o=new URL(h);I=`${o.protocol}//${o.host}`}const R=i(40),re=l.div`
    position: relative;
    height: ${M};
    background-color: var(--background-color);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    ${A("background-color")}
`,oe=l.div`
    position: absolute;
    top: 0;
    left: 0;
    ${x("100%","100%")}
    opacity: ${o=>o.show?1:0};
    z-index: ${o=>o.show?0:-1};
    pointer-events: ${o=>o.show?"auto":"none"};
`,se=l(D)`
    height: ${R};
    border-bottom: 1px solid var(--border-color);
    padding: 0 ${i(20)};
    ${A("border-color")}
`,ae=l.div`
    position: relative;
    height: calc(100% - ${R});

    > iframe {
        ${x("100%","100%")}
        border: none;
    }

    > .powered-by {
        display: block;
        ${O("absolute",null,null,i(20),i(30))}
        color: var(--graph-copyright-color);
        font-size: ${i(14)};
        user-select: none;

        img {
            height: 1em;
            filter: var(--graph-copyright-logo-filter);
            vertical-align: middle;
        }
    }
`,U=l.div`
    ${x("100%","100%")}
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    overscroll-behavior: none;
    cursor: progress;
    font-size: ${i(16)};
    line-height: ${i(60)};
`,K=s.forwardRef(({files:o,uploader:F,showAttributes:w,showInitializers:E,showNames:z,horizontal:j,onRendered:c,onOpened:m,onSearch:p,onShowModelProperties:g,onShowNodeProperties:u,onShowNodeDocumentation:d},V)=>{const{t:_}=te("graph"),C=ee(),[t,q]=$(!1),[v,f]=$(!1),[k,J]=$(!1),H=Z(null),y=T(r=>{if(r.data){const{type:b,data:a}=r.data;switch(b){case"status":switch(a){case"ready":return q(!0);case"loading":return f(!0);case"rendered":f(!1),J(!0),console.log("\u51FD\u6570\u6267\u884C\u4E86"),c==null||c();return}return;case"opened":return m==null?void 0:m(a);case"search":return p==null?void 0:p(a);case"cancel":return f(!1);case"error":S.error(a),f(!1);return;case"show-model-properties":return g==null?void 0:g(a);case"show-node-properties":return u==null?void 0:u(a);case"show-node-documentation":return d==null?void 0:d(a)}}},[c,m,p,g,u,d]),e=T((r,b)=>{var a,L;(L=(a=H.current)==null?void 0:a.contentWindow)==null||L.postMessage({type:r,data:b},I)},[]);n(()=>(window.addEventListener("message",y),e("ready"),()=>{window.removeEventListener("message",y)}),[y,e]),n(()=>{console.log("GraphStatic2",o,t),o&&t&&e("change-files",o)},[e,o,t]),n(()=>t&&e("toggle-attributes",w)||void 0,[e,w,t]),n(()=>t&&e("toggle-initializers",E)||void 0,[e,E,t]),n(()=>t&&e("toggle-names",z)||void 0,[e,z,t]),n(()=>t&&e("toggle-direction",j)||void 0,[e,j,t]),n(()=>t&&e("toggle-theme",C)||void 0,[e,C,t]),X(V,()=>({export(r){e("export",r)},changeGraph(r){e("change-graph",r)},search(r){e("search",r)},select(r){e("select",r)},showModelProperties(){e("show-model-properties")},showNodeDocumentation(r){e("show-node-documentation",r)},show2(){e("show2")}}));const P=Y(()=>!t||v?s.createElement(U,null,s.createElement(G,{size:"60px",color:W})):t&&!k?s.createElement(U,null,s.createElement(G,{size:"60px",color:W})):null,[t,v,k,F]);return s.createElement(re,null,P,s.createElement(oe,{show:!v&&k},s.createElement(se,{items:[{icon:"zoom-in",tooltip:_("graph:zoom-in"),onClick:()=>e("zoom-in")},{icon:"zoom-out",tooltip:_("graph:zoom-out"),onClick:()=>e("zoom-out")},{icon:"restore-size",tooltip:_("graph:restore-size"),onClick:()=>e("zoom-reset")}],reversed:!0,tooltipPlacement:"bottom"}),s.createElement(ae,null,s.createElement("iframe",{ref:H,src:h+B,frameBorder:0,scrolling:"no",marginWidth:0,marginHeight:0}),s.createElement("a",{className:"powered-by",href:"https://github.com/lutzroeder/netron",target:"_blank",rel:"noreferrer"},"Powered by ",s.createElement("img",{src:h+N,alt:"netron"})))))});K.displayName="Graph";export default K;
