/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { Record } from "@web/model/relational_model/record";
import { X2ManyField } from "@web/views/fields/x2many/x2many_field";

/* =========================================================================
 * PART 1 — Force every field (root form fields + nested one2many/many2many
 * line fields) to report as NOT readonly while the top-level form record
 * is in edit mode.
 * ========================================================================= */
patch(Record.prototype, {
    isReadonly(fieldName) {
        if (this.model?.root?.isInEdition) {
            return false;
        }
        return super.isReadonly(fieldName);
    },
});

/* =========================================================================
 * PART 2 — Force props.editable truthy on X2ManyField whenever the parent
 * ========================================================================= */
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

/* =========================================================================
 * PART 3 — Generic Edit / Save / Discard buttons on FormController.
 * ========================================================================= */
const originalSaveButtonClicked = FormController.prototype.saveButtonClicked;
const originalDiscard = FormController.prototype.discard;

patch(FormController.prototype, {
    setup() {
        this.props.preventEdit = this.env.inDialog ? false : true;
        super.setup();
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