/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { useService } from "@web/core/utils/hooks";

const originalSetup = FormController.prototype.setup;
const originalEdit = FormController.prototype.edit; // Note: This might be undefined in standard Odoo
const originalSaveButtonClicked = FormController.prototype.saveButtonClicked;
const originalDiscard = FormController.prototype.discard;

patch(FormController.prototype, {
    setup() {
        this.props.preventEdit = this.env.inDialog ? false : true;
        originalSetup.call(this);
    },

    async edit() {
        if (originalEdit) {
            await originalEdit.call(this);
        }

        if (this.model && this.model.root) {
            await this.model.root.switchMode("edit");
        } else {
            console.error('Model or model root is not defined');
        }
    },

    async saveButtonClicked(params = {}) {
        if (originalSaveButtonClicked) {
            await originalSaveButtonClicked.call(this, params);
        }

        if (!this.env.inDialog) {
            await this.model.root.switchMode("readonly");
        } else {
            this.model.actionService.doAction({ type: 'ir.actions.act_window_close' });
        }
    },

    async discard() {
        if (originalDiscard) {
            await originalDiscard.call(this);
        }

        if (!this.env.inDialog) {
            await this.model.root.switchMode("readonly");
        } else {
            this.model.actionService.doAction({ type: 'ir.actions.act_window_close' });
        }
    },

    async beforeLeave() {
        await this.model.root.save();
        return true;
    }
});
