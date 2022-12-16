import redis from 'redis';

const clio = redis.createClient();

clio.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

clio.on('connect', () => {
  console.log('Redis client connected to the server');
});
