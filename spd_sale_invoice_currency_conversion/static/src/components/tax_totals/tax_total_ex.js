/** @odoo-module **/

import { useService } from "@web/core/utils/hooks";
import { TaxTotalsComponent } from "@account/components/tax_totals/tax_totals";
import { patch } from "@web/core/utils/patch";
import { formatMonetary } from "@web/views/fields/formatters";
import { formatFloat } from "@web/core/utils/numbers";
import { parseFloat } from "@web/views/fields/parsers";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { registry } from "@web/core/registry";
import { getCurrency } from "@web/core/currency";
import {
    Component,
    onPatched,
    onWillUpdateProps,
    onWillRender,
    toRaw,
    useRef,
    useState,
} from "@odoo/owl";

patch(TaxTotalsComponent.prototype, {

    formatData(props) {
        let totals = JSON.parse(JSON.stringify(toRaw(props.record.data[this.props.name])));
        let value = this.props.record.data;
        if (!totals) {
            return;
        }
        const currencyFmtOpts = { currencyId: props.record.data.conversion_currency_id && props.record.data.conversion_currency_id[0] };

        let amount_untaxed = totals.amount_untaxed;
        let amount_tax = 0;
        let subtotals = [];
        this.totals = totals;
        this.value = value;
        this.model = props.record.resModel;
    },
     formatConversionMonetary(value) {
        return formatMonetary(value, {currencyId: this.value.conversion_currency_id.id});
    }
});
