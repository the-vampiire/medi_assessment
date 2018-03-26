window.addEventListener('load', () => {

  // clone billing address details to shipping address form input fields
  const sameAsBillingCheckbox = document.querySelector('#same_as_billing_checkbox');
  sameAsBillingCheckbox.addEventListener('change', ({ target }) => {
    document.querySelector('#id_shipping-street').value = document.querySelector('#id_billing-street').value;
    document.querySelector('#id_shipping-zipcode').value = document.querySelector('#id_billing-zipcode').value;
    document.querySelector('#id_shipping-city').value = document.querySelector('#id_billing-city').value;
    document.querySelector('#id_shipping-state').value = document.querySelector('#id_billing-state').value;
  });

  // update purchase total on button
  const purchaseButton = document.querySelector('#purchase_button');
  const quantityInput = document.querySelector('#quantity_input');
  quantityInput.addEventListener('input', ({ target }) => {
    purchaseButton.value = `Purchase $${ (target.value * purchaseButton.attributes.about.value).toFixed(2) } `;
  });
});