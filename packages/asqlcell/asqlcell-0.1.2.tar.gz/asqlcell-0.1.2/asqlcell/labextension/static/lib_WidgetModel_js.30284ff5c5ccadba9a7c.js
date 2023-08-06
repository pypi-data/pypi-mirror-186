(self["webpackChunkasqlcell"] = self["webpackChunkasqlcell"] || []).push([["lib_WidgetModel_js"],{

/***/ "./lib/WidgetModel.js":
/*!****************************!*\
  !*** ./lib/WidgetModel.js ***!
  \****************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SqlCellView = exports.SqlCellModel = void 0;
const widgets = __importStar(__webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base"));
const react_1 = __importDefault(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const react_dom_1 = __importDefault(__webpack_require__(/*! react-dom */ "webpack/sharing/consume/default/react-dom"));
const WidgetView_1 = __importDefault(__webpack_require__(/*! ./WidgetView */ "./lib/WidgetView.js"));
__webpack_require__(/*! ../css/widget.css */ "./css/widget.css");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const defaultModelProperties = {
    value: "",
    output: "sqlcelldf",
    event: "",
    data_range: [0, 0],
    dfs_button: "",
    data: "",
    error: "",
    show: undefined,
};
class SqlCellModel extends widgets.DOMWidgetModel {
    constructor() {
        super(...arguments);
        this.defaults = () => {
            return Object.assign(Object.assign({}, super.defaults()), { _model_name: SqlCellModel.model_name, _model_module: SqlCellModel.model_module, _model_module_version: SqlCellModel.model_module_version, _view_name: SqlCellModel.view_name, _view_module: SqlCellModel.view_module, _view_module_version: SqlCellModel.view_module_version, value: "", output: "sqlcelldf", event: undefined, data_range: undefined, dfs_button: undefined, data: undefined, error: undefined, show: undefined });
        };
    }
    initialize(attributes, options) {
        super.initialize(attributes, options);
        this.on("msg:custom", this.handle_custom_messages, this);
        this.on("change:output", this.handle_update_messages, this);
    }
    handle_custom_messages(msg) {
        if (msg.includes("\"iscommand\": true")) {
            this.trigger("show", false);
        }
        else if (msg.includes("\"iscommand\": false")) {
            this.trigger("show", true);
        }
        if (msg.includes("__ERR:")) {
            this.trigger("error", msg);
        }
        else if (msg.includes("__ERT:")) {
            this.set("error", msg);
        }
        if (msg.includes("__DFS:")) {
            this.trigger("dataframe", msg);
        }
        if (msg.includes("__DFM:")) {
            // set data into widget 
            this.trigger("data_message", msg);
        }
        else if (msg.includes("__DFT:")) {
            // store data before into widgetview
            this.set("data", msg.slice(6, msg.length));
            // set data into widget 
            this.trigger("data_message", msg);
        }
        if (msg.includes("__JSD:")) {
            this.trigger("hist", msg.slice(6, msg.length));
        }
    }
    handle_update_messages(msg) {
        this.trigger("update_outputName", msg);
    }
}
exports.SqlCellModel = SqlCellModel;
SqlCellModel.serializers = Object.assign({}, widgets.DOMWidgetModel.serializers);
SqlCellModel.model_name = "SqlCellModel";
SqlCellModel.model_module = version_1.MODULE_NAME;
SqlCellModel.model_module_version = version_1.MODULE_VERSION;
SqlCellModel.view_name = "SqlCellView"; // Set to null if no view
SqlCellModel.view_module = version_1.MODULE_NAME; // Set to null if no view
SqlCellModel.view_module_version = version_1.MODULE_VERSION;
class SqlCellView extends base_1.DOMWidgetView {
    constructor() {
        super(...arguments);
        this.render = () => {
            this.el.classList.add("custom-widget");
            const component = react_1.default.createElement(WidgetView_1.default, {
                model: this.model,
            });
            react_dom_1.default.render(component, this.el);
        };
    }
}
exports.SqlCellView = SqlCellView;
//# sourceMappingURL=WidgetModel.js.map

/***/ }),

/***/ "./lib/WidgetView.js":
/*!***************************!*\
  !*** ./lib/WidgetView.js ***!
  \***************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
const react_1 = __importStar(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const hooks_1 = __webpack_require__(/*! ./hooks */ "./lib/hooks.js");
const core_1 = __webpack_require__(/*! @mantine/core */ "webpack/sharing/consume/default/@mantine/core/@mantine/core");
const vsc_1 = __webpack_require__(/*! react-icons/vsc */ "./node_modules/react-icons/vsc/index.esm.js");
const components_1 = __webpack_require__(/*! ./components */ "./lib/components/index.js");
const ReactWidget = (props) => {
    var _a, _b, _c, _d, _e, _f, _g, _h, _j, _k, _l;
    const [hist, setHist] = react_1.useState("");
    const [sqlContent, setSqlContent] = react_1.useState((_a = props.model.get("value")) !== null && _a !== void 0 ? _a : "");
    const [show, setShow] = react_1.useState(props.model.get("show"));
    const [output, setOutput] = hooks_1.useModelState("output");
    const [outputName, setOutputName] = react_1.useState(output);
    const [page, setPage] = react_1.useState(1);
    const [data, setData] = react_1.useState((_b = props.model.get("data")) !== null && _b !== void 0 ? _b : "");
    const [error, setError] = react_1.useState((_c = props.model.get("error")) !== null && _c !== void 0 ? _c : "");
    const [rowNumber, setRowNumber] = react_1.useState(10);
    const [timeStamp, setTimeStamp] = react_1.useState(0);
    const [time, setTime] = react_1.useState(0);
    const [openTimer, setOpenTimer] = react_1.useState(false);
    const [timerId, setTimerId] = react_1.useState();
    const latestCallback = react_1.useRef(null);
    const escape = () => {
        if (document.activeElement instanceof HTMLElement) {
            if (outputName.trim().length > 0) {
                setOutput(outputName);
                document.activeElement.blur();
            }
            else {
                setOutputName(output);
            }
        }
    };
    react_1.useEffect(() => {
        latestCallback.current = () => { setTime(Date.now() - timeStamp); };
    });
    react_1.useEffect(() => {
        if (!openTimer) {
            window.clearInterval(Number(timerId));
        }
        else {
            setTimerId(window.setInterval(() => latestCallback.current(), 10));
        }
    }, [openTimer]);
    react_1.useEffect(() => {
        var _a;
        props.model.set("value", sqlContent);
        (_a = props.model) === null || _a === void 0 ? void 0 : _a.save_changes();
    }, [sqlContent]);
    // Ask back-end whether this is a command mode, so we could decide whether to show inputArea
    react_1.useEffect(() => {
        props.model.set("json_dump", new Date().toISOString());
        props.model.save_changes();
    }, []);
    // Receive event from Model
    (_d = props.model) === null || _d === void 0 ? void 0 : _d.on("error", (msg) => {
        setOpenTimer(false);
        setError(msg);
        setData("");
    });
    (_e = props.model) === null || _e === void 0 ? void 0 : _e.on("show", (msg) => {
        setShow(msg);
    });
    (_f = props.model) === null || _f === void 0 ? void 0 : _f.on("data_message", (msg) => {
        if (msg.slice(6, msg.length) !== data) {
            setData(msg.slice(6, msg.length));
        }
        setError("");
    });
    (_g = props.model) === null || _g === void 0 ? void 0 : _g.on("update_outputName", (msg) => {
        setOutputName(msg.changed.output);
    });
    (_h = props.model) === null || _h === void 0 ? void 0 : _h.on("sort", (msg) => {
        var _a, _b;
        (_a = props.model) === null || _a === void 0 ? void 0 : _a.set("index_sort", msg, "");
        (_b = props.model) === null || _b === void 0 ? void 0 : _b.save_changes();
    });
    (_j = props.model) === null || _j === void 0 ? void 0 : _j.on("setRange", (msg) => {
        var _a, _b;
        (_a = props.model) === null || _a === void 0 ? void 0 : _a.set("data_range", msg, "");
        (_b = props.model) === null || _b === void 0 ? void 0 : _b.save_changes();
    });
    (_k = props.model) === null || _k === void 0 ? void 0 : _k.on("importData", (msg) => {
        setSqlContent("select * from " + msg);
    });
    (_l = props.model) === null || _l === void 0 ? void 0 : _l.on("hist", (msg) => {
        if (msg) {
            setHist(msg);
        }
        setOpenTimer(false);
    });
    return (react_1.default.createElement("div", { className: "Widget" },
        react_1.default.createElement(core_1.Stack, { spacing: 0, align: "center" },
            show ?
                react_1.default.createElement(react_1.default.Fragment, null,
                    react_1.default.createElement(core_1.Group, { position: "apart", align: "center", sx: {
                            width: "95%",
                            height: "30px",
                        } },
                        react_1.default.createElement(components_1.DataImport, { model: props.model }),
                        react_1.default.createElement(core_1.Group, { position: "right", align: "center", sx: {
                                height: "100%",
                                gap: "0px",
                            } },
                            react_1.default.createElement(core_1.Text, { color: "#8D8D8D", sx: { marginRight: "10px" } }, "SAVED TO"),
                            react_1.default.createElement(core_1.TextInput, { size: "xs", styles: () => ({
                                    input: {
                                        width: "100px",
                                        color: "#8D8D8D",
                                        fontSize: "inherit",
                                        backgroundColor: "#fafafa",
                                        borderColor: "#fafafa",
                                        fontWeight: "bold",
                                        paddingLeft: 0,
                                        ":focus": {
                                            borderColor: outputName.trim().length === 0 ? "red" : "lightgray",
                                        }
                                    },
                                }), value: outputName, onBlur: () => {
                                    escape();
                                }, onKeyDown: (e) => {
                                    if (["Enter", "Escape"].includes(e.code)) {
                                        console.log("a");
                                        e.preventDefault();
                                        escape();
                                    }
                                }, onChange: (e) => {
                                    setOutputName(e.target.value);
                                } }))),
                    react_1.default.createElement(core_1.Group, { sx: {
                            width: "95%",
                            display: "flex",
                            gap: 0,
                        } },
                        react_1.default.createElement(core_1.Box, { sx: {
                                width: "95%"
                            } },
                            react_1.default.createElement(core_1.Textarea, { autosize: true, minRows: 3, sx: {
                                    marginTop: "10px",
                                    ".mantine-Textarea-input": {
                                        height: "88px",
                                    }
                                }, value: sqlContent, onChange: (e) => {
                                    setSqlContent(e.target.value);
                                } })),
                        react_1.default.createElement(core_1.ActionIcon, { onClick: () => {
                                var _a, _b, _c, _d;
                                setPage(1);
                                (_a = props.model) === null || _a === void 0 ? void 0 : _a.trigger("setRange", [0, rowNumber * 1]);
                                (_b = props.model) === null || _b === void 0 ? void 0 : _b.set("sql_button", new Date().toISOString());
                                (_c = props.model) === null || _c === void 0 ? void 0 : _c.save_changes();
                                props.model.set("json_dump", new Date().toISOString());
                                (_d = props.model) === null || _d === void 0 ? void 0 : _d.save_changes();
                                setTime(0);
                                setTimeStamp(Date.now());
                                setOpenTimer(true);
                            }, sx: { height: "100%" } },
                            react_1.default.createElement(vsc_1.VscDebugStart, { size: 18 }))),
                    react_1.default.createElement(core_1.Group, { sx: { width: "95%" } },
                        react_1.default.createElement(core_1.Text, null,
                            time / 1000,
                            "s")))
                :
                    react_1.default.createElement(react_1.default.Fragment, null),
            react_1.default.createElement(core_1.Group, { position: "left" },
                react_1.default.createElement(core_1.Text, { color: "red" }, error.slice(0, 6)),
                react_1.default.createElement(core_1.Text, null, error.slice(6, -1))),
            react_1.default.createElement(core_1.Group, { sx: { width: "95%" }, position: "center" }, data ?
                react_1.default.createElement(components_1.DataTable, { data: data, model: props.model, page: page, setPage: setPage, rowNumber: rowNumber, setRowNumber: setRowNumber, hist: hist, show: show })
                :
                    react_1.default.createElement(core_1.Box, { sx: { height: "60px" } })))));
};
const withModelContext = (Component) => {
    return (props) => (react_1.default.createElement(hooks_1.WidgetModelContext.Provider, { value: props.model },
        react_1.default.createElement(Component, Object.assign({}, props))));
};
exports["default"] = withModelContext(ReactWidget);
//# sourceMappingURL=WidgetView.js.map

/***/ }),

/***/ "./lib/components/dataimport.js":
/*!**************************************!*\
  !*** ./lib/components/dataimport.js ***!
  \**************************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.DataImport = void 0;
const react_1 = __importStar(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const core_1 = __webpack_require__(/*! @mantine/core */ "webpack/sharing/consume/default/@mantine/core/@mantine/core");
const ri_1 = __webpack_require__(/*! react-icons/ri */ "./node_modules/react-icons/ri/index.esm.js");
const DataImport = ({ model }) => {
    const [opened, setOpened] = react_1.useState(false);
    const [dataframe, setDataFrame] = react_1.useState("");
    const DropdownHeight = dataframe.trim().split(/\r?\n/).length >= 5 ? `125px` : `${dataframe.trim().split(/\r?\n/).length * 25}px`;
    const items = dataframe.split("\n").map((name, index) => (name === "" ?
        react_1.default.createElement(react_1.default.Fragment, null)
        :
            react_1.default.createElement(core_1.NavLink, { sx: { height: "25px" }, className: "data list", key: index, label: name.split("\t")[0], onClick: () => {
                    model === null || model === void 0 ? void 0 : model.trigger("importData", name.split("\t")[0]);
                    setOpened(false);
                }, rightSection: react_1.default.createElement(core_1.Text, { size: "xs" }, name.split("\t")[1]) })));
    model === null || model === void 0 ? void 0 : model.on("dataframe", (msg) => {
        setDataFrame(msg.slice(6, msg.length));
    });
    return (react_1.default.createElement(react_1.default.Fragment, null,
        react_1.default.createElement(core_1.Popover, { opened: opened, onChange: setOpened },
            react_1.default.createElement(core_1.Popover.Target, null,
                react_1.default.createElement(core_1.Button, { rightIcon: react_1.default.createElement(ri_1.RiArrowDownSLine, null), color: "dark", variant: "subtle", radius: "xs", sx: {
                        outline: "none",
                        "&:hover": {
                            backgroundColor: "transparent"
                        },
                    }, onClick: () => {
                        setOpened((o) => !o);
                        model === null || model === void 0 ? void 0 : model.set("dfs_button", new Date().toISOString());
                        model === null || model === void 0 ? void 0 : model.save_changes();
                    } },
                    react_1.default.createElement(core_1.Text, { color: "gray", sx: { fontWeight: "bold" } }, "Dataframe"))),
            react_1.default.createElement(core_1.Popover.Dropdown, { sx: {
                    marginLeft: "2.5%",
                    marginTop: "-15px",
                    padding: "2px",
                } }, dataframe ?
                react_1.default.createElement(core_1.ScrollArea, { sx: { height: DropdownHeight } },
                    react_1.default.createElement(core_1.Group, { style: { width: "100%" } },
                        react_1.default.createElement(core_1.Box, { sx: {
                                padding: 0,
                            } }, items)))
                :
                    react_1.default.createElement(core_1.Text, { color: "lightgray" }, "There is no dataframe.")))));
};
exports.DataImport = DataImport;
//# sourceMappingURL=dataimport.js.map

/***/ }),

/***/ "./lib/components/header.js":
/*!**********************************!*\
  !*** ./lib/components/header.js ***!
  \**********************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.DataframeHeader = void 0;
const core_1 = __webpack_require__(/*! @mantine/core */ "webpack/sharing/consume/default/@mantine/core/@mantine/core");
const bar_1 = __webpack_require__(/*! @nivo/bar */ "webpack/sharing/consume/default/@nivo/bar/@nivo/bar");
const react_1 = __importStar(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const fa_1 = __webpack_require__(/*! react-icons/fa */ "./node_modules/react-icons/fa/index.esm.js");
const DataframeHeader = ({ headerContent, header, model }) => {
    const Order = {
        Increasing: 1,
        Descending: -1,
        None: 0,
    };
    const [order, setOrder] = react_1.useState(Order.Increasing);
    let currentOrder = Order.None;
    const [col, setColName] = react_1.useState(" ");
    return (react_1.default.createElement("thead", null,
        react_1.default.createElement("tr", null,
            react_1.default.createElement("th", null),
            header.map((item, index) => react_1.default.createElement("th", { key: index, style: {
                    textAlign: "center",
                    padding: 0,
                } },
                react_1.default.createElement(core_1.Group, { position: "center", spacing: "xs" },
                    react_1.default.createElement(core_1.Button, { color: "dark", sx: {
                            height: "27px",
                            "&.mantine-UnstyledButton-root:hover": {
                                backgroundColor: "#ebebeb"
                            }
                        }, rightIcon: react_1.default.createElement(react_1.default.Fragment, null,
                            headerContent ?
                                headerContent.filter(header => header.columnName === item).length !== 0 ?
                                    react_1.default.createElement(core_1.Text, { size: "xs", fs: "italic", color: "gray" }, headerContent.filter(header => header.columnName === item)[0].dtype)
                                    : react_1.default.createElement(react_1.default.Fragment, null)
                                :
                                    react_1.default.createElement(react_1.default.Fragment, null),
                            col === item ?
                                order === Order.Increasing ?
                                    react_1.default.createElement(fa_1.FaSortUp, { color: "gray", size: 10 })
                                    :
                                        order === Order.Descending ?
                                            react_1.default.createElement(fa_1.FaSortDown, { color: "gray", size: 10 })
                                            :
                                                react_1.default.createElement(fa_1.FaSort, { color: "lightgray", size: 10 })
                                :
                                    react_1.default.createElement(fa_1.FaSort, { color: "lightgray", size: 10 })), variant: "subtle", onClick: () => {
                            if (col === item) {
                                if (order === Order.Increasing) {
                                    currentOrder = Order.Descending;
                                    setOrder(Order.Descending);
                                }
                                else if (order === Order.Descending) {
                                    currentOrder = Order.None;
                                    setOrder(Order.None);
                                }
                                else {
                                    currentOrder = Order.Increasing;
                                    setOrder(Order.Increasing);
                                }
                            }
                            else {
                                currentOrder = Order.Increasing;
                                setOrder(Order.Increasing);
                                setColName(item);
                            }
                            model === null || model === void 0 ? void 0 : model.trigger("sort", [item, currentOrder]);
                        } }, item)),
                headerContent ?
                    react_1.default.createElement(react_1.default.Fragment, null, headerContent.filter(header => header.columnName === item && (["int32", "int64", "float64"].includes(header.dtype))).length !== 0 ?
                        react_1.default.createElement(core_1.Stack, { sx: { gap: 0 } },
                            react_1.default.createElement(bar_1.Bar, { data: headerContent.filter(header => header.columnName === item)[0].bins, enableGridY: false, padding: 0.2, colorBy: "id", keys: ["count"], indexBy: "bin_start", layout: "vertical", groupMode: "stacked", reverse: false, height: 40, width: 60, enableLabel: false, valueScale: { type: "symlog" }, tooltip: ({ value, index }) => {
                                    const binRange = headerContent.filter(header => header.columnName === item)[0].bins[index];
                                    return (react_1.default.createElement("div", { style: {
                                            background: 'white',
                                            padding: '0 2px',
                                            border: '1px solid #ccc',
                                        } },
                                        react_1.default.createElement("div", { style: {
                                                padding: '3px 0',
                                                fontSize: "2px"
                                            } },
                                            react_1.default.createElement("div", { style: { display: "flex" } },
                                                "[",
                                                binRange.bin_start.toFixed(2),
                                                ",",
                                                binRange.bin_end.toFixed(2),
                                                "]:",
                                                value))));
                                } }),
                            react_1.default.createElement(core_1.Text, { size: "xs" },
                                "[",
                                Math.abs(headerContent.filter(header => header.columnName === item)[0].bins[0].bin_start) >= 100 ?
                                    headerContent.filter(header => header.columnName === item)[0].bins[0].bin_start.toFixed(0) + " "
                                    :
                                        headerContent.filter(header => header.columnName === item)[0].bins[0].bin_start.toFixed(3) + " ",
                                ",",
                                Math.abs(headerContent.filter(header => header.columnName === item)[0].bins[9].bin_end) >= 100 ?
                                    " " + headerContent.filter(header => header.columnName === item)[0].bins[9].bin_end.toFixed(0)
                                    :
                                        " " + headerContent.filter(header => header.columnName === item)[0].bins[9].bin_end.toFixed(3),
                                "]"))
                        :
                            react_1.default.createElement(react_1.default.Fragment, null))
                    :
                        react_1.default.createElement(react_1.default.Fragment, null))))));
};
exports.DataframeHeader = DataframeHeader;
//# sourceMappingURL=header.js.map

/***/ }),

/***/ "./lib/components/index.js":
/*!*********************************!*\
  !*** ./lib/components/index.js ***!
  \*********************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __exportStar = (this && this.__exportStar) || function(m, exports) {
    for (var p in m) if (p !== "default" && !Object.prototype.hasOwnProperty.call(exports, p)) __createBinding(exports, m, p);
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
__exportStar(__webpack_require__(/*! ./dataimport */ "./lib/components/dataimport.js"), exports);
__exportStar(__webpack_require__(/*! ./header */ "./lib/components/header.js"), exports);
__exportStar(__webpack_require__(/*! ./table */ "./lib/components/table.js"), exports);
//# sourceMappingURL=index.js.map

/***/ }),

/***/ "./lib/components/table.js":
/*!*********************************!*\
  !*** ./lib/components/table.js ***!
  \*********************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.DataTable = void 0;
const react_1 = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
const core_1 = __webpack_require__(/*! @mantine/core */ "webpack/sharing/consume/default/@mantine/core/@mantine/core");
const react_2 = __importDefault(__webpack_require__(/*! react */ "webpack/sharing/consume/default/react"));
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const header_1 = __webpack_require__(/*! ./header */ "./lib/components/header.js");
const DataTable = ({ data, model, page, setPage, rowNumber, setRowNumber, hist, show }) => {
    const [tempoIndex, setTempoIndex] = react_1.useState(1);
    const [outOfRange, setOutOfRange] = react_1.useState(false);
    const info = JSON.parse(data.split("\n")[0]);
    const dataLength = data.split("\n")[1] || 0;
    const header = info.columns;
    const headerContent = hist ?
        JSON.parse(hist).dfhead.slice(0, -1)
        :
            [{ columnName: "", dtype: "", bins: [{ bin_start: 0, bin_end: 0, count: 0 }] }];
    let timeDiff = 0;
    if (data) {
        const timeList = data.split("\n").pop();
        if (timeList !== "") {
            timeDiff = (new Date(timeList ? timeList.split(",")[1] : "0").getTime() - new Date(timeList ? timeList.split(",")[0] : "0").getTime()) / 1000;
        }
    }
    const rows = [...Array(info.index.length).keys()].map((index) => (react_2.default.createElement("tr", { key: base_1.uuid() },
        react_2.default.createElement("td", { key: index }, info.index[index]),
        info.data[index].map((item, tdIndex) => (react_2.default.createElement("td", { key: tdIndex, style: { fontSize: "12px" } }, typeof (item) === "boolean" ?
            item ?
                "True"
                :
                    "False"
            :
                item))))));
    return (react_2.default.createElement(core_1.Stack, { align: "center", spacing: 10, sx: {
            width: "100%",
            marginBottom: "16px",
        } },
        react_2.default.createElement(core_1.ScrollArea, { style: { width: "100%" } },
            react_2.default.createElement(core_1.Table, { withBorder: true, withColumnBorders: true, striped: true, sx: {
                    width: "100%",
                    "& tbody tr td": {
                        padding: "0px 3px",
                    },
                    "&  td:first-of-type": {
                        backgroundColor: "#ebebeb",
                        width: "7%"
                    },
                    "&  tr:first-of-type": {
                        backgroundColor: "#ebebeb",
                    },
                    "&  tr:nth-of-type(even)": {
                        backgroundColor: "#f2f2f2",
                    },
                } },
                react_2.default.createElement(header_1.DataframeHeader, { headerContent: headerContent, header: header, model: model }),
                react_2.default.createElement("tbody", null, rows))),
        react_2.default.createElement(core_1.Group, { position: "apart", sx: { width: "100%" } },
            react_2.default.createElement(core_1.Group, null,
                react_2.default.createElement(core_1.Text, { color: "#8d8d8d" },
                    dataLength,
                    " rows"),
                timeDiff !== 0 ?
                    react_2.default.createElement(core_1.Text, { color: "#8d8d8d" },
                        timeDiff,
                        " s")
                    :
                        react_2.default.createElement(react_2.default.Fragment, null)),
            react_2.default.createElement(core_1.Group, { align: "center" },
                react_2.default.createElement(core_1.Group, { sx: { gap: 0 } },
                    react_2.default.createElement(core_1.Select, { sx: {
                            width: "40px",
                            height: "22px",
                            ".mantine-Select-item": { padding: "0px" },
                            ".mantine-Select-rightSection": { width: "20px" },
                            ".mantine-Select-input": {
                                paddingLeft: "5px",
                                paddingRight: "0px",
                                height: "22px",
                                minHeight: "22px",
                                color: "#8d8d8d",
                            },
                        }, placeholder: "10", data: ["5", "10", "20", "30"], onChange: (number) => {
                            const num = number;
                            setPage(1);
                            setRowNumber(num);
                            model.trigger("setRange", [(0 * num), 1 * num]);
                        } }),
                    react_2.default.createElement(core_1.Text, { color: "#8d8d8d" }, "/page")),
                data ?
                    react_2.default.createElement(core_1.Pagination, { size: "xs", page: page, total: Math.ceil(dataLength / rowNumber), onChange: (index) => {
                            setPage(index);
                            model.trigger("setRange", [((index - 1) * rowNumber), index * rowNumber]);
                        }, styles: (theme) => ({
                            item: {
                                color: theme.colors.gray[4],
                                backgroundColor: theme.colors.gray[0],
                                "&[data-active]": {
                                    color: theme.colors.dark[2],
                                    backgroundColor: theme.colors.gray[4],
                                },
                            },
                        }) })
                    :
                        react_2.default.createElement(react_2.default.Fragment, null),
                react_2.default.createElement(core_1.Group, { sx: { gap: 0 } },
                    react_2.default.createElement(core_1.Text, { color: "#8d8d8d" }, "goto"),
                    react_2.default.createElement(core_1.NumberInput, { defaultValue: 18, size: "xs", hideControls: true, error: outOfRange, value: page, onBlur: () => {
                            if (tempoIndex > 0 && tempoIndex <= Math.ceil(dataLength / rowNumber)) {
                                setPage(tempoIndex);
                                setOutOfRange(false);
                                model.trigger("setRange", [((tempoIndex - 1) * rowNumber), tempoIndex * rowNumber]);
                            }
                            else {
                                setOutOfRange(true);
                            }
                        }, onKeyDown: (e) => {
                            if (["Escape", "Enter"].indexOf(e.key) > -1) {
                                (document.activeElement instanceof HTMLElement) && document.activeElement.blur();
                                if (tempoIndex > 0 && tempoIndex <= Math.ceil(dataLength / rowNumber)) {
                                    setPage(tempoIndex);
                                    setOutOfRange(false);
                                    model.trigger("setRange", [((tempoIndex - 1) * rowNumber), tempoIndex * rowNumber]);
                                }
                                else {
                                    setOutOfRange(true);
                                }
                            }
                        }, onChange: (page) => {
                            setTempoIndex(page);
                            (page > 0 && page <= Math.ceil(dataLength / rowNumber)) ?
                                setOutOfRange(false)
                                :
                                    setOutOfRange(true);
                        }, sx: {
                            width: "40px",
                            ".mantine-NumberInput-input": {
                                paddingLeft: "5px",
                                paddingRight: "0px",
                                height: "22px",
                                minHeight: "22px",
                            }
                        } }))))));
};
exports.DataTable = DataTable;
//# sourceMappingURL=table.js.map

/***/ }),

/***/ "./lib/hooks.js":
/*!**********************!*\
  !*** ./lib/hooks.js ***!
  \**********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.useModel = exports.useModelEvent = exports.useModelState = exports.WidgetModelContext = void 0;
const react_1 = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
exports.WidgetModelContext = react_1.createContext(undefined);
// HOOKS
//============================================================================================
/**
 *
 * @param name property name in the Python model object.
 * @returns model state and set state function.
 */
function useModelState(name) {
    const model = useModel();
    const [state, setState] = react_1.useState(model === null || model === void 0 ? void 0 : model.get(name));
    useModelEvent(`change:${name}`, (model) => {
        setState(model.get(name));
    }, [name]);
    function updateModel(val, options) {
        model === null || model === void 0 ? void 0 : model.set(name, val, options);
        model === null || model === void 0 ? void 0 : model.save_changes();
    }
    return [state, updateModel];
}
exports.useModelState = useModelState;
/**
 * Subscribes a listener to the model event loop.
 * @param event String identifier of the event that will trigger the callback.
 * @param callback Action to perform when event happens.
 * @param deps Dependencies that should be kept up to date within the callback.
 */
function useModelEvent(event, callback, deps) {
    const model = useModel();
    const dependencies = deps === undefined ? [model] : [...deps, model];
    react_1.useEffect(() => {
        const callbackWrapper = (e) => model && callback(model, e);
        model === null || model === void 0 ? void 0 : model.on(event, callbackWrapper);
        return () => void (model === null || model === void 0 ? void 0 : model.unbind(event, callbackWrapper));
    }, dependencies);
}
exports.useModelEvent = useModelEvent;
/**
 * An escape hatch in case you want full access to the model.
 * @returns Python model
 */
function useModel() {
    return react_1.useContext(exports.WidgetModelContext);
}
exports.useModel = useModel;
//# sourceMappingURL=hooks.js.map

/***/ }),

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MODULE_NAME = exports.MODULE_VERSION = void 0;
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
// eslint-disable-next-line @typescript-eslint/no-var-requires
const data = __webpack_require__(/*! ../package.json */ "./package.json");
/**
 * The _model_module_version/_view_module_version this package implements.
 *
 * The html widget manager assumes that this is the same as the npm package
 * version number.
 */
exports.MODULE_VERSION = data.version;
/*
 * The current package name.
 */
exports.MODULE_NAME = data.name;
//# sourceMappingURL=version.js.map

/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js!./css/widget.css":
/*!**************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./css/widget.css ***!
  \**************************************************************/
/***/ ((module, exports, __webpack_require__) => {

// Imports
var ___CSS_LOADER_API_IMPORT___ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
exports = ___CSS_LOADER_API_IMPORT___(false);
// Module
exports.push([module.id, ".custom-widget {\n  padding: 0px 2px;\n}\n", ""]);
// Exports
module.exports = exports;


/***/ }),

/***/ "./css/widget.css":
/*!************************!*\
  !*** ./css/widget.css ***!
  \************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var api = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
            var content = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./widget.css */ "./node_modules/css-loader/dist/cjs.js!./css/widget.css");

            content = content.__esModule ? content.default : content;

            if (typeof content === 'string') {
              content = [[module.id, content, '']];
            }

var options = {};

options.insert = "head";
options.singleton = false;

var update = api(content, options);



module.exports = content.locals || {};

/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"name":"asqlcell","version":"0.1.0","description":"Analytical sql cell for Jupyter","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/datarho/asqlcell","bugs":{"url":"https://github.com/datarho/asqlcell/issues"},"license":"BSD-3-Clause","author":{"name":"qizh","email":"qizh@datarho.tech"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/datarho/asqlcell"},"scripts":{"build":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension:dev","build:prod":"yarn run build:lib && yarn run build:nbextension && yarn run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack","clean":"yarn run clean:lib && yarn run clean:nbextension && yarn run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf asqlcell/labextension","clean:nbextension":"rimraf asqlcell/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"yarn run build:lib","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode=development","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@emotion/react":"^11.10.5","@emotion/serialize":"^1.1.1","@emotion/utils":"^1.2.0","@jupyter-widgets/base":"^1.1.10 || ^2.0.0 || ^3.0.0 || ^4.0.0","@mantine/core":"^5.10.0","@mantine/hooks":"^5.10.0","@nivo/bar":"^0.80.0","@nivo/core":"^0.80.0","react":"^17.0.2","react-dom":"^17.0.2","react-icons":"^4.7.1"},"devDependencies":{"@babel/core":"^7.5.0","@babel/preset-env":"^7.5.0","@babel/preset-react":"^7.14.5","@babel/preset-typescript":"^7.14.5","@jupyterlab/builder":"^3.0.0","@phosphor/application":"^1.6.0","@phosphor/widgets":"^1.6.0","@types/jest":"^26.0.0","@types/react":"^17.0.11","@types/react-dom":"^17.0.8","@types/webpack-env":"^1.13.6","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","babel-loader":"^8.2.2","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-plugin-react":"^7.31.11","fs-extra":"^7.0.0","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webpack":"^5.61.0","webpack-cli":"^4.0.0"},"babel":{"presets":["@babel/preset-env","@babel/preset-react","@babel/preset-typescript"]},"jupyterlab":{"extension":"lib/plugin","outputDir":"asqlcell/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_WidgetModel_js.30284ff5c5ccadba9a7c.js.map