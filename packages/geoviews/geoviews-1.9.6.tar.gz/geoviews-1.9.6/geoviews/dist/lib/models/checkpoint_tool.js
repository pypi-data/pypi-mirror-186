import * as p from "@bokehjs/core/properties";
import { copy } from "@bokehjs/core/util/array";
import { ActionTool, ActionToolView } from "@bokehjs/models/tools/actions/action_tool";
export class CheckpointToolView extends ActionToolView {
    doit() {
        const sources = this.model.sources;
        for (const source of sources) {
            if (!source.buffer) {
                source.buffer = [];
            }
            let data_copy = {};
            for (const key in source.data) {
                const column = source.data[key];
                const new_column = [];
                for (const arr of column) {
                    if (Array.isArray(arr) || (ArrayBuffer.isView(arr))) {
                        new_column.push(copy(arr));
                    }
                    else {
                        new_column.push(arr);
                    }
                }
                data_copy[key] = new_column;
            }
            source.buffer.push(data_copy);
        }
    }
}
CheckpointToolView.__name__ = "CheckpointToolView";
export class CheckpointTool extends ActionTool {
    constructor(attrs) {
        super(attrs);
        this.tool_name = "Checkpoint";
        this.icon = "bk-tool-icon-save";
    }
    static init_CheckpointTool() {
        this.prototype.default_view = CheckpointToolView;
        this.define({
            sources: [p.Array, []],
        });
    }
}
CheckpointTool.__name__ = "CheckpointTool";
CheckpointTool.__module__ = "geoviews.models.custom_tools";
CheckpointTool.init_CheckpointTool();
//# sourceMappingURL=checkpoint_tool.js.map