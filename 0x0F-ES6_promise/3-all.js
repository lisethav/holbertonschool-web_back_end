import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  try {
    const usr = await createUser();
    const phot = await uploadPhoto();
    console.log(`${phot.body} ${usr.firstName} ${usr.lastName}`);
  } catch (err) {
    console.log('Signup system offline');
  }
}
