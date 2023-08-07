// package.json
var name = "anywidget";
var version = "0.0.5";

// src/widget.js
function is_href(str) {
  return str.startsWith("http://") || str.startsWith("https://");
}
async function load_css_href(href, anywidget_id) {
  let prev = document.querySelector(`link[id='${anywidget_id}']`);
  if (prev) {
    let newLink = prev.cloneNode();
    newLink.href = href;
    newLink.addEventListener("load", () => prev?.remove());
    prev.after(newLink);
    return;
  }
  return new Promise((resolve) => {
    let link = Object.assign(document.createElement("link"), {
      rel: "stylesheet",
      href,
      onload: resolve
    });
    document.head.appendChild(link);
  });
}
function load_css_text(css_text, anywidget_id) {
  let prev = document.querySelector(`style[id='${anywidget_id}']`);
  if (prev) {
    prev.textContent = css_text;
    return;
  }
  let style = Object.assign(document.createElement("style"), {
    id: anywidget_id,
    type: "text/css"
  });
  style.appendChild(document.createTextNode(css_text));
  document.head.appendChild(style);
}
async function load_css(css, anywidget_id) {
  if (!css)
    return;
  if (is_href(css))
    return load_css_href(css, anywidget_id);
  return load_css_text(css, anywidget_id);
}
async function load_esm(esm) {
  if (is_href(esm)) {
    return import(
      /* webpackIgnore: true */
      esm
    );
  }
  let url = URL.createObjectURL(
    new Blob([esm], { type: "text/javascript" })
  );
  let widget = await import(
    /* webpackIgnore: true */
    url
  );
  URL.revokeObjectURL(url);
  return widget;
}
function widget_default(base) {
  class AnyModel extends base.DOMWidgetModel {
    static model_name = "AnyModel";
    static model_module = name;
    static model_module_version = version;
    static view_name = "AnyView";
    static view_module = name;
    static view_module_version = version;
  }
  class AnyView extends base.DOMWidgetView {
    async render() {
      await load_css(this.model.get("_css"), this.model.get("_anywidget_id"));
      let widget = await load_esm(
        this.model.get("_esm") ?? this.model.get("_module")
      );
      await widget.render(this);
    }
  }
  return { AnyModel, AnyView };
}

// src/index.js
define(["@jupyter-widgets/base"], widget_default);
