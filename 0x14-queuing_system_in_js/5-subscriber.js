/* e s d */
const redi = require('redis');
const clien = redi.createClient();

clien.on('ready', () => console.log('Redis client connected to the server'));
clien.on('error', (error) => console.log(`Redis client not connected to the server: ${error}`));

const sub_channel = 'holberton school channel'
clien.subscribe(sub_channel);
clien.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    clien.unsubscribe(sub_channel);
    clien.quit();
  }
})
