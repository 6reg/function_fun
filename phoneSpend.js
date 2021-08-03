/*Write a program to calculate the total price of your phone purchase. You will keep purchasing phones (hint: loop!) until you run out of money in your bank account. You'll also buy accessories for each phone as long as your purchase amount is below your mental spending threshold.
After you've calculated your purchase amount, add in the tax, then print out the calculated purchase amount, properly formatted.
Finally, check the amount against your bank account balance to see if you can afford it or not.
You should set up some constants for the "tax rate," "phone price," "accessory price," and "spending threshold," as well as a variable for your "bank account balance.""
You should define functions for calculating the tax and for formatting the price with a "$" and rounding to two decimal places.*/


const SPENDING_THRESHOLD = 200;
const TAX_RATE = 0.08;
const PHONE_PRICE = 129.99;
const ACCESSORY_PRICE = 9.99;

let bank_balance = 450.00;
let amt = 0;
let phoneCount = 0;
let accessoryCount = 0;

const formatPrice = (total) => `$${total.toFixed(2)}`

const addTax = (total) => total += total * TAX_RATE

const spendBankBalance = () => {
  while (bank_balance > PHONE_PRICE) {
    amt+= PHONE_PRICE;
    phoneCount++;
    bank_balance-= PHONE_PRICE;
    while (amt < SPENDING_THRESHOLD) {
      amt+= ACCESSORY_PRICE;
      accessoryCount++;
      bank_balance-= ACCESSORY_PRICE;
    }
  }
  const taxed = addTax(amt);
  const finalValue = formatPrice(taxed);
  return finalValue;
}

console.log("Total=", spendBankBalance(), "Phone count=", phoneCount, "Accessory count=", accessoryCount, "Tax=", addTax)

