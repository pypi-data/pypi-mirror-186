import*as w from"../../__snowpack__/env.js";import{Link as J,useLocation as Q}from"../../__snowpack__/pkg/react-router-dom.js";import{useHistory as Z}from"../../__snowpack__/pkg/react-router-dom.js";import n,{useCallback as ee,useEffect as C,useMemo as h,useState as T}from"../../__snowpack__/pkg/react.js";import{border as te,borderRadius as ne,rem as l,size as U,transitionProps as x,triangle as oe}from"../utils/style.js";import O from"./Icon.js";import ae from"./Language.js";import re from"./ThemeToggle.js";import R from"../../__snowpack__/pkg/@tippyjs/react.js";import se from"../utils/event.js";import B from"../routes/index.js";import{getApiToken as ce}from"../utils/fetch.js";import ie from"../assets/images/logo.svg.proxy.js";import K from"../../__snowpack__/pkg/query-string.js";import _ from"../../__snowpack__/pkg/styled-components.js";import le from"../hooks/useClassNames.js";import me from"../hooks/useComponents.js";import{useTranslation as de}from"../../__snowpack__/pkg/react-i18next.js";import{fetcher as pe}from"../utils/fetch.js";import{isArray as fe}from"../../__snowpack__/pkg/lodash.js";const M=w.SNOWPACK_PUBLIC_BASE_URI,ge=w.SNOWPACK_PUBLIC_PATH,W=w.SNOWPACK_PUBLIC_API_TOKEN_KEY,q=6,H=a=>{const r=[];return a.forEach(s=>{s.children?r.push(...H(s.children)):r.push(s)}),r};function D(a){if(!W)return a;const r=K.parseUrl(a);return K.stringifyUrl({...r,query:{...r.query,[W]:ce()}})}const ue=_.nav`
    background-color: var(--navbar-background-color);
    color: var(--navbar-text-color);
    ${U("100%")}
    padding: 0 ${l(20)};
    display: flex;
    justify-content: space-between;
    align-items: stretch;
    ${x(["background-color","color"])}

    > .left {
        display: flex;
        justify-content: flex-start;
        align-items: center;
    }

    > .right {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        margin-right: -${l(20)};
    }
`,he=_.a`
    font-size: ${l(20)};
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif,
        'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';
    font-weight: 600;
    margin-right: ${l(40)};

    > img {
        ${U(l(31),l(98))}
        vertical-align: middle;
        margin-right: ${l(8)};
    }

    > span {
        vertical-align: middle;
    }
`,y=_.div`
    height: 100%;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    background-color: var(--navbar-background-color);
    cursor: pointer;
    ${x("background-color")}

    &:hover {
        background-color: var(--navbar-hover-background-color);
    }

    &.nav-item {
        padding: 0 ${l(20)};
    }

    .nav-link {
        display: inline-block;
        width: 100%;
        height: 100%;
        display: inline-flex;
        justify-content: center;
        align-items: center;
    }

    .nav-text {
        margin: ${l(20)};
        padding: ${l(10)} 0 ${l(7)};
        ${a=>te("bottom",l(3),"solid",a.active?"var(--navbar-highlight-color)":"transparent")}
        ${x("border-bottom")}
        text-transform: uppercase;

        &.dropdown-icon {
            &::after {
                content: '';
                display: inline-block;
                width: 0;
                height: 0;
                margin-left: 0.5rem;
                vertical-align: middle;
                ${oe({pointingDirection:"bottom",width:l(8),height:l(5),foregroundColor:"currentColor"})}
            }
        }
    }
`,V=_.div`
    overflow: hidden;
    border-radius: ${ne};
`,ve=_.div`
    display: block;
    line-height: 3em;

    &,
    &:visited {
        color: ${a=>a.active?"var(--primary-color)":"var(--text-color)"};
    }

    &:hover {
        background-color: var(--background-focused-color);
    }

    > a {
        display: block;
        padding: 0 ${l(20)};
    }
`,z=({to:a,children:r,...s})=>n.createElement(J,{to:a?D(a):"",...s},r),$=n.forwardRef(({path:a,active:r,showDropdownIcon:s,children:m},c)=>{const d=le("nav-text",{"dropdown-icon":s},[s]);return a?n.createElement(y,{active:r,ref:c},n.createElement(z,{to:a,className:"nav-link"},n.createElement("span",{className:d},m))):n.createElement(y,{active:r,ref:c},n.createElement("span",{className:d},m))});$.displayName="NavbarItem";const Y=({menu:a,active:r,path:s,showDropdownIcon:m,children:c})=>n.createElement(R,{placement:"bottom-start",animation:"shift-away-subtle",interactive:!0,arrow:!1,offset:[0,0],hideOnClick:!1,role:"menu",content:n.createElement(V,null,a.map(d=>n.createElement(ve,{active:d.active,key:d.id},n.createElement(z,{to:d.path},d.name))))},n.createElement($,{active:r||!1,path:s,showDropdownIcon:m},c)),_e=()=>{const a=Z(),{t:r,i18n:s}=de("common"),{pathname:m}=Q(),[c,d]=T([]),F=ee(()=>{const e=s.language,t=(s.options.supportedLngs||[]).filter(p=>p!=="cimode"),o=t.indexOf(e),i=o<0||o>=t.length-1?t[0]:t[o+1];s.changeLanguage(i)},[s]),k=h(()=>({scalar:"scalar",histogram:"histogram",image:"image",audio:"audio",text:"text",fastdeploy_server:"fastdeploy_server",graphStatic:"static_graph",graphDynamic:"dynamic_graph","high-dimensional":"embeddings","pr-curve":"pr_curve","roc-curve":"roc_curve",profiler:"profiler","hyper-parameter":"hyper_parameters",x2paddle:"x2paddle",fastdeploy_client:"fastdeploy_client"}),[]);console.log("pathname",m);const f=h(()=>m.replace(M,""),[m]),[A]=me(),L=(e,t)=>{const o=fe(t)?[...t]:[...t.values()];if(console.log("routeEm[route.id]",c,c.includes(k[e.id])),c.includes(k[e.id]))return!0;if(e.children)for(const i of e.children)L(i,o)},b=h(()=>{const e=new Map,t=[];if(c.length>0){for(const o of A)if(c.includes(k[o.id])&&e.set(o.id,o),o.children)for(const i of o.children){const p=L(i,e);if(p&&!t.includes(o.id)){t.push(o.id);const g={...o,children:[i]};e.set(o.id,g)}else if(p&&t.includes(o.id)){const g=e.get(o.id),E={...g,children:[...g.children,i]};e.set(o.id,E)}}}return console.log("Components",[...e],e),[...e.values()]},[A,c]),N=h(()=>b.slice(0,q),[b]),P=h(()=>H(b.slice(q)),[b]);console.log("currentPath",f);const S=h(()=>P.map(e=>({...e,active:f===e.path})),[f,P]),[X,G]=T([]),I=(e,t,o)=>{let i="";if(t?i=t+`/${e.id}`:i=`/${e.id}`,k[e.id]===o){console.log("path",e),a.push(i);return}if(e.children)for(const p of e.children)I(p,i,o)};return C(()=>{pe("/component_tabs").then(e=>{console.log("component_tabs",e),d(e)})},[]),C(()=>{if(c.length>0&&m)if(console.log("pathname",m),m==="/index"){const e=c[0];for(const t of B)I(t,"",e)}else{const e=m;for(const t of B)I(t,"",e)}},[c]),C(()=>{G(e=>N.map(t=>{var i,p,g,E;const o=(i=t.children)==null?void 0:i.map(u=>({...u,active:u.path===f}));if(t.children&&!t.path){const u=t.children.find(v=>v.path===f);if(u)return{...t,cid:u.id,name:u.name,path:f,active:!0,children:o};{const v=e.find(j=>j.id===t.id);if(v)return{...t,...v,name:(E=(g=(p=t.children)==null?void 0:p.find(j=>j.id===v.cid))==null?void 0:g.name)!=null?E:t.name,active:!1,children:o}}}return{...t,active:f===t.path,children:o}}))},[N,f,c]),console.log("componentsInNavbar",N),n.createElement(ue,null,n.createElement("div",{className:"left"},n.createElement(he,{href:D(M+"/index")},n.createElement("img",{alt:"PaddlePaddle",src:ge+ie}),n.createElement("span",null,"VisualDL")),X.map(e=>e.children?n.createElement(Y,{menu:e.children,active:e.active,path:e.path,key:e.active?`${e.id}-activated`:e.id},e.name):n.createElement($,{active:e.active,path:e.path,key:e.id},e.name)),S.length?n.createElement(Y,{menu:S,showDropdownIcon:!0},r("common:more")):null),n.createElement("div",{className:"right"},n.createElement(R,{placement:"bottom-end",animation:"shift-away-subtle",interactive:!0,arrow:!1,offset:[18,0],hideOnClick:!1,role:"menu",content:n.createElement(V,null,n.createElement(re,null))},n.createElement(y,{className:"nav-item"},n.createElement(O,{type:"theme"}))),n.createElement(y,{className:"nav-item",onClick:F},n.createElement(ae,null)),n.createElement(y,{className:"nav-item",onClick:()=>se.emit("refresh")},n.createElement(O,{type:"refresh"}))))};export default _e;
