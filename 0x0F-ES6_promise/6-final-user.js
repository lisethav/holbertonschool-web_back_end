import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const usr = await signUpUser(firstName, lastName);
  let pict;
  try {
    pict = await uploadPhoto(fileName);
  } catch (err) {
    pict = err.toString();
  }
  return [
    { value: usr, status: 'fulfilled' },
    { value: pict, status: 'rejected' },
  ];
}
