import * as p from "@bokehjs/core/properties";
import { ActionTool, ActionToolView } from "@bokehjs/models/tools/actions/action_tool";
export class RestoreToolView extends ActionToolView {
    doit() {
        const sources = this.model.sources;
        for (const source of sources) {
            if (!source.buffer || (source.buffer.length == 0)) {
                continue;
            }
            source.data = source.buffer.pop();
            source.change.emit();
            source.properties.data.change.emit();
        }
    }
}
RestoreToolView.__name__ = "RestoreToolView";
export class RestoreTool extends ActionTool {
    constructor(attrs) {
        super(attrs);
        this.tool_name = "Restore";
        this.icon = "bk-tool-icon-undo";
    }
    static init_RestoreTool() {
        this.prototype.default_view = RestoreToolView;
        this.define({
            sources: [p.Array, []]
        });
    }
}
RestoreTool.__name__ = "RestoreTool";
RestoreTool.__module__ = "geoviews.models.custom_tools";
RestoreTool.init_RestoreTool();
//# sourceMappingURL=restore_tool.js.map