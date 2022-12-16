import redis from 'redis';
import { promisify } from 'util';

const clio = redis.createClient();
const ob = promisify(clio.get).bind(clio);

clio.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

clio.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  clio.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  try {
    console.log(await ob(schoolName));
  } catch (error) {
    console.log(error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
