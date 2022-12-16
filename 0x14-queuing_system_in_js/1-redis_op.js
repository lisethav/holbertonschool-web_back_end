import redis from 'redis';

const clio = redis.createClient();

clio.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

clio.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  clio.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  clio.get(schoolName, (err, res) => {
    console.log(res);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
