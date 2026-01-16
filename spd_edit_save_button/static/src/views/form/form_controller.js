/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { onMounted } from "@odoo/owl";

patch(FormController.prototype, {
    
    get modelParams() {
        const params = super.modelParams;
        
        // If we have a record ID (existing record) and we are not in a dialog, 
        // force the mode to readonly.
        if (params.config.resId && !this.env.inDialog) {
            params.config.mode = "readonly";
        }
        
        return params;
    },

    setup() {
        super.setup();
        // We can access props here, but we cannot mutate them.
        // The mode control is handled in get modelParams above.
    },

    /**
     * Custom function triggered by your XML "Edit" button
     */
    async edit() {
        // Switch the model to edit mode
        if (this.model.root) {
            await this.model.root.switchMode("edit");
        }
    },

    /**
     * Override saveButtonClicked to switch back to readonly after saving.
     */
    async saveButtonClicked(params = {}) {
        // Call the original save logic
        const saved = await super.saveButtonClicked(params);

        // If save was successful (saved is true) and we are not in a dialog,
        // switch back to readonly mode.
        if (saved && !this.env.inDialog) {
            await this.model.root.switchMode("readonly");
        }
        
        return saved;
    },

    /**
     * Override discard to switch back to readonly.
     */
    async discard() {
        await super.discard();

        // After discarding changes, if we are still on a valid record (not new),
        // switch back to readonly mode.
        if (!this.env.inDialog && !this.model.root.isNew) {
            await this.model.root.switchMode("readonly");
        }
    }
});
