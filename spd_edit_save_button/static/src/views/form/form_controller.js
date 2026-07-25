/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { X2ManyField } from "@web/views/fields/x2many/x2many_field";

patch(FormController.prototype, {
    get modelParams() {
        const params = super.modelParams;
        if (params.config.resId && !this.env.inDialog) {
            params.config.mode = "readonly";
        }
        return params;
    },

    async edit() {
        if (this.model.root) {
            await this.model.root.switchMode("edit");
        }
    },

    async saveButtonClicked(params = {}) {
        const saved = await super.saveButtonClicked(params);
        if (saved && !this.env.inDialog) {
            await this.model.root.switchMode("readonly");
        }
        return saved;
    },

    async discard() {
        await super.discard();
        if (!this.env.inDialog && !this.model.root.isNew) {
            await this.model.root.switchMode("readonly");
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