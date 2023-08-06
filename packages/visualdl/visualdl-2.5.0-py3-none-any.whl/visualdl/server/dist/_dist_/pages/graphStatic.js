import y,{AsideSection as s}from"../components/Aside.js";import ue from"../components/GraphPage/GraphStatic.js";import e,{useImperativeHandle as he,useCallback as a,useEffect as Q,useMemo as R,useRef as V,useState as r}from"../../__snowpack__/pkg/react.js";import ge from"../components/Select.js";import{actions as fe}from"../store/index.js";import{primaryColor as Ee,rem as c,size as Se}from"../utils/style.js";import{useDispatch as je}from"../../__snowpack__/pkg/react-redux.js";import P from"../components/Button.js";import N from"../components/Checkbox.js";import ke from"../components/Content.js";import j from"../components/Field.js";import we from"../../__snowpack__/pkg/react-spinners/HashLoader.js";import xe from"../components/GraphPage/ModelPropertiesDialog.js";import Ce from"../components/GraphPage/NodeDocumentationSidebar.js";import be from"../components/GraphPage/NodePropertiesSidebar.js";import X from"../components/RadioButton.js";import _e from"../components/RadioGroup.js";import De from"../components/GraphPage/Search.js";import ve from"../components/Title.js";import Ge from"../components/GraphPage/Uploader.js";import m from"../../__snowpack__/pkg/styled-components.js";import ye from"../hooks/useRequest.js";import{useTranslation as Re}from"../../__snowpack__/pkg/react-i18next.js";const Y=m(P)`
    width: 100%;
`,Pe=m(ge)`
    width: 100%;
`,Ne=m.div`
    display: flex;
    justify-content: space-between;

    > * {
        flex: 1 1 auto;

        &:not(:last-child) {
            margin-right: ${c(20)};
        }
    }
`,Fe=m(s)`
    max-height: calc(100% - ${c(40)});
    display: flex;
    flex-direction: column;

    &:not(:last-child) {
        padding-bottom: 0;
    }
`,Me=m.div`
    ${Se("100%","100%")}
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    overscroll-behavior: none;
    cursor: progress;
    font-size: ${c(16)};
    line-height: ${c(60)};
`,ze=e.forwardRef(({changeName:F,changeshowdata:M,Xpaddlae:Z,show:z=!0},ee)=>{const{t:o}=Re(["graph","common"]),A=je(),l=V(null),p=V(null),[d,te]=r(),u=a(t=>{A(fe.graph.setModel(t));const n=t[0].name.substring(t[0].name.lastIndexOf(".")+1);F&&F(n),te(t),M&&M()},[A]),h=a(()=>{p.current&&(p.current.value="",p.current.click())},[]),oe=a(t=>{const n=t.target;n&&n.files&&n.files.length&&u(n.files)},[u]),{loading:k}=ye(d?null:"/graph/graph"),[w,ne]=r([]),[B,$]=r(""),re=a(t=>{ne(t.graphs),$(t.selected||"")},[]),H=a(t=>{var n;$(t),(n=l.current)==null||n.changeGraph(t)},[]),[I,x]=r(""),[g,L]=r(!1),[O,T]=r({text:"",result:[]}),U=a(t=>{var n;x(t),(n=l.current)==null||n.search(t)},[]),W=a(t=>{var n;x(t.name),(n=l.current)==null||n.select(t)},[]),[f,le]=r(!1),[E,ae]=r(!0),[S,se]=r(!1),[C,ce]=r(!1),[ie,q]=r(null),[i,b]=r(null),[_,D]=r(null),[v,G]=r(!0);Q(()=>{x(""),T({text:"",result:[]})},[d,f,E,S]),Q(()=>{z?(G(!0),b(null)):G(!1)},[z]);const J=R(()=>g?null:e.createElement(Y,{type:"primary",rounded:!0,onClick:h},o("graph:change-model")),[o,h,g]),[K,me]=r(!1);he(ee,()=>({files:d,setNodeDocumentations:()=>{G(!1)}}));const pe=R(()=>!K||k?null:_?e.createElement(y,{width:c(360)},e.createElement(Ce,{data:_,onClose:()=>D(null)})):(console.log("nodeData && renderedflag3",i,v),i&&v?e.createElement(y,{width:c(360)},e.createElement(be,{data:i,onClose:()=>b(null),showNodeDocumentation:()=>{var t;return(t=l.current)==null?void 0:t.showNodeDocumentation(i)}})):e.createElement(y,{bottom:J},e.createElement(Fe,null,e.createElement(De,{text:I,data:O,onChange:U,onSelect:W,onActive:()=>L(!0),onDeactive:()=>L(!1)})),!g&&e.createElement(e.Fragment,null,e.createElement(s,null,e.createElement(Y,{onClick:()=>{var t;return(t=l.current)==null?void 0:t.showModelProperties()}},o("graph:model-properties"))),w.length>1&&e.createElement(s,null,e.createElement(j,{label:o("graph:subgraph")},e.createElement(Pe,{list:w,value:B,onChange:H}))),e.createElement(s,null,e.createElement(j,{label:o("graph:display-data")},e.createElement("div",null,e.createElement(N,{checked:f,onChange:le},o("graph:show-attributes"))),e.createElement("div",null,e.createElement(N,{checked:E,onChange:ae},o("graph:show-initializers"))),e.createElement("div",null,e.createElement(N,{checked:S,onChange:se},o("graph:show-node-names"))))),e.createElement(s,null,e.createElement(j,{label:o("graph:direction")},e.createElement(_e,{value:C,onChange:ce},e.createElement(X,{value:!1},o("graph:vertical")),e.createElement(X,{value:!0},o("graph:horizontal"))))),e.createElement(s,null,e.createElement(j,{label:o("graph:export-file")},e.createElement(Ne,null,e.createElement(P,{onClick:()=>{var t;return(t=l.current)==null?void 0:t.export("png")}},o("graph:export-png")),e.createElement(P,{onClick:()=>{var t;return(t=l.current)==null?void 0:t.export("svg")}},o("graph:export-svg")))))))),[o,J,I,g,O,w,B,H,U,W,f,E,S,C,K,k,i,_,v]),de=R(()=>e.createElement(Ge,{onClickUpload:h,onDropFiles:u,Xpaddlae:Z}),[h,u]);return e.createElement(e.Fragment,null,e.createElement(ve,null,o("common:graph")),e.createElement(xe,{data:ie,onClose:()=>q(null)}),e.createElement(ke,{aside:pe},k?e.createElement(Me,null,e.createElement(we,{size:"60px",color:Ee})):e.createElement(ue,{ref:l,files:d,uploader:de,showAttributes:f,showInitializers:E,showNames:S,horizontal:C,onRendered:()=>me(!0),onOpened:re,onSearch:t=>{T(t)},onShowModelProperties:t=>q(t),onShowNodeProperties:t=>{b(t),D(null)},onShowNodeDocumentation:t=>D(t)}),e.createElement("input",{ref:p,type:"file",multiple:!1,onChange:oe,style:{display:"none"}})))});export default ze;
