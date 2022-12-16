const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const toJSON = JSON.stringify;

/* - */
const app = express();
const redisClient = redis.createClient();
const redisSet = promisify(redisClient.set).bind(redisClient);
const redisGet = promisify(redisClient.get).bind(redisClient);

/* Productos */
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

/* Funciones auxiliares */
const getItemById = (id) => listProducts.find(itemObj => itemObj.id === id);
const reserveStockById = (itemId, stock) => redisSet(`item.${itemId}`, stock);
const getCurrentReservedStockById = async (itemId) => await redisGet(`item.${itemId}`);

/* Redis */
redisClient.on('ready', () => console.log('Redis client connected to the server'));
redisClient.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

app.listen(1245, () => console.log('Express server is now running'));
app.get('/list_products', (req, res) => {
  res.status(200).send(toJSON(listProducts));
});
app.get('/list_products/:itemId', async (req, res) => {
  const itemID = parseInt(req.params.itemId);
  const item = getItemById(itemID);

  if (!item) res.status(404).send(toJSON({"status":"Product not found"}));
  else {
    let currentStock = await getCurrentReservedStockById(itemID);

    if (!currentStock)
      reserveStockById(itemID, getItemById(itemID).initialAvailableQuantity);

    currentStock = parseInt(await getCurrentReservedStockById(itemID));

    res.status(200).send(
      toJSON({ ...item, currentQuantity: currentStock })
    );
  }
});
app.get('/reserve_product/:itemId', async(req, res) => {
  const itemId = parseInt(req.params.itemId);
  const iten = getItemById(itemId);

  if (!iten) res.status(404).send(toJSON({"status":"Product not found"}));
  else {
    let currentStoc = await getCurrentReservedStockById(itemId);
    if (currentStoc < 1) res.status(418).send(toJSON({"status":"Not enough stock available","itemId": itemId}));
    else {
      res.status(200).send(toJSON({"status":"Reservation confirmed","itemId":itemId}));
      reserveStockById(itemId, currentStoc - 1);
    }
  }
})

export default app;