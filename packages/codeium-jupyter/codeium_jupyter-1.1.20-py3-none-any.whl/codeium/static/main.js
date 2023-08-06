var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
define(["require", "exports", "jquery", "base/js/namespace", "base/js/keyboard", "base/js/utils", "notebook/js/cell", "notebook/js/codecell"], function (require, exports, jquery_1, Jupyter, keyboard, utils, cell, codecell) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    exports.load_jupyter_extension = exports.load_ipython_extension = void 0;
    jquery_1 = __importDefault(jquery_1);
    /* eslint-enable @typescript-eslint/ban-ts-comment */
    const CODEIUM_COOKIE_NAME = "codeium-api-key";
    const config = {};
    const baseUrl = utils.get_body_data("baseUrl") + "codeium";
    function getCookie(name) {
        const r = document.cookie.match(`\\b${name}=([^;]*)\\b`);
        return r ? r[1] : "";
    }
    function setCookie(name, value) {
        if (value === "") {
            // delete cookie
            document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT;";
        }
        else {
            document.cookie = name + "=" + value;
        }
    }
    // Get XSRF token set by Tornado web server
    // https://www.tornadoweb.org/en/stable/guide/security.html#cross-site-request-forgery-protection
    const xsrf_token = getCookie("_xsrf");
    let apiKey = getCookie(CODEIUM_COOKIE_NAME);
    let ghostWidgets = [];
    let currentCompletion = undefined;
    var CodeiumState;
    (function (CodeiumState) {
        CodeiumState[CodeiumState["CODEIUM_STATE_UNSPECIFIED"] = 0] = "CODEIUM_STATE_UNSPECIFIED";
        CodeiumState[CodeiumState["CODEIUM_STATE_INACTIVE"] = 1] = "CODEIUM_STATE_INACTIVE";
        CodeiumState[CodeiumState["CODEIUM_STATE_PROCESSING"] = 2] = "CODEIUM_STATE_PROCESSING";
        CodeiumState[CodeiumState["CODEIUM_STATE_SUCCESS"] = 3] = "CODEIUM_STATE_SUCCESS";
        CodeiumState[CodeiumState["CODEIUM_STATE_WARNING"] = 4] = "CODEIUM_STATE_WARNING";
        CodeiumState[CodeiumState["CODEIUM_STATE_ERROR"] = 5] = "CODEIUM_STATE_ERROR";
        CodeiumState[CodeiumState["UNRECOGNIZED"] = -1] = "UNRECOGNIZED";
    })(CodeiumState || (CodeiumState = {}));
    const cellsToLastChange = new Map();
    let lastRequestId = 0;
    let dismissedCompletion = false;
    const Cell = cell.Cell;
    const CodeCell = codecell.CodeCell;
    const keycodes = keyboard.keycodes;
    function loadCss(cssFilePath) {
        (0, jquery_1.default)("<link/>")
            .attr({
            type: "text/css",
            rel: "stylesheet",
            href: require.toUrl(cssFilePath),
        })
            .appendTo("head");
    }
    function signIn() {
        // generate random string
        const uid = Math.random().toString(36).substring(2);
        const searchParams = new URLSearchParams({
            response_type: "token",
            redirect_uri: "jupyter-show-auth-token",
            scope: "openid profile email",
            prompt: "login",
            redirect_parameters_type: "query",
            state: uid,
        });
        const url = "https://www.codeium.com/profile?" + searchParams.toString();
        window.open(url, "_blank");
    }
    function signOut() {
        apiKey = "";
        setCookie(CODEIUM_COOKIE_NAME, "");
        updateMenuItems();
        updateStatus(CodeiumState.CODEIUM_STATE_INACTIVE, "Not logged in to Codeium");
    }
    function getMetadata() {
        if (apiKey === "") {
            return {};
        }
        else {
            return {
                apiKey: apiKey,
                requestId: lastRequestId,
            };
        }
    }
    function getAuthenticationToken() {
        // Get the authentication token from the user.
        const token = prompt("Authentication Token", "");
        jquery_1.default.ajax({
            url: "https://api.codeium.com/register_user/",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                firebase_id_token: token,
            }),
            error: function (_jqXHR, textStatus, errorThrown) {
                console.error(textStatus);
                console.error(errorThrown);
                updateStatus(CodeiumState.CODEIUM_STATE_ERROR, textStatus);
            },
            success: function (data) {
                apiKey = data.api_key;
                setCookie(CODEIUM_COOKIE_NAME, apiKey);
                updateMenuItems();
                updateStatus(CodeiumState.CODEIUM_STATE_UNSPECIFIED, "Logged in to Codeium");
            },
        });
    }
    function updateMenuItems() {
        // Add top level Codeium menu if not already present.
        if ((0, jquery_1.default)("#codeium_menu").length === 0) {
            const menubar = (0, jquery_1.default)("#help_menu").parent().parent();
            menubar.append(`
      <li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown">Codeium</a>
        <ul id="codeium_menu" class="dropdown-menu"></ul>
      </li>`);
            (0, jquery_1.default)("#sign_in").on("click", signIn);
            (0, jquery_1.default)("#sign_out").on("click", signOut);
        }
        // Add provide authentication token menu item if not already present.
        if ((0, jquery_1.default)("#codeium_provide_auth_token").length === 0) {
            (0, jquery_1.default)("#codeium_menu").append(`<li id="codeium_provide_auth_token" title="Provide Authentication Token to Codeium">
        <a href="#">Provide Authentication Token</a>
      </li>`);
            (0, jquery_1.default)("#codeium_provide_auth_token").on("click", getAuthenticationToken);
        }
        // Add login/logout menu item if not already present.
        if (apiKey === "" && (0, jquery_1.default)("#codeium_sign_in").length === 0) {
            (0, jquery_1.default)("#codeium_menu").append(`<li id="codeium_sign_in" title="Log in to Codeium">
        <a href="#">Log In</a>
      </li>`);
            (0, jquery_1.default)("#codeium_sign_in").on("click", signIn);
            (0, jquery_1.default)("#codeium_sign_out").remove();
        }
        else if (apiKey !== "" && (0, jquery_1.default)("#codeium_sign_out").length === 0) {
            (0, jquery_1.default)("#codeium_menu").append(`<li id="codeium_sign_out" title="Log out of Codeium">
        <a href="#">Log Out</a>
      </li>`);
            (0, jquery_1.default)("#codeium_sign_out").on("click", signOut);
            (0, jquery_1.default)("#codeium_sign_in").remove();
        }
    }
    function addStatusIcon() {
        // Add status icon if not already present.
        if ((0, jquery_1.default)("#codeium-status-icon").length === 0) {
            const kernelIndicator = (0, jquery_1.default)("#kernel_indicator");
            kernelIndicator.after(`<span id="codeium-status-icon" class="codeium-status-icon"></span>`);
            if (apiKey === "") {
                updateStatus(CodeiumState.CODEIUM_STATE_INACTIVE, "");
            }
            else {
                updateStatus(CodeiumState.CODEIUM_STATE_UNSPECIFIED, "Logged into Codeium");
            }
        }
    }
    function updateStatus(state, message) {
        // Update status icon.
        (0, jquery_1.default)("#codeium-status-icon").removeClass([
            "codeium-status-active",
            "codeium-status-inactive",
            "codeium-status-success",
            "codeium-status-processing",
            "codeium-status-warning",
            "codeium-status-error",
        ]);
        switch (state) {
            case CodeiumState.CODEIUM_STATE_UNSPECIFIED:
            case CodeiumState.UNRECOGNIZED:
                (0, jquery_1.default)("#codeium-status-icon").addClass("codeium-status-active");
                break;
            case CodeiumState.CODEIUM_STATE_INACTIVE:
                (0, jquery_1.default)("#codeium-status-icon").addClass("codeium-status-inactive");
                break;
            case CodeiumState.CODEIUM_STATE_PROCESSING:
                (0, jquery_1.default)("#codeium-status-icon").addClass("codeium-status-processing");
                break;
            case CodeiumState.CODEIUM_STATE_SUCCESS:
                (0, jquery_1.default)("#codeium-status-icon").addClass("codeium-status-success");
                break;
            case CodeiumState.CODEIUM_STATE_WARNING:
                (0, jquery_1.default)("#codeium-status-icon").addClass("codeium-status-warning");
                break;
            case CodeiumState.CODEIUM_STATE_ERROR:
                (0, jquery_1.default)("#codeium-status-icon").addClass("codeium-status-error");
                break;
        }
        // Update status message.
        (0, jquery_1.default)("#codeium-status-icon").attr("title", message);
    }
    function numUtf8BytesForCodePoint(codePointValue) {
        if (codePointValue < 0x80) {
            return 1;
        }
        if (codePointValue < 0x800) {
            return 2;
        }
        if (codePointValue < 0x10000) {
            return 3;
        }
        return 4;
    }
    /**
     * Calculates for some prefix of the given text, how many bytes the UTF-8
     * representation would be. Undefined behavior if the number of code units
     * doesn't correspond to a valid UTF-8 sequence.
     * @param text - Text to examine.
     * @param numCodeUnits The number of code units to look at.
     * @returns The number of bytes.
     */
    function numCodeUnitsToNumUtf8Bytes(text, numCodeUnits) {
        if (numCodeUnits === 0) {
            return 0;
        }
        let curNumUtf8Bytes = 0;
        let curNumCodeUnits = 0;
        for (const codePoint of text) {
            curNumCodeUnits += codePoint.length;
            curNumUtf8Bytes += numUtf8BytesForCodePoint(codePoint.codePointAt(0));
            if (numCodeUnits !== undefined && curNumCodeUnits >= numCodeUnits) {
                break;
            }
        }
        return curNumUtf8Bytes;
    }
    function numUtf8BytesToNumCodeUnits(text, numUtf8Bytes) {
        if (numUtf8Bytes === 0) {
            return 0;
        }
        let curNumCodeUnits = 0;
        let curNumUtf8Bytes = 0;
        for (const codePoint of text) {
            curNumUtf8Bytes += numUtf8BytesForCodePoint(codePoint.codePointAt(0));
            curNumCodeUnits += codePoint.length;
            if (numUtf8Bytes !== undefined && curNumUtf8Bytes >= numUtf8Bytes) {
                break;
            }
        }
        return curNumCodeUnits;
    }
    function clearCompletions() {
        ghostWidgets.forEach(function (widget) {
            widget.clear();
        });
        ghostWidgets = [];
    }
    function acceptCompletion(cell) {
        if (!currentCompletion) {
            return;
        }
        cell.code_mirror.doc.replaceRange(currentCompletion.text, currentCompletion.start, currentCompletion.end);
        // Send telemetry
        jquery_1.default.ajax({
            url: baseUrl,
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                method: "accept_completion",
                metadata: getMetadata(),
                completionId: currentCompletion.id,
            }),
            error: function (_jqXHR, textStatus, errorThrown) {
                console.error(textStatus);
                console.error(errorThrown);
            },
            headers: {
                "X-Xsrftoken": xsrf_token,
            },
        });
        clearCompletions();
        currentCompletion = undefined;
    }
    function generateCompletions(cursorCell) {
        dismissedCompletion = false;
        // Cancel any previous completions requests
        if (lastRequestId !== 0) {
            jquery_1.default.ajax({
                url: baseUrl,
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify({
                    method: "cancel_request",
                    metadata: getMetadata(),
                    requestId: lastRequestId,
                }),
                error: function (_jqXHR, textStatus, errorThrown) {
                    console.error(textStatus);
                    console.error(errorThrown);
                },
                headers: {
                    "X-Xsrftoken": xsrf_token,
                },
            });
        }
        lastRequestId += 1;
        const curRequestId = lastRequestId;
        const isCode = cursorCell.cell_type === "code";
        const cells = cursorCell.notebook.get_cells();
        const relevantDocumentTexts = [];
        let foundCursorCell = false;
        let additionalUtf8ByteOffset = 0;
        cells.forEach((c, i) => {
            const cellText = c.get_text();
            if (c.cell_id === cursorCell.cell_id) {
                foundCursorCell = true;
                // Aggregate the total number of bytes of all previous cells. We use this to
                // offset the cursor computations to account for the fact that the cursor position
                // is relative to the start of the current cell.
                additionalUtf8ByteOffset =
                    relevantDocumentTexts
                        .map((el) => numCodeUnitsToNumUtf8Bytes(el))
                        .reduce((a, b) => a + b, 0) +
                        "\n\n".length * relevantDocumentTexts.length;
            }
            if (isCode) {
                if (c.cell_type === "code") {
                    relevantDocumentTexts.push(cellText);
                }
            }
            else {
                if (c.cell_type === "code") {
                    relevantDocumentTexts.push(`\`\`\`python\n${cellText}\n\`\`\``);
                }
                else {
                    relevantDocumentTexts.push(cellText);
                }
            }
        });
        if (!foundCursorCell) {
            console.error("Cursor cell not found");
            return;
        }
        const text = relevantDocumentTexts.join("\n\n");
        const cursorDoc = cursorCell.code_mirror.doc;
        const cursorCellStartOffset = cursorDoc.posFromIndex(0);
        const offset = additionalUtf8ByteOffset +
            numCodeUnitsToNumUtf8Bytes(cursorDoc.getRange(cursorCellStartOffset, cursorDoc.getCursor(), cursorDoc.lineSep));
        const documentInfo = {
            text: text,
            cursorOffset: offset,
            absolutePath: "",
            relativePath: "",
            editorLanguage: "python",
            language: "LANGUAGE_PYTHON",
            lineEnding: "\n",
        };
        const editorOptions = {
            tabSize: 4,
            insertSpaces: true,
        };
        updateStatus(CodeiumState.CODEIUM_STATE_PROCESSING, "Generating completions...");
        // Make completions request
        jquery_1.default.ajax({
            url: baseUrl,
            type: "POST",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                method: "get_completions",
                metadata: getMetadata(),
                document: documentInfo,
                editorOptions: editorOptions,
            }),
            success: (data) => {
                if (curRequestId != lastRequestId) {
                    // Stale request
                    return;
                }
                if (dismissedCompletion) {
                    // We were asked to dismiss the current completion
                    return;
                }
                updateStatus(CodeiumState.CODEIUM_STATE_SUCCESS, "Completions generated.");
                clearCompletions();
                const completionItems = data.completionItems;
                if (completionItems === undefined || completionItems.length === 0) {
                    return;
                }
                const completionItem = completionItems[0];
                if (completionItem.completion === undefined ||
                    completionItem.range === undefined) {
                    return;
                }
                const text = completionItem.completion.text;
                const range = completionItem.range;
                // Need to do this because the int protobuf fields are set to undefined
                // when they are 0.
                if (range.startOffset === undefined) {
                    range.startOffset = 0;
                }
                if (range.endOffset === undefined) {
                    range.endOffset = 0;
                }
                const completionParts = completionItem.completionParts;
                const cmDoc = cursorCell.code_mirror.doc;
                const cursorPos = cmDoc.getCursor();
                const lineNum = cursorPos.line;
                const startOffsetBytes = range.startOffset - additionalUtf8ByteOffset;
                const endOffsetBytes = range.endOffset - additionalUtf8ByteOffset;
                // abort if the range lies outside the current cell
                if (startOffsetBytes < 0 || endOffsetBytes < 0) {
                    return;
                }
                const startOffset = numUtf8BytesToNumCodeUnits(cursorCell.get_text(), startOffsetBytes);
                const endOffset = numUtf8BytesToNumCodeUnits(cursorCell.get_text(), endOffsetBytes);
                currentCompletion = {
                    text: text,
                    start: cmDoc.posFromIndex(startOffset),
                    end: cmDoc.posFromIndex(endOffset),
                    id: completionItem.completion.completionId,
                };
                completionParts.forEach(function (part) {
                    if (part.type == "COMPLETION_PART_TYPE_INLINE") {
                        // We use a CodeMirror's bookmark feature to render line ghost text elements.
                        const bookmarkElement = (0, jquery_1.default)("<span>").addClass("codeium-ghost");
                        bookmarkElement.text(part.text);
                        if (part.offset === undefined) {
                            part.offset = 0;
                        }
                        const partOffsetBytes = part.offset - additionalUtf8ByteOffset;
                        const partOffset = numUtf8BytesToNumCodeUnits(cursorCell.get_text(), partOffsetBytes);
                        const pos = cmDoc.posFromIndex(partOffset);
                        const bookmarkWidget = cmDoc.setBookmark(pos, {
                            widget: bookmarkElement[0],
                            insertLeft: true,
                        });
                        ghostWidgets.push(bookmarkWidget);
                    }
                    else if (part.type == "COMPLETION_PART_TYPE_BLOCK") {
                        // We use CodeMirror's LineWidget feature to render the block ghost text element.
                        const lineElement = (0, jquery_1.default)("<div>").addClass("codeium-ghost");
                        part.text.split(/\n/).forEach((line, i) => {
                            lineElement.append((0, jquery_1.default)("<pre>")
                                .addClass("CodeMirror-line codeium-ghost-line")
                                .text(line));
                        });
                        const lineWidget = cmDoc.addLineWidget(lineNum, lineElement[0]);
                        ghostWidgets.push(lineWidget);
                    }
                });
            },
            error: function (_jqXHR, textStatus, errorThrown) {
                updateStatus(CodeiumState.CODEIUM_STATE_ERROR, textStatus);
                console.error(textStatus);
                console.error(errorThrown);
            },
            headers: {
                "X-Xsrftoken": xsrf_token,
            },
        });
    }
    function patchCellKeyEvent() {
        // There are two relevant handlers: CodeCell.prototype.handle_codemirror_keyevent and
        // Cell.prototype.handle_codemirror_keyevent. The former only fires for code cells, while
        // the latter fires for both code and markdown cells. For code cells we must capture the
        // event via the former handler to intercept the intellisense menu which is also triggered
        // by tab. For markdown cells we must capture the event via the latter handler.
        // Code cells
        const origCodeHandleCodemirrorKeyEvent = CodeCell.prototype.handle_codemirror_keyevent;
        CodeCell.prototype.handle_codemirror_keyevent = function (editor, event) {
            // eslint-disable-next-line @typescript-eslint/no-this-alias
            const cursorCell = this;
            if (event.keyCode === keycodes.tab && currentCompletion !== undefined) {
                acceptCompletion(cursorCell);
                event.preventDefault();
                return;
            }
            if (event.keyCode === keycodes.esc && currentCompletion !== undefined) {
                clearCompletions();
                currentCompletion = undefined;
                dismissedCompletion = true;
                event.preventDefault();
                return;
            }
            // Pass the event through to the original handler.
            const retValue = origCodeHandleCodemirrorKeyEvent.call(this, editor, event);
            // Add an event handler to the cell's change.Cell event if we have not
            // already done so.
            if (!cellsToLastChange.has(cursorCell.cell_id)) {
                cellsToLastChange.set(cursorCell.cell_id, "");
                cursorCell.events.on("change.Cell", function (_, change) {
                    // Dedupe the change.Cell event, because it can fire multiple times for the same cell.
                    if (cellsToLastChange.get(change.cell.cell_id) !== change) {
                        cellsToLastChange.set(change.cell.cell_id, change);
                        clearCompletions();
                        generateCompletions(change.cell);
                    }
                });
            }
            return retValue;
        };
        // Markdown cells
        const origCellHandleCodemirrorKeyEvent = Cell.prototype.handle_codemirror_keyevent;
        Cell.prototype.handle_codemirror_keyevent = function (editor, event) {
            // eslint-disable-next-line @typescript-eslint/no-this-alias
            const cursorCell = this;
            // We handle this case above in CodeCell.prototype.handle_codemirror_keyevent.
            if (cursorCell.cell_type === "code") {
                return origCellHandleCodemirrorKeyEvent.call(this, editor, event);
            }
            if (event.keyCode === keycodes.tab && currentCompletion !== undefined) {
                acceptCompletion(cursorCell);
                event.preventDefault();
                return;
            }
            if (event.keyCode === keycodes.esc && currentCompletion !== undefined) {
                clearCompletions();
                currentCompletion = undefined;
                dismissedCompletion = true;
                event.preventDefault();
                return;
            }
            // Pass the event through to the original handler.
            const retValue = origCellHandleCodemirrorKeyEvent.call(this, editor, event);
            // Add an event handler to the cell's change.Cell event if we have not
            // already done so.
            if (!cellsToLastChange.has(cursorCell.cell_id)) {
                cellsToLastChange.set(cursorCell.cell_id, "");
                cursorCell.events.on("change.Cell", function (_, change) {
                    // Dedupe the change.Cell event, because it can fire multiple times for the same cell.
                    if (cellsToLastChange.get(change.cell.cell_id) !== change) {
                        cellsToLastChange.set(change.cell.cell_id, change);
                        clearCompletions();
                        generateCompletions(change.cell);
                    }
                });
            }
            return retValue;
        };
    }
    function patchCellClickEvent() {
        const origCellClickEvent = Cell.prototype._on_click;
        Cell.prototype._on_click = function (event) {
            clearCompletions();
            currentCompletion = undefined;
            dismissedCompletion = true;
            return origCellClickEvent.call(this, event);
        };
    }
    function load_notebook_extension() {
        return Jupyter.notebook.config.loaded
            .then(function on_success() {
            jquery_1.default.extend(true, config, Jupyter.notebook.config.data.codeium);
            loadCss("./main.css");
        }, function on_error(err) {
            console.warn("error loading config:", err);
        })
            .then(function on_success() {
            updateMenuItems();
            addStatusIcon();
            patchCellKeyEvent();
            patchCellClickEvent();
        });
    }
    function load_ipython_extension() {
        load_notebook_extension();
    }
    exports.load_ipython_extension = load_ipython_extension;
    function load_jupyter_extension() {
        load_notebook_extension();
    }
    exports.load_jupyter_extension = load_jupyter_extension;
});
