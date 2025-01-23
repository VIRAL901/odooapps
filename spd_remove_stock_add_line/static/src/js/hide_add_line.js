/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ListRenderer } from "@web/views/list/list_renderer";
import { onWillStart ,onWillRender} from "@odoo/owl";
import {_t} from "@web/core/l10n/translation";

patch(ListRenderer.prototype, {
    setup(){
        super.setup();
        if (this.props.nestedKeyOptionalFieldsData) {
            onWillRender(() => {
                if (this.props.nestedKeyOptionalFieldsData.model == 'stock.picking'){
                    if (this.env.model.config.resId != false ){
                        this.creates = [];
                    }
                    else{
                        this.creates = this.props.archInfo.creates.length
                    ? this.props.archInfo.creates
                    : [{ type: "create", string: _t("Add a line") }];
                    }
                }
            })
        }
    }
});
