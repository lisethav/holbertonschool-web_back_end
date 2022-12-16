import redis from 'redis';

const clio = redis.createClient();
const key = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const valu = [50, 80, 20, 20, 40, 2];

clio.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

clio.on('connect', () => {
  console.log('Redis client connected to the server');
});

key.forEach((key, index) => {
  clio.hset('HolbertonSchools', key, valu[index], redis.print);
});

clio.hgetall('HolbertonSchools', (err, res) => {
  console.log(res);
});
