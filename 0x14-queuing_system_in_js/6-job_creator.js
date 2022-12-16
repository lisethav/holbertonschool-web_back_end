/* c s a */
const kue = require('kue'),
      queue = kue.createQueue();

const jobDat = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
}

let wok = queue
  .create('push_notification_code', jobDat)
  .save((err) => {
    if (!err) console.log(`Notification job created: ${wok.id}`)
  })
  .on('complete', () => console.log('Notification job completed'))
  .on('failed', () => console.log('Notification job failed'));
