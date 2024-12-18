/** @odoo-module **/

import { unique } from "@web/core/utils/arrays";
import { visitXML } from "@web/core/utils/xml";
import { archParseBoolean } from "@web/views/utils";

export class MapArchParser {
    parse(arch) {
        const archInfo = {
            fieldNames: [],
            fieldNamesMarkerPopup: [],
        };

        visitXML(arch, (node) => {
            switch (node.tagName) {
                case "leaflet_map":
                    this.visitMap(node, archInfo);
                    break;
                case "field":
                    this.visitField(node, archInfo);
                    break;
            }
        });

        archInfo.fieldNames = unique(archInfo.fieldNames);
        archInfo.fieldNamesMarkerPopup = unique(archInfo.fieldNamesMarkerPopup);

        return archInfo;
    }

    visitMap(node, archInfo) {
//        archInfo.resPartnerField = node.getAttribute("res_partner");
//        archInfo.latitudeField = node.getAttribute("field_latitude");
//        archInfo.longitudeField = node.getAttribute("field_longitude");

//        archInfo.fieldNames.push(archInfo.resPartnerField);
//        archInfo.fieldNames.push(archInfo.latitudeField);
//        archInfo.fieldNames.push(archInfo.longitudeField);

        if (node.hasAttribute("limit")) {
            archInfo.limit = parseInt(node.getAttribute("limit"), 10);
        }
        if (node.hasAttribute("panel_title")) {
            archInfo.panelTitle = node.getAttribute("panel_title");
        }
        if (node.hasAttribute("routing")) {
            archInfo.routing = archParseBoolean(node.getAttribute("routing"));
        }
        if (node.hasAttribute("hide_title")) {
            archInfo.hideTitle = archParseBoolean(node.getAttribute("hide_title"));
        }
        if (node.hasAttribute("hide_address")) {
            archInfo.hideAddress = archParseBoolean(node.getAttribute("hide_address"));
        }
        if (node.hasAttribute("hide_name")) {
            archInfo.hideName = archParseBoolean(node.getAttribute("hide_name"));
        }
        if (!archInfo.hideName) {
            archInfo.fieldNames.push("display_name");
        }
        if (node.hasAttribute("default_order")) {
            archInfo.defaultOrder = {
                name: node.getAttribute("default_order"),
                asc: true,
            };
        }
    }
    visitField(node, params) {
        params.fieldNames.push(node.getAttribute("name"));
        params.fieldNamesMarkerPopup.push({
            fieldName: node.getAttribute("name"),
            string: node.getAttribute("string"),
        });
    }
}
