odoo.define("point_of_sale.ProductItem", function (require) {
    "use strict";

    const ProductItem = require("point_of_sale.ProductItem");
    const Registries = require("point_of_sale.Registries");

    const QuickInfoProductItem = (OriginalProductItem) =>
        class extends OriginalProductItem {
            async onProductInfoClick(event) {

            }
        };

    Registries.Component.extend(ProductItem, QuickInfoProductItem);

    return QuickInfoProductItem;
});