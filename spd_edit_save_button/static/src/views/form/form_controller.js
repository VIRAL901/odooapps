/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { X2ManyField } from "@web/views/fields/x2many/x2many_field";

patch(FormController.prototype, {
    /**
     * Force existing records to open in readonly mode
     * so the user must click "Edit" explicitly.
     */
    get modelParams() {
        const params = super.modelParams;
        if (params.config && params.config.resId && !this.env.inDialog) {
            params.config.mode = "readonly";
        }
        return params;
    },

    /**
     * Switch the root record into edit mode.
     */
    async edit() {
        if (this.model.root) {
            await this.model.root.switchMode("edit");
        }
    },

    /**
     * After a successful save, return to readonly mode (outside dialogs).
     */
    async saveButtonClicked(params = {}) {
        const saved = await super.saveButtonClicked(params);
        if (saved && !this.env.inDialog && this.model.root && !this.model.root.isNew) {
            await this.model.root.switchMode("readonly");
        }
        return saved;
    },

    /**
     * After discard, return to readonly mode (outside dialogs / new records).
     */
    async discard() {
        await super.discard();
        if (!this.env.inDialog && this.model.root && !this.model.root.isNew) {
            await this.model.root.switchMode("readonly");
        }
    },
});

/**
 * When the parent form is in edit mode, allow inline editing
 * of x2many list renderers.
 */
patch(X2ManyField.prototype, {
    get isParentFormEditing() {
        return !!this.props.record?.model?.root?.isInEdition;
    },

    get rendererProps() {
        const props = super.rendererProps;
        if (this.props.viewMode === "list" && this.isParentFormEditing) {
            props.readonly = false;
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
