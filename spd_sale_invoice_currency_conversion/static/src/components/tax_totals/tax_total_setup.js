/** @odoo-module **/

import { useService } from "@web/core/utils/hooks";
import { TaxTotalsComponent } from "@account/components/tax_totals/tax_totals";
import { patch } from "@web/core/utils/patch";
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
    setup() {
        this.totals = {};
        this.carat = {};
        this.formatData(this.props);
        onWillRender(() => this.formatData(this.props));
    }
});