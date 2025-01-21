/** @odoo-module */

import { registry } from "@web/core/registry";
import { useAutofocus } from "@web/core/utils/hooks";
import { archParseBoolean } from '@web/views/utils';
import { formatFloat } from "@web/views/fields/formatters";
import { FloatField } from '@web/views/fields/float/float_field';

const { useState, useRef, useEffect } = owl;


export class PurchaseProductCatalogQuantity extends FloatField {
    setup() {
        super.setup(...arguments);
        const refName = 'numpadDecimal';
        useAutofocus({ refName });
        this.state = useState({
            readonly: this.props.readonly,
            addSmallClass: this.props.value.toString().length > 5,
        });

        const ref = useRef(refName);
        useEffect( // remove 0 when the input is focused.
            (el) => {
                if (el) {
                    if (["INPUT", "TEXTAREA"].includes(el.tagName) && el.type === 'number') {
                        el.value = el.value === '0' ? '' : el.value;
                    }
                }
            },
            () => [ref.el]
        );
    }

    get formattedValue() {
        if (!this.state.readonly && this.props.inputType === "number") {
            return this.props.value;
        }
        return formatFloat(this.props.value, { noTrailingZeros: true });
    }

    toggleMode() {
        this.state.readonly = !this.state.readonly;
    }

    setReadonly(readonly) {
        if (this.state.readonly !== readonly) {
            this.toggleMode();
        }
    }

    getSession() {
        let sessionData = sessionStorage.getItem("current_action")
        sessionData = JSON.parse(sessionData)
        return sessionData
    }

    onInput(ev) {
        let sale_product_qty = Number(ev.target.value.replace(",", ""))
        let product_id = this.props.record.data.id
        let context = this.getSession().context
        let _purchase_id = context.purchase_id;
        $.ajax({
            url: "/update/purchase_order_items",
            method: "GET",
            dataType: 'json',
            data: { quantity: sale_product_qty, product_id: product_id, purchase_id: _purchase_id }
        });
        this.state.addSmallClass = ev.target.value.length > 5;
    }

    /**
     * Handle the keydown event on the input
     *
     * @param {KeyboardEvent} ev
     */
    onKeyDown(ev) {
        if (ev.key === 'Enter') {
            ev.target.dispatchEvent(new Event('change'));
            ev.target.dispatchEvent(new Event('blur'));
        }
    }
}

PurchaseProductCatalogQuantity.props = {
    ...FloatField.props,
    hideButtons: { type: Boolean, optional: true }
};
PurchaseProductCatalogQuantity.defaultProps = {
    ...FloatField.defaultProps,
    hideButtons: false,
};

PurchaseProductCatalogQuantity.template = 'spd_product_catalog_purchase.PurchaseCartQuantity';
PurchaseProductCatalogQuantity.extractProps = (props) => {
    return {
        ...FloatField.extractProps(props),
        hideButtons: archParseBoolean(props.attrs.hide_buttons),
    };
};

registry.category('fields').add('purchase_cart_product_quantity', PurchaseProductCatalogQuantity);
