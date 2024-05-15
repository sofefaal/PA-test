const product = {
    name: "Nike trainers",
    price: 100,
    getDetails: function getDetails() {
        return `Name of product: ${product.name}, Price: £${product.price}`
    }
}
//The function should create a new object that is a clone of the original,
function updatePrice(originalProduct, newPrice) {
  const newProduct = { ...originalProduct };

//update the price in the new object, with the new price provided
  newProduct.price = newPrice;

  newProduct.getDetails = originalProduct.getDetails.bind(newProduct)

  return newProduct
}

const newProduct = updatePrice(product, 200)

console.log(product.getDetails());
console.log(newProduct.getDetails());