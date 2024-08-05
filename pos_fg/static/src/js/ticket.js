odoo.define('pos_button.CustomButtonPaymentScreen', function(require) {
  'use strict';
  const { Gui } = require('point_of_sale.Gui');
  const PosComponent = require('point_of_sale.PosComponent');
  const { identifyError } = require('point_of_sale.utils');
  const ProductScreen = require('point_of_sale.ProductScreen');
  const { useListener } = require("@web/core/utils/hooks");
  const Registries = require('point_of_sale.Registries');
  const PaymentScreen = require('point_of_sale.PaymentScreen');
  const Chrome = require('point_of_sale.Chrome');
//        Bottom PaymentScreen
   const CustomButtonPaymentScreen = (PaymentScreen) =>
       class extends PaymentScreen {
           IsCustomButton() {
              // click_ticket
              Gui.showPopup("ConfirmPopup", {
                      title: this.env._t('Title'),
                      body: this.env._t('Total..)'),
                  });
          }
      };
   Registries.Component.extend(PaymentScreen, CustomButtonPaymentScreen);
   return CustomButtonPaymentScreen;
});
