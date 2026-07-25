/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { X2ManyField } from "@web/views/fields/x2many/x2many_field";

const originalSetup = FormController.prototype.setup;
const originalSaveButtonClicked = FormController.prototype.saveButtonClicked;
const originalDiscard = FormController.prototype.discard;

/* =========================================================================
 * FormController — view first, click "Edit" to edit.
 * ========================================================================= */
patch(FormController.prototype, {
    setup() {
        this.props.preventEdit = this.env.inDialog ? false : true;
        originalSetup.call(this);
    },

    async edit() {
        if (this.model && this.model.root) {
            await this.model.root.switchMode("edit");
        }
    },

    async saveButtonClicked(params = {}) {
        if (!("onError" in params)) {
            params.onError = this.onSaveError.bind(this);
        }
        const saved = await originalSaveButtonClicked.call(this, params);
        if (!this.env.inDialog) {
            if (this.model && this.model.root) {
                await this.model.root.switchMode("readonly");
            }
        } else {
            this.actionService.doAction({ type: "ir.actions.act_window_close" });
        }
        return saved;
    },

    async discard() {
        await originalDiscard.call(this);
        if (!this.env.inDialog) {
            if (this.model && this.model.root) {
                await this.model.root.switchMode("readonly");
            }
        } else {
            this.actionService.doAction({ type: "ir.actions.act_window_close" });
        }
    },
});

patch(X2ManyField.prototype, {
    get isParentFormEditing() {
        return !!this.props.record.model?.root?.isInEdition;
    },

    get rendererProps() {
        const props = super.rendererProps;
        if (this.props.viewMode === "list" && this.isParentFormEditing) {
            props.editable = props.editable || "bottom";
            if (props.activeActions) {
                props.activeActions = {
                    ...props.activeActions,
                    edit: true,
                    create: true,
                };
            }
        }
        return props;
    },
});