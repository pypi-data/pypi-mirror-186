import * as p from "@bokehjs/core/properties";
import { ActionTool, ActionToolView } from "@bokehjs/models/tools/actions/action_tool";
export class ClearToolView extends ActionToolView {
    doit() {
        for (var source of this.model.sources) {
            for (const column in source.data) {
                source.data[column] = [];
            }
            source.change.emit();
            source.properties.data.change.emit();
        }
    }
}
ClearToolView.__name__ = "ClearToolView";
export class ClearTool extends ActionTool {
    constructor(attrs) {
        super(attrs);
        this.tool_name = "Clear data";
        this.icon = "bk-tool-icon-reset";
    }
    static init_ClearTool() {
        this.prototype.default_view = ClearToolView;
        this.define({
            sources: [p.Array, []],
        });
    }
}
ClearTool.__name__ = "ClearTool";
ClearTool.__module__ = "geoviews.models.custom_tools";
ClearTool.init_ClearTool();
//# sourceMappingURL=clear_tool.js.map