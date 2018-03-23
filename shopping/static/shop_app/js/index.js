window.addEventListener('load', () => {
  const sameAsBillingCheckbox = document.querySelector('#same_as_billing_checkbox');
  sameAsBillingCheckbox.addEventListener('change', ({ target }) => {
    document.querySelector('#id_shipping-street').value = document.querySelector('#id_billing-street').value;
    document.querySelector('#id_shipping-zipcode').value = document.querySelector('#id_billing-zipcode').value;
    document.querySelector('#id_shipping-city').value = document.querySelector('#id_billing-city').value;
    document.querySelector('#id_shipping-state').value = document.querySelector('#id_billing-state').value;
  });  
});