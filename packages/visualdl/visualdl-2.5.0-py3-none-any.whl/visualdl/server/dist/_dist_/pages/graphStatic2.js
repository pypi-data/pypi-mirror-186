import R,{AsideSection as s}from"../components/Aside.js";import ge from"../components/GraphPage/GraphStatic2.js";import e,{useImperativeHandle as fe,useCallback as a,useEffect as N,useMemo as P,useRef as Q,useState as o}from"../../__snowpack__/pkg/react.js";import Ee from"../components/Select.js";import{actions as Se}from"../store/index.js";import{primaryColor as je,rem as c,size as we}from"../utils/style.js";import{useDispatch as ke}from"../../__snowpack__/pkg/react-redux.js";import F from"../components/Button.js";import M from"../components/Checkbox.js";import Ce from"../components/Content.js";import j from"../components/Field.js";import xe from"../../__snowpack__/pkg/react-spinners/HashLoader.js";import _e from"../components/GraphPage/ModelPropertiesDialog.js";import be from"../components/GraphPage/NodeDocumentationSidebar.js";import De from"../components/GraphPage/NodePropertiesSidebar.js";import V from"../components/RadioButton.js";import ve from"../components/RadioGroup.js";import Ge from"../components/GraphPage/Search.js";import ye from"../components/Title.js";import Re from"../components/GraphPage/Uploader.js";import p from"../../__snowpack__/pkg/styled-components.js";import Ne from"../hooks/useRequest.js";import{useTranslation as Pe}from"../../__snowpack__/pkg/react-i18next.js";const X=p(F)`
    width: 100%;
`,Fe=p(Ee)`
    width: 100%;
`,Me=p.div`
    display: flex;
    justify-content: space-between;

    > * {
        flex: 1 1 auto;

        &:not(:last-child) {
            margin-right: ${c(20)};
        }
    }
`,ze=p(s)`
    max-height: calc(100% - ${c(40)});
    display: flex;
    flex-direction: column;

    &:not(:last-child) {
        padding-bottom: 0;
    }
`,Ae=p.div`
    ${we("100%","100%")}
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    overscroll-behavior: none;
    cursor: progress;
    font-size: ${c(16)};
    line-height: ${c(60)};
`,Be=e.forwardRef(({changeRendered:z,show:A=!0},Y)=>{const{t:n}=Pe(["graph","common"]),B=ke(),l=Q(null),d=Q(null),[w,Z]=o(),[k,ee]=o([]),[$,H]=o(""),{loading:C}=Ne(w?null:"/graph/graph"),i=a(t=>{B(Se.graph.setModel(t)),Z(t)},[B]),u=a(()=>{d.current&&(d.current.value="",d.current.click())},[]),te=a(t=>{const r=t.target;r&&r.files&&r.files.length&&i(r.files)},[i]),oe=a(t=>{ee(t.graphs),H(t.selected||"")},[]),I=a(t=>{var r;H(t),(r=l.current)==null||r.changeGraph(t)},[]),[L,x]=o(""),[h,T]=o(!1),[U,W]=o({text:"",result:[]}),q=a(t=>{var r;x(t),(r=l.current)==null||r.search(t)},[]),O=a(t=>{var r;x(t.name),(r=l.current)==null||r.select(t)},[]),[g,ne]=o(!1),[f,re]=o(!0),[E,le]=o(!1),[_,ae]=o(!1),[se,J]=o(null),[m,b]=o(null),[D,S]=o(null),[v,ce]=o(!1),[K,ie]=o(0),[me,pe]=o(0),[G,y]=o(!0);N(()=>{x(""),W({text:"",result:[]})},[w,g,f,E]),N(()=>{K>1&&me===0&&(z&&z(),pe(1),S(null))},[K]),N(()=>{A?(y(!0),b(null)):y(!1)},[A]);const de=P(()=>h?null:e.createElement(X,{type:"primary",rounded:!0,onClick:u},n("graph:change-model")),[n,u,h]);fe(Y,()=>({setModelFiles:t=>{i(t)},setNodeDocumentations:()=>{y(!1)},rendered:v}));const ue=P(()=>!v||C?null:D?e.createElement(R,{width:c(360)},e.createElement(be,{data:D,onClose:()=>S(null)})):(console.log("nodeData && renderedflag3",m,G),m&&G?e.createElement(R,{width:c(360)},e.createElement(De,{data:m,onClose:()=>b(null),showNodeDocumentation:()=>{var t;return(t=l.current)==null?void 0:t.showNodeDocumentation(m)}})):e.createElement(R,null,e.createElement(ze,null,e.createElement(Ge,{text:L,data:U,onChange:q,onSelect:O,onActive:()=>T(!0),onDeactive:()=>T(!1)})),!h&&e.createElement(e.Fragment,null,e.createElement(s,null,e.createElement(X,{onClick:()=>{var t;return(t=l.current)==null?void 0:t.showModelProperties()}},n("graph:model-properties"))),k.length>1&&e.createElement(s,null,e.createElement(j,{label:n("graph:subgraph")},e.createElement(Fe,{list:k,value:$,onChange:I}))),e.createElement(s,null,e.createElement(j,{label:n("graph:display-data")},e.createElement("div",null,e.createElement(M,{checked:g,onChange:ne},n("graph:show-attributes"))),e.createElement("div",null,e.createElement(M,{checked:f,onChange:re},n("graph:show-initializers"))),e.createElement("div",null,e.createElement(M,{checked:E,onChange:le},n("graph:show-node-names"))))),e.createElement(s,null,e.createElement(j,{label:n("graph:direction")},e.createElement(ve,{value:_,onChange:ae},e.createElement(V,{value:!1},n("graph:vertical")),e.createElement(V,{value:!0},n("graph:horizontal"))))),e.createElement(s,null,e.createElement(j,{label:n("graph:export-file")},e.createElement(Me,null,e.createElement(F,{onClick:()=>{var t;return(t=l.current)==null?void 0:t.export("png")}},n("graph:export-png")),e.createElement(F,{onClick:()=>{var t;return(t=l.current)==null?void 0:t.export("svg")}},n("graph:export-svg")))))))),[n,de,L,h,U,k,$,I,q,O,g,f,E,_,v,C,m,D,G]),he=P(()=>e.createElement(Re,{onClickUpload:u,onDropFiles:i}),[u,i]);return e.createElement(e.Fragment,null,e.createElement(ye,null,n("common:graph")),e.createElement(_e,{data:se,onClose:()=>J(null)}),e.createElement(Ce,{aside:ue},C?e.createElement(Ae,null,e.createElement(xe,{size:"60px",color:je})):e.createElement(ge,{ref:l,files:w,uploader:he,showAttributes:g,showInitializers:f,showNames:E,horizontal:_,onRendered:()=>{ce(!0),ie(t=>t+1)},onOpened:oe,onSearch:t=>{W(t)},onShowModelProperties:t=>J(t),onShowNodeProperties:t=>{b(t),S(null)},onShowNodeDocumentation:t=>S(t)}),e.createElement("input",{ref:d,type:"file",multiple:!1,onChange:te,style:{display:"none"}})))});export default Be;
